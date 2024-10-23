'''
Övning 2: Logistisk Regression för Binär Klassificering

Implementera logistisk regression för att klassificera iris-blommor.

1. Ladda iris-datasetet från Scikit-learn.
2. Välj endast två klasser för binär klassificering (t.ex. versicolor och virginica).
3. Dela upp data i tränings- och testset.
4. Skapa och träna en logistisk regressionsmodell.
5. Utvärdera modellen med accuracy, precision, recall och F1-score.
'''

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Ladda datasetet
iris = load_iris()
X = iris.data       # Funktioner (de olika egenskaperna hos blommorna)
y = iris.target     # Klasserna (typ av iris-blomma)

# först vi kolla hur många klasser och vilken index är versicolor och virginica
print(iris.keys())
print(iris['target_names'])
print(iris.target_names[0])     # Setosa är klass 0

# Vi skapar en mask för att filtrera ut de två klasserna
mask = y != 0           # Vi ignorerar setosa (klass 0)
X_binary = X[mask]
y_binary = y[mask] - 1  # Omvandla klasserna till 0 och 1 (versicolor = 0, virginica = 1)

# Dela upp data i tränings- och testset
X_train, X_test, y_train, y_test = train_test_split(X_binary, y_binary, test_size=0.2, random_state=42)

# Skapa logistisk regressionsmodell
model = LogisticRegression()

# Träna model
model.fit(X_train, y_train)

# Göra förutsägelser
y_pred = model.predict(X_test)

# Beräkna utvärderingsmått
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# Skriv ut resultaten
print(f'Accuracy: {accuracy:.2f}')
print(f'Precision: {precision:.2f}')
print(f'Recall: {recall:.2f}')
print(f'F1 Score: {f1:.2f}')

