import cv2
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from typing import Optional, List, Tuple
from handwritten_digit_classifier import HandwrittenDigitClassifier

# Standardinställningar för bildhantering i maskininlärning
IMAGE_EXTENSIONS = ('.png', '.jpg', '.jpeg', '.bmp', '.gif')
DEFAULT_IMAGE_SIZE = (28, 28)  # Samma storlek som MNIST-datasetet använder

class ImageProcessor:
    """
    Bildprocessor för maskininlärning av handskrivna siffror.
    Huvudfunktioner:
    1. Förbehandling av bilder för ML
    2. Segmentering av siffror
    3. Integration med ML-klassificerare
    """
    def __init__(self, image_size: tuple[int, int] = DEFAULT_IMAGE_SIZE):
        self.image_size = image_size

    def analyze_new_image(self, image_path: str, model_comparator, loader, collector):
        """
        Analyserar ny bild med tränad modell och visar prediktioner
        """

        # Ladda och träna modell på existerande dataset
        images, labels = loader.load_existing_data(collector)
        X_train, X_test, y_train, y_test = loader.split_data(images, labels)
        results = model_comparator.train_and_evaluate(X_train, X_test, y_train, y_test)

        # Processera ny bild och få regioner med prediktioner
        regions, predictions = self.detect_digit_regions(image_path, results['best_model'])

        # Visualize results
        img = cv2.imread(image_path)
        plt.figure(figsize=(15, 10))
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

        for (x, y, w, h), pred in zip(regions, predictions):
            plt.gca().add_patch(plt.Rectangle((x,y), w, h, fill=False, color='red'))
            plt.text(x, y-5, f'Pred: {pred}', color='red')
    
        plt.axis('off')
        plt.show()

    def prepare_image(self, image: np.ndarray) -> np.ndarray:
        """
        Förbereder bilder för ML-modellen genom standardisering:
        1. Konvertering till gråskala (en kanal istället för RGB)
        2. Storleksändring till ML-modellens format
        3. Normalisering av pixelvärden till intervallet [0,1]
        """
        if image.ndim == 3: # -----------
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Förbättrad kontrastjustering
        image = cv2.equalizeHist(image)

        # Mer känslig tröskling för att behålla detaljer
        _, image = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        image = cv2.resize(image, self.image_size)
        return image.astype('float32') / 255.0

    def enhance_image(self, image: np.ndarray) -> np.ndarray:
        """
        Förbättrar bildkvaliteten för bättre ML-resultat genom:
        1. Brusreducering: Tar bort störningar i bilden
        2. Kontrastförbättring: Gör siffror tydligare mot bakgrunden
        """
        # Öka kontrasten först
        enhanced = cv2.convertScaleAbs(image, alpha=1.5, beta=10)

        # Brusreducering med bevarad detaljskärpa
        denoised = cv2.fastNlMeansDenoising(enhanced)

        # Adaptiv kontrastförbättring
        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(4, 4))
        return clahe.apply(denoised)

    def detect_digit_regions(self, image_path: str, classifier=None) -> Tuple[List[Tuple[int, int, int, int]], List[int]]:
        """
        Hittar och isolerar siffror i en bild. Om classifier anges görs även prediktioner.
        """
        self.image = cv2.imread(image_path)
        if self.image is None:
            raise FileNotFoundError(f"Kunde inte läsa bilden: {image_path}")

        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        enhanced = self.enhance_image(gray)

        thresh = cv2.adaptiveThreshold(
            enhanced, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY_INV, 21, 4
        )

        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        regions = []

        # Samla alla giltiga regioner först
        for contour in contours:
            if cv2.contourArea(contour) > 100:  # Ökat tröskelvärde att filtrerar bort brus
                x, y, w, h = cv2.boundingRect(contour)
                if self._is_valid_digit_region(w, h):
                    regions.append((x, y, w, h))

        # Slå ihop närliggande regioner
        merged_regions = []
        used = set()

        for i, (x1, y1, w1, h1) in enumerate(regions):
            if i in used:
                continue

            current_region = [x1, y1, w1, h1]
            used.add(i)

            # Kolla närliggande regioner
            for j, (x2, y2, w2, h2) in enumerate(regions):
                if j in used:
                    continue

                # Om regionerna överlappar eller är mycket nära varandra ---------------------------------------
                if (abs(x1 - x2) < max(w1, w2) * 0.85 and  # Använd största bredden som referens
                    abs(y1 - y2) < max(h1, h2) * 1.1 and    # Öka vertikalt avstånd för split digits
                    self._check_connectivity(x1, y1, w1, h1, x2, y2, w2, h2, thresh)):


                    # Uppdatera nuvarande region till att omfatta båda
                    x = min(current_region[0], x2)
                    y = min(current_region[1], y2)
                    w = max(current_region[0] + current_region[2], x2 + w2) - x
                    h = max(current_region[1] + current_region[3], y2 + h2) - y

                    current_region = [x, y, w, h]
                    used.add(j)

            merged_regions.append(tuple(current_region))

        if classifier is None:
            return merged_regions
        else:
            # Gör prediktioner för de detekterade regionerna
            processed_digits, predictions = self.process_regions_with_ai(merged_regions, classifier)
            return merged_regions, predictions

    def process_regions_with_ai(self, regions: List[Tuple[int, int, int, int]], 
                          classifier: HandwrittenDigitClassifier) -> Tuple[np.ndarray, List[int]]:
        """
        Klassificerar detekterade sifferregioner med ML-modellen
        """
        processed_digits = []
        predictions = []
        
        for x, y, w, h in regions:
            # Extrahera region of interest (ROI)
            roi = self.image[y:y+h, x:x+w]
            
            # Förbered bilden för ML-modellen
            digit = self.prepare_image(roi)
            
            # Konvertera till float32 och forma om till rätt format
            digit_vector = digit.astype('float32').reshape(1, -1)
            processed_digits.append(digit_vector.flatten())
            
            try:
                pred = classifier.predict(digit_vector)
                predictions.append(int(pred[0]))
            except:
                # Om prediktionen misslyckas, använd 0 som standardvärde
                predictions.append(0)
        
        return np.array(processed_digits), predictions

    # Hjälpfunktioner för intern användning
    def _is_valid_digit_region(self, width: int, height: int) -> bool:
        """Validerar sifferproportioner baserat på ML-träningsdata"""
        aspect_ratio = width / height
        return 0.2 <= aspect_ratio <= 2.0 and min(width, height) >= 8

    def _check_connectivity(self, x1, y1, w1, h1, x2, y2, w2, h2, thresh_image):
        """Kontrollerar om två regioner är sammankopplade genom att analysera pixlar mellan dem"""
        # Beräkna området mellan regionerna -------------------------------------------------------------
        connection_area = thresh_image[int(min(y1, y2)):int(max(y1+h1, y2+h2)),
                                int(min(x1, x2)):int(max(x1+w1, x2+w2))]
    
        # Beräkna viktiga mätvärden för regionanalys
        vertical_overlap = min(y1 + h1, y2 + h2) - max(y1, y2)  # Vertikal överlappning
        density = np.mean(connection_area)  # Pixeldensitet i området
        x_center1 = x1 + w1/2       # Centrumpunkt för första regionen
        x_center2 = x2 + w2/2       # Centrumpunkt för andra regionen
    
        # Speciallogik för vertikalt kopplade komponenter (t.ex. siffran 4)
        if (vertical_overlap > min(h1, h2) * 0.1 and            # Minimal vertikal överlappning krävs
            abs(x_center1 - x_center2) < min(w1, w2) * 0.9 and  # Centrumpunkterna är nära horisontellt
            density > 20):          # Tillräcklig pixeldensitet mellan regionerna
            return True             # Regionerna tillhör samma siffra
    
        # Separera alla andra fall (horisontellt angränsande siffror
        return False    # Regionerna tillhör olika siffror
    
