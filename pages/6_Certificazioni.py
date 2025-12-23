
import streamlit as st
from pathlib import Path

# Imposta la configurazione della pagina con titolo e icona
st.set_page_config(page_title="Certificazioni", page_icon="🎓")

# Titolo principale della pagina
st.title("✅ Certificazioni")

# ============================
# Helpers
# ============================
def download_if_exists(label: str, path_str: str, key: str, primary: bool = False):
    """Mostra un download_button se il file esiste, altrimenti una caption."""
    if not path_str or path_str.strip() == "--":
        st.caption(f"{label}: non disponibile")
        return
    path = Path(path_str)
    if path.exists():
        with open(path, "rb") as f:
            st.download_button(
                label=label,
                data=f.read(),
                file_name=path.name,
                mime="application/pdf",
                key=key,
                type="primary" if primary else "secondary",
                use_container_width=True,
            )
    else:
        st.caption(f"{label}: file non trovato ({path})")

# ============================
# Sezione 1: Certificazioni recenti ottenute
# ============================
st.header(" Certificazioni **recenti** ottenute")

col1, col2, col3 = st.columns(3)

with col1:
    with st.expander("📘 **EIRSAF Advanced Full**", expanded=True):
        st.markdown(
            "- Certificazione Internazionale di Alfabetizzazione Digitale\n"
            "- Data: 25-09-2025"
        )
        download_if_exists(" Visualizza badge (PDF)", "assets/cert/Eirsaf_full.pdf", key="eirsaf_full", primary=True)

with col2:
    with st.expander("📕 **EIPASS Progressive Advanced**", expanded=True):
        st.markdown(
            "- Certificazione avanzata di competenze digitali\n"
            "- Data: 13/02/2025"
        )
        download_if_exists(" Visualizza badge (PDF)", "assets/cert/Eipass_progressive.pdf", key="eipass_progressive", primary=True)

with col3:
    with st.expander("📗 **Certificato livello B2 Inglese**", expanded=True):
        st.markdown(
            "- Certificazione internazionale di competenze linguistiche\n"
            "- Data: 24/09/2024"
        )
        download_if_exists(" Visualizza badge (PDF)", "assets/cert/Inglese_B2.pdf", key="inglese_b2", primary=True)

# ============================
# Sezione 2: Altri percorsi formativi
# ============================
st.header("📚 Altri percorsi formativi")

# Riga 1 — ECDL
st.markdown("**ECDL Full Standard Certificate** — 24/09/2016")
download_if_exists(" Visualizza certificato (PDF)", "assets/cert/Ecdl_full.pdf", key="ecdl_full")

# Riga 2 — Percorso docenti
st.markdown("**Percorso formativo docenti 600 ore (4 esami universitari)** — 20/07/2022")
download_if_exists(" Visualizza certificato (PDF)", "assets/cert/Esperto_NPercorsoformativodocenti600ore.pdf", key="percorso_docenti")

# ============================
# Sezione 3: Autoformazione
# ============================
st.header("🧠 Autoformazione")
st.markdown(
    "- **VBA** — Applicazioni evolute per Excel\n"
    "- **Python** — Applicazioni semplici per Analisi Dati\n"
    "- **CMD e PowerShell** — Applicazioni semplici per Gestione PC\n"
)
