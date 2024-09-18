# Skriv en funktion som vänder (reverse) på en sträng om dess längd är en multipel av 4.


def reverse_string(text):

    # Check if the length of the string is a multiple of 4
    if len(text) % 4 == 0:

        # Reverse the string
        reversed_text = text[::-1]
        return reversed_text
    else:
        # Return the original string
        return text

input_text = input("Enter a string: ")

result = reverse_string(input_text)
print(result)
