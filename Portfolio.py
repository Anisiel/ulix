# =============================================================================
# STRUTTURA DELLA PAGINA — Portfolio.py (Selettore)
# -----------------------------------------------------------------------------
# Questa pagina Streamlit funge da selettore iniziale per il portfolio.
# Mostra una sidebar con due opzioni:
# - "Minimal" → carica Home.py
# - "Ricca" → carica Home_altera.py
#
# Il caricamento dinamico avviene tramite `importlib`, che esegue il file
# selezionato come modulo, evitando problemi di layout e compatibilità.
#
# Comandi principali:
# - `st.set_page_config(...)`: imposta layout e titolo della pagina.
# - `st.sidebar.radio(...)`: selettore visivo per scegliere la Home.
# - `importlib.util`: carica il file scelto in modo sicuro.
#
# ⚠️ La patch a `set_page_config` è stata rimossa per permettere alle Home
# di gestire autonomamente il layout.
# =============================================================================

# selettore.py
import streamlit as st
from pathlib import Path
import importlib.util  # importlib invece di runpy

# 0) Config base del selettore (sidebar visibile)
st.set_page_config(
    page_title="Selettore — Portfolio Ulisse",
    page_icon="🔀",
    layout="wide",
    initial_sidebar_state="expanded"  # sidebar aperta per mostrare il selettore
)

# 1) Selettore nella SIDEBAR
with st.sidebar:
    st.markdown("#### 🧭 Seleziona la Home")
    labels = ["Minimal", "Ricca"]
    default_index = st.session_state.get("home_idx", 0)
    choice = st.radio(" ", labels, index=default_index)
    st.session_state["home_idx"] = labels.index(choice)

# 2) Mappa scelta -> file (entrambi nel root)
label_to_file = {
    "Minimal": "Home.py",
    "Ricca": "Home_altera.py",
}
target = label_to_file[choice]
target_path = str((Path(__file__).resolve().parent / target).resolve())

# 3) Esegui la Home scelta con importlib (invece di runpy)
def run_home(path):
    spec = importlib.util.spec_from_file_location("home_module", path)
    home = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(home)

run_home(target_path)

# 4) Stop Streamlit dopo l'esecuzione
st.stop()