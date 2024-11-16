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

   
