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
# DOCUMENTAZIONE COMPLETA SU GITHUB
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

# =========================================================
# CODICE E DOCUMENTAZIONE INTERNA AL PORTFOLIO
# =========================================================

st.markdown("## 🔗 Codice e documentazione")

st.markdown(
    """
Per evitare dispersione e facilitare la consultazione, di seguito sono
disponibili **collegamenti diretti** ai principali materiali del progetto:
codice sorgente, documentazione operativa ed esempi strutturali.

Tutti i file sono consultabili direttamente da questa pagina.
"""
)

# =============================================================================
# PERCORSO ASSETS
# =============================================================================
from pathlib import Path

ASSETS = Path(__file__).resolve().parents[1] / "assets" / "crediti-contributi-pipeline"

def load_bytes(rel_path: str) -> bytes:
    return (ASSETS / rel_path).read_bytes()

def load_text(rel_path: str) -> str:
    return (ASSETS / rel_path).read_text(encoding="utf-8")

# =============================================================================
# README
# =============================================================================
st.markdown("### README del progetto")

cols = st.columns([0.75, 0.25])
with cols[0]:
    st.markdown(
        """
Il README descrive l’architettura generale della pipeline, le sue finalità
e la struttura del repository.
"""
    )
with cols[1]:
    data = load_text("README.md")
    st.download_button(
        label="⬇Scarica README",
        data=data,
        file_name="README.md",
        mime="text/plain",
        use_container_width=True
    )

with st.expander("Apri README"):
    st.code(data, language="markdown")

# =============================================================================
# MANUALE OPERATIVO PDF
# =============================================================================
st.markdown("### Manuale operativo")

cols = st.columns([0.75, 0.25])
with cols[0]:
    st.markdown(
        """
Manuale completo del sistema, con descrizione dettagliata della pipeline,
dei file Excel, dei log e degli output prodotti.
"""
    )
with cols[1]:
    pdf = load_bytes("documenti/Manuale_Pacchetto_Crediti_Contributi.pdf")
    st.download_button(
        label="⬇Scarica PDF",
        data=pdf,
        file_name="Manuale_Pacchetto_Crediti_Contributi.pdf",
        mime="application/pdf",
        use_container_width=True
    )

# =============================================================================
# SORGENTI
# =============================================================================
st.markdown("### Codice sorgente")

cols = st.columns([0.75, 0.25])
with cols[0]:
    st.markdown(
        """
Script Python che implementano la normalizzazione dei dati,
la generazione dell’Excel di analisi e dei report.
"""
    )
with cols[1]:
    src_code = load_text("sorgenti/crea_excel_imprese_incroci.py")
    st.download_button(
        label="Scarica script",
        data=src_code,
        file_name="crea_excel_imprese_incroci.py",
        mime="text/plain",
        use_container_width=True
    )

with st.expander("Apri codice sorgente"):
    st.code(src_code, language="python")

# =============================================================================
# ESEMPI
# =============================================================================
st.markdown("###File di esempio (input/output)")

st.markdown(
    """
File Excel di esempio utilizzati per illustrare la struttura
dei dati di input e dell’output analitico finale.
I dati sono fittizi o assenti.
"""
)

EXAMPLE_FILES = [
    ("credito_esempio.xlsx", "Credito d’imposta – esempio"),
    ("contributo_esempio.xlsx", "Contributo non diretto – esempio"),
    ("contributi_diretti_esempio.xlsx", "Contributi diretti – esempio"),
    ("imprese_crediti_contributi.xlsx", "Output analitico (strutturale)")
]

for fname, descr in EXAMPLE_FILES:
    cols = st.columns([0.75, 0.25])
    with cols[0]:
        st.markdown(f"**{descr}**  \n`{fname}`")
    with cols[1]:
        data = load_bytes(f"esempio/{fname}")
        st.download_button(
            label="Scarica",
            data=data,
            file_name=fname,
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True
        )

st.markdown("---")

st.caption(
    "Case study tecnico sviluppato in Python per la gestione strutturata "
    "di crediti, contributi e reportistica istituzionale e"
    "accesso diretto a codice, documentazione ed esempi per facilitare "
    "la comprensione del progetto senza navigare manualmente il repository."
)