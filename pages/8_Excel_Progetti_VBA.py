
import streamlit as st

# Configurazione della pagina
st.set_page_config(page_title="Excel - Progetti e VBA", page_icon="📊")

# Titolo principale
st.title("📊 Crediti d’imposta: gestione F24")
st.header("✅Progetto con Excel, Power Query e VBA")
st.markdown("""
In questa pagina presento un progetto ***reale e in corso*** per la gestione dei flussi F24 tra il Dipartimento per l'informazione e l'editoria (DIE) e l'Agenzia delle Entrate (AdE), utilizzando strumenti come Excel, Power Query e VBA per automatizzare l'esportazione e l'importazione dei dati relativi ai crediti d'imposta per le imprese editrici.
""")

st.divider()
# ============================
# Progetto principale
# ============================

def mostra_progetto(titolo, data, descrizione, tecnologie, link):
    with st.expander(f"🗂️ Progetto: {titolo}", expanded=True):
        st.markdown(f"""
        **📅 Data:** {data}  
        **📝 Descrizione:** {descrizione}

        **🛠️ Tecnologie utilizzate:** 
        """)
        for tech in tecnologie:
            st.markdown(f"- {tech}")

        st.markdown(f"🔗 {link}")

mostra_progetto(
    titolo="Gestione F24 per crediti d’imposta con Excel, Power Query e VBA",
    data="15/06/2022 - in corso",
    descrizione="Progetto completo per la gestione dei flussi F24 tra Dipartimento e Agenzia delle Entrate, con strumenti Excel e VBA.",
    tecnologie=["Excel avanzato", "Power Query", "VBA"],
    link=("assets/EsportaCrediti/Esempio_report_progetto.pdf")
)

# ============================
# Sottoprogetti
# ============================

with st.expander("📤 Sottoprogetto: Esportazione crediti d’imposta", expanded=False):
    st.markdown("""
    - 📅 Data: 15/06/2022 - in corso  
    - 📝 Mini software in VBA per esportare i dati secondo specifiche AdE  
    - 🔗 assets/EsportaCrediti/Esempio_report_progetto.pdf
    """)

with st.expander("📥 Sottoprogetto: Importazione crediti d’imposta", expanded=False):
    st.markdown("""
    - 📅 Data: 15/06/2022 - in corso  
    - 📝 Automazione per importare i flussi mensili da AdE e generare report  
    - 🔗 assets/cert/Report_VBA.pdf
    """)

# ============================
# Flusso operativo
# ============================

with st.expander("📊 Flusso operativo del progetto", expanded=False):
    st.markdown("""
    #### 🎯 Premessa
    Il Dipartimento provvede a finanziare crediti d’imposta per le imprese editrici.

    ---
    #### 🏁 1. Invio flussi all’Agenzia delle Entrate (AdE)
    - Pubblicazione del decreto
    - Generazione dei flussi da inviare ad AdE
    - Programma in VBA per esportazione dati testuali secondo specifiche AdE
    - Processo ripetuto nel tempo
    - 🔗 assets/EsportaCrediti/Esempio_report_progetto.pdf

    ---
    #### 📥 2. Ricezione flussi da AdE
    - Cadenza mensile
    - File testuali con crediti utilizzati 
    - Programma di decodifica e importazione automatica
    - Directory separate per ogni tipo di credito

    ---
    #### 📊 3. Riepilogo e analisi con Power Query
    - Aggiornamento automatico dei fogli di riepilogo
    - Suddivisione per anno di concessione e utilizzo
    - Visualizzazione aggregata delle imprese
    """)

    st.image("assets/img/Flusso operativo gestione F24.png", caption="Flusso operativo gestione F24")

# ============================
# Competenze Power Query (opzionale: spostare in pagina separata)
# ============================

st.header("⚙️ Competenze Power Query")

st.markdown("""
- 🔄 **Unione di tabelle** da fonti diverse (Excel, CSV, Web)  
- 🧹 **Pulizia dati**: rimozione duplicati, gestione valori nulli  
- 📊 **Trasformazioni**: pivot, raggruppamenti, colonne calcolate  
- 🔗 assets/cert/PowerQuery_Esempio.pdf
""")
