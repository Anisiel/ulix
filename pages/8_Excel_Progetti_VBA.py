
import streamlit as st
from pathlib import Path

# =========================
#  FUNZIONE DI SUPPORTO
# =========================

# Percorso assoluto della cartella 'assets', partendo dal file corrente (che è in 'pages/')
ASSETS = Path(__file__).resolve().parents[1] / "assets"


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

def mostra_progetto(titolo, data, descrizione, link):
    with st.expander(f"🗂️ Progetto: {titolo}", expanded=True):
        st.markdown(f"""
        **📅 Data:** {data}
        
        **📝 Descrizione:** {descrizione}
        
        **📥 Link al report del progetto:** [Scarica il report]({link})
    """)
       
mostra_progetto(
    titolo="Gestione F24 per crediti d’imposta con Excel, Power Query e VBA",
    data="15/06/2022 - in corso",
    descrizione="Progetto completo per la gestione dei flussi F24 tra Dipartimento e Agenzia delle Entrate, con strumenti Excel e VBA.",
    link="assets/EsportaCrediti/Esempio_report_progetto.pdf"
)

# ============================
# Sottoprogetti e funzioni per mostrare un sottoprogetto con file scaricabile
# ============================




# Funzione per leggere un file come testo (stringa)
def load_text(path):
    # Apre il file in modalità lettura testuale con codifica UTF-8
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

# Funzione per leggere un file come bytes (necessario per il download)
def load_bytes(path):
    # Apre il file in modalità binaria, utile per download_button
    with open(path, "rb") as f:
        return f.read()

def mostra_sottoprogetto(titolo, data, descrizione, tecnologie, file_paths=None):
    # Crea un espansore con il titolo del sottoprogetto
    with st.expander(f"📁 & 📥 Sottoprogetto: {titolo}", expanded=False):
    
    # Mostra la data e la descrizione del sottoprogetto
        st.markdown(f"""
        - 📅 **Data:** {data}  
        - 📝 **Descrizione:** {descrizione}
        - 🛠️ **Tecnologie utilizzate:** {", ".join(tecnologie)}
        """)  

    # Se c'è una lista di file associata al sottoprogetto, mostrali insieme a un pulsante di download
        if file_paths:
            for file_path in file_paths:
                try:
                    full_path = ASSETS / Path(file_path).relative_to("assets") # Percorso completo del file per accedervi da /pages
                   
                   
                    # Carica il file in modalità binaria per il download
                    data = load_bytes(full_path)

                    # Estrae solo il nome del file dal percorso
                    file_name = Path(file_path).name

                    # Determina il tipo MIME in base all'estensione del file
                    # text/plain per file leggibili (codice), generico altrimenti
                    mime = "text/plain" if file_name.endswith((".txt", ".py", ".bat", ".bas")) else "application/octet-stream" # MIME (identificatore generico): dice al browser che tipo di file si sta servendo

                    # Mostra un pulsante per scaricare il file
                    st.download_button(
                        label=f"📄 Scarica: {file_name}",
                        data=data,
                        file_name=file_name,
                        mime=mime,
                        use_container_width=True
                    )
                    # Espansore per visualizzare il contenuto del file come codice
                    with st.expander(f"📄 Mostra codice: {file_name}"):
                        code = load_text(full_path)
                        st.code(code)

                except FileNotFoundError:
                    # Mostra errore se il file non esiste
                    st.error(f"❌ File non trovato. Verifica il percorso.: {file_path}")


# ============================
# Sottoprogetti specifici
# ============================

mostra_sottoprogetto(
    titolo="Esportazione crediti d’imposta",
    data="15/06/2022 - in corso",
    descrizione="Mini software in VBA per esportare i dati secondo specifiche AdE.",
    tecnologie=["VBA", "Excel"],
    file_paths=[
        "assets/EsportaCrediti/Esporta crediti.png",
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
