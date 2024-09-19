# Skriv ett program som kontrollerar om ett givet ord är ett palindrom (läses likadant framifrån som bakifrån).

def is_palindrome(word):
    # Remove spaces and convert to lowercase
    text = word.replace(" ", "").lower()
    
    # Check if the word text is equal to its reverse
    return text == text[::-1]

# Get input from the user
input_word = input("Enter a word to check if it's a palindrome: ")

if is_palindrome(input_word):
    print(f"'{input_word}' is a palindrome.")
else:
    print(f"'{input_word}' is not a palindrome.")
