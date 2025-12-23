import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Organizzazione del sito", page_icon="📁")
st.title("📁 Come è organizzato e costruito questo sito?")

st.markdown("""
Questo sito è  progettato come portfolio interattivo con lo scopo di far valutare ***per quanto possibile*** le competenze di python
            e il curriculum.
            
Per realizzarlo è stata necessaria una fase di progettazione e una di realizzazione.
La velocità realizzativa è stata resa possibile dall'integrazione con l'intelligenza artificiale,
che ha il suo punto di forza più grande nel supporto alla programmazione.
Il codice sorgente è disponibile su Github (vedi la sezione dedicata più avanti in questa pagina).
Il sito è realizzato in Streamlit (open source e gratuito).
Il deploy è effettuato su Railway, una piattaforma cloud per il deployment di applicazioni.
            
""")

st.markdown("""
Il porfolio si compone delle seguenti sezioni:
            
### 🏠 Homepages
- Due versioni della homepage sono disponibili: una **minimal** e una **ricca**, gestibili tramite un selettore.

###  Selettore iniziale
All'avvio del sito, viene mostrata, in basso nel frame di sinistra, una **sidebar** con un selettore che permette di scegliere tra le due versioni di Home:

- **Minimal**: layout semplice e contenuti essenziali.
- **Ricca**: layout più elaborato, con galleria immagini e link estesi.

Il selettore è gestito dal file `Portfolio.py`, che utilizza `importlib` per caricare dinamicamente la Home selezionata.

Questa struttura serve solo a valorizzare una funzionalità interessante del python.

### 📄 Pagine interne
- Le pagine sono organizzate nella cartella `pages/` e includono:
    - **Grafici avanzati**: visualizzazioni interattive basate sul file `grafici_speciali.xlsx`.
    - **Programmini (in)utili**: script `.bat` e `.py` creati per lavoro.
    - **Pubblicazioni**: elenco di alcune delle pubblicazioni scientifiche.
    - **Titoli & Certificazioni**:in pagine distinte l'elenco dei titoli accademici e delle certificazioni professionali.
    - **Progetto in VBA/Excel/Query**: esempio di progetto ***reale concreto ed in corso*** elaborato da me per l'Ufficio.
    - **GIS PCM**: esempio di mappe con dati spaziali fittizi relativi al rischio sismico e alla distanza tra le sedi della PCM
            
###  Dati e grafici
- I grafici utilizzano dati contenuti nel file `grafici_speciali.xlsx` che si trova nella cartella `repo/` e riportano dati metereologici fittizi.
            
###  Codice sorgente
- Il codice sorgente completo del sito è disponibile su GitHub:
    - [🔗 Github.com/Anisiel/ulix](https://github.com/Anisiel/ulix) 
- Il sito è costruito con un framework Python per applicazioni web interattive chiamato Streamlit:
    - [🔗 Streamlit.io](https://streamlit.io/)
    - Utilizza file statici (`.pdf`, `.xlsx`, `.py`) e stili personalizzati (`styles.css`).
- Il deploy è effettuato su Railway, una piattaforma cloud per il deployment di applicazioni:
      [🔗 railway.app] (https://railway.com/)

""", unsafe_allow_html=True
)
st.divider()
# Mostra immagine illustrativa sito
st.markdown("### 📂 Struttura delle cartelle e dei file del sito")
img_path = "assets/img/struttura_sito.png"
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