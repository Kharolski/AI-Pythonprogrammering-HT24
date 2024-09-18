# intro_python.py

# 1. Basic syntax, kommentarer, printing

print("Hej, klassen")   # Printa i Python

# 2. Variabler och datatyper
x = 30               # int
y = 3.14            # float
name = "Python"     # string
is_fun = True       # boolian

# 3. Type checking, typkonvertering
print(type(x))

z = str(x)
print(type(z))

a = "10"
b = int(a) + 1
print(b)

#  4. String operations
print(len("Bertil"))
print(name.upper())
print(name.lower())
print("   spaces   ".strip())

# 5. String format
print(f"My name is {name}, i'm {x} years old")
print("Pi is approximately {:.2f}".format(y))

# 6. Lists
fruits = ["apple", "banana", "cherry", "apple"]
print(fruits[2])
fruits.append("date")
print(fruits)

fruits.insert(0, "strawberry")
print(fruits)

# 7. Dictionaries
personal_dict1 = {"name": "Bob", "age": 30, "city": "New York"}
print(personal_dict1["name"])

personal_dict1["jobb"] = "Developer"
print(personal_dict1)

personal_dict2 = {"name": "Alice", "age": 20, "city": "Stockholm"}

personal_list = []      # = list()
personal_list.append(personal_dict1)
personal_list.append(personal_dict2)

print(personal_list)

# 8. Sets
unique_numbers = {1, 2, 3, 4, 5, 6, 5, 6}
print(unique_numbers)

unique_fruits = set(fruits)
print(unique_fruits)

# 9. Input från användare
username_input = input("Enter your name: ")
print(f"You enter username: {username_input}")


# 10. Conditionals
age = 20
if age >= 18:
    print("Du får gå på klubb")
elif age >= 13:
    print("Du är tonåring")
else:
    print("Du är ett barn")

if username_input == str(""):
    print("You are not enter any charectar")

# 11. Loops
# For loops
for fruit in fruits:
    print(fruit)

count = 0
while count  < 5:
    print(count)
    count = count + 1

print("Range loop")

for i in range(5):      # range(5) = [0, 1, 2, 3, 4]
    print(i)


# Functions
def Greet(name):
    #print(f"Hello, {name}!")
    return f"Hello, {name}!"    # med return då måste vi printa ut eller store till en variable och sedan printa ut

greetings = Greet("Calle")
print(greetings)

print(Greet("Calle"))