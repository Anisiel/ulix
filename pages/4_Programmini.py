import streamlit as st

st.set_page_config(page_title="Titoli & Certificazioni", page_icon="🎓")
st.title("Titoli & Certificazioni")

st.markdown(
    """
    - ✅ **EIRSAF Full** — Certificazione Internazionale di Alfabetizzazione Digitale
    - ✅ **EIPASS Progressive** (in valutazione)
    - 🔜 Unipass Interactive 9 / Coding / Robotica Educativa / STEAM
    """,
    unsafe_allow_html=True
)

st.success("Aggiungi date, ID certificato e link ai badge quando li hai.")
