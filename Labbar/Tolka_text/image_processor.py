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
        _, image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # Rensa brus efter tröskling
        kernel = np.ones((2,2), np.uint8)
        image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

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
        Huvudfunktion för att hitta och analysera siffror i en bild.
        Returnerar regioner med siffror och eventuella AI-prediktioner om classifier anges.
        """
        # Läs in originalbilden
        self.image = cv2.imread(image_path)
        if self.image is None:
            raise FileNotFoundError(f"Kunde inte läsa bilden: {image_path}")

        # Konvertera till gråskala och förbättra bildkvaliteten
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        enhanced = self.enhance_image(gray)

        # Använd adaptiv tröskling för att separera siffror från bakgrund
        # Parametrarna 21, 4 är optimerade för att minska brus men behålla sifferdetaljer
        thresh = cv2.adaptiveThreshold(
            enhanced, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY_INV, 21, 4  # Ökade trösklingsvärden (21, 4) för att minska brus
        )

        # Hitta alla möjliga sifferregioner i bilden
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        regions = []

        # Filtrera fram giltiga sifferregioner baserat på storlek och form
        for contour in contours:
            if cv2.contourArea(contour) > 45:  # Lite lägre tröskel för att fånga fler siffror
                x, y, w, h = cv2.boundingRect(contour)
                if self._is_valid_digit_region(w, h):
                    regions.append((x, y, w, h))

        # Hantera uppdelade siffror genom att slå ihop närliggande regioner
        merged_regions = []
        used = set()        # Håll koll på redan behandlade regioner
        
        for i, (x1, y1, w1, h1) in enumerate(regions):
            if i in used:
                continue

            current_region = [x1, y1, w1, h1]
            used.add(i)

            # Leta efter regioner som bör slås ihop med nuvarande region
            for j, (x2, y2, w2, h2) in enumerate(regions):
                if j in used:
                    continue

                # Om regionerna överlappar eller är mycket nära varandra ---------------------------------------
                # Kontrollera om regionerna bör kombineras baserat på:
                # - Horisontellt avstånd (85% av största bredden)
                # - Vertikalt avstånd (110% av största höjden)
                # - Pixelkoppling mellan regionerna
                if (abs(x1 - x2) < max(w1, w2) * 0.85 and  # Använd största bredden som referens
                    abs(y1 - y2) < max(h1, h2) * 1.1 and    # Öka vertikalt avstånd för split digits
                    self._check_connectivity(x1, y1, w1, h1, x2, y2, w2, h2, thresh)):

                    # Beräkna ny region som omfattar båda delarna
                    x = min(current_region[0], x2)
                    y = min(current_region[1], y2)
                    w = max(current_region[0] + current_region[2], x2 + w2) - x
                    h = max(current_region[1] + current_region[3], y2 + h2) - y

                    current_region = [x, y, w, h]
                    used.add(j)

            merged_regions.append(tuple(current_region))

        # Returnera antingen bara regioner eller även AI-prediktioner
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
        """
        Validerar sifferproportioner för att avgöra om en region innehåller en giltig siffra.
        
        aspect_ratio = width / height:
        - 0.1: Tillåter mycket smala siffror (höjd upp till 10x bredden)
        - 3.0: Tillåter breda siffror (bredd upp till 3x höjden)
        
        min(width, height) >= 4:
        - Säkerställer att siffran är minst 4 pixlar i både bredd och höjd
        - Filtrerar bort för små områden som troligen är brus
        """
        # Beräkna förhållandet mellan bredd och höjd
        aspect_ratio = width / height

        # Finjusterade värden för att fånga alla siffror
        # - 0.1 tillåter mycket smala siffror (som "1")
        # - 3.0 tillåter breda siffror (som "2" eller "5")
        # - Minst 4 pixlar i både höjd och bredd för att undvika brus
        return 0.1 <= aspect_ratio <= 3.0 and min(width, height) >= 4

    def _check_connectivity(self, x1, y1, w1, h1, x2, y2, w2, h2, thresh_image):
        """
            Analyserar om två regioner tillhör samma siffra genom att undersöka området mellan dem.
            Särskilt viktig för siffror som kan delas upp i separata delar, som "4".
        """
        # Extrahera området mellan de två regionerna för analys
        connection_area = thresh_image[int(min(y1, y2)):int(max(y1+h1, y2+h2)),
                                int(min(x1, x2)):int(max(x1+w1, x2+w2))]
    
        # Beräkna viktiga mätvärden för att avgöra om regionerna hör ihop
        vertical_overlap = min(y1 + h1, y2 + h2) - max(y1, y2)  # Hur mycket regionerna överlappar vertikalt
        density = np.mean(connection_area)  # Hur många pixlar som finns mellan regionerna
        x_center1 = x1 + w1/2       # Mittpunkt för första regionen
        x_center2 = x2 + w2/2       # Mittpunkt för andra regionen
    
        # Kontrollera om regionerna tillhör samma siffra baserat på tre kriterier:
        if (vertical_overlap > min(h1, h2) * 0.1 and            # Minimal vertikal överlappning krävs
            abs(x_center1 - x_center2) < min(w1, w2) * 0.9 and  # Centrumpunkterna ligger nära varandra
            density > 20):          # Tillräckligt många pixlar mellan regionerna
            return True             # Regionerna tillhör samma siffra
    
        # Separera alla andra fall (horisontellt angränsande siffror)
        return False    # Regionerna tillhör olika siffror
    
