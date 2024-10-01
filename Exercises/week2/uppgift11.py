
# 1. Skapa en lista med kvadrater av talen 1 till 10.
squares = [x ** 2 for x in range(1, 11)]
print(squares)

# 2. Filtrera ut alla jämna tal från en given lista:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
event_numbers = [x for x in numbers if x % 2 == 0]
print(event_numbers)

# 3. Skapa en lista med längden av varje ord i en given mening:
sentence = "Python är ett kraftfullt programmeringsspråk"
word_length = [len(word) for word in sentence.split()]
print(word_length)

# 4. Lista med kuber av talen 1 till 10:
cubes = [x ** 3 for x in range(1, 11)]
print(cubes)

# 5. Filtrera ut alla udda tal:
odd_numbers = [x for x in numbers if x % 2 != 0]
print(odd_numbers)

# 6. Filtrera ut ord som är längre än 5 bokstäver:
long_word = [word for word in sentence.split() if len(word) > 5]
print(long_word)








