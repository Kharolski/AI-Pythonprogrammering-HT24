# Projekt 4: Black Jack

# Skapa ett program som simulerar ett blackjack-spel mellan en spelare och en dator.
# Spelet spelas med en vanlig kortlek som blandas innan varje runda.
# Varje spelare får två kort i början av spelet. Datorn visar bara upp ett av sina kort.
# Spelaren kan välja att ta fler kort (hit) eller stanna på sina nuvarande kort (stand).
# Spelaren kan fortsätta att ta kort tills hen når 21 poäng eller över.
# Om spelaren går över 21 poäng förlorar hen direkt.
# När spelaren stannar, spelar datorn sin tur. Datorn måste ta kort så länge summan av korten är mindre än 17 poäng och stanna när datorns kortsumma är 17 poäng eller mer.
# Om datorn går över 21 poäng vinner spelaren oavsett vilka kort spelaren har.
# Om varken spelaren eller datorn går över 21 poäng så vinner den som har högst kortsumma.


import random

# Kortleksklass
class Deck:
    def __init__(self):
        self.cards = self.create_deck()

    def create_deck(self):

        # Skapar en kortlek med 52 kort (utan jokrar).
        suits = ["Hjärter", "Ruter", "Klöver", "Spader"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        deck = [(rank, suit) for suit in suits for rank in ranks]
        random.shuffle(deck)
        return deck

    def deal_card(self):
        # Ger ut ett kort från toppen av kortleken.
        return self.cards.pop()

# Handklass för spelare och dealer
class Hand:
    def __init__(self, name):
        self.cards = []
        self.name = name

    def add_card(self, card):
        # Lägger till ett kort i handen.
        self.cards.append(card)

    def calculate_value(self):
        # Beräknar värdet på handen.
        value = 0
        aces = 0
        for card, suit in self.cards:
            if card in ['J', 'Q', 'K']:
                value += 10
            elif card == 'A':
                value += 11
                aces += 1
            else:
                value += int(card)
        
        # Om värdet överstiger 21 och vi har ess, räknar vi esset som 1 istället för 11
        while value > 21 and aces:
            value -= 10
            aces -= 1
        
        return value

    def display_hand(self, reveal_dealer=False):
        # Visar korten i handen.
        if self.name == "Dealer" and not reveal_dealer:
            print(f"{self.name}s hand: [Dolt kort] {self.cards[1]}")
        else:
            print(f"{self.name}s hand: {self.cards} - Värde: {self.calculate_value()}")

# Black Jack-spelklassen
class BlackJack:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand("Spelare")
        self.dealer_hand = Hand("Dealer")

    def deal_starting_hands(self):
        # Delar ut de första två korten till både spelaren och dealern.
        for _ in range(2):
            self.player_hand.add_card(self.deck.deal_card())
            self.dealer_hand.add_card(self.deck.deal_card())

    def player_turn(self):
        # Spelarens tur: Dra kort eller stanna.
        while True:
            self.player_hand.display_hand()
            choice = input("\nVill du 'dra' ett kort eller 'stanna'? (dra/stanna): ").lower()
            if choice == 'dra':
                self.player_hand.add_card(self.deck.deal_card())
                if self.player_hand.calculate_value() > 21:
                    print("\nDu har blivit tjock! (" + str(self.player_hand.calculate_value()) + " poäng)")
                    return False
            elif choice == 'stanna':
                break
            else:
                print("Ogiltigt val. Välj 'dra' eller 'stanna'.")
        return True

    def dealer_turn(self):
        # Dealerns tur: Dealern måste dra tills handen är minst 17.
        while self.dealer_hand.calculate_value() < 17:
            self.dealer_hand.add_card(self.deck.deal_card())

    def check_winner(self):
        # Kontrollerar vinnaren baserat på handens värden.
        player_value = self.player_hand.calculate_value()
        dealer_value = self.dealer_hand.calculate_value()

        if dealer_value > 21:
            print("\nDealern blev tjock! Du vann!")
        elif player_value > dealer_value:
            print("\nGrattis! Du vann!")
        elif player_value == dealer_value:
            print("\nDet är oavgjort!")
        else:
            print("\nTyvärr, dealern vann!")

    def play(self):
        # Den huvudsakliga spel-loopen.
        print("Välkommen till Black Jack!\n")
        self.deal_starting_hands()
        self.dealer_hand.display_hand()  # Visar dealerns hand (ett dolt kort)
        if self.player_turn():           # Spelarens tur
            self.dealer_turn()           # Om spelaren inte blir tjock, dealerns tur
            print("\nDealerns tur:")
            self.dealer_hand.display_hand(reveal_dealer=True)  # Visar hela dealerns hand
            self.check_winner()          # Kontrollerar vinnaren
        else:
            print("\nTyvärr, du förlorade spelet.")

def main():
    while True:
        game = BlackJack()
        game.play()

        play_again = input("\nVill du spela igen? (j/n): ").lower()
        if play_again != 'j':
            print("Tack för att du spelade! Hej då!")
            break

if __name__ == "__main__":
    main()







