# Skriv en funktion som konverterar en given sträng till versaler (uppercase) 
# om den innehåller minst 2 versaler bland de 4 första tecknen.

def uppercase_convert(text):

    # Get the first 4 characters of the string
    first_four_chars = text[:4]
    
    # Count how many of the first 4 characters are uppercase
    uppercase_count = 0

    for char in first_four_chars:
        if char.isupper():
            uppercase_count += 1
    
    # If there are at least 2 uppercase letters, convert the whole string to uppercase
    if uppercase_count >= 2:
        return text.upper()

    return text

input_text = input("Enter a string: ")

result = uppercase_convert(input_text)
print(result)
