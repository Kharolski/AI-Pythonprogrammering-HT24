# Skriv ett program som tar två strängar som input och skapar en ny sträng där de två första tecken i varje sträng
# bytts ut. Exempel-input: "abc", "xyz" Förväntad output: "xyc abz"

def change_string(text1, text2):

    if len(text1) < 2 or len(text2) < 2:
        return "Båda strängarna måste vara minst två tecken långa."
    else:
        # Byt de två första tecknen i båda strängarna
        ny_string1 = text2[:2] + text1[2:]
        ny_string2 = text1[:2] + text2[2:]

        return f"{ny_string1} {ny_string2}"

# Användarens input
input_text1 = input("Ange första strängen: ")
input_text2 = input("Ange andra strängen: ")

resultat = change_string(input_text1, input_text2)
print(resultat)
