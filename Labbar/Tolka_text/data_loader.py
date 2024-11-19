import os
import sys
import numpy as np
from sklearn.model_selection import train_test_split
from collections import Counter
from typing import Tuple, Optional
from data_collector import DataCollector
from user_interaction import UserInteraction

class DataLoader:
    """
    ML Dataset Manager för handskrivna siffror.
    
    Huvudfunktioner:
    1. Datasethantering och validering
    2. Train-test split med stratifiering
    3. Klassbalansering och kvalitetskontroll
    
    ML-specifika egenskaper:
    - Stratifierad uppdelning för balanserad träning
    - Validering av klassfördelning
    - Automatisk dataformattering för ML
    """
    def __init__(self, data_dir: str = 'data') -> None:
        self.data_dir = data_dir
        self.dataset_stats = {}  # Lagrar statistik om datasetet

    def load_data(self, filename: str) -> Tuple[np.ndarray, np.ndarray]:
        """
        Laddar och validerar ML-dataset.
        
        Args:
            filename: Dataset-fil (.npz format)
            
        Returns:
            images: Bilddata i format (N_samples, N_features)
            labels: Etiketter i format (N_samples,)
        """
        dataset_path = os.path.join(self.data_dir, filename)
        
        self._validate_path(dataset_path)
        
        data = np.load(dataset_path)
        images, labels = data['images'], data['labels']
        
        # Uppdatera dataset-statistik
        self._update_dataset_stats(images, labels)
        
        return images, labels

    def validate_data(self, images: np.ndarray, labels: np.ndarray, 
                     min_samples_per_class: int = 2) -> bool:
        """
        Validerar dataset för ML-träning.
        
        Kontrollerar:
        1. Tillräckligt antal samples
        2. Klassbalans
        3. Dataformat och kvalitet
        """
        if len(images) < 2:
            print("\nOtillräckligt antal träningsexempel för ML")
            return False
        
        class_distribution = Counter(labels)
        for cls, count in class_distribution.items():
            if count < min_samples_per_class:
                print(f"ML-varning: Klass {cls} har endast {count} exempel " 
                      f"(minimum {min_samples_per_class} krävs)")
                return False
        
        return True

    def split_data(self, images: np.ndarray, labels: np.ndarray, 
               test_size: float = 0.2) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """
        Delar data för ML-träning och validering.
        
        Strategi:
        1. Förbehandling av bilddata
        2. Stratifierad uppdelning om möjligt
        3. Automatisk justering av test_size
        4. Klassbalansering
        """
        # Reshape images för ML-modeller
        n_samples = len(images)
        X = images.reshape(n_samples, -1)
        labels = np.array(labels, dtype=int)
        
        # Analysera möjlighet till stratifiering
        class_counts = np.bincount(labels)
        min_count = np.min(class_counts[class_counts > 0])
        can_stratify = min_count >= 2
        
        stratify = labels if can_stratify else None
        if not can_stratify:
            print("ML-notering: Stratifiering ej möjlig - obalanserad data")
        
        # Justera test_size för små dataset
        num_classes = len(np.unique(labels))
        min_test_size = num_classes / len(images)
        adjusted_test_size = max(test_size, min_test_size) if can_stratify else test_size
        
        return train_test_split(
            X, labels, 
            test_size=adjusted_test_size, 
            stratify=stratify,
            random_state=42  # Reproducerbarhet
        )

    def _validate_path(self, dataset_path: str) -> None:
        """Validerar datasetsökvägar och format"""
        if not os.path.exists(self.data_dir):
            raise FileNotFoundError(f"ML-data-mapp saknas: '{self.data_dir}'")
        
        if not os.path.exists(dataset_path):
            raise FileNotFoundError(f"Dataset saknas: '{dataset_path}'")
        
        if not dataset_path.endswith('.npz'):
            raise ValueError("Felaktigt datasetformat - måste vara .npz")

    def _update_dataset_stats(self, images: np.ndarray, labels: np.ndarray) -> None:
        """Uppdaterar dataset-statistik för ML-analys"""
        self.dataset_stats = {
            'num_samples': len(images),
            'num_classes': len(np.unique(labels)),
            'class_distribution': Counter(labels),
            'image_shape': images[0].shape if len(images) > 0 else None
        }

    def get_dataset_info(self) -> dict:
        """Returnerar dataset-statistik för ML-analys"""
        return self.dataset_stats
    
    def load_existing_data(self, collector: DataCollector) -> Tuple[np.ndarray, np.ndarray]:
        """Laddar befintlig träningsdata och hanterar backup vid behov"""
        MIN_DATASET_SIZE = 50
        ui = UserInteraction()
        
        try:
            images, labels = self.load_data('dataset.npz')
            
            # Kontrollera minimum dataset storlek och erbjud backup
            if len(images) < MIN_DATASET_SIZE:
                print(f"\nDataset innehåller {len(images)} bilder")
                print(f"Minst {MIN_DATASET_SIZE} bilder krävs för träning")
                
                if ui.get_user_choice("Vill du ladda bilder från backup? (j/n): "):
                    backup_images, backup_labels = collector.collect_from_backup(collector.image_folder)
                    if len(backup_images) > 0:
                        total_images = len(images) + len(backup_images)
                        if total_images >= MIN_DATASET_SIZE:
                            images = np.concatenate([images, backup_images])
                            labels = np.concatenate([labels, backup_labels])
                            print(f"Totalt dataset efter backup: {total_images} bilder")
                            collector.save_data(images, labels, 'dataset.npz')
                            return images, labels
                        else:
                            print(f"Även med backup-bilder ({total_images}) nås inte minimikravet på {MIN_DATASET_SIZE} bilder")
                    else:
                        print("Inga backup-bilder hittades")
                
                print("Använd alternativ 1 för att lägga till fler bilder först")
                sys.exit()

            if not self.validate_data(images, labels):
                print("\nDatasetet behöver kompletteras")
                if ui.get_user_choice("Ladda backup-bilder? (j/n): "):
                    backup_images, backup_labels = collector.collect_from_backup(collector.image_folder)
                    images = np.concatenate([images, backup_images])
                    labels = np.concatenate([labels, backup_labels])
                    
                    collector.save_data(images, labels, 'dataset.npz')
            
            return images, labels
            
        except FileNotFoundError:
            print("\nInget dataset hittades.")
            if ui.get_user_choice("Vill du ladda bilder från backup? (j/n): "):
                backup_images, backup_labels = collector.collect_from_backup(collector.image_folder)
                if len(backup_images) > 0:
                    collector.save_data(backup_images, backup_labels, 'dataset.npz')
                    return backup_images, backup_labels
                else:
                    print("Inga backup-bilder hittades")
                    
            raise FileNotFoundError("Kunde inte hitta varken dataset eller backup-bilder")

    def __str__(self) -> str:
        return f"ML-DataLoader(data_dir='{self.data_dir}', samples={self.dataset_stats.get('num_samples', 0)})"

    def __repr__(self) -> str:
        return self.__str__()
