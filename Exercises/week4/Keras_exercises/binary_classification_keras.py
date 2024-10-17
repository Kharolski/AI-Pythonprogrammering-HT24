# Övning 2: Binär klassificering med Keras

# Data: Använd Breast Cancer Wisconsin-datasetet från Scikit-learn.
# Uppgift: Bygg ett neuralt nätverk för binär klassificering för att förutsäga om en tumör är elakartad eller godartad.

# Steg:
# 1: Ladda Breast Cancer-datasetet med sklearn.datasets.load_breast_cancer().
# 2: Normalisera egenskapsdata med sklearn.preprocessing.StandardScaler.
# 3: Skapa en sekventiell modell i Keras med två täta lager och en binär output.
# 4: Kompilera modellen med binär korsentropiförlust och träna den på data.
# 5: Utvärdera modellens noggrannhet på ett testset.

import numpy as np
import tensorflow as tf
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split    # För att dela upp data i tränings- och testset
from sklearn.preprocessing import StandardScaler        # För att normalisera datan (Standardisering)

# Ladda data
data = load_breast_cancer()
X, y = data.data, data.target

# Dela upp data och normalisera
X_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(x_test) 

# Skapa och kompilera modellen
model = tf.keras.Sequential([

    # Dense(16) har 16 neuroner i detta lager
    # activation='relu' innebär att vi använder ReLU som aktiveringsfunktion
    tf.keras.layers.Dense(16, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(8, activation='relu'),

    # activation='sigmoid' används i utgångslagret för binär klassificering
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Träna modellen
# batch_size=32 betyder att vi tränar på 32 exempel åt gången
# epochs=50 betyder att vi tränar modellen i 50 omgångar
model.fit(X_train_scaled, y_train, epochs=50, batch_size=32, validation_split=0.2, verbose=1)

# Utvärdera modellen
test_loss, test_accuracy = model.evaluate(X_test_scaled, y_test, verbose=0)
print(f"Test accuracy: {test_accuracy:.2f}")









