
import streamlit as st
from pathlib import Path

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
# Progetto principale e funzione relativa
# ============================

def mostra_progetto(titolo, data, descrizione, percorso_file):
    with st.expander(f"🗂️ Progetto: {titolo}", expanded=True):
        st.markdown(f"""
        **📅 Data:** {data}
        
        **📝 Descrizione:** {descrizione}
    """)
        try:
            with open(percorso_file, "rb") as file:
                st.download_button(
                    label="📥 Scarica il report del progetto",
                    data=file,
                    file_name=percorso_file.split("/")[-1],
                    mime="application/pdf"
                )
        except FileNotFoundError:
            st.error("❌ Il file del report non è stato trovato. Verifica il percorso.")

# Chiamata alla funzione per mostrare il progetto principale
mostra_progetto(
    titolo="Gestione F24 per crediti d’imposta con Excel, Power Query e VBA",
    data="15/06/2022 - in corso",
    descrizione="Progetto completo per la gestione dei flussi F24 tra Dipartimento e Agenzia delle Entrate, con strumenti Excel e VBA.",
    percorso_file="assets/EsportaCrediti/Esempio_report_progetto.pdf"
)

# ============================
# Sottoprogetti
# =============================================================================
# FUNZIONE: mostra_sottoprogetto
# Questa funzione mostra un sottoprogetto con:
# - titolo, data, descrizione, tecnologie
# - eventuali file scaricabili (PDF, TXT, immagini, ecc.)
# -----------------------------------------------------------------------------
# Questa funzione serve per visualizzare un "sottoprogetto".
# Ogni sottoprogetto può contenere:
# - un titolo
# - una data
# - una descrizione
# - una lista di tecnologie utilizzate
# - una lista di file associati (es. script, immagini, PDF, ecc.)
#
# Per ogni file associato, la funzione:
# 1. Controlla se il file esiste.
# 2. Se esiste, mostra un pulsante per scaricarlo.
# 3. Se il file è di testo o codice (.txt, .py, .bat, .bas), mostra anche il contenuto.
#
# Il pulsante di download usa `st.download_button`, che permette all'utente
# di scaricare il file direttamente dal browser.
#
# La funzione è pensata per essere semplice, compatibile con tutti i tipi di file,
# e facilmente estendibile per altri tipi di contenuti (es. immagini, PDF, ecc.).
# =============================================================================
def mostra_sottoprogetto(titolo, data, descrizione, tecnologie, file_paths=None):
    # Crea un espansore cliccabile con il titolo del sottoprogetto
    with st.expander(f"📁 Sottoprogetto: {titolo}", expanded=False):
        
        # Mostra le informazioni principali del sottoprogetto
        st.markdown(f"""
        - 📅 **Data:** {data}  
        - 📝 **Descrizione:** {descrizione}  
        - 🛠️ **Tecnologie utilizzate:** {", ".join(tecnologie)}
        """)


        # Se ci sono file associati al sottoprogetto, li mostra uno per uno
        if file_paths:
            for file_path in file_paths:
                file = Path(file_path)  # Converte la stringa in oggetto Path per gestire meglio il percorso

                if file.exists():  # Controlla se il file esiste
                    try:
                        data = file.read_bytes()  # Legge il contenuto del file in modalità binaria
                        file_name = file.name     # Estrae solo il nome del file (senza percorso)

                        # Mostra il pulsante per scaricare il file
                        # Questo pulsante è visibile e cliccabile se il file è stato letto correttamente
                        st.download_button(
                            label=f"⬇️ Scarica: {file_name}",  # Etichetta del pulsante
                            data=data,                         # Contenuto del file da scaricare
                            file_name=file_name,               # Nome del file che verrà salvato
                            mime="application/octet-stream",   # Tipo MIME generico, va bene per quasi tutti i file
                            use_container_width=True           # Fa occupare al pulsante tutta la larghezza disponibile
                        )

                        # Se il file è di testo o codice, mostra anche il contenuto in un espansore
                        if file.suffix in [".txt", ".py", ".bat", ".bas"]:
                            with st.expander(f"📄 Mostra contenuto: {file_name}"):
                                st.code(file.read_text(), language="text")  # Visualizza il contenuto come codice
                    except Exception as e:
                        # Mostra un messaggio di errore se qualcosa va storto nella lettura del file
                        st.error(f"❌ Errore nel caricamento del file: {file_path}\n{e}")
                else:
                    # Mostra un messaggio di errore se il file non esiste
                    st.error(f"❌ File non trovato: {file_path}")

# ============================
# Sottoprogetti specifici
# ============================

mostra_sottoprogetto(
    titolo="Esportazione crediti d’imposta",
    data="15/06/2022 - in corso",
    descrizione="Mini software in VBA per esportare i dati secondo specifiche AdE.",
    tecnologie=["VBA", "Excel"],
    file_paths=[
        "assets/EsportaCrediti/Esporta_Credito_Pubblicita.txt",
        "assets/EsportaCrediti/Esporta_Crediti.txt"
    ]
)


# ============================


# ============================
# Flusso operativo
# ============================

with st.expander("📊 Flusso operativo del progetto", expanded=False):
    st.markdown("""
    #### 🎯 Premessa
    Il Dipartimento provvede a finanziare crediti d’imposta per le imprese editrici.

    ---
    #### 🏁 1. Invio flussi all’Agenzia delle Entrate (AdE) [Sottoprogetto 1] 
    - Pubblicazione del decreto
    - Generazione dei flussi da inviare ad AdE
    - Programma in VBA per esportazione dati testuali secondo specifiche AdE
    - Processo ripetuto nel tempo
    - 🔗 assets/EsportaCrediti/Esempio_report_progetto.pdf

    ---
    #### 📥 2. Ricezione flussi da AdE [Sottoprogetto 2]
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
