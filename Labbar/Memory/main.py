# Projekt 2: Memory

# Skapa en version av spelet Memory.

# Datorn väljer ett antal slumpmässiga siffror eller bokstäver (beroende på svårighetsgrad) och visar dem i en viss ordning.
# Sedan visar datorn samma siffror eller bokstäver igen, men denna gång blandat.
# Spelaren ska gissa i vilken ordning siffrorna eller bokstäverna visades första gången.
# Spelet fortsätter tills spelaren har gissat rätt ordning.


import random

class MemoryGame:
    def __init__(self):
        self.svarighetsgrad = ""
        self.sekvens = []

    def __str__(self):
        return f"Memory-spel med svårighetsgrad: {self.svarighetsgrad}. Sekvenslängd: {len(self.sekvens)}."

    def valj_svarighetsgrad(self):
        
        # spelaren välja svårighetsgrad och sparar den i attributet 'svarighetsgrad'.
        while self.svarighetsgrad not in ["lätt", "medel", "svår"]:
            self.svarighetsgrad = input("Välj svårighetsgrad (lätt, medel, svår): ").lower()

    def generera_sekvens(self):
        
        # Genererar en lista av slumpmässiga siffror eller bokstäver beroende på vald svårighetsgrad.
        if self.svarighetsgrad == "lätt":
            self.sekvens = random.sample(range(1, 10), 5)  # 5 slumpmässiga siffror från 1 till 9
        elif self.svarighetsgrad == "medel":
            self.sekvens = random.sample("abcdefghijklmnopqrstuvwxyzåäö", 5)  # 5 slumpmässiga bokstäver
        elif self.svarighetsgrad == "svår":
            self.sekvens = random.sample("abcdefghijklmnopqrstuvwxyzåäö0123456789", 7)  # 7 slumpmässiga bokstäver och siffror

    def visa_sekvens(self):
        
        # Visar den ursprungliga sekvensen för spelaren.
        print("\nKom ihåg denna sekvens:")
        print(" ".join(map(str, self.sekvens)))
        input("\nTryck Enter när du är redo att fortsätta...")

    def blanda_och_visa_sekvens(self):
        
        # Blandar sekvensen och visar den blandade sekvensen för spelaren.
        blandad_sekvens = self.sekvens.copy()
        random.shuffle(blandad_sekvens)
        print("\nHär är den blandade sekvensen:")
        print(" ".join(map(str, blandad_sekvens)))

    def ta_spelarens_gissning(self):
        
        # Tar spelarens gissning och returnerar den som en lista.
        print("\nNu ska du skriva in sekvensen i den ursprungliga ordningen:")
        spelarens_gissning = input("Ange din gissning (separera med mellanslag): ").split()

        # Om svårighetsgraden är 'lätt', konvertera gissningen till siffror
        if self.svarighetsgrad == "lätt":
            spelarens_gissning = [int(num) for num in spelarens_gissning]
        return spelarens_gissning

    def kontrollera_gissning(self, spelarens_gissning):
    
        # Jämför spelarens gissning med den ursprungliga sekvensen.
        if spelarens_gissning == self.sekvens:
            print("\nGrattis! Du kom ihåg sekvensen korrekt.")
        else:
            print("\nTyvärr, det var inte rätt ordning.")
            print(f"Den korrekta sekvensen var: {' '.join(map(str, self.sekvens))}")

    def spela(self):
        
        # Den huvudsakliga spelloopen som hanterar hela spelet.
        print("Välkommen till Memory-spelet!")
        self.valj_svarighetsgrad()
        self.generera_sekvens()
        self.visa_sekvens()
        self.blanda_och_visa_sekvens()
        spelarens_gissning = self.ta_spelarens_gissning()
        self.kontrollera_gissning(spelarens_gissning)

def main():
    spel = MemoryGame()
    spela_igen = True

    while spela_igen:
        spel.spela()
        print(spel)  # Visar spelets information efter omgången
        val = input("Vill du spela igen? (j/n): ").lower()
        if val != "j":
            spela_igen = False
            print("Tack för att du spelade Memory! Hej då!")

if __name__ == "__main__":
    main()

