# Uppgift 2 Skriv ett program som skriver ut frekvensen av tecken i en given sträng. Exempel-input: "banana"
# Förväntad output: {"b":1, "a":3, "n":2}


def frekvensen(text):
    frekv = {}

    # Loopa genom varje tecken i strängen
    for tecken in text:
        # Om tecknet redan finns i ordboken, öka värdet med 1
        if tecken in frekv:
            frekv[tecken] += 1
        # Annars, lägg till tecknet med värdet 1
        else:
            frekv[tecken] = 1

    return frekv

input_text = input("Enter en sträng att se frekvensen av tecken:")
resultat = frekvensen(input_text)

if len(resultat) != str(""):
    print(f"Length på string du skrivit är: {resultat}")
else:
    print("Du har inte skrivit några characters")