# Skriv ett program som tar två strängar som input och skapar en ny sträng där de två första tecken i varje sträng
# bytts ut. Exempel-input: "abc", "xyz" Förväntad output: "xyc abz"

def change_string(text1, text2):

    if len(text1) < 2 or len(text2) < 2:
        return "Båda strängarna måste vara minst två tecken långa."
    else:
        # Byt de två första tecknen i båda strängarna
        ny_sträng1 = text2[:2] + text1[2:]
        ny_sträng2 = text1[:2] + text2[2:]
        
        # Returnera de nya strängarna separerade med ett mellanslag
        return f"{ny_sträng1} {ny_sträng2}"

# Ta två strängar som input
input_text1 = input("Ange första strängen: ")
input_text2 = input("Ange andra strängen: ")

# Byt ut tecknen och skriv ut resultatet
resultat = change_string(input_text1, input_text2)
print(resultat)
