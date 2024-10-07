#
#  Pandas-övningar

# 1. - Skapa en DataFrame från en dictionary av listor som innehåller information om 5 olika länder (namn, befolkning, yta, kontinent).
# 2. - Ladda filen 'sample_data0.csv' och visa de sista 10 raderna.
# 3. - Beräkna och visa medianlönen för varje avdelning.
# 4. - Hitta den anställda med högst prestationspoäng i varje stad.
# 5. - Skapa en ny kolumn 'Lön_per_År_Erfarenhet' genom att dividera 'Salary' med 'Years_Experience'. Hantera eventuella division-med-noll-fel.
# 6. - Använd funktionen pd.melt() för att omforma DataFrame:n, och gör 'Salary' och 'Performance_Score' kolumnerna till variabler.
# 7. - Pivota DataFrame:n för att visa genomsnittlig lön för varje kombination av Stad och Avdelning.

import pandas as pd
import numpy as np
import os

class PandasExercise:
    def __init__(self):
        self.df = None
        self.country_df = None

    def country_dataframe(self):
        # skapa en ordbok med information om 5 olika länder
        country_data = {
            'Land': ['Sverige', 'Norge', 'Danmark', 'Finland', 'Island'],
            'Befolkning': [10379295, 5379475, 5822763, 5540720, 368792],
            'Yta': [450295, 385207, 43094, 338424, 103000],  # Yta i km²
            'Kontinent': ['Europa', 'Europa', 'Europa', 'Europa', 'Europa']
            }
        self.country_df = pd.DataFrame(country_data)
        print("DataFrame för länder:")
        print(self.country_df)
        print("\n")

    def load_data(self, filename):
        try:
            # Kontrollera om filen existerar
            if not os.path.exists(filename):
                raise FileNotFoundError(f"Filen '{filename}' hittades inte.")
            
            # Läs in data från CSV-filen
            self.df = pd.read_csv(filename)
            
            # Kontrollera om DataFrame:n är tom
            if self.df.empty:
                raise ValueError(f"Filen '{filename}' är tom eller innehåller ingen giltig data.")

            print("Sista 10 rader av sample_data0.csv:")
            print(self.df.tail(10)) # self.df.tail(10) visar de sista 10 raderna
            print("\n")

        except FileNotFoundError as e:
            print(f"Fel: {e}")
            raise
        except pd.errors.EmptyDataError:
            print(f"Fel: Filen '{filename}' är tom.")
            raise
        except Exception as e:
            print(f"Ett oväntat fel uppstod vid inläsning av '{filename}': {e}")
            raise

    def avg_salary(self):
        # groupby() för att gruppera data efter 'Department'.
        # ['Salary'].median() beräknar medianlönen för varje grupp.
        median_salary = self.df.groupby('Department')['Salary'].median()

        print("Medianlön för varje avdelning:")
        print(median_salary)
        print("\n")

    def highest_performance(self):
        try:
            if self.df is None or self.df.empty:
                raise ValueError("Ingen data laddad. Kör load_data först.")
            
            # self.df.loc[...] använder dessa index för att hämta de motsvarande raderna.
            # groupby('City')['Performance_Score'].idxmax() hittar indexet för den högsta prestationspoängen i varje stad.
            highest_point = self.df.loc[self.df.groupby('City')['Performance_Score'].idxmax()]

            print("Anställd med högst prestationspoäng i varje stad:")
            print(highest_point[['City', 'Name', 'Performance_Score']])
            print("\n")

            return highest_point[['City', 'Name', 'Performance_Score']]
        
        except KeyError as e:
            print(f"Fel: Kolumnen {e} finns inte i datasetet.")
        except Exception as e:
            print(f"Ett oväntat fel uppstod: {e}")

    
    def salary_by_experience(self):
        try:
            if self.df is None or self.df.empty:
                raise ValueError("Ingen data laddad. Kör load_data först.")

            # -------------------------------- 1 -------------------------------------
            # skapar en ny kolumn genom att dividera Salary med Years_Experience.
            self.df['Salary_by_Experience'] = self.df['Salary'] / self.df['Years_Experience']

            # Om någon har noll år erfarenhet så vi ersätter dessa med 0 med hjälp av replace().
            self.df['Salary_by_Experience'].replace([float('inf'), -float('inf')], 0, inplace=True)

            # -------------------------------- 2 -------------------------------------
            # använder apply() med en lambda-funktion för att skapa en ny kolumn.
            # Lambda-funktionen dividerar lön med erfarenhet, men returnerar NaN 
            # om erfarenheten är 0 för att undvika division med noll.
            self.df['Salary_by_Experience'] = self.df.apply(
                lambda row: row['Salary'] / row['Years_Experience'] 
                if row['Years_Experience'] != 0 else np.nan, axis=1
            )
            #------------------------------------------------------------------------

            # Visa de första raderna av den uppdaterade DataFrame:n
            print("DataFrame med ny kolumn Salary_by_Experience:")
            print(self.df[['Name', 'Salary', 'Years_Experience', 'Salary_by_Experience']].head())
            print("\n")

            # Beräkna och visa några statistiska mått
            stats = self.df['Salary_by_Experience'].describe()
            print("Statistik för Salary_by_Experience")
            print(stats)
            print("\n")

            return self.df[['Name', 'Salary', 'Years_Experience', 'Salary_by_Experience']]

        except KeyError as e:
            print(f"Fel: Kolumnen {e} finns inte i datasetet.")
        except Exception as e:
            print(f"Ett oväntat fel uppstod: {e}")


    def melt_dataframe(self):
        # Använder pd.melt() för att omforma DataFrame:n 
        # och göra 'Salary' och 'Performance_Score' till variabler.
        if self.df is not None:
            melted_data = pd.melt(
                self.df,
                id_vars=['Name', 'City', 'Department'],
                value_vars=['Salary', 'Performance_Score'],
                var_name='Variable',
                value_name='Value'
            )
            print("Omformad DataFrame med pd.melt():")
            print(melted_data.head(10))
            print("\n")
        else:
            print("Ingen data är laddad.")


    def pivot_dataframe(self):
        try:
            if self.df is None or self.df.empty:
                raise ValueError("Ingen data laddad. Kör load_data först.")
            
            # Pivota DataFrame:n för att visa genomsnittlig lön för varje kombination av Stad och Avdelning
            pivoted_df = self.df.pivot_table(
                values='Salary',
                index='City',
                columns='Department',
                aggfunc='mean'
            )

            print("Pivoterad DataFrame med genomsnittlig lön per Stad och Avdelning:")

            # pd.options.display.float_format = '{:.2}'.format

            print(pivoted_df)

            print("\n")

            return pivoted_df

        except KeyError as e:
            print(f"Fel: Kolumnen {e} finns inte i datasetet.")
        except Exception as e:
            print(f"Ett oväntat fel uppstod: {e}")


def main():
    analys = PandasExercise()

    analys.country_dataframe()
    analys.load_data('sample_data0.csv')

    analys.avg_salary()
    analys.highest_performance()
    analys.salary_by_experience()
    analys.melt_dataframe()
    analys.pivot_dataframe()


if __name__ == "__main__":
    main()

