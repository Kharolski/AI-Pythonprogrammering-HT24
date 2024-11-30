# Standard libraries
import os

# Custom ML pipeline components
from visualizer import Visualizer
from data_collector import DataCollector
from model_comparator import ModelComparator
from data_loader import DataLoader
from user_interaction import UserInteraction
from image_processor import ImageProcessor 


def setup_paths():
    """Konfigurerar sökvägar för ML-pipeline"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return {
        'base': os.path.join(current_dir),
        'images': os.path.join(current_dir, "images"),
        'data': os.path.join(current_dir, "data"),
        'new_image': os.path.join(current_dir, "images", "siffror", "image1.jpg")   # <-- ändra till bild med siffror som ska analyseras
    }

def main():
    while True:
        try:
            # Setup och initiering
            paths = setup_paths()
            collector = DataCollector(data_dir=paths['data'], image_folder=paths['images'])
            loader = DataLoader(paths['data'])
            ui = UserInteraction()
            model_comparator = ModelComparator()
            image_processor = ImageProcessor()
            visualizer = Visualizer()

            # Visa meny och hantera datainsamling
            val = ui.get_menu_choice()

            if val == 1:
                # Samla in nya siffror från bild
                images, labels = collector.collect_new_data(paths['new_image'])

                # Om inga nya unika bilder, återgå till menyn
                if images is None or labels is None:
                    print("Ingen ny data insamlad. Avslutar...")
                    continue            # Återgå direkt till menyn  

                # Kombinera befintlig data med nya bilder
                combined_images, combined_labels = collector.combine_datasets(images, labels)

                # Träna modeller på kombinerad data
                X_train, X_test, y_train, y_test = loader.split_data(combined_images, combined_labels)
                model = model_comparator.train_and_evaluate(X_train, X_test, y_train, y_test)

                # Granska prediktioner för nya bilder
                verified_data = visualizer.review_predictions(images, labels, model['best_model'])
                if verified_data is None:       # Om användaren avbryter
                    print("Avslutar utan att spara data...")
                    continue                    # Återgå direkt till menyn

                # Spara verifierad data och kontrollera resultatet
                if collector.save_data(verified_data['images'], verified_data['corrected_labels'], 'dataset.npz'):
                    print("Verifierad data sparad!")
                continue  # Återgå till menyn efter sparande

            elif val == 2:
                try:
                    image_processor.analyze_new_image(paths['new_image'], model_comparator, loader, collector)
                    continue                                                                            
                except Exception as e:
                    print(f"Fel vid bildanalys: {e}")
                    continue
            
            elif val == 3:
                try:
                    images, labels = loader.load_existing_data(collector)
                except FileNotFoundError:
                    print("Återgår till huvudmenyn...")
                    continue
            
            elif val == 4:
                print("Avslutar programmet...")
                break
            
            if len(images) < 2:
                raise ValueError("Otillräckligt med träningsdata")

            # Datapreparering
            X_train, X_test, y_train, y_test = loader.split_data(images, labels)

            # Modellträning och utvärdering
            results = model_comparator.train_and_evaluate(
                X_train, X_test, y_train, y_test
            )

            # Visa detaljerad prestandarapport
            print("\n=== Modellprestanda ===")
            for model_name, score in results['scores'].items():
                print(f"{model_name} - Accuracy: {score:.4f}")

            print(f"\nBästa modellen är: {results['best_model_name']}")
            print(f"Total noggrannhet: {results['best_model'].score(X_test, y_test):.4f}")

            # Skapa visualisering
            
            visualizer.plot_complete_analysis(
                images=X_test,
                labels=y_test,
                conf_matrix=results['conf_matrix'],
                predictions=results['predictions'],
                model=results['best_model'],
                X_train=X_train,
                y_train=y_train,
                scores=results['scores']
            )

        except Exception as e:
                print(f"\nFel i ML-pipeline: {e}")
                print("Återgår till huvudmenyn...")


if __name__ == '__main__':
    main()
