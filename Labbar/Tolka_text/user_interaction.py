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
        if has_dataset:
            print("1. Samla in ny träningsdata")
        print("2. Använd befintligt dataset")
        print("3. Avsluta programmet")
        print("-" * 40)
        
        while True:
            try:
                val = int(input("Välj alternativ: "))
                if not has_dataset and val == 1:
                    print("Alternativ 1 är inte tillgängligt förrän grunddata har laddats")
                    continue
                if val in [1, 2, 3]:
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
  
    def review_predictions(self, images, labels, trained_model, batch_size=5):
        """
        Granska och korrigera prediktioner för nya bilder.
        """
        print("\n=== Granskning av prediktioner ===")
        predictions = trained_model.predict(images)
        corrected_labels = []
        valid_images = []
        
        plt.ion()
        
        i = 0
        while i < len(images):
            batch_images = images[i:i + batch_size]
            batch_preds = predictions[i:i + batch_size]
            
            # Visa batch med bilder
            fig = plt.figure(figsize=(15, 3))
            for j, (img, pred) in enumerate(zip(batch_images, batch_preds)):
                plt.subplot(1, batch_size, j + 1)
                plt.imshow(img.reshape(28, 28), cmap='gray')
                plt.title(f"Bild {i+j+1}: Pred {pred}")
                plt.axis('off')
            plt.tight_layout()
            plt.show()
            
            while True:  # Loop tills giltig input eller avbryt
                print("\nInstruktioner:")
                print("J - Korrekt prediktion")
                print("X - Ogiltig siffra (skippa)")
                print("0-9 - Korrigera till denna siffra")
                print("Q - Avbryt granskning")
                print(f"\nAnge {len(batch_images)} värden (separerade med mellanslag):")
                print(f"Nuvarande prediktioner: {' '.join(str(p) for p in batch_preds)}")
                
                response = input("Dina korrigeringar: ").lower().split()
                
                if 'q' in response:
                    plt.close('all')
                    print("\nKorrigeringen avbröts av användaren...")
                    print("Återgår till huvudmenyn...")
                    return None
                
                if len(response) != len(batch_images):
                    print(f"Fel antal värden angivna. Förväntade {len(batch_images)}, fick {len(response)}.")
                    continue
                
                # Giltig input - process batch och gå vidare
                for img, resp in zip(batch_images, response):
                    if resp == 'j':
                        valid_images.append(img)
                        corrected_labels.append(pred)
                    elif resp == 'x':
                        continue
                    elif resp.isdigit() and 0 <= int(resp) <= 9:
                        valid_images.append(img)
                        corrected_labels.append(int(resp))
                
                plt.close(fig)  # Stäng bara nuvarande batch-figur
                break  # Gå vidare till nästa batch
            
            i += batch_size  # Gå vidare till nästa batch bara när current batch är klar
        
        plt.close('all')  # Stäng alla kvarvarande figurer
        return {
            'images': np.array(valid_images),
            'corrected_labels': np.array(corrected_labels)
        }


