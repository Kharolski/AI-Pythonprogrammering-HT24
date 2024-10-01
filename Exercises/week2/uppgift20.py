import numpy as np

# 1: Skapa två 3x3 matriser med slumpmässiga heltal
matrix_a = np.random.randint(1, 10, size=(3, 3))
matrix_b = np.random.randint(1, 10, size=(3, 3))

print("Matriser:")
print("Matrix A:\n", matrix_a)
print("Matrix B:\n", matrix_b)

# 2: Beräkna produkten av matriserna
product = np.dot(matrix_a, matrix_b)

# Alternativt kan man använda @-operatorn:
# product = matrix_a @ matrix_b

print("Produkten av Matrix A och Matrix B:\n", product)

# 3: Beräkna determinanten av den resulterande matrisen
determinant = np.linalg.det(product)

print("Determinanten av den resulterande matrisen:", determinant)




