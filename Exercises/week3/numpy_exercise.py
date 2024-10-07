#
# NumPy-övningar

# 1. - Skapa en 3x3 matris av slumpmässiga heltal mellan 1 och 10.
# 2. - Utför elementvis multiplikation av två 4x4 matriser.
# 3. - Använd NumPy för att lösa ett system av linjära ekvationer (Ax = b).
# 4. - Generera en array med 1000 prover från en binomialfördelning med n=10 och p=0,5.
# 5. - Skapa en 5x5 identitetsmatris och ersätt sedan dess diagonal med en anpassad array.

import numpy as np

class NumpyExercises:
    def __init__(self):
        pass

    # 1. Skapa en 3x3 matris av slumpmässiga heltal mellan 1 och 10
    def random_matrix(self):
        # np.random.randint() skapar slumpmässiga heltal och size=(3, 3): skapar en 3x3 matris
        matrix = np.random.randint(1, 11, size=(3, 3))

        print("1. 3x3 matris av slumpmässiga heltal:")
        print(matrix)
        print("\n")

    # 2. Multiplikation av två 4x4 matriser
    def matrix_multiplication(self):
        # Skapa två 4x4 matriser
        matrix1 = np.random.randint(1, 11, size=(4, 4))
        matrix2 = np.random.randint(1, 11, size=(4, 4))

        # Utför elementvis multiplikation
        result = matrix1 * matrix2

        print("2. Elementvis multiplikation av två 4x4 matriser:")
        print("Matris 1:")
        print(matrix1)
        print("Matris 2:")
        print(matrix2)
        print("Resultat:")
        print(result)
        print("\n")

    # 3. Lösa ett system av linjära ekvationer (Ax = b)
    # np.linalg.solve() löser ekvationssystemet Ax = b
    def solve_linear_equations(self):
        A = np.array([[2, 1, -1],       # A är koefficient-matrisen
                      [1, 3, 2],
                      [-1, 2, 4]])
        b = np.array([8, 14, 18])       # b är konstant-vektorn

        # Lös ekvationssystemet
        x = np.linalg.solve(A, b)       # x är lösningsvektorn som returneras

        print("3. Lösning av linjärt ekvationssystem:")
        print("A:", A)
        print("b:", b)
        print("Lösning x:", x)
        print("\n")

    # 4. Generera 1000 prover från en binomialfördelning
    # np.random.binomial() genererar prover från en binomialfördelning
    def binomial_distribution(self):
        # n=10: antal försök
        # p=0.5: sannolikhet för framgång i varje försök
        # size=1000: antal prover att generera
        samples = np.random.binomial(n=10, p=0.5, size=1000)

        print("4. Prover från binomialfördelning:")
        print("Första 10 prover:", samples[:10])
        print("Medelvärde:", np.mean(samples))
        print("Standardavvikelse:", np.std(samples))
        print("\n")

    # 5. 5x5 identitetsmatris och ersätt sedan
    # np.eye() skapar en identitetsmatris (1:or på diagonalen, 0:or annars)
    # np.fill_diagonal() ersätter diagonalen med de angivna värdena
    def custom_identity_matrix(self):
        # Skapa en 5x5 identitetsmatris
        identity = np.eye(5)

        # Skapa en anpassad array för diagonalen
        diagonal = np.array([1, 2, 3, 4, 5])

        # Ersätt diagonalen
        np.fill_diagonal(identity, diagonal)

        print("5. Anpassad identitetsmatris:")
        print(identity)


def main():
    exercises = NumpyExercises()

    exercises.random_matrix()
    exercises.matrix_multiplication()
    exercises.solve_linear_equations()
    exercises.binomial_distribution()
    exercises.custom_identity_matrix()






if __name__ == "__main__":
    main()