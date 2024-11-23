# Supervised Learning Project - Klassificering av Egna Handskrivna Siffror

---

## Introduktion
Detta maskininlärningsprojekt syftar till att klassificera handskrivna siffror insamlade från användare. Projektet fungerar som en guide för utvecklingen och implementeringen av en maskininlärningsmodell och demonstrerar hur teknik kan användas för att lösa vardagliga problem.

## Applikationsbeskrivning

### Grundläggande idé
Utveckla ett personligt system för igenkänning av handskrivna siffror som lär sig och anpassar sig till individens unika handstil genom användning av maskininlärning och bildbehandlingstekniker.

### Mål
1. Att bygga en fungerande modell som kan känna igen användarens handskrivna siffror med en noggrannhet på minst 90%.
2. Att ge praktisk erfarenhet av hela maskininlärningsprocessen, inklusive datainsamling, förbehandling, modellträning och utvärdering.

### Vad jag vill uppnå
- En djupare förståelse för hur bildklassificering fungerar i praktiken.
- Praktisk erfarenhet av att träna och finjustera en maskininlärningsmodell.
- Ett verktyg som kan användas för att demonstrera principerna bakom maskininlärning på ett intuitivt sätt.
- En grund för framtida projekt inom bildbehandling och mönsterigenkänning.

### Projektets betydelse
Detta projekt illustrerar hur AI kan anpassas till individuella behov och preferenser. Genom att skapa en modell som lär sig specifikt från användarens handstil, visar vi hur maskininlärning kan skapa personliga lösningar. Detta koncept kan utvidgas till många andra områden där personlig anpassning är värdefull.

## Data
- Bilder av egna handskrivna siffror (28x28 pixlar, svartvita).
- Etiketter som anger vilken siffra varje bild representerar (0-9), där varje bild är kopplad till användarens inmatning för att säkerställa korrekthet.

### Datakälla
- Egna handskrivna siffror, fotograferade och förbehandlade.

## Modell
- **Multi-layer Perceptron (MLP) Classifier**: Används för att hantera komplexa relationer i data och är effektiv för att modellera icke-linjära mönster.
- **Support Vector Machine (SVM)**: Används för sin effektivitet i högdimensionella rum, vilket är särskilt användbart när datamängden är liten.
- **Random Forest Classifier**: Används för att förbättra noggrannheten genom ensemblemetodik, vilket minskar överanpassning.
- **Modelloptimering genom GridSearchCV**: Implementeras för att optimera hyperparametrar och förbättra modellens prestanda.

### Val av Algoritm/Modell
Valet av algoritmer grundas på deras egenskaper och hur väl de lämpar sig för uppgiften att klassificera handskrivna siffror:
- **MLP**: Fungerar bra med komplexa mönster och icke-linjära relationer.
- **SVM**: Utmärkt för små datamängder och högdimensionella rum.
- **Random Forest**: Robust mot överanpassning och effektiv i att hantera varians.

## Funktioner

1. Samlar in och förbehandlar bilder av handskrivna siffror
2. Intelligent segmentering av siffror med optimerad separation
3. Batch-granskning med interaktiv verifiering (5 siffror åt gången)
4. Tränar och jämför flera ML-modeller automatiskt
5. Analyserar nya bilder med tränad modell
6. Sparar verifierad data med dublettkontroll

## Användargränssnitt

### Menystruktur
1. Samla in ny träningsdata
2. Analysera ny bild
3. Använd/återställ befintligt dataset
4. Avsluta programmet

### Verifieringsprocess
- Visar 5 siffror åt gången för effektiv granskning
- Stöd för snabbkommandon (J/X/0-9/Q)
- Direkt feedback med bildvisning
- Möjlighet att korrigera felaktiga prediktioner

## ImageProcessor
- Förbättrad regionseparering med optimerade tröskelvärden
- Intelligent sammanslagning av närliggande regioner
- Robust detektering av enskilda siffror
- Automatisk kontrastförbättring och brusreducering

## Visualizer
- Batch-visualisering med subplot-layout
- Interaktiv granskning med matplotlib
- Tydlig presentation av prediktioner
- Effektiv hantering av figurvisning

## Begränsningar
- Kräver tydlig separation mellan siffror för optimal detektering
- Batch-granskning begränsad till 5 siffror åt gången
- Dataset måste finnas för att använda vissa funktioner
- Fixerad bildstorlek (28x28 pixlar) måste följa specifikationer

## Krav
Följande krav specificerar de nödvändiga elementen för att genomföra projektet.

### Datakrav
- Bilddata: 28x28 pixlar, svartvita (gråskala).
- Etiketter: Heltal 0-9.
- Minst 10 exempel per siffra för att säkerställa tillförlitlighet.

### Bibliotek
- **scikit-learn**: För modellträning och utvärdering.
- **numpy**: För numeriska operationer och hantering av data.
- **PIL (Python Imaging Library)**: För grundläggande bildhantering.
- **opencv (cv2)**: För avancerad bildbehandling och segmentering.
- **matplotlib**: För visualisering av resultat.

### Klasser och metoder

**DataCollector**
- `collect_images()`: Samlar in handskrivna siffror från användare.
- `load_existing_dataset()`: Laddar ett befintligt dataset om det finns.
- `preprocess_images()`: Förbehandlar bilder för analys.

**DataLoader**
- `load_data()`: Laddar det förbehandlade datasetet.
- `split_data()`: Delar upp data i tränings- och testset.

**HandwrittenDigitClassifier**
- `train_model()`: Tränar MLP Classifier-modellen.
- `evaluate_model()`: Utvärderar modellens prestanda.
- `predict()`: Klassificerar nya handskrivna siffror.

**ImageProcessor**
- `analyze_new_image()`: Analyserar nya bilder med tränad modell
- `detect_digit_regions()`: Detekterar och separerar sifferregioner
- `enhance_image()`: Förbättrar bildkvalitet med kontrastjustering
- `prepare_image()`: Förbereder bilder för ML-modellen
- `process_regions_with_ai()`: Klassificerar detekterade sifferregioner med ML-modellen

**ModelComparator**
- `train_and_evaluate()`: Tränar och utvärderar flera modeller
- `optimize_hyperparameters()`: Optimerar modellparametrar
- `compare_models()`: Jämför olika modellers prestanda

**Visualizer**
- `review_predictions()`: Hanterar batch-granskning av prediktioner
- `plot_complete_analysis()`: Visar omfattande analysresultat
- `setup_style()`: Konfigurerar visualiseringsstil

**Main**
- Huvudfunktionen som sköter hela processen från datainsamling till utvärdering.

## Tekniska Detaljer

### Bildbehandling
- Optimerad regionseparering (0.8 horisontell, 1.0 vertikal tolerans)
- Adaptiv tröskling för robust segmentering
- Kontrastförbättring med CLAHE
- Brusreducering med bevarad detaljskärpa

### ML Pipeline
- Automatisk modelloptimering med GridSearchCV
- Jämförelse av flera modelltyper (MLP, SVM, Random Forest)
- Interaktiv verifiering av prediktioner
- Inkrementell datasetuppbyggnad

## Framtida förbättringar
- **Implementera mer avancerade modeller**: Utforska och implementera Convolutional Neural Networks (CNNs) för att fånga mer komplexa mönster i handskrivna siffror.
- **Utöka projektet**: Utforska möjligheten att inkludera klassificering av bokstäver eller andra symboler.
- **Realtidsigenkänning**: Implementera en live-kameraström för direktklassificering av handskrivna siffror.
- **Förbättrad segmentering**: Utveckla mer robusta metoder för att hantera sammanhängande siffror och olika skrivstilar.
- **Webbgränssnitt**: Skapa ett användarvänligt webbgränssnitt för enkel interaktion med systemet.
- **Automatisk dataaugmentering**: Implementera tekniker för att automatiskt generera fler träningsexempel genom rotation, skalning och brusning.
