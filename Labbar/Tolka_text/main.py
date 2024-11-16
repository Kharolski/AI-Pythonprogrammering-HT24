# Standard libraries
import os

# Custom ML pipeline components
from data_collector import DataCollector
from model_comparator import ModelComparator
from data_loader import DataLoader
from user_interaction import UserInteraction

def setup_paths():
    """Konfigurerar sökvägar för ML-pipeline"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return {
        'base': os.path.join(current_dir),
        'images': os.path.join(current_dir, "images"),
        'data': os.path.join(current_dir, "data"),
        'new_image': os.path.join(current_dir, "images", "siffror", "test_image.png")   # ändra till din fil med bilder om du har en
    }

def main():
    """
    Huvudfunktion för ML-pipeline:
    1. Datainsamling/laddning
    2. Datapreparering
    3. Modellträning
    4. Utvärdering
    5. Visualisering
    """
    while True:
        try:
            # Setup och initiering
            paths = setup_paths()
            collector = DataCollector(data_dir=paths['data'], image_folder=paths['images'])
            loader = DataLoader(paths['data'])
            ui = UserInteraction()
            model_comparator = ModelComparator()

            # Visa meny och hantera datainsamling
            val = ui.get_menu_choice()

            if val == 1:
                images, labels = collector.collect_new_data(paths['new_image'])

            elif val == 2:
                try:
                    images, labels = loader.load_existing_data(collector)
                except FileNotFoundError:
                    print("Återgår till huvudmenyn...")
                    continue

            elif val == 3:
                print("Avslutar programmet...")
                break

            if len(images) < 2:
                raise ValueError("Otillräckligt med träningsdata")

            # Datapreparering
            X_train, X_test, y_train, y_test = loader.split_data(images, labels)

            # Modellträning och utvärdering
            best_model, conf_matrix = model_comparator.train_and_evaluate(
                X_train, X_test, y_train, y_test
            )

        except Exception as e:
                print(f"\nFel i ML-pipeline: {e}")
                print("Återgår till huvudmenyn...")


if __name__ == '__main__':
    main()
