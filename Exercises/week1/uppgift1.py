# Uppgift 1
# Skriv ett program som emot en sträng som input och skriver ut längden på strängen. Exempel-input: "thisIsAString"
# Förväntad output: 13


user_input = input("Enter a string: ")
default_string = "thisIsAString"

if len(user_input) == 0:
    print(f"You didn't enter any characters. The default string is \"{default_string}\" "
          f"with length {len(default_string)}")
else:
    print(f"The length of the entered string is {len(user_input)}")
