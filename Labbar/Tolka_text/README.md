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
Multi-layer Perceptron (MLP) Classifier, en enkel typ av neuralt nätverk lämplig för bildklassificering.

## Funktioner
1. Datainsamling och förbehandling av egna handskrivna siffror
2. Uppdelning av data i tränings- och testset
3. Modellträning
4. Utvärdering av modellens prestanda
5. Möjlighet att klassificera nya handskrivna siffror

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
- PIL (Python Imaging Library): för bildbehandling
- matplotlib: för visualisering

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

**Visualizer**
- plot_sample_images(): Visar exempel på bilder från datasetet
- plot_confusion_matrix(): Visar förväxlingsmatris för modellens prestanda

**Main**
- Huvudfunktionen som sköter hela processen från datainsamling till utvärdering.

## Framtida förbättringar
**Utöka datasetet**: Samla fler exempel per siffra för att förbättra modellens noggrannhet.
**Spara uppdelad data**: Implementera funktionalitet för att spara den uppdelade datan (tränings- och testset) för att möjliggöra noggranna jämförelser mellan olika modeller och inställningar.
**Implementera mer avancerade modeller**: Utforska och implementera mer avancerade modeller, som Convolutional Neural Networks (CNNs).
**Skillnad mellan siffror**: Skapa en modell som kan skilja mellan siffror som 1 och 11, vilket kan kräva mer noggrann analys av avstånd och former i handstilen.
**Utöka projektet**: Utforska möjligheten att utöka projektet till att inkludera klassificering av bokstäver eller andra symboler.

