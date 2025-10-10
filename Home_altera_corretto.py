import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Ulisse Fabiani — Portfolio", page_icon="🌿", layout="wide")

# Intestazione colorata e centrale
st.markdown(
    """
    <div style='text-align:center;padding:2rem;background-color:#f0f2f6;border-radius:10px'>
        <h1 style='margin-bottom:0.2em'>🌟 Ulisse Fabiani</h1>
        <p style='font-size:1.2em'>Benvenuto nel mio portfolio interattivo — versione ricca</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Galleria immagini in griglia centrale
IMMAGINI = [
    {"src": "assets/hero.jpg",  "note": "Mocking Face"},
    {"src": "assets/hero2.jpg", "note": "Le Discret"},
    {"src": "assets/hero3.jpg", "note": "San Govanni Battista"},
]

def render_gallery(items):
    safe_items = [it for it in items if Path(it["src"]).exists()]
    if not safe_items:
        st.warning("Nessuna immagine trovata nella cartella 'assets/'.")
        return
    st.markdown("### 🎨 Galleria")
    cols = st.columns(3)
    for col, it in zip(cols, safe_items):
        with col:
            st.markdown(
                f"<img src='{it['src']}' class='gallery-thumb' />",
                unsafe_allow_html=True
            )
            if it.get("note"):
                st.caption(it["note"])

render_gallery(IMMAGINI)

# CSS per altezza immagini
st.markdown("""
<style>
img.gallery-thumb {
    height: 180px !important;
    object-fit: cover;
    width: 100%;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# Box informativi con link esterni
st.markdown("---")
st.markdown("### 🔗 Link utili")
col1, col2 = st.columns(2)
with col1:
    st.markdown("📘 [Academia.edu](https://independent.academia.edu/FabianiUlisse)")
with col2:
    st.markdown("💻 [GitHub](https://github.com/Anisiel/ulix)")

# Download CV
cv_path = Path("assets/Ulisse_Fabiani_CV.pdf")
if cv_path.exists():
    st.markdown("---")
    st.download_button(
        "📄 Scarica il mio CV",
        data=cv_path.read_bytes(),
        file_name="Ulisse_Fabiani_CV.pdf",
        mime="application/pdf",
        key="cv_download_altera"
    )

# Navigazione interna con icone
st.markdown("---")
st.markdown("### 🧭 Navigazione")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("📊 [Grafici](pages/1_Grafici.py)")
with col2:
    st.markdown("📚 [Pubblicazioni](pages/2_Pubblicazioni.py)")
    st.markdown("🎓 [Titoli & Certificazioni](pages/3_Titoli_Certificazioni.py)")
with col3:
    st.markdown("🖥️ [Programmini (in)utili](pages/4_Programmini.py)")
