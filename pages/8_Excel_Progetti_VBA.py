import streamlit as st

# Configurazione della pagina
st.set_page_config(page_title="Excel - Progetti e VBA", page_icon="📊")

# Titolo principale
st.title("📊 Progetti Excel & VBA")

# ============================
# Sezione: Progetto 1 - Gestione F24 per crediti d'imposta  Excel
# ============================
with st.expander("🗂️ Progetto: Gestione F24 per crediti d'imposta Excel", expanded=True):
    st.markdown("""
    - 📅 Data: 15/03/2023  
    - 📝 Descrizione: Creazione di una serie di query per la gestione **mensile** dei flussi F24 provenienti da Agenzia delle Entrate , con fogli interconnessi, formule avanzate, protezione dati.  
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

st.divider()

def mostra_progetto(titolo, data, descrizione, tecnologie, link):
    """
    Visualizza un progetto.
    Parametri:
    - titolo: Titolo del progetto
    - data: Data del progetto (stringa)
    - descrizione: Descrizione del progetto (stringa)
    - tecnologie: Lista di tecnologie utilizzate
    - link: URL al documento o risorsa
    """
    with st.expander(f"🗂️ Progetto: {titolo}", expanded=True):
        st.markdown(f"""
        **📅 Data:** {data}  
        **📝 Descrizione:**  
        {descrizione}

        **🛠️ Tecnologie utilizzate:**
        """)
        for tech in tecnologie:
            st.markdown(f"- {tech}")

        st.markdown(f"**🔗 Visualizza progetto**")


mostra_progetto(
    titolo="Gestione F24 per crediti d'imposta Excel",
    data="15/06/2022 - in corso",
    descrizione="Creazione di query per la gestione mensile dei flussi F24 da Agenzia delle Entrate, con fogli interconnessi, formule avanzate e protezione dati.",
    tecnologie=["Excel avanzato", "Power Query", "Protezione con password"],
    link="assets/cert/Database_Iscrizioni.pdf"
    
)

with st.expander("📊 Descrizione del flusso operativo Gestione F24 per crediti d'imposta Excel", expanded=False):
    st.markdown("""
    #### 🎯 Premessa
    Il Dipartimento provvede a finanziare crediti d’imposta per le imprese editrici.

    ---
    #### 🏁 1. Invio flussi all’Agenzia delle Entrate (AdE)
    - Pubblicazione del decreto
    - Generazione dei flussi da inviare ad AdE
    - Programma in VBA per esportazione dati testuali secondo specifiche AdE
                with st.expander("📊 Esempio di istruzioni operative", expanded=False):
                    st.image("assets/Esporta crediti.png", caption="istruzioni operative per l'esportazione dei crediti")
    - Processo ripetuto nel tempo
    - 🔗 Link al progetto VBA

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

st.image("assets/Flusso operativo gestione F24.png", caption="Flusso operativo gestione F24")