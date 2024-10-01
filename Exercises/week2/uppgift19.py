# Uppgift 19: Enkel dataanalys med Pandas

import pandas as pd
import matplotlib.pyplot as plt
import os

# -------------------------------------------------------------------------------------
#               Uppgift 19: Enkel dataanalys med Pandas
# Ska används klasser för att organisera koden och inkluderar felhantering 
# för att hantera eventuella problem med filoperationer

# 1. - Läs in CSV-fil
# 2. - Visa de första 5 raderna
# 3. - Beräkna total försäljning per produkt
# 4. - Beräkna genomsnittlig försäljning per månad
# 5. - Hitta den dag med högst total försäljning
# 6. - Hitta produkten med högst total försäljning
# 7. - Skapa ett linjediagram över försäljningen över tid
# 8. - Spara diagrammet som en PNG-fil
# 9. - Skriva en sammanfattning till en textfil

class SalesAnalyzer:
    def __init__(self, filename) -> None:
        self.filename = filename
        self.data = None

    # Läs in CSV-fil
    def load_data(self):
        try:
            self.data = pd.read_csv(self.filename)

            # Konverterar datumkolumnen till datetime-format
            self.data['Date'] = pd.to_datetime(self.data['Date'], format='%Y-%m-%d')
            print(f"{self.filename} har lästs in korrekt.")
        except FileNotFoundError:
            print(f"Filen {self.filename} hittades inte.")
        except pd.errors.EmptyDataError:
            print(f"Filen {self.filename} är tom.")
        except pd.errors.ParserError:
            print(f"Filen {self.filename} har ett felaktigt format.")

    # Visa de första 5 raderna
    def show_first_rows(self, num_rows=5):
        if self.data is not None:
            total_sales = self.data.groupby('Product')['SalesAmount'].sum()
            print("\nTotal försäljning per produkt:")
            print(total_sales)
            return total_sales
        else:
            print("Data har inte laddats ännu.")
            return None

    # Beräkna total försäljning per produkt    
    def total_sales_per_product(self):
        if self.data is not None:
            try:
                if 'Product' in self.data.columns and 'SalesAmount' in self.data.columns:
                    total_sales = self.data.groupby('Product')['SalesAmount'].sum()
                    print("\nTotal försäljning per produkt:")
                    print(total_sales)
                    return total_sales
                else:
                    print("Kolumnerna 'Product' eller 'SalesAmount' saknas i datan.")
            except Exception as e:
                print(f"Ett fel inträffade under beräkningen: {e}")
        else:
            print("Data har inte laddats ännu.")
        return None
            
    # Beräkna genomsnittlig försäljning per månad
    def avg_sales_per_month(self):
        if self.data is not None:
            try:
                # Extrahera månad från datumet
                self.data['Month'] = self.data['Date'].dt.to_period('M')
                
                # Gruppindelning efter månad och beräkning av genomsnittlig försäljning
                avg_sales = self.data.groupby('Month')['SalesAmount'].mean()
                
                print("\nGenomsnittlig försäljning per månad:")
                for month, avg in avg_sales.items():
                    print(f"Månad: {month}, Genomsnittlig försäljning: {avg:.2f} SEK")
                
                return avg_sales
            except Exception as e:
                print(f"Ett fel inträffade under beräkningen: {e}")
                return None
        else:
            print("Data har inte laddats ännu.")
            return None
   
    # Hitta den dag med högst total försäljning
    def day_with_highest_sales(self):
        if self.data is not None:
            try:
                if 'Date' in self.data.columns and 'SalesAmount' in self.data.columns:
                    highest_sales_day = self.data.groupby('Date')['SalesAmount'].sum().idxmax()
                    
                    # Konvertera till datum utan tid
                    formatted_date = highest_sales_day.date()

                    print(f"\nDagen med högst försäljning är: {formatted_date}")
                    return formatted_date
                else:
                    print("Kolumnerna 'Date' eller 'SalesAmount' saknas i datan.")
            except Exception as e:
                print(f"Ett fel inträffade under beräkningen: {e}")
        else:
            print("Data har inte laddats ännu.")
        return None
    
    # Hitta produkten med högst total försäljning
    def product_with_highest_sales(self):
        if self.data is not None:
            try:
                if 'Product' in self.data.columns and 'SalesAmount' in self.data.columns:
                    highest_sales_product = self.data.groupby('Product')['SalesAmount'].sum().idxmax()

                    print(f"\nProdukten med högst försäljning är: {highest_sales_product}")
                    return highest_sales_product
                else:
                    print("Kolumnerna 'Date' eller 'SalesAmount' saknas i datan.")
            except Exception as e:
                print(f"Ett fel inträffade under beräkningen: {e}")
        else:
            print("Data har inte laddats ännu.")
        return None

    # Skapa ett linjediagram över försäljningen över tid
    def plot_sales_over_time(self, save_as_png=False):
        if self.data is not None:
            dayly_sales = self.data.groupby('Date')['SalesAmount'].sum()

            plt.figure(figsize=(10, 6))
            plt.plot(dayly_sales.index, dayly_sales.values, color='blue', linestyle='-', linewidth=2.0)
            plt.title("Försäljning över tid")
            plt.xlabel("Datum")
            plt.ylabel("Försäljning")
            plt.grid(True)
            if save_as_png:
                plt.savefig("sales_over_time.png")
                print("Diagram sparat som 'sales_over_time.png'.")
            plt.show()
        else:
            print("Data har inte laddats ännu.")

    # Skriva en sammanfattning till en textfil
    def save_summary(self):
        if self.data is not None:
            try:
                with open("sales_summary.txt", 'w', encoding='utf-8') as file:
                    file.write("Försäljningsanalys Sammanfattning\n")
                    file.write("===============================\n\n")

                    total_sales = self.total_sales_per_product()
                    if total_sales is not None:
                        file.write("Total försäljning per produkt:\n")
                        file.write(total_sales.to_string())
                        file.write("\n\n")

                    avg_sales = self.avg_sales_per_month()
                    if avg_sales is not None:
                        file.write("Genomsnittlig försäljning per månad:\n")
                        file.write(avg_sales.to_string())
                        file.write("\n\n")

                    highest_sales_product = self.product_with_highest_sales()
                    if highest_sales_product is not None:
                        file.write(f"Produkten med högst försäljning: {highest_sales_product}\n\n")

                print("Sammanfattning sparad till 'sales_summary.txt'.")
            except Exception as e:
                print(f"Ett fel uppstod vid sparning av sammanfattningen: {e}")
        else:
            print("Data har inte laddats ännu.")



def main():
    
    file_path = "sales_data.csv"

    # Skapa instans av SalesAnalyzer
    analyzer = SalesAnalyzer(file_path)

    # Ladda data från CSV
    analyzer.load_data()

    # Visa de första 5 raderna by default
    analyzer.show_first_rows()

    # Beräkna total försäljning per produkt
    analyzer.total_sales_per_product()

    # Beräkna genomsnittlig försäljning per månad
    analyzer.avg_sales_per_month()

    # Hitta den dag med högst total försäljning
    analyzer.day_with_highest_sales()

    # Hitta produkten med högst total försäljning
    analyzer.product_with_highest_sales()
        
    # Skapa ett linjediagram över försäljningen över tid
    analyzer.plot_sales_over_time(save_as_png=False)

    # Skriva en sammanfattning till en textfil
    analyzer.save_summary()


if __name__ == "__main__":
    main()


# --------------------------------------------------------------------------
# Intro to Pandas

# Ladda data från en CSV-fil
# data_frame = pd.read_csv(file_path)      # DataFrame är Pandas datastruktur

# Visar de första 5 raderna i DataFrame
# print(data_frame)

# Ger en översikt över DataFramen, inklusive datatyper och antal null-värden
# print(data_frame.info)

# Ger grundläggande statistik (medelvärde, standardavvikelse, etc.) för numeriska kolumner
# print(data_frame.describe())

# Välj specifika kolumner:
# selected_column = data_frame[['Product', 'SalesAmount']]

# Filtrera data (exempel: alla rader där värdet i en kolumn är större än ett visst värde):
# filtered_data = data_frame[data_frame['SalesAmount'] < 10]

# Räknar antalet saknade värden i varje kolumn
# print(data_frame.isnull().sum())

# Gruppera data efter en kolumn och räkna medelvärdet:
# grouped_data = data_frame.groupby('SalesAmount').mean()
# print(grouped_data)

# data_frame['SalesAmount'].plot(kind='hist') # Exempel på ett histogram
# plt.show()

