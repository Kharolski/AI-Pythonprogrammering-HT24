#
# Kombinerade övningar

# 1. - Använd Pandas för att beräkna korrelationsmatrisen för numeriska kolumner, 
#       använd sedan seaborn för att skapa en heatmap av denna matris.
# 2. - Skapa en NumPy-array med slumpmässiga tal, använd sedan Pandas för att skapa 
#       en DataFrame från denna array och Matplotlib för att plotta ett histogram av värdena.
# 3. -Använd Pandas för att gruppera data efter 'City' och 'Department', beräkna 
#       genomsnittlig 'Salary' för varje grupp, använd sedan dessa data för att 
#       skapa ett grupperat stapeldiagram med Matplotlib.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class CombinedExercises:
    def __init__(self, data_file):
        try:
            self.df = pd.read_csv(data_file)
            print(f"Data laddad från {data_file}")
        except FileNotFoundError:
            print(f"Fel: Filen {data_file} hittades inte.")
            self.df = None
        except Exception as e:
            print(f"Ett oväntat fel uppstod vid inläsning av data: {e}")
            self.df = None

    def correlation_heatmap(self):
        print("1. Korrelationsheatmap:")
        try:
            if self.df is None or self.df.empty:
                raise ValueError("Ingen data tillgänglig.")
            
            # Välj numeriska kolumner
            numeric_df = self.df.select_dtypes(include=[np.number])

            # Beräkna korrelationsmatrisen
            corr_matrix = numeric_df.corr()

            # Skapa heatmap
            plt.figure(figsize=(10, 8))
            sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
            plt.title('Korrelationsheatmap för numeriska kolumner')
            plt.tight_layout()
            plt.show()

        except ValueError as e:
            print(f"Fel: {e}")
        except Exception as e:
            print(f"Ett fel uppstod vid skapande av korrelationsheatmap: {e}")

    def numpy_pandas_histogram(self):
        print("2. NumPy array till Pandas DataFrame histogram:")
        try:
            # Skapa Numpy array med slumpmässiga tal
            np_array = np.random.randn(1000)  # 1000 slumpmässiga tal från normalfördelningen
            
            # Skapa Pandas DataFrame
            df = pd.DataFrame(np_array, columns=['Värden'])
            
            # Skapa histogram med Matplotlib
            plt.figure(figsize=(10, 6))
            plt.hist(df['Värden'], bins=30, edgecolor='black')
            plt.title('Histogram av slumpmässiga värden')
            plt.xlabel('Värde')
            plt.ylabel('Frekvens')
            plt.show()
        
        except Exception as e:
            print(f"Ett fel uppstod vid skapande av histogram: {e}")


    def grouped_bar_chart(self):
        print("3. Grupperat stapeldiagram:")
        try:
            if self.df is None:
                raise ValueError("Ingen data tillgänglig.")
            
            # Gruppera data och beräkna genomsnittlig lön
            grouped_data = self.df.groupby(['City', 'Department'])['Salary'].mean().unstack()
            
            # Skapa grupperat stapeldiagram
            ax = grouped_data.plot(kind='bar', figsize=(12, 6), width=0.8)
            plt.title('Genomsnittlig lön per stad och avdelning')
            plt.xlabel('Stad')
            plt.ylabel('Genomsnittlig lön')
            plt.legend(title='Avdelning', bbox_to_anchor=(1.05, 1), loc='upper left')
            plt.tight_layout()
            
            # Rotera x-axelns etiketter för bättre läsbarhet
            plt.xticks(rotation=45)
            
            plt.show()
        
        except ValueError as e:
            print(f"Fel: {e}")
        except Exception as e:
            print(f"Ett fel uppstod vid skapande av grupperat stapeldiagram: {e}")


def main():
    exercises = CombinedExercises('sample_data0.csv')

    exercises.correlation_heatmap()
    exercises.numpy_pandas_histogram()
    exercises.grouped_bar_chart()


if __name__ == "__main__":
    main()
