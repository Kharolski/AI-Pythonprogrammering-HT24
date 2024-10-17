# Importera nödvändiga bibliotek
import numpy as np
import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# 1: Ladda Iris-datasetet
iris = load_iris()
X = iris.data  # Egenskaper 
y = iris.target  # Målvariabel 

# 2: One-hot-koda målvariabeln
# Konverterar målvariabeln till en binär matris
y_onehot = tf.keras.utils.to_categorical(y)

# Dela upp data i tränings- och testset
# 80% för träning, 20% för test
X_train, X_test, y_train, y_test = train_test_split(X, y_onehot, test_size=0.2, random_state=42)

# Normalisera data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 3: Bygg TensorFlow-modellen
model = tf.keras.Sequential([
    # Första dolda lagret med 10 neuroner och ReLU-aktivering
    tf.keras.layers.Dense(10, activation='relu', input_shape=(4,)),
    # Andra dolda lagret med 10 neuroner och ReLU-aktivering
    tf.keras.layers.Dense(10, activation='relu'),
    # Utgångslagret med 3 neuroner (en för varje klass) och softmax-aktivering
    tf.keras.layers.Dense(3, activation='softmax')
])

# Kompilera modellen
model.compile(optimizer='adam',  # Adam-optimerare för att justera vikter
              loss='categorical_crossentropy',  # Förlustfunktion för flerklass-klassificering
              metrics=['accuracy'])  # Mätvärde för att övervaka under träning

# Steg 4: Träna modellen
history = model.fit(X_train_scaled, y_train, 
                    epochs=50,  # Antal träningsiterationer
                    batch_size=32,  # Antal exempel som processas i varje iteration
                    validation_split=0.2,  # 20% av träningsdata används för validering
                    verbose=1)  # Visa träningsförloppet

# Plotta träningshistoriken
plt.figure(figsize=(12, 4))

# Plotta noggrannhet
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Träningsnoggrannhet')
plt.plot(history.history['val_accuracy'], label='Valideringsnoggrannhet')
plt.title('Modellnoggrannhet')
plt.xlabel('Epoch')
plt.ylabel('Noggrannhet')
plt.legend()

# Plotta förlust
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Träningsförlust')
plt.plot(history.history['val_loss'], label='Valideringsförlust')
plt.title('Modellförlust')
plt.xlabel('Epoch')
plt.ylabel('Förlust')
plt.legend()

plt.tight_layout()
plt.show()

# Steg 5: Gör förutsägelser på testset
y_pred = model.predict(X_test_scaled)
# Konvertera sannolikheter till klassindex
y_pred_classes = np.argmax(y_pred, axis=1)
y_true_classes = np.argmax(y_test, axis=1)

# Skapa förvirringsmatris
cm = confusion_matrix(y_true_classes, y_pred_classes)

# Plotta förvirringsmatris
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Förvirringsmatris')
plt.xlabel('Förutsagd klass')
plt.ylabel('Sann klass')
plt.show()

# Skriv ut klassificeringsrapport
print(classification_report(y_true_classes, y_pred_classes, target_names=iris.target_names))
