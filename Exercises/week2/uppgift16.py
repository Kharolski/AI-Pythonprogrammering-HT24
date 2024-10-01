# List comprehensions vs. for-loopar

# 1. En lista med alla tal mellan 1 och 100 som är delbara med 3 eller 5.

#       List comprehension:
divisible_by_3_or_5 = [x for x in range(1, 101) if x % 3 == 0 or x % 5 == 0]
print(divisible_by_3_or_5)

#       For-loop version:
divisible_by_3_or_5 = []
for i in range(1, 101):
    if i % 3 == 0 or i % 5 == 0:
        divisible_by_3_or_5.append(i)

print(divisible_by_3_or_5)


# 2. en lista med tupler (x, y) för alla x och y där 0 <= x < 5 och 0 <= y < 5.

#       List comprehension:
tuple_list = [(x, y) for x in range(5) for y in range(5)]
print(tuple_list)

#       For-loop version:
tuple_list = []
for x in range(5):
    for y in range(5):
        tuple_list.append((x, y))

print(tuple_list)
