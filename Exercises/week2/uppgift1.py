# Skriv ett bank konto Class

# Den ska ha attributerna ´´owner´´ och dess balans kommer initiellt vara 0.
# Skapa metoder såsom ´´deposit(amount)´´ för att lägga till pengar till kontot samt ´´withdraw(amount)´´ 
# för att ta ut pengar från kontot. Se också till att balansen kan ej bli negativ!
# Skapa en metod ´´display_balance()´´ för att sedan printa kontots nuvarande balans


class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} kr har satts in på kontot.")
        else:
            print("Insättningsbelopp måste vara större än 0.")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Uttag misslyckades! Du har inte tillräckligt med pengar. Nuvarande balans: {self.balance} kr")
        elif amount <= 0:
            print("Uttagsbelopp måste vara större än 0.")
        else:
            self.balance -= amount
            print(f"{amount} kr har tagits ut från kontot.")
            print(f"nuvarande balans: {self.balance} kr")

    def display_balance(self):
        print(f"{self.owner} ditt nuvarande balans: {self.balance} kr")


# Huvudprogram
owner = input("Ange ditt namn för att öppna ett konto: ")
if owner.strip() == "":
    owner = "Gäst"

konto = BankAccount(owner)
is_running = True

while is_running:
    print("\nBanking Program")
    print("-----------------------")
    print("1. Visa Balance.")
    print("2. Sätta in.")
    print("3. Uttag.")
    print("4. Exit")
    print("-----------------------")

    choice = input("Välj ett alternativ (1-4): " )

    if choice == "1":                   # visa balans
        konto.display_balance()

    elif choice == "2":                 # insättning
        while True:
            print("\nX för Exit:")
            amount_input = input(f"Hej, {konto.owner}. Hur mycket vill du sätta in? ").lower()

            # Kontrollera om inmatningen är ett giltigt tal
            if amount_input.replace('.', '', 1).isdigit():          # tillåter decimalpunkt
                amount = float(amount_input)
                if amount > 0:
                    konto.deposit(amount)
                    break
                else:
                    print("Beloppet måste vara större än 0.")
            elif amount_input == "x":
                print("Avbröt insättningen. Återgår till menyn...")
                break
            elif amount_input[0] == "-":
                print("Du kan inte sätta in negativ belopp")
            else:
                print("Felaktigt belopp. Ange ett giltigt nummer.")

    elif choice == "3":                 # uttag
        while True:
            print("\nX för Exit:")
            amount_input = input(f"Hej, {konto.owner}. Hur mycket vill du ta ut? ").lower()

            # Kontrollera om inmatningen är ett giltigt tal
            if amount_input.replace('.', '', 1).isdigit():          # tillåter decimalpunkt
                amount = float(amount_input)
                if amount > 0:
                    konto.withdraw(amount)
                    break
                else:
                    print("Beloppet måste vara större än 0.")
            elif amount_input == "x":
                print("Avbröt uttaget. Återgår till menyn...")
                break
            elif amount_input[0] == "-":
                print("Du kan inte ta ut negativ belop")
            else:
                print("Felaktigt belopp. Ange ett giltigt nummer.")
        
    elif choice == "4":                 # avsluta programmet
        print("Tack för att du använde banktjänsten! Hej då!\n")
        break

    else:
        print("Ogiltigt val, försök igen.")

