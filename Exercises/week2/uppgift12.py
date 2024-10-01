# både map() och filter() uppgifterna

def double(x):
    return x * 2

def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Använder map() för att dubbla varje tal i listan
# map() = map(function, iterable)
doubled_numbers = list(map(double, numbers))
print(doubled_numbers)


# Använder filter() för att filtrera ut jämna tal
# filter(function, iterable)
even_number = list(filter(is_even, numbers))
print(even_number)

print("----------------------------------------")

# Använder map() med en lambda-funktion för double
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(doubled_numbers)


# Använder filter() med en lambda-funktion för is_even
even_number = list(filter(lambda x: x % 2 == 0, numbers))
print(even_number)
