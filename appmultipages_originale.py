import streamlit as st

st.set_page_config(page_title="Ulisse Fabiani", page_icon="🌱", layout="centered")

# HERO / COPERTINA
st.image("assets/hero.jpg", use_container_width=True, caption="")

st.title("Hello, lettore! 👋")
st.subheader("Dammi un buon voto! 😄")

st.caption("Portfolio minimal & zen — fatto con Python + Streamlit")

st.divider()

# LINK RAPIDI (interni ed esterni)
col1, col2, col3 = st.columns(3)

with col1:
    # Link interno a una pagina della app
    st.page_link("pages/1_Grafici.py", label="📈 Grafici")

with col2:
    st.page_link("pages/2_Pubblicazioni.py", label="📚 Pubblicazioni")

with col3:
    st.page_link("pages/3_Titoli_Certificazioni.py", label="🎓 Titoli & Certificazioni")

st.divider()

# Link esterni (facoltativi)
st.markdown(
    """
    - 🌐 LinkedIn  
    - 💻 [GitHub    """,
    unsafe_allow_html=True,
)

# Download CV (se hai caricato il file)
from pathlib import Path
cv_path = Path("assets/Ulisse_Fabiani_CV.pdf")
if cv_path.exists():
    with cv_path.open("rb") as f:
        st.download_button("📄 Scarica il mio CV", f, file_name="Ulisse_Fabiani_CV.pdf", mime="application/pdf")
