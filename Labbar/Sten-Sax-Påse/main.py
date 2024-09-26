# Projekt 3: Sten-sax-påse

# Skapa en version av spelet sten-sax-påse.

# ·   Datorn slumpar vilken av sten, sax eller påse den ska välja.
# ·   Spelaren väljer också sten, sax eller påse.
# ·   Datorn och spelaren visar sedan upp sina val samtidigt.
# ·   Reglerna är enligt följande: sten vinner över sax, sax vinner över påse, och påse vinner över sten. Om båda väljer samma alternativ blir det oavgjort.
# ·   Spelaren spelar tills hen vinner eller förlorar mot datorn.


import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]

    def get_computer_choice(self):
        return random.choice(self.choices)
    
    def get_player_choice(self):
        player = None
        while player not in self.choices:
            player = input("Välj ett av följande (-- rock, paper, or scissors --): ").lower()
        return player

    def check_winner(self, player, computer):
        if player == computer:
            return "Tie!"
        elif (player == "rock" and computer == "scissors") or \
             (player == "scissors" and computer == "paper") or \
             (player == "paper" and computer == "rock"):
            return "Grattis! Du vann!"
        else:
            return "Tyvärr! Du har förlurat!"

    def play_game(self):
        print("Välkommen till spelet sten, sak, påse!")
        while True:
            computer = self.get_computer_choice()
            player = self.get_player_choice()

            # Visar både datorns och spelarens val
            print(f"Computer: {computer}")
            print(f"Player: {player}")

            # Kontrollera vinnaren
            result = self.check_winner(player, computer)
            print(result)

            play_again = input("Vill du spela igen? (y/n): ").lower()
            if play_again != "y":
                print("Tack för att du spelade. Hej då!")
                break

def main():
    game = RockPaperScissors()
    game.play_game()


if __name__ == "__main__":
    main()


