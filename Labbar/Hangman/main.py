# Projekt 1: Hangman

# Skapa en version av det klassiska spelet Hangman.
# Datorn väljer ett slumpmässigt ord från en fördefinierad lista av ord.
# Spelet visar hur många bokstäver ordet består av, men inte vilka bokstäver som är rätt.
# Spelaren ska gissa en bokstav i taget, och datorn ger feedback om bokstaven finns i ordet eller inte.
# Spelet fortsätter tills spelaren har gissat hela ordet eller har gjort tillräckligt många felaktiga gissningar.


import random

class Hangman:
    def __init__(self):
        self.word_list = ["python", "javascript", "hangman", "computer", "programming"]
        self.attempts = 6
        self.word = ""
        self.guessed_word = []
        self.guessed_letters = []

    def choose_word(self):
        self.word = random.choice(self.word_list)
        self.guessed_word = ["_"] * len(self.word)
        self.guessed_letters = []
        self.attempts = 6

    def display_status(self):
        print("\nGuessed so far:", ' '.join(self.guessed_word))
        print(f"Remaining attempts: {self.attempts}")

    def get_guess(self):
        guess = input("Guess a letter or whole word: ").lower()
        return guess

    def process_guess(self, guess):
        if guess in self.guessed_letters:
            print(f"You have already guessed the letter '{guess}'. Try another one.")
            return

        self.guessed_letters.append(guess)

        if guess == self.word:  # If the entire word is guessed correctly
            self.guessed_word = list(self.word)
        elif guess in self.word:
            print(f"Good job! The letter '{guess}' is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.guessed_word[i] = guess
        else:
            print(f"Sorry! The letter or word '{guess}' is incorrect.")
            self.attempts -= 1

    def is_word_guessed(self):
        return "_" not in self.guessed_word

    def is_game_over(self):
        return self.attempts == 0 or self.is_word_guessed()

    def display_end_result(self):
        if self.is_word_guessed():
            print(f"\nCongratulations! You guessed the word: {self.word}")
        else:
            print(f"\nGame over! You've run out of attempts. The word was: {self.word}")

    def play(self):
        self.choose_word()
        print("Welcome to Hangman!")
        print(f"The word has {len(self.word)} letters: {' '.join(self.guessed_word)}")
        print(f"You have {self.attempts} attempts to guess the word.")

        while not self.is_game_over():
            self.display_status()
            guess = self.get_guess()
            self.process_guess(guess)

        self.display_end_result()

def main():
    game = Hangman()
    playing = True

    while playing:
        game.play()
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            playing = False
            print("Thanks for playing Hangman! Goodbye!")

if __name__ == "__main__":
    main()

