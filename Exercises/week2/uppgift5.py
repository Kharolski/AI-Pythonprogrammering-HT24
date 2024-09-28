class ContactBook:
    # dict för lagring av kontakter key(name), value(phone)
    def __init__(self):
        self.contacts = {}

    # lägg till en ny kontakt
    def add_contact(self, name, phone):
        if name in self.contacts:
            print(f"Kontakten {name} finns redan.")
        else:
            self.contacts[name] = phone
            print(f"Kontakt '{name}' med nummer '{phone}' har lagts till. ")

    
    # ta bort en kontakt
    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Kontakten {name} har tagits bort.")
        else:
            print(f"Kontakten '{name}' hittades inte.")

    
    # uppdatera kontaktens telefonnummer
    def update_contact(self, name, new_phone):
        if name in self.contacts:
            self.contacts[name] = new_phone
            print(f"Kontakt '{name}' har uppdaterats med nytt nummer '{new_phone}'.")
        else:
            print(f"Kontakten '{name}' hittades inte.")


    # vissa alla kontakter
    def display_contacts(self):
        if self.contacts:
            print("\nTelefonbok:")
            print("-----------------------------")
            for name, phone in self.contacts.items():
                print(f"Namn: {name} - Nummer: {phone}")
        else:
            print("Telefonboken är tom.")


def main():
    contact_book = ContactBook()

    while True:
        print("\nVälj ett alternativ:")
        print("1. Lägg till kontakt")
        print("2. Ta bort kontakt")
        print("3. Uppdatera kontakt")
        print("4. Visa kontakter")
        print("5. Avsluta")

        choice = input("Ditt val: ")

        if choice == '1':
            name = input("Ange namn: ")
            phone = input("Ange telefonnummer: ")
            contact_book.add_contact(name, phone)
        
        elif choice == '2':
            name = input("Ange namnet på kontakten du vill ta bort: ")
            contact_book.remove_contact(name)
        
        elif choice == '3':
            name = input("Ange namnet på kontakten du vill uppdatera: ")
            new_phone = input("Ange nytt telefonnummer: ")
            contact_book.update_contact(name, new_phone)
        
        elif choice == '4':
            contact_book.display_contacts()

        elif choice == '5':
            print("Avslutar programmet.")
            break

        else:
            print("Ogiltigt val, försök igen.")



if __name__ == '__main__':
    main()
