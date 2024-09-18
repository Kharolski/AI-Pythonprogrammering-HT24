# Skriv ett program som för en given sträng skriver ut de två första och de två sista tecknen 
# i strängen (på valfritt format) Exempel-input: "banana" Förväntad output: "ba na"

# funktionen som returnerar första 2 och sista 2 char
def första_sista_tecken(user_input):
    if len(user_input) < 2:
        return "Strängen är för kort. "
    else:
        # Ta de två första och två sista tecknen
        first_string = user_input[:2]
        second_string = user_input[-2:]

        # Returnera dem i formatet 
        return f"{first_string} {second_string}"

input_string = input("Ange en sträng: ")
resultat = första_sista_tecken(input_string)
print(resultat)
