import numpy as np
from pathlib import Path
import hashlib
import cv2
from typing import Tuple, List
import sys
import os

from handwritten_digit_classifier import HandwrittenDigitClassifier
from image_processor import ImageProcessor

IMAGE_EXTENSIONS = ('.png', '.jpg', '.jpeg', '.bmp', '.gif')
DEFAULT_IMAGE_SIZE = (28, 28)

class DataCollector:
    """
    ML-datahanterare för bildklassificering.
    
    Huvudfunktioner:
    1. Datainsamling och preprocessing
    2. Dataset-hantering och versionshantering
    3. Bildvalidering och kvalitetskontroll
    """
    def __init__(self, image_size: tuple[int, int] = DEFAULT_IMAGE_SIZE, 
                 data_dir: str ='data', image_folder: str ='images') -> None:
        self.image_size = image_size
        self.image_folder = Path(image_folder)
        self.data_dir = Path(data_dir)
        self.log_file = self.data_dir / "processed_images_log.txt"
        self.processed_images = set()
        self.image_processor = ImageProcessor(image_size=self.image_size)
        
        self._initialize_directories()

    def collect_new_data(self, image_path: str) -> Tuple[np.ndarray, np.ndarray]:
        """
        Samlar in och förbereder nya träningsbilder
        """
        MIN_DATASET_SIZE = 50
        print("\n=== Samlar in ny träningsdata.  ===")
        
        # 1. Kontrollera om dataset finns
        existing_images, existing_labels = self.load_existing_dataset('dataset.npz')
        detected_regions = self.image_processor.detect_digit_regions(image_path)
        classifier = HandwrittenDigitClassifier()
        
        # Om dataset finns
        if len(existing_images) > 0:
            # Läs nya bilder och uppdatera dataset
            new_digits, predictions = self.image_processor.process_regions_with_ai(detected_regions, classifier)
            
            return new_digits, predictions
            
        # Om dataset saknas
        else:
            # Skapa nytt dataset
            new_digits, predictions = self.image_processor.process_regions_with_ai(detected_regions, classifier)
            
            # Spara nya bilder
            self.save_data(new_digits, predictions, 'dataset.npz')
            
            # Kontrollera storlek innan träning
            if len(new_digits) < MIN_DATASET_SIZE:
                print(f"\nDataset innehåller {len(new_digits)} siffror")
                print(f"Minst {MIN_DATASET_SIZE} siffror krävs för träning")
                print("Lägg till fler unika siffror och försök igen")
                sys.exit()
                
            return np.array(new_digits), np.array(predictions)
    
    def collect_from_backup(self, backup_dir: str) -> Tuple[np.ndarray, np.ndarray]:
        """Samlar in bilder från backup-mappen"""
        print(f"\nSöker efter backup-bilder i: {backup_dir}")
        backup_images = []
        backup_labels = []
        total_processed = 0
        
        for label in range(10):  # 0-9 siffror
            label_dir = os.path.join(backup_dir, str(label))
            if os.path.exists(label_dir):
                image_files = [f for f in os.listdir(label_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]
                print(f"Hittade {len(image_files)} bilder i mapp {label}")
                
                for img_file in image_files:
                    img_path = os.path.join(label_dir, img_file)
                    processed_img = self.image_processor.prepare_image(cv2.imread(img_path, cv2.IMREAD_GRAYSCALE))
                    img_hash = self._get_image_hash(processed_img)
                    
                    backup_images.append(processed_img.flatten())
                    backup_labels.append(label)
                    total_processed += 1
        
        print(f"Processade totalt {total_processed} bilder från backup")
        
        if total_processed > 0:
            return np.array(backup_images), np.array(backup_labels)
        return np.array([]), np.array([])

    def save_data(self, images: np.ndarray, labels: np.ndarray, filename: str) -> bool:
        """
        Sparar och versionshanterar ML-dataset med dublettkontroll.
        """
        save_path = self.data_dir / f"{filename.removesuffix('.npz')}.npz"
        hash_path = self.data_dir / "image_hashes.txt"

        # Ensure images are in correct format before saving 
        processed_images = []
        for img in images:
            if img.ndim == 1:
                img = img.reshape(28, 28)
            processed_images.append(img.flatten())  # Store as flattened array 
            
        processed_images = np.array(processed_images) 
        
        try:
            # Ladda existerande hashes
            existing_hashes = set()
            if hash_path.exists():
                with open(hash_path, 'r') as f:
                    existing_hashes = set(f.read().splitlines())
            
            # Skapa hash för nya bilder
            new_image_hashes = {hashlib.md5(img.tobytes()).hexdigest(): (img, label) 
                            for img, label in zip(processed_images, labels)}
            
            if save_path.exists():
                existing_data = np.load(save_path)
                
                # Filtrera ut unika bilder
                unique_images = []
                unique_labels = []
                new_hashes = []
                for img_hash, (img, label) in new_image_hashes.items():
                    if img_hash not in existing_hashes:
                        unique_images.append(img)
                        unique_labels.append(label)
                        new_hashes.append(img_hash)

                if not unique_images:
                    print("Inga nya unika siffror att lägga till - dem siffror fanns redan i dataset")
                    return False
                
                # Kombinera med existerande data
                combined_images = np.vstack((existing_data['images'], unique_images))
                combined_labels = np.concatenate((existing_data['labels'], unique_labels))
                print(f"Lagt till {len(unique_images)} nya unika siffror i dataset")
                    
                # Uppdatera hash-filen
                existing_hashes.update(new_hashes)
                with open(hash_path, 'w') as f:
                    f.write('\n'.join(existing_hashes))
               
            else:
                # Första gången - spara alla bilder och hashes
                combined_images = processed_images
                combined_labels = labels
                with open(hash_path, 'w') as f:
                    f.write('\n'.join(new_image_hashes.keys()))
            
            np.savez(save_path, images=combined_images, labels=combined_labels)
            return True
            
        except Exception as e:
            print(f"Fel vid datasetsparande: {str(e)}")

    def _initialize_directories(self) -> None:
        """Initierar mappstruktur för ML-pipeline"""
        if not self.image_folder.exists():
            raise FileNotFoundError(f"Källmappen '{self.image_folder}' saknas")
        self.data_dir.mkdir(parents=True, exist_ok=True)

    def _get_image_hash(self, img_path) -> str:
        """Genererar unik hash för bildspårning"""
        if isinstance(img_path, np.ndarray):
            return hashlib.md5(img_path.tobytes()).hexdigest()
        else:
            with open(img_path, 'rb') as img_file:
                return hashlib.md5(img_file.read()).hexdigest()

    def load_existing_dataset(self, filename: str) -> Tuple[np.ndarray, np.ndarray]:
        """
        Laddar befintligt ML-dataset om det existerar.
        
        Args:
            filename: Namnet på dataset-filen
            
        Returns:
            Tuple med (bilder, etiketter) som numpy arrays
        """
        dataset_path = self.data_dir / filename
        
        if dataset_path.exists():
            data = np.load(dataset_path)
            return data['images'], data['labels']
        
        return np.array([]), np.array([])
  
    def combine_datasets(self, new_images: np.ndarray, new_labels: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """Kombinerar nytt data med befintligt dataset"""
        existing_images, existing_labels = self.load_existing_dataset('dataset.npz')
        
        if len(existing_images) > 0:
            combined_images = np.vstack((existing_images, new_images))
            combined_labels = np.concatenate((existing_labels, new_labels))
            return combined_images, combined_labels
        
        return new_images, new_labels