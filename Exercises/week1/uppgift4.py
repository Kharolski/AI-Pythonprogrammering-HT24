# Skriv ett program som tar två strängar som input och skapar en ny sträng där de två första tecken i varje sträng
# bytts ut. Exempel-input: "abc", "xyz" Förväntad output: "xyc abz"

def change_string(text1, text2):

    if len(text1) < 3 or len(text2) < 3:
        return "Båda strängarna måste vara minst tre tecken långa."
    else:
        # Swap the first two characters in both strings
        new_string1 = text2[:2] + text1[2:]
        new_string2 = text1[:2] + text2[2:]

        return f"{new_string1} {new_string2}"

# Användarens input
input_text1 = input("Ange första strängen: ")
input_text2 = input("Ange andra strängen: ")

resultat = change_string(input_text1, input_text2)
print(resultat)


# Annat lösning
 
# Vi konverterar strängerna till listor för att lättare kunna modifiera dem
first_string = list(input("Enter the first string: "))
second_string = list(input("Enter the second string: "))

temp_character = first_string[0]    # Sparar ner första strängens första tecken i en "temporär" variabel
first_string[0] = second_string[0]  # Byter värdet på första strängens första tecken
second_string[0] = temp_character   # Byter värdet på andra strängens första tecken

temp_character = first_string[1]    # Upprepar processen för strängarnas andra (second) tecken
first_string[1] = second_string[1]
second_string[1] = temp_character

# Vi gör listorna till strängar igen med jon(), och lägger ihop till en enda sträng som sparas ner i variabeln 'combined_string'
combined_string = "".join(first_string) + " " + "".join(second_string)  
print(combined_string) 