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

    def prepare_image(self, image: np.ndarray) -> np.ndarray:
        """
        Förbereder bilder för ML-modellen genom standardisering:
        1. Konvertering till gråskala (en kanal istället för RGB)
        2. Storleksändring till ML-modellens format
        3. Normalisering av pixelvärden till intervallet [0,1]
        """
        if image.ndim == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.resize(image, self.image_size)
        return image.astype('float32') / 255.0

    def enhance_image(self, image: np.ndarray) -> np.ndarray:
        """
        Förbättrar bildkvaliteten för bättre ML-resultat genom:
        1. Brusreducering: Tar bort störningar i bilden
        2. Kontrastförbättring: Gör siffror tydligare mot bakgrunden
        """
        denoised = cv2.fastNlMeansDenoising(image)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        return clahe.apply(denoised)

    def detect_digit_regions(self, image_path: str) -> List[Tuple[int, int, int, int]]:
        """
        Hittar och isolerar siffror i en bild genom:
        1. Bildförbättring
        2. Adaptiv tröskling för att hitta siffror
        3. Konturdetektering
        4. Filtrering av giltiga sifferregioner
        """

        self.image = cv2.imread(image_path)
        if self.image is None:
            raise FileNotFoundError(f"Kunde inte läsa bilden: {image_path}")
        
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        enhanced = self.enhance_image(gray)
        
        # Adaptiv tröskling anpassar sig till olika ljusförhållanden
        thresh = cv2.adaptiveThreshold(
            enhanced, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
            cv2.THRESH_BINARY_INV, 11, 2
        )
        
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        regions = []
        
        for contour in contours:
            if cv2.contourArea(contour) > 50:  # Filtrerar bort brus
                x, y, w, h = cv2.boundingRect(contour)
                if self._is_valid_digit_region(w, h):
                    regions.append((x, y, w, h))
        
        return sorted(regions, key=lambda r: r[0])

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
            
            # Gör prediktion med klassificeraren
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


