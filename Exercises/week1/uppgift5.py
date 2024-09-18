# Skriv ett program som lägger till "ing" i slutet av en given sträng, om strängen är kortare än 3 tecken 
# ska den lämnas ofärndrad. Expempel-input: "Python" Förväntad output: "Pythoning"

def Adding_ing(text):

    # Kontrollera om strängen är minst 3 tecken lång
    if len(text) >= 3:
        return text + "ing"
    else:
        return text

input_text = input("Ange en sträng: ")

resultat = Adding_ing(input_text)
print(resultat)
