import streamlit as st

# Configurazione della pagina
st.set_page_config(page_title="Excel - Progetti e VBA", page_icon="📊")

# Titolo principale
st.title("📊 Progetti Excel & VBA")

# ============================
# Sezione: Progetto 1 - Database Excel
# ============================
with st.expander("🗂️ Progetto: Database Excel", expanded=True):
    st.markdown("""
    - 📅 Data: 15/03/2023  
    - 📝 Descrizione: Creazione di un database Excel per la gestione di iscrizioni scolastiche, con fogli interconnessi, formule avanzate e protezione dati.  
    - 🔗 [Visualizza progetto](assets/cert/Database_Iscrizioni.pdf)
    """)
# ============================
# Sezione: Progetto 2 - Automazione con VBA
# ============================
with st.expander("🤖 Progetto: Automazione con VBA", expanded=True):
    st.markdown("""
    - 📅 Data: 10/06/2024  
    - 📝 Descrizione: Automazione di report mensili con macro VBA, generazione automatica di grafici e invio email con allegati.  
    - 🔗 [Visualizza progetto](assets/cert/Report_VBA.pdf)
    """)
# ============================
# Sezione: Competenze Power Query
# ============================
st.header("⚙️ Competenze Power Query")

st.markdown("""
- 🔄 **Unione di tabelle** da fonti diverse (Excel, CSV, Web)  
- 🧹 **Pulizia dati**: rimozione duplicati, gestione valori nulli  
- 📊 **Trasformazioni**: pivot, raggruppamenti, colonne calcolate  
- 🔗 [Esempio pratico](assets/cert/PowerQuery_Esempio.pdf)
            """)