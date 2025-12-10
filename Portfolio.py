
# =============================================================================
# STRUTTURA DELLA PAGINA — Portfolio.py (Selettore)
# -----------------------------------------------------------------------------
# Selettore iniziale per il portfolio:
# - "Minimal" → carica Home.py
# - "Ricca"   → carica Home_altera.py
# Uso di importlib per eseguire il file scelto come modulo.
# =============================================================================

import streamlit as st
from pathlib import Path
import importlib.util

# 0) Config base del selettore (chiamata unica in tutta l'app)
if not st.session_state.get("_page_config_done"):
    st.set_page_config(
        page_title="Selettore — Portfolio Ulisse",
        page_icon="🔀",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    st.session_state["_page_config_done"] = True

# 1) Selettore nella SIDEBAR
with st.sidebar:
    st.markdown("#### 🧭 Seleziona la Home")
    labels = ["Minimal", "Ricca"]
    default_index = st.session_state.get("home_idx", 0)
    choice = st.radio(" ", labels, index=default_index)
    st.session_state["home_idx"] = labels.index(choice)

# 2) Mappa scelta -> file (entrambi nel root)
label_to_file = {
    #"Minimal": "Home.py",
    "Minimal": "Home_ora.py",
    "Ricca": "Home_altera.py",

}

# 3) Costruisci path assoluto
root = Path(__file__).resolve().parent
target = label_to_file[choice]
target_path = str((root / target).resolve())

st.caption(f"Carico: {target_path}")

# 4) Esegui la Home scelta con importlib (robusto, con try/except)
def run_home(path: str):
    try:
        spec = importlib.util.spec_from_file_location("home_module", path)
        if spec is None or spec.loader is None:
            raise ImportError(f"Impossibile caricare il modulo da: {path}")
        home = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(home)
    except Exception as e:
        st.error(f"Errore durante il caricamento di `{path}`:\n\n{e}")
        st.stop()

run_home(target_path)

# 5) (Facoltativo) stop esplicito
