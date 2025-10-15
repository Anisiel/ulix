import streamlit as st
from pathlib import Path

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

""", unsafe_allow_html=True
)
st.divider()
# Mostra immagine illustrativa sito
st.markdown("### 📂 Struttura delle cartelle e dei file del sito")
img_path = "assets/struttura_sito.png"
if Path(img_path).exists():
    st.image(img_path, caption="Struttura delle cartelle e dei file del sito",
             width=400)
    with open(img_path, "rb") as file:
        st.download_button(
            label="⬇️ Scarica immagine",
            data=file,
            file_name="struttura_sito.png",
            mime="image/png"
        )
else:
    st.info("Puoi aggiungere un'immagine chiamata 'struttura_sito.png' nella cartella assets per visualizzare la struttura del sito.")