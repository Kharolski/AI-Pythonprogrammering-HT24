# 1. Importera nödvändiga bibliotek

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from tensorflow import keras
from keras import models, layers, Sequential

# I detta exempel vi kommer att använda Air Passengers-datasetet (som visar antalet passagerare per månad över en tid) 

# 2. Ladda Air Passengers dataset
# ---------------------------------------------------------------------------------
# Vi använder pandas för att läsa in data. Alternativt kan man skapa en syntetisk tidsserie
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv"
data = pd.read_csv(url, usecols=[1])  # Vi tar endast passagerarkolumnen

# 3. Förbehandla tidsseriedata
# ---------------------------------------------------------------------------------
# Normalisera data för att få alla värden mellan 0 och 1, vilket förbättrar modellens träning
scaler = MinMaxScaler(feature_range=(0, 1))
scaler_data = scaler.fit_transform(data)

# Skapa input-output-sekvenser för LSTM. Vi vill skapa par av (X, y) där X är tidigare 
# datapunkter och y är nästa värde i sekvensen.
# Här använder vi ett fönster på 10 tidssteg som input för att förutsäga nästa värde.
def create_sequences(data, seq_lenght):
    X, y = [], []
    for i in range(len(data) - seq_lenght):
        X.append(data[i:i + seq_lenght])
        y.append(data[i + seq_lenght])
    return np.array(X), np.array(y)

sequence_length = 10    # Vi använder de senaste 10 månadernas data för att förutsäga nästa
X, y = create_sequences(scaler_data, sequence_length)

# Omforma input (X) för att vara 3D, eftersom LSTM förväntar sig input i formatet [samples, timesteps, features]
X = X.reshape((X.shape[0], X.shape[1], 1))

# 4. Skapa LSTM-modellen
# ---------------------------------------------------------------------------------
model = models.Sequential([
    layers.Input(shape=(sequence_length, 1)),      # 'input_shape' anger att vi har en sekvens med 'sequence_length' och 1 feature (passagerardata)
    layers.LSTM(50, return_sequences=False),       # LSTM-lager med 50 neuroner. 
    layers.Dense(1)                                # Lägg till ett dense-lager för att producera output-värdet
])

# Kompilera modellen med MSE (Mean Squared Error) som förlustfunktion, eftersom det är en regressionsuppgift
model.compile(optimizer='adam',
              loss='mean_squared_error')

# 5. Träna modellen
# ---------------------------------------------------------------------------------
# Dela upp datasetet i träning och test
train_size = int(len(X) * 0.8)
X_train, y_train = X[:train_size], y[:train_size]
X_test, y_test = X[train_size:], y[train_size:]

# Träna modellen på träningsdatan i 20 epoker med en batch-storlek på 32
history = model.fit(X_train, y_train, epochs=20, batch_size=32, validation_data=(X_test, y_test))

# 6. Utvärdera och göra framtida förutsägelser
# ---------------------------------------------------------------------------------
# Förutsäg testdata för att se hur modellen presterar
predictions = model.predict(X_test)

# Omvandla förutsägelserna och den faktiska testdatan tillbaka till den ursprungliga skalan
predictions = scaler.inverse_transform(predictions)
y_test_scaled = scaler.inverse_transform(y_test.reshape(-1, 1))

# Beräkna och skriv ut felvärdet (MSE) mellan de förutsagda och faktiska värdena
mse = mean_squared_error(y_test_scaled, predictions)
print(f"Mean Squared Error på testdatan: {mse:.4f}")


# Skapa framtida prediktioner
last_sequence = X_test[-1]
future_predictions = []

for _ in range(12):  # Prediktera 12 månader framåt
    next_pred = model.predict(last_sequence.reshape(1, sequence_length, 1))
    future_predictions.append(next_pred[0, 0])
    last_sequence = np.roll(last_sequence, -1)
    last_sequence[-1] = next_pred

future_predictions = scaler.inverse_transform(np.array(future_predictions).reshape(-1, 1))

# Skapa en figur med 4 subplots
fig, axs = plt.subplots(2, 2, figsize=(20, 15)) # justera figsize om man behöver ändra storleken på figuren för bättre läsbarhet
fig.suptitle('LSTM Model for Time Series Forecasting', fontsize=16)

# Plot 1: Tränings- och valideringsförlust
axs[0, 0].plot(history.history['loss'], label='Training Loss')
axs[0, 0].plot(history.history['val_loss'], label='Validation Loss')
axs[0, 0].set_title('Model Loss')
axs[0, 0].set_xlabel('Epoch')
axs[0, 0].set_ylabel('Loss')
axs[0, 0].legend()

# Plot 2: Faktiska vs. förutsagda värden (testdata)
axs[0, 1].plot(y_test_scaled, label="Actual Values", color='blue')
axs[0, 1].plot(predictions, label="Predicted Values", color='red')
axs[0, 1].set_title('Actual vs Predicted Passenger Numbers (Test Data)')
axs[0, 1].set_xlabel('Time Step')
axs[0, 1].set_ylabel('Passenger Count')
axs[0, 1].legend()

# Plot 3: Hela datasetet med framtida prediktioner
full_data = scaler.inverse_transform(scaler_data)
axs[1, 0].plot(range(len(full_data)), full_data, label='Historical Data')
axs[1, 0].plot(range(len(full_data), len(full_data) + len(future_predictions)), future_predictions, label='Future Predictions')
axs[1, 0].set_title('Full Dataset with Future Predictions')
axs[1, 0].set_xlabel('Time')
axs[1, 0].set_ylabel('Passenger Count')
axs[1, 0].legend()

# Plot 4: Felfördelning
errors = y_test_scaled - predictions
axs[1, 1].hist(errors, bins=25)
axs[1, 1].set_title('Error Distribution')
axs[1, 1].set_xlabel('Prediction Error')
axs[1, 1].set_ylabel('Frequency')

# Justera layouten och visa figuren
plt.tight_layout()
plt.show()

# Skriv ut MSE
print(f"Mean Squared Error on test data: {mse:.4f}")



