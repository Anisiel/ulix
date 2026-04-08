# File di esempio

Questa cartella contiene file Excel di **ESEMPIO** utilizzati
per illustrare la struttura dei dati di input e di output
del progetto **crediti-contributi-pipeline**.

I file NON contengono dati reali.
I codici fiscali e le denominazioni sono fittizi oppure assenti.

L’obiettivo di questi file è esclusivamente **documentale e didattico**.

---

## Contenuto

- `credito_esempio.xlsx`  
  Esempio di file per i **crediti d’imposta**.  
  Mostra la struttura minima corretta dei fogli Excel di input:
  intestazioni, anno nel nome del foglio e riga `TOTALI`.

- `contributo_esempio.xlsx`  
  Esempio di file per i **contributi non diretti**.  
  Illustra il formato previsto per l’importo concesso e la gestione
  delle imprese beneficiarie.

- `contributi_diretti_esempio.xlsx`  
  Esempio di file per i **contributi diretti**, organizzati per impresa
  e per anno, con una colonna dedicata a ciascuna annualità.
  Gli importi pari a zero indicano assenza di contributo per l’anno.

- `imprese_crediti_contributi.xlsx`  
  File di **output di esempio** generato dal sistema.  
  Il file è volutamente privo di dati numerici e contiene esclusivamente
  il foglio `LEGENDA`, che descrive la struttura e la funzione dei fogli
  analitici che il sistema produce in esecuzione reale.

  Questo file serve a mostrare:
  - la struttura dell’output finale
  - i nomi e il significato dei fogli
  - il tipo di analisi disponibile

  Il contenuto completo viene generato automaticamente in fase operativa
  a partire da dati reali.

---

## Nota

I file di esempio rispettano **esattamente** le regole strutturali
utilizzate dal sistema in produzione, ma:

- contengono solo poche righe
- non rappresentano risultati reali
- non devono essere interpretati come dati ufficiali

I file sono inclusi nel repository esclusivamente per chiarire
la logica del progetto e facilitare la comprensione del codice.