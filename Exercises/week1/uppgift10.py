# Skriv en funktion som skapar en ny sträng bestående av 4 kopior av de två sista tecken 
# i en given sträng. Exempel-input: "Python" Förväntad output: "onononon"

def repeat_chars(text):

    # Get the last two characters from the string
    last_two_chars = text[-2:]
    
    # Repeat those characters 4 times
    result = last_two_chars * 4
    
    return result

input_text = input("Enter a string: ")

result = repeat_chars(input_text)
print(result)
