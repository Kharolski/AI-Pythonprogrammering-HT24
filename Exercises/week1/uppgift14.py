# Skapa ett enkelt gissningsspel där datorn väljer ett slumpmässigt tal mellan 1-100 (eller annat intervall), 
# och låt användaren gissa tills de hittar rätt nummer. För varje felaktig gissning berättar 
# datorn om det rätta svaret är högre eller lägre än spelarens gissning.

import random

def guess_the_number():
    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)

    # tracking whether the guess is correct
    guessed_correctly = False

    print("Welcome to the Number Guessing Game!")

    while not guessed_correctly:
        choose_number = input("Choose a number between 1 and 100: ")
        # checking if user typed a number
        if choose_number.isdigit():
            # convert users input to integer
            choose_number = int(choose_number)

            # checking if user typed a number between 1-100
            if choose_number <= 0 or choose_number >= 101:
                print("Please type a number between 1 and 100")
                continue
        else:
            print('Please type a number next time!')
            continue

        if choose_number == random_number:
            print(f"Congratulations! You've guessed the number {random_number} correctly.")
            guessed_correctly = True
        elif choose_number < random_number:
            print("The number is higher. Try again.")
        else:
            print("The number is lower. Try again.")
    
# Start the game
guess_the_number()


