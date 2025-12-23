
import streamlit as st
from pathlib import Path

# ================
# Config pagina
# ================
st.set_page_config(page_title="Certificazioni", page_icon="✅")
st.title("✅ Certificazioni")

# ================
# Percorsi assoluti
# ================
CERT_DIR = ("cert").resolve()  # solo resolve perchè calcola l'assoluto giusto (ulix in questo caso)

def download_pdf(label: str, filename: str, key: str, primary: bool = False):
    """
    Mostra un download_button usando PERCORSO ASSOLUTO in 'cert/'.
    - filename: nome file (es. 'Eirsaf_full.pdf')
    """
    abs_path = CERT_DIR / filename
    if abs_path.exists():
        data = abs_path.read_bytes()
        st.download_button(
            label=label,
            data=data,
            file_name=abs_path.name,
            mime="application/pdf",
            key=key,
            type="primary" if primary else "secondary",
            use_container_width=True,
        )
    else:
        st.caption(f" File non trovato: {abs_path}")

# ============================
# Sezione 1: Certificazioni recenti ottenute
# ============================
st.header(" Certificazioni **recenti** ottenute")

col1, col2, col3 = st.columns(3)

with col1:
    with st.expander(" **EIRSAF Advanced Full**", expanded=True):
        st.markdown("- Certificazione Internazionale di Alfabetizzazione Digitale\n- Data: 25-09-2025")
        download_pdf(" Visualizza badge (PDF)", "Eirsaf_full.pdf", key="eirsaf_full", primary=True)

with col2:
    with st.expander(" **EIPASS Progressive Advanced**", expanded=True):
        st.markdown("- Certificazione avanzata di competenze digitali\n- Data: 13/02/2025")
        download_pdf(" Visualizza badge (PDF)", "Eipass_progressive.pdf", key="eipass_progressive", primary=True)

with col3:
    with st.expander(" **Certificato livello B2 Inglese**", expanded=True):
        st.markdown("- Certificazione internazionale di competenze linguistiche\n- Data: 24/09/2024")
        download_pdf(" Visualizza badge (PDF)", "Inglese_B2.pdf", key="inglese_b2", primary=True)

# ============================
# Sezione 2: Altri percorsi formativi
# ============================
st.header(" Altri percorsi formativi")

st.markdown("**ECDL Full Standard Certificate** — 24/09/2016")
download_pdf(" Visualizza certificato (PDF)", "Ecdl_full.pdf", key="ecdl_full")

st.markdown("**Percorso formativo docenti 600 ore (4 esami universitari)** — 20/07/2022")
download_pdf(" Visualizza certificato (PDF)", "Esperto_NPercorsoformativodocenti600ore.pdf", key="percorso_docenti")

# ============================
# Sezione 3: Autoformazione
# ============================
st.header(" Autoformazione")
st.markdown(
    "- **VBA** — Applicazioni evolute per Excel\n"
    "- **Python** — Applicazioni semplici per Analisi Dati, le trovi nella pagina \n"
    "- **CMD e PowerShell** — Applicazioni semplici per Gestione PC\n"
)
