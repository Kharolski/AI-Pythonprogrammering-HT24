# Importera nödvändiga bibliotek
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from keras import callbacks
from keras import layers, models, datasets, utils


#    1. Ladda MNIST-dataset
# -------------------------------------------------------------------------------------------

# dataset innehåller 28x28 bilder av handskrivna siffror (0-9)
(X_train, y_train), (X_test, y_test) = datasets.mnist.load_data()

# Utforska datan
print(f"Träningsdata: {X_train.shape}. Träningsetiketter: {y_train.shape}")
print(f"Testdata: {X_test.shape}, Testetiketter: {y_test.shape}")

#   2. Förbehandla data
# -------------------------------------------------------------------------------------------

# CNN fungerar bättre när alla värden ligger i samma skala och förväntar sig en 4D input: (antal bilder, bredd, höjd, kanaler)
# Eftersom MNIST är gråskala (1 kanal), behöver vi lägga till en extra dimension
# # Normalisera pixelvärden (från intervallet 0-255 till 0-1) genom / 255.0
X_train = X_train.reshape((X_train.shape[0], 28, 28, 1)) / 255.0
X_test = X_test.reshape((X_test.shape[0], 28, 28, 1)) / 255.0

# Detta är nödvändigt för att matcha nätverkets output för klassificering
y_train = utils.to_categorical(y_train, 10)
y_test = utils.to_categorical(y_test, 10)


#   3. Skapa CNN-modellen
# --------------------------------------------------------------------------------------------

# Starta en sekventiell modell
model = models.Sequential()

# använder ett Input-lager separat istället för att ange input_shape direkt i första lagret att slipa varning rekomendation
# Input(shape) specificerar formen på varje bild (28x28 pixlar och 1 kanal)
model.add(layers.Input(shape=(28,  28, 1)))

# 32 filter, storlek 3x3 och ReLU-aktiveringsfunktion. 
model.add(layers.Conv2D(32, (3, 3), activation='relu'))

# Maxpooling minskar bildens dimensioner (28x28 blir 14x14), vilket hjälper till att reducera komplexiteten
model.add(layers.MaxPooling2D((2, 2)))

# Lägg till ett till convolution-lager och pooling-lager
# Detta hjälper modellen att lära sig mer komplexa mönster
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

# Lägger till ytterligare ett convolution-lager utan pooling
# Detta ökar modellens djup och förmåga att lära sig mer detaljer
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

# Flatten lagret omformar den 3D-bildrepresentationen till en 1D-vektor
# Det här är nödvändigt innan vi lägger till täta (dense) lager
model.add(layers.Flatten())

# Lägger till ett dense lager med 64 noder och ReLU-aktiveringsfunktion
# Detta är ett fullständigt anslutet lager som behandlar den omformade bilden
model.add(layers.Dense(64, activation='relu'))

# Lägger till det slutliga output-lagret med 10 noder (en för varje siffra 0-9)
# Softmax-aktiveringsfunktionen konverterar output till sannolikheter för varje klass
model.add(layers.Dense(10, activation='softmax'))

# den model man kunde skriva lättare så här:
'''
model = models.Sequential([
    layers.Input(shape=(28, 28, 1)),
    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])
'''

#   4. Kompilera modellen
# ---------------------------------------------------------------------------------------------------------

# För binär klassificering skulle vi använda "binary_crossentropy", men här använder vi "categorical_crossentropy"
# eftersom det är flerklass-klassificering (10 klasser).
# Vi använder Adam som optimerare eftersom det fungerar bra i många praktiska problem.
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Visa en sammanfattning av modellen för att se dess arkitektur
model.summary()


#   5. Träna modellen
# ---------------------------------------------------------------------------------------------------------------

# Lägger till callbacks som EarlyStopping för att spara den bästa modellen och förhindra överträning.
early_stopping = callbacks.EarlyStopping(monitor='val_loss', patience=3)

# Vi tränar modellen på träningsdatan, använder 10% av den för validering (validation_split=0.1) och
# lägger till en callback (early_stopping) för att stoppa träningen tidigt om valideringsfelet slutar förbättras.
history = model.fit(X_train, y_train, epochs=5, batch_size=64, validation_split=0.1, callbacks=[early_stopping])

# Visualisera träningshistorik
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()

plt.tight_layout()
plt.show()


#   6. Utvärdera modellen på testdatan
# --------------------------------------------------------------------------------------------------------------

# Detta ger oss en uppfattning om hur bra modellen fungerar på osedda data
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {test_acc:.4f}")


# 7. Visa några felklassificerade exempel
# ---------------------------------------------------------------------------------------------------------------

# Gör förutsägelser på testdatan
y_pred = model.predict(X_test)

# Omvandla one-hot encoded predictions och labels till faktiska siffror
y_pred_classes = np.argmax(y_pred, axis=1)
y_true = np.argmax(y_test, axis=1)

# Hitta index för felklassificerade bilder
errors = np.where(y_pred_classes != y_true)[0]

# dem 3 råder av kod kan man skriva:
# errors = np.where(np.argmax(y_pred, axis=1) != np.argmax(y_test, axis=1))[0]

# Visualisera några av felklassificeringarna
print(f"Antal felklassificerade bilder: {len(errors)}")

# Visa de första 5 felklassificerade bilderna
fig, axes = plt.subplots(1, 5, figsize=(15, 5))
for i, ax in enumerate(axes.flat):
    error_idx = errors[i]
    ax.imshow(X_test[error_idx].reshape(28, 28), cmap='grey')
    ax.set_title(f"Pred: {y_pred_classes[error_idx]}, True: {y_true[error_idx]}")
    ax.axis('off')

plt.tight_layout()
plt.show()



