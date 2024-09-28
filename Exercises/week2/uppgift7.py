# Uppgift 7: Implementera en stack med en klass
# Skapa en klass Stack som implementerar en stack (sista in, första ut) datastruktur med metoderna:

# push(item): Lägger till ett element överst i stacken.
# pop(): Tar bort och returnerar det översta elementet i stacken.
# peek(): Returnerar det översta elementet utan att ta bort det.
# is_empty(): Returnerar True om stacken är tom, annars False.

class Stack():

    def __init__(self):
        self.stacklist = []

    def __str__(self):
        return str(self.stacklist)

    # Lägger till ett element sist i stacken.
    def push(self, item):
        self.stacklist.append(item)
        print(f"{item} har lagts till i stacken.")

    # Tar bort och returnerar det sista elementet i stacken.
    def pop(self):
        if self.is_empty():
            return "Stacken är tom. Det finns inget att ta bort."
        return self.stacklist.pop()

    # Returnerar det översta elementet utan att ta bort det.
    def peek(self):
        if self.is_empty():
            return "Stacken är tom. Det finns inget att visa."
        return self.stacklist[-1]

    # Returnerar True om stacken är tom, annars False.
    def is_empty(self):
        return len(self.stacklist) == 0
    
    # Visar alla element i stacken.
    def display(self):
        print(f"Nuvarande stack: {self.stacklist}")


def main():
    my_stack = Stack()

    while True:
        print("\nVälj ett alternativ:")
        print("1. Lägg till ett element i stacken (push)")
        print("2. Ta bort det översta elementet (pop)")
        print("3. Visa det översta elementet (peek)")
        print("4. Kontrollera om stacken är tom")
        print("5. Visa hela stacken")
        print("6. Avsluta")

        choice = input("Ditt val: ")

        if choice == '1':
            item = input("Ange elementet att lägga till: ")
            my_stack.push(item)

        elif choice == '2':
            popped_item = my_stack.pop()
            print(f"Elementet '{popped_item}' har tagits bort från stacken.")

        elif choice == '3':
            top_item = my_stack.peek()
            print(f"Det sista elementet i stacken är: {top_item}")

        elif choice == '4':
            if my_stack.is_empty():
                print("Stacken är tom.")
            else:
                print("Stacken är inte tom.")

        elif choice == '5':
            my_stack.display()

        elif choice == '6':
            print("Avslutar programmet.")
            break

        else:
            print("Ogiltigt val, försök igen.")


if __name__ == "__main__":
    main()


