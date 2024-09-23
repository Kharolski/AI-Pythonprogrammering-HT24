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


# Annat lösning

string_to_modify = input("Enter a string: ")

stripped_string = string_to_modify.replace(' ', '') # Tar bort all whitespace från strängen, inklusive space (" "), tab ("\t"), newline ("\n"), genom att byta ut dessa mot en tom sträng ("").
print(stripped_string)

final_string = ""   # Vi skapar en ny, tom sträng som kommer innehålla alla tecken på jämna index från ursprungliga strängen.

# Vi går igenom varje index i stripped_string, från index 0 upp TILL längden av strängen.
for i in range(len(stripped_string)):    # range(x) ger oss intervallet/listan [0, 1, 3,.., x-1]. len(string) ger oss längden av string.
    # Om indexet är jämnt, dvs om indexet 'i' är jämnt delbart med 2, lägger vi till tecknet som ligger på index 'i' till den nya strängen.
    # Modulo-operatorn '%' ger resten vid division, i detta fallet resten när vi dividerar 'i' med 2. Om resten är 0, vet vi att 'i' är jämnt delbart med täljaren, 2 i detta fall.
    if (i%2==0):
        # Kan också använda addition istället för append() eftersom 'final_string' är en sträng:
         final_string = final_string + stripped_string[i]

print(final_string)

