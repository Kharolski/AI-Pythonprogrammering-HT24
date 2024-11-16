import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

class HandwrittenDigitClassifier:
    """
    Neural Network-baserad klassificerare för handskrivna siffror.
    
    Huvudfunktioner:
    1. Träning av neuralt nätverk
    2. Prediktion av siffror
    3. Modellvalidering och utvärdering
    
    ML-arkitektur:
    - Input: 784 neuroner (28x28 pixlar)
    - Dolda lager: Konfigurerbart (default: 100 neuroner)
    - Output: 10 neuroner (siffror 0-9)
    """
    def __init__(self, 
                 hidden_layer_sizes=(100, 50), 
                 max_iter=2000, 
                 learning_rate='constant', 
                 learning_rate_init=0.0005):
        """
        Initierar neural network med specificerade hyperparametrar.
        
        Args:
            hidden_layer_sizes: Struktur för dolda lager
            max_iter: Max antal träningsepoker
            learning_rate: Inlärningsstrategi
            learning_rate_init: Initial inlärningshastighet
        """
        self.model = MLPClassifier(
            hidden_layer_sizes=hidden_layer_sizes,
            max_iter=max_iter,
            random_state=42,
            learning_rate=learning_rate,
            learning_rate_init=learning_rate_init,
            batch_size=32,  # Låt sklearn välja optimal batch size
            solver='adam'       # Använd adam optimizer
        )
        self.is_trained = False

    def train_model(self, X_train: np.ndarray, y_train: np.ndarray):
        """
        Tränar modellen på bilddata.
        """
        MIN_DATASET_SIZE = 30
        
        if len(X_train) < MIN_DATASET_SIZE:
            raise ValueError(f"Dataset måste innehålla minst {MIN_DATASET_SIZE} bilder för träning")
        
        if X_train.ndim != 2 or y_train.ndim != 1:
            raise ValueError("X_train måste vara 2D (samples, features) och y_train 1D (samples)")
        
        unique_classes = np.unique(y_train)
        if len(unique_classes) < 2:
            raise ValueError("Dataset måste innehålla minst två olika klasser för träning")
        
        self.model.fit(X_train, y_train)
        self.is_trained = True

    def evaluate_model(self, X_test: np.ndarray, y_test: np.ndarray) -> tuple[float, np.ndarray]:
        """
        Utvärderar modellens prestanda med testdata.
        
        Args:
            X_test: Testbilder
            y_test: Korrekta etiketter
            
        Returns:
            accuracy: Andel korrekta prediktioner (0-1)
            conf_matrix: Förväxlingsmatris (10x10)
            
        Raises:
            ValueError: Om modellen inte är tränad
        """
        if not self.is_trained:
            raise ValueError("Modellen måste tränas innan utvärdering!")
        
        predictions = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        conf_matrix = confusion_matrix(y_test, predictions)
        
        return accuracy, conf_matrix

    def predict(self, image: np.ndarray) -> int:
        """
        Klassificerar en sifferbild.
        
        Args:
            image: Bild i format (784,) eller (28, 28)
            
        Returns:
            Predikterad siffra (0-9)
            
        Raises:
            ValueError: Om modellen inte är tränad
        """
        if not self.is_trained:
            raise ValueError("Modellen måste tränas innan prediktion!")
        
        # Formatera input korrekt
        if image.ndim == 2:
            image = image.flatten()
        image = image.reshape(1, -1)
        
        return self.model.predict(image)[0]

    def reset_model(self):
        """Återställer modellen till ursprungligt tillstånd"""
        self.is_trained = False
        self.model = MLPClassifier(
            hidden_layer_sizes=self.model.hidden_layer_sizes,
            max_iter=self.model.max_iter,
            random_state=42,
            learning_rate=self.model.learning_rate,
            learning_rate_init=self.model.learning_rate_init
        )

    def __str__(self) -> str:
        """Strängrepresentation av modellens status"""
        status = "tränad" if self.is_trained else "otränad"
        return f"HandwrittenDigitClassifier(status='{status}')"

    def __repr__(self) -> str:
        return self.__str__()
