# Användarguide för Sifferigenkännings-AI

## Första start av programmet
Vid första körningen visas endast två alternativ:
- 2. Använd befintligt dataset (backup)
- 3. Avsluta programmet

### Initial setup
1. Välj alternativ 2
2. Svara 'j' på frågan om backup
3. Programmet laddar grunddataset (110 bilder)
4. Efter träning blir alternativ 1 tillgängligt

## Utöka dataset
När grunddataset är laddat kan du:
1. Välja alternativ 1 för att lägga till nya siffror
2. Ändra testbild i setup_paths():
   - Från: 'test_image.png' (10 siffror)
   - Till: 'test_image2.png' (50 siffror)
   
3. Starta om programmet för att aktivera ny sökväg
4. Nu visas tre alternativ i menyn:
   - 1. Samla in ny träningsdata
   - 2. Använd befintligt dataset
   - 3. Avsluta programmet

## Modellprestanda

### Grunddataset (110 bilder)
- SVM: ~54% noggrannhet
- RandomForest: ~45% noggrannhet
- MLP: ~45% noggrannhet

### Utökat dataset (160 bilder)
- SVM: ~58% noggrannhet
- RandomForest: ~67% noggrannhet
- MLP: ~58% noggrannhet

## Funktioner
- Automatisk bildbehandling och normalisering
- Träning av tre olika ML-modeller
- Optimering av hyperparametrar
- Visualisering av träningsresultat
- Backup-system för dataset
- Felhantering och validering