# Importera och använd functools.reduce()

from functools import reduce

# 1. Beräkna produkten av alla tal i en lista.
numbers = [1, 2, 3, 4, 5]
product_of_numbers = reduce(lambda x, y: x * y, numbers)
print(product_of_numbers)


# 2. Hitta det största talet i en lista.
second_numbers = [3, 7, 2, 8, 1, 9, 4]
largest_number = reduce(lambda x, y: x if x > y else y, second_numbers)
print(largest_number)


