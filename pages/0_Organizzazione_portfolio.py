import streamlit as st

st.set_page_config(page_title="Organizzazione del sito", page_icon="📁")
st.title("📁 Come è organizzato e costruito questo sito?")

st.markdown("""
Questo sito è stato progettato come portfolio interattivo e si compone delle seguenti sezioni:

### 🏠 Homepages
- Due versioni della homepage sono disponibili: una **minimal** e una **più ricca**, selezionabili tramite un selettore.

### 📄 Pagine interne
- Le pagine sono organizzate nella cartella `pages/` e includono:
    - **Grafici avanzati**: visualizzazioni interattive basate sul file `grafici_speciali.xlsx`.
    - **Programmini (in)utili**: script `.bat` e `.py` creati per lavoro.
    - **Pubblicazioni**: elenco delle pubblicazioni scientifiche.
    - **Titoli & Certificazioni**: elenco dei titoli accademici e certificazioni professionali.

### 📊 Dati e grafici
- I grafici utilizzano dati contenuti nel file `grafici_speciali.xlsx` che si trova nella cartella `repo/` e riportano dati metereologici fittizi.

### 💻 Codice sorgente
- Il codice sorgente completo del sito è disponibile su GitHub:
    - [🔗 Github.com/Anisiel/ulix](https://github.com/Anisiel/ulix) 
- Il sito è costruito con un framework Python per applicazioni web interattive chiamato Streamlit:
    - [🔗 Streamlit.io](https://streamlit.io/)
    - Utilizza file statici (`.pdf`, `.xlsx`, `.py`) e stili personalizzati (`styles.css`).

Se hai curiosità sul funzionamento interno o vuoi contribuire, visita il repository GitHub!
""", unsafe_allow_html=True)

# Mostra immagine illustrativa se presente
img_path = "assets/struttura_sito.png"
if Path(img_path).exists():
    st.image(img_path, caption="Struttura delle cartelle e dei file del sito", use_column_width=True)
else:
    st.info("Puoi aggiungere un'immagine chiamata 'struttura_sito.png' nella cartella assets per visualizzare la struttura del sito.")