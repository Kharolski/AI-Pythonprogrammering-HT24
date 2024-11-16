import matplotlib.pyplot as plt

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
        print("\n=== ML Pipeline för Sifferigenkänning ===")
        print("Tillgängliga val:")
        print("1. Samla in ny träningsdata")
        print("2. Använd befintligt dataset")
        print("3. Avsluta programmet")
        print("-" * 40)
        
        while True:
            try:
                val = int(input("Välj alternativ (1-3): "))
                if val in [1, 2, 3]:
                    return val
                print("Vänligen välj 1, 2 eller 3")
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
  
    def verify_predictions(self, digits: list, predictions: list) -> list:
        """Verifiera prediktioner med användaren.
        
        Args:
            digits (list): Lista över detekterade siffror (i form av arrays).
            predictions (list): Lista över modellens prediktioner.
        
        Returns:
            list: Verifierade prediktioner från användaren.
        """
        plt.ion()
        fig = self._setup_prediction_display(digits, predictions)
        verified = self._handle_verification(predictions)
        plt.ioff()
        plt.close(fig)
        return verified

