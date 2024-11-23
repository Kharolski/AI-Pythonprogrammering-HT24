import matplotlib.pyplot as plt
import os
import numpy as np

class UserInteraction:
    """Klass för att hantera användarinteraktion i programmet.

    Denna klass ansvarar för:
    - Hantering av menyval
    - Validering av användarinput
    - Verifiering av modellens prediktioner

    Exempel:
        ui = UserInteraction()
        # Hantera menyval
        choice = ui.get_menu_choice()
        # Verifiera prediktioner
        verified_predictions = ui.verify_predictions(digits, predictions)
    """
    
    @staticmethod
    def get_menu_choice() -> int:
        """Hanterar menyval för ML-pipeline"""

        # Kontrollera om dataset finns
        dataset_path = os.path.join(os.path.dirname(__file__), "data", "dataset.npz")
        has_dataset = os.path.exists(dataset_path)

        print("\n=== ML Pipeline för Sifferigenkänning ===")
        print("Tillgängliga val:")
        print("1. Samla in ny träningsdata")
        print("2. Analysera ny bild")               
        print("3. Använd/Återställ befintligt dataset")
        print("4. Avsluta programmet")
        print("-" * 40)
        
        while True:
            try:
                val = int(input("Välj alternativ: "))
                if not has_dataset and val in [1, 2]:  # Om dataset inte finns, tillåt inte val 1 eller 2
                    print("Detta alternativ kräver att dataset finns, snälla välj alternativ 3 först")
                    continue
                if val in [1, 2, 3, 4]:             
                    return val
                print("Ogiltigt val. Försök igen.")
            except ValueError:
                print("Vänligen ange en siffra")

    @staticmethod
    def get_user_choice(prompt: str) -> bool:
        """Validerar ja/nej input från användaren"""
        while True:
            choice = input(prompt).lower()
            if choice == 'j':
                return True
            if choice == 'n':
                return False
            print("Vänligen svara med 'j' eller 'n'")
  
    

