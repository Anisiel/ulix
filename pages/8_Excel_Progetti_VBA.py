
import streamlit as st
from pathlib import Path


# =============================================================================
# STRUTTURA DELLA PAGINA
# -----------------------------------------------------------------------------
# Questa pagina Streamlit mostra un progetto principale come "cornice fissa",
# con sezioni interne espandibili:
# - Flusso operativo (testo descrittivo)
# - Sottoprogetti (ognuno con titolo, descrizione, tecnologie e file scaricabili)
#
# Ogni sottoprogetto è gestito tramite la funzione `mostra_sottoprogetto`,
# che viene chiamata all'interno di un `st.expander`, così da mantenere
# la struttura ordinata e modulare.
# =============================================================================

# ============================
# Info generali della pagina
# ============================

# Configurazione della pagina
st.set_page_config(page_title="Excel - Progetti e VBA", page_icon="📊")

# Titolo principale
st.title("📊 Gestione del flusso dati relativo ai crediti d’imposta utilizzando Excel, Power Query e VBA")
st.markdown("###### ✅Esempio di progetto reale per l'Ufficio")

st.markdown("""
In questa pagina presento un progetto ***complesso, reale ed attualmente in corso*** per la gestione dei flussi di dati tra il Dipartimento per l'informazione e l'editoria (DIE) e l'Agenzia delle Entrate (AdE), utilizzando strumenti come Excel, Power Query e VBA per automatizzare l'esportazione e l'importazione dei dati relativi ai crediti d'imposta per le imprese editrici.
""")

st.divider()
##############################
# IL PROGETTO (cornice)
##############################

def mostra_progetto(titolo, data, descrizione, percorso_file=None, percorso_immagine=None, caption_immagine=None):
    # Mostra il titolo del progetto come intestazione principale
    st.markdown(f"### 🗂️ {titolo}")

    # Mostra la data e la descrizione del progetto
    st.markdown(f"""
    - 📅 **Data:** *{data}*  
    - 📝 **Descrizione:** *{descrizione}*
    """)
    
    # Mostra l'immagine del progetto (es. schema, flusso operativo)
    if percorso_immagine:
        st.image(percorso_immagine, caption= caption_immagine)

    # Prova a caricare il file PDF associato al progetto
    try:
        # Apre il file in modalità binaria ("rb" = read binary)
        with open(percorso_file, "rb") as file:
            # Mostra un pulsante per scaricare il file
            st.download_button(
                label="📥 Scarica il report del progetto",  # Testo del pulsante
                data=file,                                  # Contenuto del file da scaricare
                file_name=Path(percorso_file).name,         # Nome del file (estratto dal percorso)
                mime="application/pdf"                      # Tipo MIME: PDF
            )
    except FileNotFoundError:
        # Se il file non viene trovato, mostra un messaggio di errore
        st.error("❌ Il file del report non è stato trovato. Verifica il percorso.")

# Sezioni interne del progetto (espandibili)
    # ============================
    # Flusso operativo
    # ============================
    with st.expander("📌 Flusso operativo", expanded=False):
        st.markdown("""
            #### 🎯 Premessa
            Il Dipartimento provvede a finanziare crediti d’imposta per le imprese editrici.

            ---
            #### 🏁 1. Invio flussi all’Agenzia delle Entrate (AdE) [Sottoprogetto 1] 
            - Pubblicazione del decreto
            - Generazione dei flussi da inviare ad AdE
            - Programma in VBA per esportazione dati testuali secondo specifiche AdE
            - Processo ripetuto nel tempo a **scadenze irregolari**

            ---
            #### 📥 2. Ricezione flussi da AdE [Sottoprogetto 2]
            - File testuali con crediti utilizzati 
            - Programma di decodifica e importazione automatica
            - Directory separate per ogni tipo di credito
            - Processo ripetuto nel tempo a **cadenza mensile**

            ---
            #### 📊 3. Riepilogo e analisi con Power Query
            - Aggiornamento automatico dei fogli di riepilogo
            - Suddivisione per anno di concessione e utilizzo
            - Visualizzazione aggregata delle imprese
            """)

# ============================
# Sottoprogetti
# =============================================================================
# FUNZIONE: mostra_sottoprogetto
# -----------------------------------------------------------------------------
# Questa funzione mostra un sottoprogetto all'interno di un espander.
# Ogni sottoprogetto include:
# - titolo, data, descrizione, tecnologie
# - file scaricabili (es. script, immagini, PDF)
#
# Per ogni file:
# - controlla se esiste
# - mostra un pulsante per scaricarlo
# - se è un file di testo/codice, ne mostra anche il contenuto
# =============================================================================
    def mostra_sottoprogetto(titolo, data, descrizione, tecnologie, percorso_file=None, livello=None, percorso_immagine=None, caption_immagine=None):
        # Crea un espansore cliccabile con il titolo del sottoprogetto
        with st.expander(f"📁 Sottoprogetto: {titolo}", expanded=False):
            
            # Mostra le informazioni principali del sottoprogetto
            st.markdown(f"""
            - 📅 **Data:** {data}  
           - 📝 **Descrizione:** {descrizione} 
            - 🛠️ **Tecnologie utilizzate e competenze richieste:** {", ".join(tecnologie)}
            -  👑 **Livello:** {livello} 
            """)

             # Mostra l'immagine del progetto (es. schema, flusso operativo)
            if percorso_immagine:
                st.image(percorso_immagine, caption=caption_immagine)

            # Se ci sono file associati al sottoprogetto, li mostra uno per uno
            if percorso_file:
                for file_path in percorso_file:
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
        titolo="Esportazione dei crediti d’imposta verso Agenzia delle Entrate",
        data="15/06/2022 - in corso",
        descrizione="Mini software in VBA per esportare i dati secondo specifiche AdE.",
        tecnologie=["VBA", "Excel"],
        percorso_file=[
            "assets/Crediti/Esporta_Credito_Pubblicita.txt",
            "assets/Crediti/Esporta_Crediti.txt"
        ],
        livello="Media difficoltà, progettazione sintetica",
        caption_immagine="Flusso operativo gestione F24"
    )

    mostra_sottoprogetto(
        titolo="Importazione dei crediti d’imposta verso Agenzia delle Entrate e sviluppo di **report mensili**",
        data="15/06/2022 - in corso",
        descrizione= """
            Software in VBA articolato in più step (>2000 righe di codice).
                - Premessa:
                    Il progetto è articolato in un file padre "Credito_xxxx(carta, pubblicità...)_meseanno.xlsx" ed in una serie di file figli aggiornati mensilmente, suddivisi in concessione e fruizione del credito.
                    Ad esempio: Il file "Credito_carta_settembre2025.xlsx" ha i file figli con i dati suddivisi in:
                            
                            - Concesso anno1, Concesso anno2, Concesso annon
                            - Fruito anno1, Fruito anno2, Fruito annon
                I file relativi alle **concessioni** sono aggiornati aperiodicamente in base a quando avvengono le concessioni di credito [vedi sottoprogetto 1];
                i file relativi alle **fruizioni** vengono aggiornati mensilmente.
                
                Ecco gli step con cui si aggiornano mensilmente i dati:
                - Step 1:
                    1. import dei file testuali
                    2. decodifica dei file importati
                    3. suddivisione per tipo di credito in base al codice identificativo
                    4. stampa a video di un primo report recante informazioni sui dati (numero, tipo, nome file...)
                - Step 2:
                    1. copia (in locale) dei dati (query di accodamento) nei file F24 di ciascun credito
                    2. operazioni di aggiornamento nei singoli file F24 (Totali, controllo, identità, lunghezza...)
                    3. realizzazione di una copia di backup (in locale) dei file del mese precedente (F24 e file .xlsx) 
                - Step 3:    
                    1. copia (sulla nuvola) dei dati aggiornati e sostituzione dei precedenti  
                - Step 4 (operazioni interne al file .xlsx generale):
                    1. query di aggiornamento pre rendere coerenti i dati di concessione e quelli di fruizione
        """,
        tecnologie=["VBA", "Excel Avanzato", "Power Query"],
        percorso_file=["assets/Crediti/Importa_file_F24.txt"],
        livello="Alta difficoltà, progettazione di alto profilo",
        percorso_immagine="assets/Crediti/ImportaF24.png",
        caption_immagine="Report per importazione file F24"
    )

mostra_progetto(
    titolo="Progetto per la gestione dei flussi dati con Agenzia delle entrate",
    data="15/06/2022 - in corso",
    descrizione= "Progetto completo per la gestione dei flussi F24 tra Dipartimento e Agenzia delle Entrate, con strumenti Excel, programmazione VBA, Power Query.",
    percorso_file="assets/Crediti/Esempio_report_progetto.pdf",
    percorso_immagine="assets/Crediti/Flusso operativo gestione.png"
)

st.divider()

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