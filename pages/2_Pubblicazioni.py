import streamlit as st

st.set_page_config(page_title="Pubblicazioni", page_icon="📚")
st.title("Pubblicazioni")

st.markdown(
    """
    - **Titolo pubblicazione 1** — PDF  
    - **Titolo pubblicazione 2** — PDF
    """,
    unsafe_allow_html=True
)

st.caption("Carica i PDF nel repo (es. `assets/pubs/...`) e metti i link qui sopra.")
