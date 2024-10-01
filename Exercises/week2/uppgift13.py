# 1.Skapa en lista med kvadrater av alla jämna tal i en given lista.

# Funktion för att kontrollera om ett tal är jämnt
def is_even(x):
    return x % 2 == 0

# Lista med tal
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Använd filter() för att filtrera ut jämna tal
even_number = list(filter(is_even, numbers))

# Använd map() för att kvadrera de jämna talen
squered_even_numbers = list(map(lambda x: x ** 2, even_number))

print(squered_even_numbers)
print("---------------------------------------------------")

# 2. Filtrera ut alla primtal från en lista med tal.

# Funktion för att kontrollera om ett tal är ett primtal
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % 2 == 0:
            return False
    return True


# Lista med tal
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Använd filter() för att filtrera ut primtal
prime_numbers = list(filter(is_prime, numbers))
print(prime_numbers)

print("----------------------------------------------------")

# Dessa funktioner kan skrivas om med lambda-funktioner 
# om man vill ha en mer kompakt syntax:

# Med lambda för jämna kvadrater
squered_even_numbers = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(squered_even_numbers)

# Med lambda för att filtrera primtal (dock blir lambda här lite komplicerat 
# så bättre med separat funktion)
prime_numbers = list(filter(lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1)), numbers))
print(prime_numbers)