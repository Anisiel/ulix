# selettore.py
import streamlit as st
from pathlib import Path
import runpy
import streamlit as _st_mod  # per la patch di set_page_config nelle Home

# 0) Config base del selettore (sidebar visibile)
st.set_page_config(
    page_title="Selettore — Portfolio Ulisse",
    page_icon="🔀",
    layout="wide",
    initial_sidebar_state="expanded"   # sidebar aperta per mostrare il selettore
)

# 1) Forza il "primo run" per evitare che la sidebar sparisca al cambio Home
#import time  # modifica
#if "_first_run" not in st.session_state:                 # modifica
#    st.session_state["_first_run"] = True                # modifica
#    st.experimental_set_query_params(v=str(time.time())) # modifica
#    st.rerun()                                           # modifica


# 2) Selettore nella SIDEBAR
with st.sidebar:
    st.markdown("#### 🧭 Seleziona la Home")
    labels = ["Minimal", "Ricca"]
    default_index = st.session_state.get("home_idx", 0)
    choice = st.radio(" ", labels, index=default_index)
    st.session_state["home_idx"] = labels.index(choice)

# 3) Mappa scelta -> file (entrambi nel root)
label_to_file = {
    "Minimal": "Home.py",
    "Ricca":   "Home_altera.py",
}
target = label_to_file[choice]
target_path = str((Path(__file__).resolve().parent / target).resolve())

# 4) Evita l'errore "set_page_config chiamato più volte" dentro le Home
#    (patch DOPO la nostra set_page_config qui sopra)
_st_mod.set_page_config = lambda *args, **kwargs: None

# 5) Esegui la Home scelta
runpy.run_path(target_path, run_name="__main__")

# 6) Non aggiungere altro sotto
st.stop()