import streamlit as st

# =========================================================
# CONFIG
# =========================================================

st.set_page_config(
    page_title="Crediti e Contributi – Data Pipeline",
    page_icon="📊"
)

# =========================================================
# TITOLO
# =========================================================

st.title(" Crediti e Contributi – Data Pipeline (Case study)")

st.markdown(
    """
Questo progetto nasce come **case study tecnico** per la progettazione
di una pipeline di analisi dati in ambito amministrativo e istituzionale.

L’obiettivo non è la semplice aggregazione dei numeri, ma la costruzione
di un **processo completo, verificabile e documentato**, capace di
garantire coerenza tra dati di input, controlli intermedi e output finali.
"""
)

# =========================================================
# IL PROBLEMA
# =========================================================

st.markdown("##  Il problema")

st.markdown(
    """
In contesti reali, i dati relativi a **crediti**, **contributi** e
**contributi diretti** sono spesso distribuiti su:

- più file Excel
- annualità diverse
- strutture non omogenee
- regole implicite non documentate

Il problema principale non è solo “sommarli”, ma poter rispondere in modo
affidabile a domande come:

- quali imprese hanno beneficiato di quali misure?
- in quali anni?
- con quali importi?
- con quali controlli a supporto?

Questo richiede **tracciabilità, separazione delle fasi e verificabilità**.
"""
)

# =========================================================
# LA SOLUZIONE
# =========================================================

st.markdown("##  La soluzione progettata")

st.markdown(
    """
Ho progettato una **pipeline dati modulare**, interamente sviluppata in
Python, che separa chiaramente ogni fase del processo:

- ingestione dei file Excel
- normalizzazione dei dati in database JSON
- generazione automatica di file di log
- produzione di Excel analitici strutturati
- generazione di report Word coerenti

Ogni fase è **indipendente**, **ripetibile** e **documentata**.
"""
)

# =========================================================
# ARCHITETTURA
# =========================================================

st.markdown("##  Architettura della pipeline")

st.markdown(
    """
La pipeline segue una sequenza logica ben definita:
Excel di input
↓
Database JSON unificato
↓
Log di controllo
↓
Excel di analisi e incrocio
↓
Report Word
Questa architettura consente controlli puntuali a ogni livello e garantisce
la totale coerenza tra i diversi output prodotti.
"""
)

# =========================================================
# OUTPUT
# =========================================================
st.markdown("## Output prodotti")

st.markdown(
    """
Il sistema genera automaticamente:

**Excel di analisi e incrocio**, con:
- matrice delle imprese
- statistiche di popolazione
- analisi per singola misura (crediti e contributi)
- andamento temporale delle erogazioni
- sintesi economica per impresa

**Report Word**:
- report singoli per impresa
- report unico riepilogativo

**File di log**:
- controllo di coerenza tra Excel e dati elaborati
- supporto ad audit e verifiche amministrative
"""
)

# =========================================================
# VALORE DEL PROGETTO
# =========================================================

st.markdown("## Perché è un progetto rilevante")

st.markdown(
    """
Questo non è un semplice esercizio di analisi dati, ma un esempio di
**progettazione di un sistema informativo orientato alla qualità del dato**.

Il progetto dimostra competenze in:

- data engineering
- normalizzazione dei dati
- controllo di coerenza
- automazione della reportistica
- documentazione tecnica

L’attenzione non è sul singolo output, ma sull’intero **processo**.
"""
)

# =========================================================
# CODICE E DOCUMENTAZIONE
# =========================================================

st.markdown("## Codice e documentazione")

st.markdown(
    """
Il codice e la documentazione completa del progetto sono disponibili su GitHub.

- **Repository GitHub:**  
  https://github.com/Anisiel/crediti-contributi-pipeline

- **Documentazione PDF:**  
  Manuale operativo con descrizione della pipeline, degli output e dei log

Il repository **non contiene dati reali né versioni eseguibili**:
sono presenti solo codice, esempi strutturali e documentazione.
"""
)

st.markdown("---")

st.caption(
    "Case study tecnico sviluppato in Python per la gestione strutturata "
    "di crediti, contributi e reportistica istituzionale."
)