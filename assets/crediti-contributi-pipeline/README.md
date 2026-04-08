# crediti-contributi-pipeline
# Analisi crediti e contributi – pipeline dati e reportistica

## Descrizione
Questo progetto realizza una pipeline completa per:
- ingestione dati Excel
- normalizzazione in database JSON
- controllo di coerenza tramite log
- produzione di Excel analitici
- generazione di report Word

Il progetto è pensato per contesti istituzionali
in cui siano richieste:
- tracciabilità
- verificabilità
- separazione tra dati, analisi e output.

## Architettura
(qui uno schema o elenco a punti)

## Output principali
- Excel di incrocio con statistiche
- Report Word singoli e riepilogativi
- Log di verifica

## Documentazione
Vedi `docs/Manuale_Pacchetto_Crediti_Contributi.pdf`

## Note
Il repository non contiene dati reali né versioni portable/eseguibili.


Ogni passaggio è indipendente, riproducibile e verificabile.

---

## Tipologie di dati gestiti

Il sistema gestisce tre grandi categorie di dati:

- **Crediti**
  - crediti d’imposta
  - suddivisi per singola misura (es. credito carta, credito distribuzione, ecc.)
  - organizzati per anno

- **Contributi**
  - contributi economici non diretti
  - suddivisi per tipologia di intervento
  - organizzati per anno

- **Contributi diretti**
  - gestiti tramite file Excel dedicato
  - struttura per impresa e colonne annuali
  - importi a zero utilizzati per la storicità

---

## Componenti principali

### Normalizzazione dati (JSON)

I file Excel di input vengono letti e trasformati in un **database JSON unificato** che rappresenta la fonte dati centrale per tutte le elaborazioni successive.

Il database JSON contiene:
- anagrafiche imprese
- misure ricevute
- anni di riferimento
- importi
- tipologia di intervento

I file JSON NON vengono modificati manualmente.

---

### Log di controllo

Durante l’elaborazione il sistema genera file di log che permettono di:

- verificare la corrispondenza tra totali Excel e totali elaborati
- individuare errori di struttura o compilazione
- segnalare codici fiscali non validi
- garantire coerenza tra database e report

Il file più importante è `log_unito.txt`, che rappresenta la sintesi finale dei dati unificati.

---

### Excel di analisi e incrocio

Il progetto genera un file Excel strutturato con più fogli analitici, tra cui:

- **LEGENDA**  
  Descrizione del contenuto e della funzione dei fogli.

- **Matrice_Incrocio**  
  Elenco completo delle imprese con indicazione della presenza di crediti, contributi e contributi diretti.

- **Fogli di incrocio**  
  Sottoinsiemi di imprese che ricadono in specifiche combinazioni (crediti + contributi, ecc.).

- **Statistiche di base sulla popolazione**  
  Numero imprese, distribuzione per tipologia, copertura temporale.

- **Statistiche per singola misura**  
  Analisi economica di ciascuna misura (totali, media, mediana, massimo).

- **Statistiche temporali per misura**  
  Analisi anno per anno di ciascuna misura.

- **Sintesi per impresa**  
  Totale crediti, contributi e contributi diretti per ogni impresa.

Questo Excel costituisce **lo strumento principale di analisi e verifica**.

---

### Report Word

A partire dal database JSON vengono generati automaticamente:

- report singoli per ciascuna impresa
- un report unico riepilogativo

I report mantengono coerenza totale con:
- Excel di incrocio
- database JSON
- file di log

---

## Struttura del repository


crediti-contributi-pipeline/
│
├── README.md
│
├── docs/
│   └── Manuale_Pacchetto_Crediti_Contributi.pdf
│
├── src/
│   ├── crea_json_crediti.py
│   ├── crea_json_contributi.py
│   ├── crea_json_contributi_diretti.py
│   ├── crea_json_unito.py
│   ├── crea_excel_imprese_incroci.py
│   ├── crea_report_singoli.py
│   └── crea_report_unico.py
│
├── examples/
│   ├── struttura_excel_input.md
│   └── esempi_output_anonimi.xlsx
│
└── diagrams/
└── pipeline_flusso.png

---

## Documentazione

La documentazione completa del sistema è disponibile in:


docs/Manuale_Pacchetto_Crediti_Contributi.pdf

Il manuale descrive:
- la logica del sistema
- la struttura dei file
- il significato dei fogli Excel
- l’uso dei log
- il flusso operativo completo

---

## Note importanti

- Il repository NON contiene dati reali
- Il repository NON contiene versioni eseguibili o portabili
- Tutti gli esempi sono anonimi o dimostrativi
- Il progetto è pubblicato a scopo documentale e dimostrativo

---

## Contesto professionale

Questo progetto nasce come applicazione reale di:
- data engineering
- controllo qualità del dato
- reportistica istituzionale
- automazione di processi ripetibili

È pensato per ambienti in cui la correttezza e la verificabilità dei dati
sono più importanti della semplicità immediata.

