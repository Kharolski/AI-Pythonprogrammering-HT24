# Skriv ett program som först tar bort all whitespace (mellanslag, tab (\t), newline(\n)), 
# och sedan även tar bort alla tecken på ojämna indexvärden, från given sträng. 
# Exempel-input: "a string with spaces and a newline character\n" Förväntad output: "atigihpcsnaelncaatr"

def remove_all(text):
    # Remove all whitespaces (spaces, tabs, newlines)
    text_without_whitespace = ''.join(text.split())
    
    # Create a new string using only characters at even index positions
    result = ""
    
    # Loop through each character in the string
    for i in range(len(text_without_whitespace)):
        
        # If the index is even, add the character to the result
        if i % 2 == 0:
            result += text_without_whitespace[i]
    
    return result

input_text = input("Enter a string: ")

result = remove_all(input_text)
print(result)


