# Skriv ett program som tar en komma-separerad sekvens av ord och skriver ut de unika orden i alfabetisk ordning. 
# Exempel-input: "red, white, black, red, green, black" Förväntad output: "black, green, red, white"

def sort_unique_words(input_text):

    # Split the string into a list of words using a comma as the separator
    word_list = input_text.split(",")

    # Remove extra spaces around each word
    cleaned_word_list = []
    for word in word_list:
        cleaned_word_list.append(word.strip())
    
    # Create a set to get unique words and sort them in alphabetical order
    unique_words = sorted(set(cleaned_word_list))
    
    # Convert the list back to a comma-separated string
    result = ", ".join(unique_words)
    
    return result

# Take a comma-separated string as input
input_text = input("Skriv en komma-separerad sekvens av ord: ")

result = sort_unique_words(input_text)
print(result)
