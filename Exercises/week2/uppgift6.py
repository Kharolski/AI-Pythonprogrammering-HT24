import os

class FileManager:
    def __init__(self):
        pass
    
    # Läser innehållet i en fil och returnerar det som en sträng.
    def read_file(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            return f"Filen '{filename}' hittades inte."

    # Skriver innehållet till en fil, skriver över om filen redan existerar.
    def write_file(self, filename, content):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(filename)
        print(f"Innehåll har lagts till i filen '{filename}'.")

    # Lägger till innehåll i slutet av en befintlig fil.
    def append_file( self, filename, content):
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(filename)
        print(f"Innehåll har lagts till i filen '{filename}'.")

    # Raderar en fil.
    def delete_file(self, filename):
        if os.path.exists(filename):
            os.remove(filename)
            print(f"Filen '{filename}' har raderats.")
        else:
            print(f"Filen '{filename}' hittades inte och kunde inte raderas.")



def main():
    file_manager = FileManager()

    while True:
        print("\nVälj ett alternativ:")
        print("-----------------------------")
        print("1. Läs fil")
        print("2. Skriv till fil")
        print("3. Lägg till innehåll i fil")
        print("4. Radera fil")
        print("5. Avsluta")
        print("-----------------------------")

        choice = input("Ditt val: ")

        if choice == '1':
            filename = input("Ange filnamn att läsa: ")
            content = file_manager.read_file(filename)
            print(f"\nInnehåll i filen '{filename}':\n{content}")

        elif choice == '2':
            filename = input("Ange filnamn att skriva till: ")
            content = input("Skriv innehållet som du vill skriva till filen: ")
            file_manager.write_file(filename, content)

        elif choice == '3':
            filename = input("Ange filnamn att lägga till innehåll i: ")
            content = input("Skriv innehållet som du vill lägga till i filen: ")
            file_manager.append_file(filename, content)

        elif choice == '4':
            filename = input("Ange filnamn att radera: ")
            file_manager.delete_file(filename)

        elif choice == '5':
            print("Avslutar programmet.")
            break

        else:
            print("Ogiltigt val, försök igen.")



if __name__ == '__main__':
    main()

