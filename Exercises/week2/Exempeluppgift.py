#   Exempeluppgift 1 - class Person

# Skapa en enkel klass Person med följande steg:
# Definiera klassen Person. Lägg till en konstruktor (__init__-metod) som tar emot name och age som parametrar. 
# Skapa en metod introduce() som returnerar en presentation av personen. 
# Skapa några instanser av Person och anropa introduce() metoden för var och en.


#   Exempeluppgift del 2 - Attribut och metoder för Person

# Utöka Person-klassen från föregående uppgift:

# 1. Lägg till ett attribut hobbies som en lista i konstruktorn.
# 2. Skapa en metod add_hobby(hobby) för att lägga till en hobby.
# 3. Skapa en metod get_hobbies() som returnerar en sträng med alla hobbies.
# 4. Skriv över/overwritea __str__ metoden för att ge en fin strängrepresentation av objektet, när man till exempel printar ett Person-objekt.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hobbies = []

    def introduce(self):
        return f"Hej! Mitt namn är {self.name} och jag är {self.age} gammal."
    
    def add_hobby(self, hobby):
        # Lägg till en hobby till listan
        self.hobbies.append(hobby)

    def get_hobbies(self):
        # Returnera listan av hobbies
        if not self.hobbies:
            return "Inga hobbies angivna."
        return ", ".join(self.hobbies)

    def __str__(self):
        # stäng representation av person objekt
        hobbies_str = self.get_hobbies()    # hämta hobbies för representation
        return f"{self.introduce()} Mina hobbies är: {hobbies_str}"


def main():
    person1 = Person("Aleh", 44)
    person2 = Person("Lucina", 38)

    # Lägger till hobbies
    person1.add_hobby("läsa")
    person1.add_hobby("Promenera")
    person2.add_hobby("cyckla")

    print(person1)
    print(person2)



if __name__ == "__main__":
    main()









