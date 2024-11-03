# Supervised Learning Project - Klassificering av Egna Handskrivna Siffror

---

## Introduktion
Detta är ett maskininlärningsprojekt som syftar till att klassificera egna handskrivna siffror. Det fungerar som en guide för projektets utveckling och implementering.

## Applikationsbeskrivning

### Grundläggande idé
Skapa ett personligt system för igenkänning av handskrivna siffror som kan lära sig och anpassa sig till en individs unika handstil. Detta projekt syftar till att demonstrera hur maskininlärning kan användas för att lösa ett vardagligt problem och samtidigt ge insikt i processen att skapa en egen datauppsättning.

### Mål
1. Att bygga en fungerande modell som kan känna igen användarens handskrivna siffror med hög noggrannhet.
2. Att ge praktisk erfarenhet av hela maskininlärningsprocessen, från datainsamling till modellträning och utvärdering.

### Vad jag vill uppnå
- En djupare förståelse för hur bildklassificering fungerar i praktiken.
- Praktisk erfarenhet av att träna och finjustera en maskininlärningsmodell.
- Ett verktyg som kan användas för att demonstrera principerna bakom maskininlärning på ett intuitivt sätt.
- En grund för framtida projekt inom bildbehandling och mönsterigenkänning.

### Projektets betydelse
Detta projekt illustrerar hur AI kan anpassas till individuella behov och preferenser. Genom att skapa en modell som lär sig specifikt från användarens handstil, visar vi hur maskininlärning kan skapa personliga lösningar. Detta koncept kan utvidgas till många andra områden där personlig anpassning är värdefull.

## Data
- Bilder av egna handskrivna siffror (28x28 pixlar, svartvita)
- Etiketter som anger vilken siffra varje bild representerar (0-9)

### Datakälla
- Egna handskrivna siffror, fotograferade och förbehandlade

## Modell
- Multi-layer Perceptron (MLP) Classifier
- Support Vector Machine (SVM)
- Random Forest Classifier
- Modelloptimering genom GridSearchCV

## Funktioner
1. Datainsamling och förbehandling av egna handskrivna siffror
2. Uppdelning av data i tränings- och testset
3. Modellträning
4. Utvärdering av modellens prestanda
5. Möjlighet att klassificera nya handskrivna siffror
6. Jämförelse av olika maskininlärningsmodeller
7. Automatisk hyperparameteroptimering
8. Validering av sifferkvalitet
9. Batch-processering av bilder

## Begränsningar
- Begränsat till siffror 0-9
- Använder endast svartvita bilder
- Fixerad bildstorlek (28x28 pixlar)
- Begränsat antal träningsexempel (beroende på hur många bilder ska samlas in)

## Krav
Följande krav specificerar de nödvändiga elementen för att genomföra projektet

### Datakrav
- Bilddata: 28x28 pixlar, svartvita (gråskala)
- Etiketter: Heltal 0-9
- Minst 10 exempel per siffra, helst fler

### Bibliotek
- scikit-learn: för modellträning och utvärdering
- numpy: för numeriska operationer
- PIL (Python Imaging Library): för grundläggande bildhantering i DataCollector
- opencv (cv2): för avancerad bildbehandling och segmentering
- matplotlib: för visualisering
- seaborn: för förbättrad statistisk visualisering
- glob: för filhantering
- os: för operativsystemsoperationer

### Klasser och metoder

**DataCollector**
- collect_images(): Samlar in bilder av handskrivna siffror
- is_image_saved(): Kontrollera om en bild redan finns sparad genom att jämföra
- load_existing_dataset(): Kollar om dataset redan finns och laddar den
- preprocess_images(): Förbehandlar bilder (storleksändring, svartvitt, etc.)
- save_dataset(): Sparar det förbehandlade datasetet

**DataLoader**
- load_data(): Laddar det förbehandlade datasetet
- split_data(): Delar upp data i tränings- och testset

**HandwrittenDigitClassifier**
- train_model() : Tränar MLP Classifier-modellen
- evaluate_model() : Utvärderar modellens prestanda
- predict() : Klassificerar nya handskrivna siffror

**ImageProcessor**
- enchance_image(): Förbättrar bildkvaliteten
- process_with_prediction(): Visar och validerar extraherade siffror
- batch_process(): Hanterar flera bilder samtidigt
- _segment_image(): Segmenterar bilder till individuella siffror
- _is_valid_digit(): Validerar sifferkvalitet

**ModelComparator**
- optimize_hyperparameters(): Optimerar hyperparametrar för varje modell
- compare_models(): Jämför och visualiserar modellernas prestanda

**Visualizer**
- plot_sample_images(): Visar exempel på bilder från datasetet
- plot_confusion_matrix(): Visar förväxlingsmatris för modellens prestanda

**Main**
- Huvudfunktionen som sköter hela processen från datainsamling till utvärdering.

## Framtida förbättringar

**Implementera mer avancerade modeller**: Utforska och implementera Convolutional Neural Networks (CNNs) och andra djupa arkitekturer.
**Utöka projektet**: Utforska möjligheten att utöka projektet till att inkludera klassificering av bokstäver eller andra symboler.
**Realtidsigenkänning**: Implementera en live-kameraström för direktklassificering av handskrivna siffror.
**Förbättrad segmentering**: Utveckla mer robusta metoder för att hantera sammanhängande siffror och olika skrivstilar.
**Webbgränssnitt**: Skapa ett användarvänligt webbgränssnitt för enkel interaktion med systemet.
**Automatisk dataaugmentering**: Implementera tekniker för att automatiskt generera fler träningsexempel genom rotation, skalning och brusning.


