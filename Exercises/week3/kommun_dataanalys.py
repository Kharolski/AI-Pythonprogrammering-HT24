import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


# Läser in data från en Excel-fil (.xlsx).
def load_data(filename):
    try:
        if not filename.endswith('.xlsx'):
            raise ValueError("Filen måste vara i Excel-format (.xlsx)")
        
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Filen {filename} hittades inte.")

        print(f"Läser in data från {filename}...")
        
        # Läser Excel-filen och skapar en DataFrame (df)
        df = pd.read_excel(filename, sheet_name='Sheet')
        print("Data inläst!")
        return df
    
    except ValueError as ve:
        print(str(ve))
    except FileNotFoundError as fnf:
        print(str(fnf))
    except Exception as e:
        print(f"Ett fel uppstod vid inläsning av data: {e}")

    return None


# Utför grundläggande analys av datan.
def display_basic_info(df):
    try:

        print("\nGrundläggande information om datasetet:")
        print(df.info())

        print("\nStatistik för numeriska kolumner:")
        print(df.describe())

        print("\nKolumner i datasetet:")
        print(df.columns.tolist())

        print("\nAntal saknade värden per kolumn:")
        print(df.isnull().sum())

    except Exception as e:
        print(f"Ett fel uppstod vid visning av grundläggande information: {e}")


# Skapar visualiseringar av datan.
def visualize_data(df):

    # Visualisera fördelningen av löner för ett specifikt område
    # Låt användaren välja område 
    print("Tillgängliga områden:")
    print(df['Område'].unique())

    work_area = input("Ange vilket område du vill analysera: ")    # området som ska analyseras
    while True:
        if work_area in df['Område'].values:
            break
        else:
            print("Du måste skriva den område som finns i listan..")

    # Nu kan du använda work_area för din analys
    print(f"Du har valt att analysera området: {work_area}")

    # Filtrera datan för det området
    df_filtrerad = df[df['Område'] == work_area]

    # Visualisera fördelningen av löner
    plt.figure(figsize=(10, 6))
    df_filtrerad['Lontothel'].hist(bins=30)

    plt.title(f'Fördelning av löner - {work_area}')
    plt.xlabel('Lön')
    plt.ylabel('Antal anställda')
    plt.savefig(f'lonfordelning_{work_area}.png')
    plt.close()
    print(f"Lönfördelning för {work_area} sparad som 'lonfordelning_{work_area}.png'")
    
    # Visualisera genomsnittlig lön per förvaltning
    avg_lon_per_forvaltning = df.groupby('Förvaltning')['Lontothel'].mean().sort_values(ascending=False)
    plt.figure(figsize=(12, 6))
    avg_lon_per_forvaltning.plot(kind='bar')

    plt.title('Genomsnittlig lön per förvaltning')
    plt.xlabel('Förvaltning')
    plt.ylabel('Genomsnittlig lön')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('lon_per_forvaltning.png')
    plt.close()
    print("Genomsnittlig lön per förvaltning sparad som 'lon_per_forvaltning.png'")


# Utför databehandling och skapar nya kolumner.
def process_data(df):

    # Skapa en ny kolumn för lönekvartiler
    df['Lönekvartil'] = pd.qcut(df['Lontothel'], q=4, labels=['Låg', 'Medellåg', 'Medelhög', 'Hög'])
    
    # Beräkna ålder baserat på anställningsdatum (om det finns)
    if 'Anställningsdatum' in df.columns:
        df['Anställningstid'] = (pd.Timestamp.now() - pd.to_datetime(df['Anställningsdatum'])).astype('<m8[Y]')
    
    return df



def main():
    filename = 'kommun.xlsx'
    df = load_data(filename)

    if df is not None:
        # display_basic_info(df)
        visualize_data(df)
 
        


if __name__ == "__main__":
    main()
