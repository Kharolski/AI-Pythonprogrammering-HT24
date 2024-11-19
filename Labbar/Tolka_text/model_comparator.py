import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from visualizer import Visualizer


class ModelComparator:
    """Klass för jämförelse och optimering av olika maskininlärningsmodeller.
        
        Använd denna klass när du behöver:
        - Jämföra olika ML-modeller (MLP, SVM, RandomForest)
        - Optimera hyperparametrar för varje modell
        - Visualisera modellprestanda
        - Hitta den bästa modellen för ditt dataset
        
        Exempel:
            comparator = ModelComparator()
            # Optimera hyperparametrar
            best_params = comparator.optimize_hyperparameters(X_train, y_train)
            # Jämför modeller
            best_model = comparator.compare_models(X_train, X_test, y_train, y_test, plot=True)
            
        """
    def __init__(self, models = None, param_grids = None):
        """
        Initierar modellkomparatorn med ML-pipelines och parameterrutnät
        """
        # Definiera ML-pipelines med standardisering för varje modell
        self.models = {
            # Neural Network pipeline
            'MLP': Pipeline([
                ('scaler', StandardScaler()),  # Standardiserar features till samma skala
                ('mlp', MLPClassifier(
                    hidden_layer_sizes=(100,),
                    max_iter=1000,
                    solver='adam',
                    activation='relu',
                    early_stopping=True,
                    validation_fraction=0.1,
                    random_state=42

                    ))  # Neural Network med ökad träningstid
            ]),
            
            # Support Vector Machine pipeline
            'SVM': Pipeline([
                ('scaler', StandardScaler()),  # Standardisering krävs för SVM
                ('svm', SVC(probability=True, cache_size=1000, random_state=42))  # SVM med sannolikhetsestimat
            ]),
            
            # Random Forest pipeline
            'RandomForest': Pipeline([
                ('scaler', StandardScaler()),  # Standardisering kan hjälpa RF
                ('rf', RandomForestClassifier(
                    n_estimators=100,
                    max_depth=10,
                    min_samples_split=5,
                    random_state=42
                    
                    ))  # Parallell processing med alla CPU-kärnor
            ])
        }

        # Hyperparametrar för optimering av varje modell
        self.param_grids = param_grids or {
            # MLP hyperparametrar
            'MLP': {
                'mlp__hidden_layer_sizes': [(100,50), (50,25), (100,50,25)],  # Olika nätverksarkitekturer
                'mlp__learning_rate_init': [0.001, 0.01],  # Inlärningshastighet
                'mlp__batch_size': [16],  # Batchstorlek för stokastisk optimering
                'mlp__activation': ['relu', 'tanh']  # Aktiveringsfunktioner
            },
            
            # SVM hyperparametrar
            'SVM': {
                'svm__C': [1.0, 10.0, 100.0],  # Regulariseringsstyrka
                'svm__kernel': ['rbf', 'poly'],  # Kernelfunktioner
                'svm__gamma': ['scale', 0.01, 0.001]  # Kernelkoefficient
            },
            
            # Random Forest hyperparametrar
            'RandomForest': {
                'rf__n_estimators': [300, 500],  # Antal beslutsträd
                'rf__max_depth': [30, 50],  # Maximalt träddjup
                'rf__min_samples_split': [2, 3],  # Minsta antal samples för split
                'rf__class_weight': ['balanced', 'balanced_subsample']  # Hantering av obalanserade klasser
            }
        }

        self.visualizer = Visualizer()

        self.best_params = {}
        self.scores = {}

    def optimize_hyperparameters(self, X_train: np.ndarray, y_train: np.ndarray):
        """Optimerar hyperparametrar för varje modell."""

        for name, model in self.models.items():
            try:
                # Använd GridSearchCV för att hitta bästa parametrarna
                grid = GridSearchCV(model, self.param_grids[name], cv=3)

                grid.fit(X_train, y_train)
                self.best_params[name] = grid.best_params_
                self.models[name] = grid.best_estimator_

            except Exception as e:
                print(f"Fel vid optimering av {name}: {e}")
        
        return self.best_params

    def compare_models(self, X_train: np.ndarray, X_test: np.ndarray,
                  y_train: np.ndarray, y_test: np.ndarray):
        """
        Jämför olika ML-modellers prestanda
        
        Args:
            X_train: Träningsdata (features)
            X_test: Testdata (features)
            y_train: Träningsetiketter
            y_test: Testetiketter
        
        Returns:
            best_model: Den bäst presterande modellen
        """
        # Initialisera variabler för att spåra bästa modellen
        best_score = 0
        best_model = None
        best_model_name = None

        # Iterera genom alla modeller för utvärdering
        for name, model in self.models.items():
            # Träna modellen på träningsdata
            model.fit(X_train, y_train)
            
            # Beräkna modellens accuracy på testdata
            score = model.score(X_test, y_test)
            self.scores[name] = score

            # Uppdatera bästa modellen om current score är högre
            if score > best_score:
                best_score = score
                best_model = model
                best_model_name = name

        return best_model, best_model_name

    def train_and_evaluate(self, X_train, X_test, y_train, y_test):
        """
        Genomför komplett träning och utvärdering av ML-modeller
        
        Returns:
            dict: Innehåller all träningsdata och resultat
        """
        try:
            # Optimera hyperparametrar
            self.optimize_hyperparameters(X_train, y_train)
            
            # Jämför och välj bästa modellen
            best_model, best_model_name = self.compare_models(X_train, X_test, y_train, y_test)
            
            # Kontrollera att en modell valdes framgångsrikt
            if best_model is None:
                raise ValueError("Ingen modell kunde tränas framgångsrikt")

            # Detaljerad utvärdering av bästa modellen
            accuracy = best_model.score(X_test, y_test)
            predictions = best_model.predict(X_test)
            conf_matrix = confusion_matrix(y_test, predictions)
            scores = {
                'MLP': self.models['MLP'].score(X_test, y_test),
                'SVM': self.models['SVM'].score(X_test, y_test),
                'RandomForest': self.models['RandomForest'].score(X_test, y_test)
            }
            
            return {
                'best_model': best_model,
                'best_model_name': best_model_name,
                'accuracy': accuracy,
                'conf_matrix': conf_matrix,
                'predictions': predictions,
                'scores': scores
            }
            
        except Exception as e:
            raise RuntimeError(f"Fel vid modellträning: {str(e)}")
        
