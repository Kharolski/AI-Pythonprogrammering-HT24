import random

# välkomstmeddelande
print("Welcome to the game rock, paper, scissors!")
choices = ["rock", "paper", "scissors"]

# loop för att låta användaren spela flera gånger
while True:
    computer = random.choice(choices)
    player = None

    # En loop som fortsätter tills spelaren gör ett giltigt val
    while player not in choices:
        player = input("Please choose (-- rock, paper, or scissors --): ").lower()

    # Visar både datorns och spelarens val
    print(f"Computer: {computer}")
    print(f"Player: {player}")

    if player == computer:
        print("Tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        print("You Win!")
    else:
        print("You lose!")

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != "y":
        break

print("Thanks for playing. Bye!")







