import random

word_list = ["python", "javascript", "hangman", "computer", "programming"]
playing = True

while playing:

    word = random.choice(word_list)

    # Håller koll på de korrekta gissningarna och antal felaktiga gissningar
    guessed_word = ["_"] * len(word)  
    guessed_letters = []  
    attempts = 6                    # Max tillåtna felaktiga gissningar

    # Välkomstmeddelande
    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters: {' '.join(guessed_word)}")
    print(f"You have {attempts} attempts to guess the word.")

    # Loopar tills spelaren har gissat hela ordet eller använt alla försök
    while attempts > 0 and "_" in guessed_word:
        print("\nGuessed so far:", ' '.join(guessed_word))
        print(f"Remaining attempts: {attempts}")

        guess = input("Guess a letter or whole word: ").lower()

        # Kontrollera om bokstaven redan har gissats
        if guess in guessed_letters:
            print(f"You have already guessed the letter '{guess}'. Try another one.")
            continue

        # Lägger till gissningen
        guessed_letters.append(guess)

        # Om gissningen är rätt
        if guess in word:

            # om man gissat hela ordet
            if guess == word:
                guessed_word = guess
                break

            print(f"Good job! The letter '{guess}' is in the word.")
            
            # Uppdaterar guessed_word med den gissade bokstaven på rätt positioner
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            # Om gissningen är fel, minskas antalet försök
            if len(guess) > 0:
                print(f"Sorry! This is wrong word '{guess}' ")
                attempts -= 1
            else:
                attempts -= 1
                print(f"Sorry! The letter '{guess}' is not in the word.")

    # Resultat av spelet
    if "_" not in guessed_word:
        print(f"\nCongratulations! You guessed the word: {word}")
    else:
        print(f"\nGame over! You've run out of attempts. The word was: {word}")
    
    # Om man vill spela igen
    play_again = input("Do you want to play again? (y/n): ").lower()
    if not play_again == "y":
        playing = False


