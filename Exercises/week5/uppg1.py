# Importera nödvändiga bibliotek
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import mean_squared_error, root_mean_squared_error, root_mean_squared_log_error     # MSE, RMSE, RMSLE
'''
Mått    |	            Fokus           	 |              När används det?                       |
----------------------------------------------------------------------------------------------------
MSE     |	Kvadratiska fel, straffar stora  |  När du vill mäta den genomsnittliga avvikelsen     |
        |   fel mer.	                     |  med kvadrerade fel, och du bryr dig om stora fel.  |
----------------------------------------------------------------------------------------------------        
RMSE    |	Samma som MSE, men återgår till  |  När du vill ha ett felmått i samma enhet som de    |
        |   samma enhet som målet.	         |  faktiska värdena och är känslig för stora fel.     |
----------------------------------------------------------------------------------------------------        
RMSLE   |	Logaritmiska fel, dämpar         |  När du vill fokusera på relativa skillnader eller  |
        |   effekten av stora värden.	     |  när data innehåller exponentiell tillväxt.         |
----------------------------------------------------------------------------------------------------        
'''

# ladda data 
housing = fetch_california_housing()

# för att förstå datastrukturen vi printar ut nycklar
print(housing.keys())

X, y = housing.data, housing.target

# Dela upp data i tränings- och testset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Skapa linjär regressionsmodell
model = LinearRegression()

# Träna modellen på träningsdata
model.fit(X_train, y_train)

# Gör förutsägelser på testdatan
y_pred = model.predict(X_test)

# Beräkna och vi testar alla 3 
mse = mean_squared_error(y_test, y_pred)
mse1 = root_mean_squared_error(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"Root Mean Squared Error: {mse1:.2f}")

def negative_and_zero_check(y_train, y_test, y_pred):
    """
    Kontrollerar om det finns negativa värden eller nollor i y_train, y_test och y_pred.
    
    Parameters:
        y_train (np.array): Träningsdata.
        y_test (np.array): Testdata.
        y_pred (np.array): Predikterade värden.
    
    Returns:
        dict: Innehåller boolean-värden för negativa värden och nollor.
    """
    has_neg_train = np.any(y_train < 0)
    has_neg_test = np.any(y_test < 0)
    has_neg_pred = np.any(y_pred < 0)

    has_zero_train = np.any(y_train == 0)
    has_zero_test = np.any(y_test == 0)
    has_zero_pred = np.any(y_pred == 0)

    return {
        'neg_train': has_neg_train,
        'neg_test': has_neg_test,
        'neg_pred': has_neg_pred,
        'zero_train': has_zero_train,
        'zero_test': has_zero_test,
        'zero_pred': has_zero_pred
    }

# Lagrar resultatet från negative_and_zero_check
results = negative_and_zero_check(y_train, y_test, y_pred)

# Hanterar negativa resultat
if results['neg_train'] or results['neg_test']:
    print("Negativa värden finns i träning eller test data. RMSLE kan inte beräknas.")
elif results['neg_pred']:
    print("Negativa värden finns i prediktionerna. Vi använder np.clip() innan vi beräknar RMSLE.")
    # Clipar negativt värden i prediktioner
    y_pred = np.clip(y_pred, a_min=1e-10, a_max=None)
    rmsle = root_mean_squared_log_error(y_test, y_pred)
    print(f"Root Mean Squared Logarithmic Error: {rmsle:.2f}")
else:
    # Om det inte finns negativa värden, fortsätt med RMSLE
    rmsle = root_mean_squared_log_error(y_test, y_pred)
    print(f"Root Mean Squared Logarithmic Error: {rmsle:.2f}")


# Skapa ett spridningsdiagram för att visualisera de faktiska vs. förutsagda priserna
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--r', lw=2)
plt.xlabel('Faktiska priser')
plt.ylabel('Förutsagda priser')
plt.title('Faktiska vs. Förutsagda huspriser')
plt.tight_layout()
plt.show()




