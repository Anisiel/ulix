import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Organizzazione del sito", page_icon="📁")
st.title("📁 Come è organizzato e costruito questo sito?")

st.markdown("""
Questo sito è  progettato come portfolio interattivo con lo scopo di far valutare ***per quanto possibile*** le competenze di python
            e il curriculum.
            
Per realizzarlo è stata necessaria una fase di progettazione e una di realizzazione.
La velocità realizzativa (pochi giorni) è stata resa possibile dal supporto dell'intelligenza artificiale,
che nel supporto alla programmazione ha il suo punto di forza più grande.
Il codice sorgente è disponibile su Github (vedi la sezione dedicata più avanti in questa pagina).
Il sito è realizzato in Streamlit (open source e gratuito, motivo dei ritardi di visualizzazione).
            
""")

st.markdown("""
Ad ogni modo il porfolio si compone delle seguenti sezioni:
            
### 🏠 Homepages
- Due versioni della homepage sono disponibili: una **minimal** e una **più ricca**, selezionabili tramite un selettore.

### 🧭 Selettore iniziale
All'avvio del sito, viene mostrata, in basso nel frame di sinistra, una **sidebar** con un selettore che permette di scegliere tra due versioni della homepage:

- **Minimal**: layout semplice, immagini a sinistra e contenuti essenziali.
- **Ricca**: layout più elaborato, con galleria immagini, link estesi e navigazione avanzata.

Il selettore è gestito dal file `Portfolio.py`, che utilizza `importlib` per caricare dinamicamente la pagina selezionata, evitando problemi di layout e mantenendo il sito stabile.

Questa struttura consente di esplorare il portfolio in due modalità diverse, a seconda delle preferenze dell’utente.

### 📄 Pagine interne
- Le pagine sono organizzate nella cartella `pages/` e includono:
    - **Grafici avanzati**: visualizzazioni interattive basate sul file `grafici_speciali.xlsx`.
    - **Programmini (in)utili**: script `.bat` e `.py` creati per lavoro.
    - **Pubblicazioni**: elenco delle pubblicazioni scientifiche.
    - **Titoli & Certificazioni**:in pagine distinte l'elenco dei titoli accademici e delle certificazioni professionali.
    - **Progetto in VBA/Excel/Query**: esempio di grande progetto ***reale concreto ed in corso*** elaborato per l'Ufficio.
            
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