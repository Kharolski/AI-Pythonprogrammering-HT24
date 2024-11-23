import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Optional, Tuple
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import learning_curve

class Visualizer:
    """ML-resultatvisualisering för sifferigenkänning"""
    
    def __init__(self, figsize: Tuple[int, int] = (10, 6)):
        self.figsize = figsize
        self.setup_style()
    
    def setup_style(self) -> None:
        """Konfigurerar visualiseringsstil för ML-resultat"""
        plt.style.use('seaborn-v0_8-whitegrid')
        sns.set_context("notebook", font_scale=1.1)
    
    def _validate_data(self, images: np.ndarray, labels: np.ndarray) -> None:
        """Validerar indata för visualisering"""
        if len(images) != len(labels):
            raise ValueError("Antal bilder matchar inte antal etiketter")
        if len(images) == 0:
            raise ValueError("Tomt dataset")

    def review_predictions(self, images, labels, trained_model, batch_size=5):
        """
        Visar och låter användaren verifiera ML-prediktioner
        
        Returns:
            dict med verifierade bilder och etiketter, eller None om användaren avbryter
        """
        print("\n=== Granskning av prediktioner ===")
        predictions = trained_model.predict(images)
        corrected_labels = []
        valid_images = []
        
        plt.ion()
        
        i = 0
        while i < len(images):
            batch_images = images[i:i + batch_size]
            batch_preds = predictions[i:i + batch_size]
            
            # Visa batch med bilder
            fig = plt.figure(figsize=(15, 3))
            for j, (img, pred) in enumerate(zip(batch_images, batch_preds)):
                plt.subplot(1, batch_size, j + 1)
                plt.imshow(img.reshape(28, 28), cmap='gray')
                plt.title(f"Bild {i+j+1}: Pred {pred}")
                plt.axis('off')
            plt.tight_layout()
            plt.show()
            
            while True:  # Loop tills giltig input eller avbryt
                print("\nInstruktioner:")
                print("J - Korrekt prediktion")
                print("X - Ogiltig siffra (skippa)")
                print("0-9 - Korrigera till denna siffra")
                print("Q - Avbryt granskning")
                print(f"\nAnge {len(batch_images)} värden (separerade med mellanslag):")
                print(f"Nuvarande prediktioner: {' '.join(str(p) for p in batch_preds)}")
                
                response = input("Dina korrigeringar: ").lower().split()
                
                if 'q' in response:
                    plt.close('all')
                    print("\nKorrigeringen avbröts av användaren...")
                    print("Återgår till huvudmenyn...")
                    return None
                
                if len(response) != len(batch_images):
                    print(f"Fel antal värden angivna. Förväntade {len(batch_images)}, fick {len(response)}.")
                    continue
                
                # Giltig input - process batch och gå vidare
                for img, resp in zip(batch_images, response):
                    if resp == 'j':
                        valid_images.append(img)
                        corrected_labels.append(pred)
                    elif resp == 'x':
                        continue
                    elif resp.isdigit() and 0 <= int(resp) <= 9:
                        valid_images.append(img)
                        corrected_labels.append(int(resp))
                
                plt.close(fig)  # Stäng bara nuvarande batch-figur
                break  # Gå vidare till nästa batch
            
            i += batch_size  # Gå vidare till nästa batch bara när current batch är klar
        
        plt.close('all')  # Stäng alla kvarvarande figurer
        return {
            'images': np.array(valid_images),
            'corrected_labels': np.array(corrected_labels)
        }

    def plot_complete_analysis(self, images: np.ndarray, labels: np.ndarray, 
                         conf_matrix: np.ndarray, predictions: np.ndarray,
                         model, X_train, y_train, scores: dict,
                         num_samples: int = 5) -> None:
        """
        Skapar en komplett visualisering med följande layout:
        - Övre del: Predikterade siffror
        - Nedre del (vänster till höger): 
            1. Modell-jämförelse
            2. Förväxlingsmatris
            3. Inlärningskurvor
        """
        self._validate_data(images, labels)
        
        # Create figure with GridSpec and store reference
        fig = plt.figure(figsize=(20, 10))
        gs = plt.GridSpec(2, 5, height_ratios=[1, 2], width_ratios=[0.8, 0.8, 1, 1, 1.9])

        # Övre rad: Exempel på prediktioner
        for i in range(num_samples):
            ax = fig.add_subplot(gs[0, i])
            ax.imshow(images[i].reshape(28, 28), cmap='gray')
            ax.set_title(f'Sann: {int(labels[i])}\nPred: {int(predictions[i])}')
            ax.axis('off')
        
        # Nedre vänster: Modell-jämförelse
        ax = fig.add_subplot(gs[1, 0:2])    # Spans first two columns
        sns.barplot(x=list(scores.keys()), y=list(scores.values()), ax=ax)
        ax.set_title('Modell-jämförelse')
        ax.set_ylabel('Accuracy')
        ax.tick_params(axis='x', rotation=45)
        
        # Nedre mitten: Förväxlingsmatris
        ax = fig.add_subplot(gs[1, 2:4])    # Spans middle two columns
        sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues',
                    square=True, cbar_kws={'label': 'Antal prediktioner'}, ax=ax)
        accuracy = np.trace(conf_matrix) / np.sum(conf_matrix)
        ax.set_title(f'Förväxlingsmatris\n(Accuracy: {accuracy:.2%})')
        ax.set_ylabel('Sann siffra')
        ax.set_xlabel('Predikterad siffra')
        
        # Nedre höger: Learning curves
        ax = fig.add_subplot(gs[1, 4])      # Takes the last column
        train_sizes, train_scores, test_scores = learning_curve(
            model, X_train, y_train,
            train_sizes=np.linspace(0.1, 1.0, 10),
            cv=5,
            scoring='accuracy',
            n_jobs=-1,
            shuffle=True
        )
        ax.plot(train_sizes, np.mean(train_scores, axis=1), label='Träning')
        ax.plot(train_sizes, np.mean(test_scores, axis=1), label='Validering')
        ax.set_title('Inlärningskurvor')
        ax.set_xlabel('Träningsdatastorlek')
        ax.set_ylabel('Accuracy')
        ax.legend(loc='best')
        ax.grid(True)

        fig.tight_layout()
        plt.show()

   
