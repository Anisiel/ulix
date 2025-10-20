import streamlit as st

st.set_page_config(page_title="Titoli & Certificazioni", page_icon="🎓")
st.title("Titoli & Certificazioni")

st.markdown(
    """
    - ✅ **EIRSAF Full** — Certificazione Internazionale di Alfabetizzazione Digitale
    - ✅ **EIPASS Progressive** (in valutazione)
    - 🔜 Unipass Interactive 9 / Coding / Robotica Educativa / STEAM
    """,
    unsafe_allow_html=True
)

st.success("Aggiungi date, ID certificato e link ai badge quando li hai.")
import streamlit as st

# Imposta la configurazione della pagina con titolo e icona
st.set_page_config(page_title="Titoli & Certificazioni", page_icon="🎓")

# Titolo principale della pagina
st.title("🎓 Titoli & Certificazioni")

# ============================
# Sezione 1: Certificazioni ottenute
# ============================
st.header("✅ Certificazioni ottenute")

# Layout a tre colonne per mostrare le certificazioni in modo ordinato
col1, col2, col3 = st.columns(3)

with col1:
    # Dettagli sulla certificazione EIRSAF Full
    with st.expander("📘 **EIRSAF Advanced Full**", expanded=False):    
        st.markdown("""
    - Certificazione Internazionale di Alfabetizzazione Digitale  
    - 📅 Data: 25-09-2025  
    - 🔗 [Visualizza badge](assets/cert/Eirsaf_full.pdf)
     """)
with col2:
    # Dettagli sulla certificazione EIPASS Progressive
    with st.expander("📕 **EIPASS Progressive Advanced**", expanded=False):
        st.markdown("""
    - Certificazione avanzata di competenze digitali  
    - 📅 Data: 13/02/2025  
    - 🔗 [Visualizza badge](assets/cert/Eipass_progressive.pdf)
    """)
with col3:

    # Dettagli sulla certificazione ECDL Full Standard
    with st.expander("📗 **ECDL Full Standard Certificate**", expanded=False):
        st.markdown("""
    - Certificazione avanzata di competenze digitali  
    - 📅 Data: 24/09/2016  
    - 🔗 [Visualizza badge](assets/cert/Ecdl_full.pdf)
    """)

# ============================
# Sezione 2: Altri percorsi formativi
# ============================
st.header("🚀 Altri percorsi formativi")

# Lista colorata e descrittiva delle competenze
st.markdown("""
- 🔵 **Certificato livello B2 Inglese** - 24/09/2024 - [Visualizza cert.](assets/cert/Inglese_B2.pdf) - 
- 🟢 **Esperto nella Normativa e nella Contrattualistica del lavoro** - 27/11/2014 - [Visualizza cert.](assets/cert/Esperto_Normativa.pdf) - [Visualizza diploma](assets/cert/Esperto_Normativa_diploma.pdf)
- 🔴 **VBA** — Applicazioni evolute per Excel   
- 🟣 **Python** — Applicazioni semplici per Analisi Dati
- 🟡 **CMD e Power Shell** — Applicazioni semplici per Gestione PC
""")

