import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Pubblicazioni", page_icon="📚")
st.title("Pubblicazioni")

# Pulsante per il profilo generale
ACADEMIA_URL = "https://independent.academia.edu/FabianiUlisse"
st.link_button("📚 Vai al mio profilo su Academia.edu", ACADEMIA_URL)

st.divider()

# Elenco con link diretti alle pubblicazioni
st.markdown(
    """
    - [**Spatial research and geomatic resources applied to the archaeology of the Farafra Oasis**](https://www.academia.edu/5109115/Spatial_relo pubblicazione 3)**
    - [**Titolo pubblicazione 2**](https://www.academia.edu/link_pubblicazione_2)**
    """,
    unsafe_allow_html=True
)

# Pulsante per scaricare elenco completo
pubs_path = Path("assets/pubblicazioni.pdf")
if pubs_path.exists():
    st.download_button(
        "⬇️ Scarica elenco completo",
        data=pubs_path.read_bytes(),
        file_name=pubs_path.name,
        mime="application/pdf"
    )
else:
    st.caption("Carica il file `assets/pubblicazioni.pdf` per attivare il download.")