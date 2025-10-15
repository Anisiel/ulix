import streamlit as st
from pathlib import Path

# Configurazione della pagina con titolo e icona
st.set_page_config(page_title="Pubblicazioni", page_icon="📚")

# Titolo principale della pagina
st.title("📖 Pubblicazioni")

# Breve descrizione introduttiva
st.markdown(
    """
    In fondo alla pagina puoi scaricare l'elenco completo delle mie pubblicazioni oppure stampare la pagina.
    """,
    unsafe_allow_html=True
)

# Pulsante per il profilo su Academia.edu
ACADEMIA_URL = "https://independent.academia.edu/FabianiUlisse"
st.link_button("🔗 Vai al mio profilo su Academia.edu", ACADEMIA_URL)

# Separatore visivo
st.divider()

# Sezione informativa su come sono strutturati i link
with st.expander("ℹ️ Informazioni sui link alle pubblicazioni"):
    st.markdown(
        """
        Alcuni esempi di stile per linkare le pubblicazioni (con link esterni ed interni).
        Una breve spiegazione di come sono linkati i documenti si trova 'in coda' alla singola pubblicazione.

        Possibili risorse per la formattazione del testo in Markdown:
        - [Guida ufficiale di Markdown](https://www.markdownguide.org/)
        - [Dillinger - Markdown Editor](https://dillinger.io/)
        - [StackEdit - Markdown Editor](https://stackedit.io/)
        """,
        unsafe_allow_html=True
    )

# Separatore visivo
st.divider()

# Intestazione della sezione delle pubblicazioni
st.markdown("## 📚 Elenco selezionato di pubblicazioni", unsafe_allow_html=True)

# Lettura e visualizzazione dell'elenco delle pubblicazioni
pubs_file = Path("2_Pubblicazioni.py")
if pubs_file.exists():
    with pubs_file.open("r", encoding="utf-8") as f:
        lines = f.readlines()
        # Estrazione delle righe che contengono le pubblicazioni (modifica secondo necessità)
        start_line = 44
        end_line = 69
        for i in range(start_line, end_line + 1):
            st.markdown(lines[i].strip(), unsafe_allow_html=True)
else:
    st.warning("⚠️ Impossibile trovare il file delle pubblicazioni.")

# Pulsante per scaricare l'elenco completo in PDF
pubs_path = Path("assets/pubblicazioni.pdf")
if pubs_path.exists():
    st.download_button(
        "⬇️ Scarica elenco completo",
        data=pubs_path.read_bytes(),
        file_name=pubs_path.name,
        mime="application/pdf"
    )
else:
    st.caption("📄 Carica il file `assets/pubblicazioni.pdf` per attivare il download.")

# Separatore visivo
st.divider()

# Pulsante per stampare la pagina
st.markdown(
    """
    <button onclick="window.print()" style="padding:8px 16px; font-size:16px;">
    🖨️ Stampa questa pagina
    </button>
    """,
    unsafe_allow_html=True
)