# Skriv en funktion som tar emot en lista med ord och returnerar det längsta ordet samt dess längd

def find_longest_word(word_list):
    # Initialize variables to store the longest word and its length
    longest_word = ""
    max_length = 0
    
    # Loop through each word in the list
    for word in word_list:
        # Check if the current word is longer than the longest word found so far
        if len(word) > max_length:
            longest_word = word
            max_length = len(word)
    
    # Return the longest word and its length
    return longest_word, max_length

# Example list of words
cities = ["New York", "Los Angeles", "Chicago", "Philadelphia", "San Francisco", "Las Vegas"]

# Find and print the longest word and its length
longest_word, length = find_longest_word(cities)
print(f"The longest word is '{longest_word}' with length {length}")
