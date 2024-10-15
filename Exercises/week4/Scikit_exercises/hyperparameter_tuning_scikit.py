from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

# lada Wine-dataset
wine = load_wine()
X, y = wine.data, wine.target   # Separerar features (X) och målvariabel (y)

# dela upp data i tränings och testet
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# definiera ett parameterrutnät för Random Förest Classifier
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 3]
}

# skapa en Random Forest Classifier
rf = RandomForestClassifier(random_state=42)

# använd GridSearchCV för att hitta de bästa hyperparametrarna
# cv=5 betyder 5-faldig korsvalidering
# n_jobs=-1 använder alla tillgängliga processorkärnor
grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, n_jobs=-1, verbose=1)

# utför sökningen efter bästa parametrar
grid_search.fit(X_train, y_train)

# skriv ut de bästa parametrarna som hittades
print("Bästa parametrar:", grid_search.best_params_)

# träna en slutlig modell med de bästa hyperparametrarna
best_rf = grid_search.best_estimator_

# gör prediktioner på testdata
y_pred = best_rf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Noggrannhet på testdata: {accuracy:.4f}")

