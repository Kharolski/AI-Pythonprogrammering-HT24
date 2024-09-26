# Uppgift 3: Grundläggande filhantering

# Skriv ett program som gör följande:

# 1. Skapar en textfil och skriver några rader till den.
# 2. Läser innehållet i filen och skriver ut det.
# 3. Lägger till mer text i slutet av filen.
# 4. Läser filen igen och visar det uppdaterade innehållet.
# 5. Använd with-satser för att säkerställa att filen stängs korrekt.


class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def file_read(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                print(file.read())
        except FileNotFoundError:
            print(f"Filen '{self.filename}' hittades inte!")
        except UnicodeDecodeError as e:     # om filen var redan encodat med annat 
            print(f"Fel vid avkodning: {e}")
    
    def file_write(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            file.write("Hej! världen!\n")
            file.write("Detta är en exempelfil.\n")
        print(f"Data har skrivits till '{self.filename}'.")

    def file_add_text(self):
        with open(self.filename, 'a', encoding='utf-8') as file:
            file.write("Detta är ytterligare en rad.\n")
        print(f"Ytterligare en rad har lagts till {self.filename}")


def main():
    file_path = "example.txt"
    my_file = FileManager(file_path)

    # läsa filen
    my_file.file_read()

    # skriver till filen 
    my_file.file_write()

    # lägger till text i filen
    my_file.file_add_text()

    # läsa igen text fill att ser resultat
    my_file.file_read()



if __name__ == "__main__":
    main()





