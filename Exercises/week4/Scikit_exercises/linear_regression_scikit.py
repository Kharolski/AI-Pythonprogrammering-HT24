
# Data: Använd Boston Housing-datasetet från Scikit-learn.
# Uppgift: Skapa en enkel linjär regressionsmodell för att förutsäga huspriser.

# Steg:
# 1. Ladda Boston Housing-datasetet med sklearn.datasets.load_boston().
# 2. Dela upp data i tränings- och testset.
# 3. Skapa en LinearRegression-modell och anpassa den till träningsdata.
# 4. Gör förutsägelser på testsettet och beräkna genomsnittligt kvadratfel (MSE).

# nödvändiga bibliotek
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split    # Dela upp data i tränings- och testset
from sklearn.linear_model import LinearRegression       # Skapa en linjär regressionsmodell
from sklearn.metrics import mean_squared_error          # För att beräkna medelkvadratfel (MSE)


# 1: Ladda Boston Housing-datasetet
# 'load_boston' innehåller information om bostadspriser.
california = fetch_california_housing()

# Boston Housing-datasetet har två huvuddelar:
# - boston.data: De oberoende variablerna (features) som vi använder för att göra förutsägelser
# - boston.target: Det är den beroende variabeln (målvariabeln) som representerar bostadspriser
X = california.data     # Funktioner (input)
y = california.target   # Målvariabel (output)

# 2: Dela upp data i tränings- och testset
# test_size=0.2 betyder att 20% av data används för test och 80% för träning
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3: Skapa en LinearRegression-modell och anpassa den till träningsdata
model = LinearRegression()
# Lär modellen sig att koppla ihop features (oberoende variabler) med målvariabeln (priset).
model.fit(X_train, y_train) # Träna modellen på träningsdata

# 4: Gör förutsägelser på testsettet
y_pred = model.predict(X_test)

# Beräkna genomsnittligt kvadratfel (MSE)
mse = mean_squared_error(y_test, y_pred)

print(f"Genomsnittligt kvadratfel (MSE): {mse:.2f}")

# Modellens koefficienter (viktning för varje variabel) och intercept (skärningspunkten)
for feature, coef in zip(california.feature_names, model.coef_):
    print(f"{feature}: {coef:.4f}")
print(f"Intercept: {model.intercept_:.4f}")















