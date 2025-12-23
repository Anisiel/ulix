
import streamlit as st
from pathlib import Path

# ================
# Config pagina
# ================
st.set_page_config(page_title="Certificazioni", page_icon="🎓")
st.title("✅ Certificazioni")

# Base dir robusta (relativa a questo file)
BASE_DIR = Path(__file__).parent
CERT_DIR = BASE_DIR / "assets" / "cert"

def download_pdf(label: str, rel_path: str, key: str, primary: bool = False):
    """
    Mostra un download_button che funziona in locale e in deploy.
    - label: testo del bottone
    - rel_path: percorso relativo alla cartella 'assets/cert' oppure assoluto
    - key: chiave unica per il widget
    """
    # Se rel_path è relativo (tipico), risolviamolo da CERT_DIR; altrimenti usa il path assoluto
    path = CERT_DIR / rel_path if not rel_path.startswith("/") else Path(rel_path)
    if path.exists():
        try:
            data = path.read_bytes()  # bytes certi
            st.download_button(
                label=label,
                data=data,
                file_name=path.name,
                mime="application/pdf",
                key=key,
                type="primary" if primary else "secondary",
                use_container_width=True,
            )
        except Exception as e:
            st.error(f"Errore nel leggere il file '{path.name}': {e}")
    else:
        st.caption(f" File non trovato: {path}")

# ============================
# Sezione 1: Certificazioni recenti ottenute
# ============================
st.header(" ✅ Certificazioni **recenti** ottenute")

col1, col2, col3 = st.columns(3)

with col1:
    with st.expander(" **EIRSAF Advanced Full**", expanded=True):    
        st.markdown(
            "- Certificazione Internazionale di Alfabetizzazione Digitale\n"
            "- Data: 25-09-2025"
        )
        download_pdf(" Visualizza badge (PDF)", "Eirsaf_full.pdf", key="eirsaf_full", primary=True)

with col2:
    with st.expander(" **EIPASS Progressive Advanced**", expanded=True):
        st.markdown(
            "- Certificazione avanzata di competenze digitali\n"
            "- Data: 13/02/2025"
        )
        download_pdf(" Visualizza badge (PDF)", "Eipass_progressive.pdf", key="eipass_progressive", primary=True)

with col3:
    with st.expander(" **Certificato livello B2 Inglese**", expanded=True):
        st.markdown(
            "- Certificazione internazionale di competenze linguistiche\n"
            "- Data: 24/09/2024"
        )
        download_pdf(" Visualizza badge (PDF)", "Inglese_B2.pdf", key="inglese_b2", primary=True)

# ============================
# Sezione 2: Altri percorsi formativi
# ============================
st.header(" Altri percorsi formativi")

st.markdown("**ECDL Full Standard Certificate** — 24/09/2016")
download_pdf(" Visualizza certificato (PDF)", "Ecdl_full.pdf", key="ecdl_full")

st.markdown("**Percorso formativo docenti 600 ore (4 esami universitari)** — 20/07/2022")
download_pdf(
    " Visualizza certificato (PDF)",
    "Esperto_NPercorsoformativodocenti600ore.pdf",
    key="percorso_docenti"
)

# ============================
# Sezione 3: Autoformazione
# ============================
st.header(" Autoformazione")
st.markdown(
    "- **VBA** — Applicazioni evolute per Excel\n"
    "- **Python** — Applicazioni semplici per Analisi Dati\n"
    "- **CMD e PowerShell** — Applicazioni semplici per Gestione PC\n"
)
