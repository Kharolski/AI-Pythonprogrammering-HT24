# Enkla lambda-funktioner 

# 1. Skriv en lambda-funktion som returnerar kvadraten av ett tal.
square = lambda x: x ** 2
print(square(5))


# 2. Använd sorted() med en lambda-funktion för att sortera en lista av tupler baserat på det andra elementet.
tuple_list = [(1, 'b'), (3, 'a'), (2, 'c')]
sorted_tuples = sorted(tuple_list, key=lambda x: x[1]) # returnerar det andra elementet (x[1]) för sortering.
print(sorted_tuples)


# 3. Använd filter() med en lambda-funktion för att filtrera ut negativa tal från en lista.
numbers = [5, -3, 2, -8, 7, -1, 0]
positiva_numbers = list(filter(lambda x: x >= 0, numbers))
print(positiva_numbers)

# sorterar positiva numbers
sorted_positiva_numbers = list(sorted(filter(lambda x: x >= 0, numbers)))
print(sorted_positiva_numbers)









