#
# Matplotlib- och Seaborn-övningar

# 1. - Skapa ett staplat stapeldiagram som visar antalet anställda i varje Experience_Category för varje Stad.
# 2. - Generera ett par-plot med seaborn för de numeriska kolumnerna i DataFrame:n.
# 3. - Skapa ett violindiagram som jämför fördelningen av Performance_Scores över olika Avdelningar.
# 4. - Gör ett cirkeldiagram som visar andelen anställda i varje Avdelning.
# 5. - Skapa en 2x2 subplot med olika typer av diagram (linje, spridning, stapel och histogram) med data från DataFrame:n.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class VisualizationExercises:
    def __init__(self, data_file):
        try:
            self.df = pd.read_csv(data_file)
            print(f"Data laddad från {data_file}")
            
            # 
            self.generate_experiance_category()
        
        except FileNotFoundError:
            print(f"Fel: Filen {data_file} hittades inte.")
            self.df = None
        except pd.errors.EmptyDataError:
            print(f"Fel: Filen {data_file} är tom.")
            self.df = None
        except Exception as e:
            print(f"Ett oväntat fel uppstod vid inläsning av data: {e}")
            self.df = None

    # Kontrollerar först om 'Years_Experience' kolumnen finns i datasetet.
    # definierar en inre funktion categorize som tar antalet års erfarenhet som input och returnerar en kategori baserat på följande logik:
    #   - Om mindre än 3 års erfarenhet: 70% chans för "Junior", 30% chans för "Mid"
    #   - Om mellan 3 och 7 års erfarenhet: 20% chans för "Junior", 60% chans för "Mid", 20% chans för "Senior"
    #   - Om 7 eller fler års erfarenhet: 30% chans för "Mid", 70% chans för "Senior"
    # använder apply funktionen för att applicera categorize på varje rad i 'Years_Experience' kolumnen
    def generate_experiance_category(self):
        try:
            if 'Years_Experience' not in self.df.columns:
                raise KeyError("Kolumnen 'Years_Experience' saknas i datasetet.")
            
            # Definiera gränser för kategorierna
            def categorize(years):
                if years < 3:
                    return np.random.choice(['Junior', 'Mid'], p=[0.7, 0.3])
                elif years < 7:
                    return np.random.choice(['Junior', 'Mid', 'Senior'], p=[0.2, 0.6, 0.2])
                else:
                    return np.random.choice(['Mid', 'Senior'], p=[0.3, 0.7])
                
            # Applicera kategorisering och lägg till slumpmässighet
            self.df['Experience_Category'] = self.df['Years_Experience'].apply(categorize)

            print("Kolumnen 'Experience_Category' har skapats.")
            print(self.df['Experience_Category'].value_counts())

        except KeyError as e:
            print(f"Fel: {e}")
        except Exception as e:
            print(f"Ett fel uppstod vid generering av Experience_Category: {e}")


    # 1. Staplat stapeldiagram som visar antalet anställda i varje Experience_Category för varje Stad
    def stacked_bar_chart(self):
        print("1. Staplat stapeldiagram:")
        try:
            if self.df is None or self.df.empty:
                raise ValueError("Ingen data tillgänglig.")
            
            # Räkna antalet anställda i varje kategori och stad
            # groupby() grupperar data efter stad och erfarenhetskategori
            # size() räknar antalet i varje grupp
            # unstack() omformar data för att passa stapeldiagrammet
            data = self.df.groupby(['City', 'Experience_Category']).size().unstack()

            # Diagrammet
            # plot(kind='bar', stacked=True) skapar ett staplat stapeldiagram
            data.plot(kind='bar', stacked='True', figsize=(10, 6))

            plt.title('Antal anställda per erfarenhetskategori i varje stad')
            plt.xlabel('Stad')
            plt.ylabel('Antal anstälda')

            plt.legend(title='Erfarenhetskategori', bbox_to_anchor=(1.05, 1), loc='upper left')
            plt.tight_layout()
            plt.show()

        except KeyError as e:
            print(f"Fel: Kolumnen {e} saknas i datasetet.")
        except Exception as e:
            print(f"Ett fel uppstod vid skapande av staplat stapeldiagram: {e}")

    # 2. Par-plot med seaborn för de numeriska kolumnerna i DataFrame:n.
    def pair_plot(self):
        print("2. Par-plot:")
        try:
            if self.df is None or self.df.empty:
                raise ValueError("Ingen data tillgänglig.")

            sns.pairplot(self.df, vars=['Salary', 'Years_Experience', 'Performance_Score'], hue='Department')
            plt.show()
        
        except ValueError as e:
            print(f"Fel: {e}")
        except Exception as e:
            print(f"Ett fel uppstod vid skapande av par-plot: {e}")

    # 3. Ett violindiagram som jämför fördelningen av Performance_Scores
    def violin_plot(self):
        print('3. Violindiagram:')
        try:
            if self.df is None or self.df.empty:
                raise ValueError("Ingen data tillgänglig.")
            
            plt.figure(figsize=(12, 6))
            sns.violinplot(x='Department', y='Performance_Score', data=self.df)

            plt.title('Fördelning av prestationspoäng över avdelningar')
            plt.xlabel('Avdelning')
            plt.ylabel('Prestationspoäng')
            plt.tight_layout()
            plt.show()
            
        except KeyError as e:
            print(f"Fel: Kolumnen {e} saknas i datasetet.")
        except Exception as e:
            print(f"Ett fel uppstod vid skapande av violindiagram: {e}")

    # 4. Cirkeldiagram som visar andelen anställda i varje Avdelning.
    def pie_chart(self):
        print("4. Cirkeldiagram:")
        try:
            if self.df is None or self.df.empty:
                raise ValueError("Ingen data tillgänglig.")
            
            # value_counts() räknar antalet anställda i varje avdelning
            department_counts = self.df['Department'].value_counts()
            plt.figure(figsize=(10, 8))

            # plt.pie() skapar cirkeldiagrammet
            # autopct='%1.1f%%' visar procentandelar på diagrammet
            plt.pie(department_counts.values, labels=department_counts.index, autopct='%1.1f%%')

            plt.title('Andel anställda i varje avdelning')
            plt.axis('equal')
            plt.show()
            
        except KeyError as e:
            print(f"Fel: Kolumnen {e} saknas i datasetet.")
        except Exception as e:
            print(f"Ett fel uppstod vid skapande av cirkeldiagram: {e}")

    # 5. En 2x2 subplot med olika typer av diagram (linje, spridning, stapel och histogram) 
    def subplot_grid(self):
        print("5. 2x2 subplot:")
        try:
            if self.df is None or self.df.empty:
                raise ValueError("Ingen data tillgänglig.")
            
            # plt.subplots(2, 2) skapar en 2x2 grid av subplots
            # Varje axs[i, j] representerar en subplot där vi kan rita olika diagram
            fig, axs = plt.subplots(2, 2, figsize=(12, 10))

            # Linjediagram
            self.df.groupby('Years_Experience')['Salary'].mean().plot(ax=axs[0, 0])
            axs[0, 0].set_title('Genomsnittlig lön vs. Erfarenhet')
            axs[0, 0].set_xlabel('År av erfarenhet')
            axs[0, 0].set_ylabel('Prestationspoäng')

            # Spridningsdiagram
            axs[0, 1].scatter(self.df['Years_Experience'], self.df['Performance_Score'])
            axs[0, 1].set_title('Erfarenhet vs. Prestationspoäng')
            axs[0, 1].set_xlabel('År av erfarenhet')
            axs[0, 1].set_ylabel('Prestationspoäng')

            # Stapeldiagram
            self.df['City'].value_counts().plot(kind='bar', ax=axs[1, 0])
            axs[1, 0].set_title('Antal anställda per stad')
            axs[1, 0].set_xlabel('Stad')
            axs[1, 0].set_ylabel('Antal anställda')

            # Histogram
            axs[1, 1].hist(self.df['Salary'], bins=20)
            axs[1, 1].set_title('Fördelning av löner')
            axs[1, 1].set_xlabel('Lön')
            axs[1, 1].set_ylabel('Antal anställda')

            plt.tight_layout()
            plt.show()

        except KeyError as e:
            print(f"Fel: Kolumnen {e} saknas i datasetet.")
        except Exception as e:
            print(f"Ett fel uppstod vid skapande av subplot grid: {e}")



def main():
    viz = VisualizationExercises('sample_data0.csv')

    # viz.stacked_bar_chart()
    # viz.pair_plot()
    # viz.violin_plot()
    # viz.pie_chart()
    viz.subplot_grid()




if __name__ == "__main__":
    main()
