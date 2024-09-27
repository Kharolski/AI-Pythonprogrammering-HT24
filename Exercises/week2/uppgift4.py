# Uppgift 4: Filläsning och ordräkning

# Skapa en textfil (i samma mapp som ditt program). 
# Skriv in eller kopiera in en text av valfri längd. 
# Läs in textfilen och använd ett dictionary för att räkna förekomsten av varje ord. 
# Ignorera skiljetecken och konvertera alla ord till lowercase.

import string
import os

class FileWordCounter:
    def __init__(self, filename):
        self.filename = filename

    # Rensa texten från skiljetecken och konvertera allt till små bokstäver.
    def clean_text(self, text):
        # ta bort skiljetecken
        translator = str.maketrans('', '', string.punctuation)
        clean_text = text.translate(translator)

        return clean_text.lower()

    # Läs in textfilen och räkna förekomsten av varje ord.
    def count_words(self):
        word_count = {}

        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                content = file.read()

                clean_content = self.clean_text(content)

                # dela upp texten i en lista av ord
                words = clean_content.split()

                # räkna varje ord
                for word in words:
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1

        except FileNotFoundError:
            print(f"Filen '{self.filename}' hittades inte")

        return word_count

    # Skriv ut ordlistan och antalet för varje ord.
    def display_word_count(self):
        word_count = self.count_words()
        print(f"\nOrdräkning för filen {self.filename}")

        for word, count in word_count.items():
            print(f"{word}: {count}")

    # Hantera om filen ska skrivas över, läggas till eller skapas.
    def manage_file(self):
        if os.path.exists(self.filename):
            print(f"Filen '{self.filename}' existerar redan.")
            overwrite = input("Vill du skriva över filen? (ja/nej): ").lower()

            if overwrite == 'ja':
                self.write_new_content()
            else:
                adding = input("Vill du lägga till mer text? (ja/nej): ").lower()
                if adding == 'ja':
                    self.append_content()
                else:
                    print("Filhantering avbröts.")
        else:
            self.write_new_content()

    # Lägg till text i filen.
    def append_content(self):
        with open(self.filename, 'a', encoding='utf-8') as file:
            file.write("Detta är en extra rad text som lagts till.\n")
        print(f"Text har lagts till i '{self.filename}'.")

    # Skriv ny text och skapa filen om den inte finns.
    def write_new_content(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            file.write("Hej, världen! Detta är ett exempel. Detta exempel innehåller text som ska analyseras.\n")
            file.write("Analyseringen sker genom att räkna varje ord. Varje ord räknas noggrant.\n")
        print(f"Filen '{self.filename}' har skapats och text har skrivits till den.")



def main():
    
    file_path = "sample_text.txt"

    word_counter = FileWordCounter(file_path)

    # Hantera filen (lägg till eller skriv över beroende på användarens val)
    word_counter.manage_file()

    # Visa ordräkningen för filen
    word_counter.display_word_count()
    

    


if __name__ == '__main__':
    main()







