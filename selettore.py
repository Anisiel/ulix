# selettore.py
import streamlit as st
from pathlib import Path
import runpy
import streamlit as _st_mod  # modulo reale per patch

# Config del selettore (puoi personalizzare titolo e icona)
st.set_page_config(
    page_title="Selettore — Portfolio Ulisse",
    page_icon="🔀",
    layout="wide",
    initial_sidebar_state="collapsed"  # 👈 fix: sidebar chiuso
)


# --- Selettore in alto ---
st.markdown("### Scegli la Home")
choice = st.radio("Selettore Home", ["Minimal", "Ricca"], index=0, horizontal=True, label_visibility="collapsed")

# Mappa scelta -> file di destinazione (entrambi nel root)
label_to_file = {
    "Minimal": "Home.py",
    "Ricca":   "Home_altera.py",
}
target = label_to_file[choice]

# Path assoluto del file da eseguire
BASE_DIR = Path(__file__).resolve().parent
target_path = str((BASE_DIR / target).resolve())

# --- Patch: disattiva set_page_config dentro la Home scelta (evita errore doppia config) ---
# NB: le Home fanno "import streamlit as st": importeranno lo stesso modulo già patchato qui.
_st_mod.set_page_config = lambda *args, **kwargs: None  # <-- patch no-op

# --- Esegui il file scelto come se fosse la "pagina" corrente ---
# Nota: Streamlit riesegue lo script ad ogni interazione, quindi questo basta.
runpy.run_path(target_path, run_name="__main__")

# Ferma l'esecuzione del selettore qui, così non si "accoda" UI dopo la Home caricata
st.stop()
