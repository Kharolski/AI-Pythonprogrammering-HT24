# Användarguide för Sifferigenkännings-AI

## Första start av programmet
Vid första körningen visas fyra alternativ:
1. Samla in ny träningsdata
2. Analysera ny bild
3. Använd/återställ befintligt dataset
4. Avsluta programmet

### Initial setup
1. Välj alternativ 3 för att ladda grunddataset
2. Svara 'j' på frågan om backup
3. Programmet laddar grunddataset (110 bilder)
4. Efter träning blir alla alternativ tillgängliga

## Utöka dataset
När grunddataset är laddat kan du:
1. Välja alternativ 1 för att lägga till nya siffror
2. Granska prediktioner i batch om 5 siffror
   - J: Acceptera prediktion
   - X: Skippa bild
   - 0-9: Korrigera till rätt siffra
   - Q: Avbryt granskning
   
## Analysera nya bilder
1. Välj alternativ 2
2. Programmet visar:
   - Detekterade sifferregioner
   - Prediktioner för varje siffra
   - Visualisering med röda ramar

## Modellprestanda

### Grunddataset (110 bilder)
- SVM: ~54% noggrannhet
- RandomForest: ~45% noggrannhet
- MLP: ~45% noggrannhet

### Utökat dataset (160 bilder)
- SVM: ~58% noggrannhet
- RandomForest: ~67% noggrannhet
- MLP: ~58% noggrannhet

**Notera:**    För varje ny bild med verifierade siffror som läggs till i datasetet ökar modellernas noggrannhet. 
               Detta visar hur modellen kontinuerligt förbättras med mer träningsdata.

## Funktioner
- Intelligent sifferseparering
- Batch-granskning med interaktiv verifiering
- Automatisk bildbehandling och normalisering
- Träning av tre olika ML-modeller
- Optimering av hyperparametrar
- Visualisering av träningsresultat
- Backup-system för dataset
- Felhantering och validering