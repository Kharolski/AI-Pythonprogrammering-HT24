# Intro Matplotlib - Visualisering

import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------------------
#           Intro:

x_label = [1, 2, 3, 4, 5, 6, 7, 8]   # x-axelns värden, de som kommer att visas horisontellt på grafen
y_label = [1, 4, 6, 7, 5, 3, 7, 10]  # y-axelns värden, de som kommer att visas vertikalt och representerar datapunkternas höjd

# plt.plot() används för att skapa en linje i diagrammet:
# - x_label: Värdena längs x-axeln (horisontell axel)
# - y_label: Värdena längs y-axeln (vertikal axel)
# - color='blue': Färgen på linjen blir blå.
# - linestyle='dashdot': Linjestilen är en kombination av punkter och streck (andra alternativ är '-' (solid), '--' (streckad), ':' (prickad)).
# - marker='o': Markerar varje datapunkt med en cirkel.
# - linewidth=2.0: Sätter tjockleken på linjen till 2.0 (tunnare eller tjockare beroende på värdet).
# - label='Inner titel': Namnet eller titeln för denna linje, som visas i en legend (förklaringsruta) om den aktiveras.
# plt.plot(x_label, y_label, color='blue', linestyle='dashdot', marker='o', linewidth=2.0, label='Inner titel')

# plt.axis() används för att bestämma gränserna på axlarna:
# - [0, 15]: x-axeln börjar vid 0 och sträcker sig till 15.
# - [0, 10]: y-axeln börjar vid 0 och sträcker sig till 10.
# plt.axis([0, 15, 0, 10])

# Lägg till titel och etiketter för axlarna:
# plt.title("Min titel")          # Titel visas ovanför diagrammet
# plt.xlabel("Horizontal Titel")  # Etikett för x-axeln (den horisontella axeln) visas under diagrammet
# plt.ylabel("Vertical Titel")    # Etikett för y-axeln (den vertikala axeln) visas till vänster om diagrammet

# plt.legend() visar legenden, där etiketten för linjen (definierad med 'label' i plt.plot()) visas:
# plt.legend()                    # Visar legenden med etiketten 'Inner titel'

# plt.grid() lägger till ett rutnät i diagrammet för att göra det lättare att läsa av punkterna.
# True betyder att rutnätet visas, False skulle dölja det.
# plt.grid(True)                  # Aktiverar rutnät i bakgrunden

# plt.show() används för att visa grafen på skärmen.
# plt.show()                      # Visar det slutgiltiga diagrammet med alla ovanstående inställningar

# -----------------------------------------------------------------------------------------
#           Uppgift:

# Temperaturdata för en vecka (sju dagar)
temperatures = [15.5, 16.0, 14.6, 12.9, 14.3, 16.2, 15.7]

# Dagarna på veckan
days = ["Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag", "Söndag"]

# Skapa linjediagram
plt.plot(days, temperatures, color='blue', linestyle='--', marker='o', markersize=8, label='Temperatur (°C)')

# Lägga till titel och etiketter
plt.title("Medeltemperatur under veckan", fontsize=14)
plt.xlabel("Dagar", fontsize=12)
plt.ylabel("Temperatur (°C)", fontsize=12)

# Anpassa stil och färg på linjen
plt.grid(True)  # Lägg till ett rutnät i diagrammet
plt.legend()  # Visa legend för linjen

# Visa diagrammet
plt.show()





