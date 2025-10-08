import streamlit as st
from pathlib import Path  # servirà per CV e per check immagini

st.set_page_config(page_title="Ulisse Fabiani", page_icon="🌱", layout="wide")

# Titolo principale: mostrato una sola volta, indipendentemente dal layout
st.markdown(
    """
    <div style='line-height:1.05'>
        <h1>Ulisse Fabiani — Portfolio</h1>
        <div class='subtitle'>Hello, lettore! 👋 • Dammi un buon voto! 😄</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Carica CSS esterno (se presente)
try:
    css_path = Path("assets/styles.css")
    if css_path.exists():
        st.markdown(f"<style>{css_path.read_text()}</style>", unsafe_allow_html=True)
except Exception:
    pass

# Parametri
STAMP_WIDTH = 120
GRID_COLS = 5

IMMAGINI = [
    {"src": "assets/hero.jpg", "note": "Mocking Face"},
    {"src": "assets/hero2.jpg", "note": "Le Discret"},
    {"src": "assets/hero3.jpg", "note": "San Govanni Battista"},
]

def render_thumbs(items, width=STAMP_WIDTH, cols=GRID_COLS):
    safe_items = [it for it in items if Path(it["src"]).exists()]
    if not safe_items:
        return
    for i in range(0, len(safe_items), cols):
        row = safe_items[i : i + cols]
        columns = st.columns(len(row), gap="small")
        for col, it in zip(columns, row):
            with col:
                st.image(it["src"], use_container_width=True)
                if it.get("note"):
                    st.caption(it["note"])

# Layout flag (vai in alternativa minimal se True)
ALT_LAYOUT = True

if not ALT_LAYOUT:
    st.title("Hello, lettore! 👋")
    st.subheader("Dammi un buon voto! 😄")
    render_thumbs(IMMAGINI)

    st.divider()
    # External links
    st.markdown(
        """
        - 🎓 [Academia.edu](https://independent.academia.edu/FabianiUlisse)
        - 💻 [GitHub](https://github.com/Anisiel/ulix)
        """,
        unsafe_allow_html=True,
    )
    # CV download (unique key)
    cv_path = Path("assets/Ulisse_Fabiani_CV.pdf")
    if cv_path.exists():
        st.download_button(
            "📄 Scarica il mio CV",
            data=cv_path.read_bytes(),
            file_name="Ulisse_Fabiani_CV.pdf",
            mime="application/pdf",
            key="cv_download_alt",
        )

    st.divider()
    # Internal links (columns)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("📈 [Grafici](pages/1_Grafici.py)", unsafe_allow_html=True)
    with col2:
        st.markdown("📚 [Pubblicazioni](pages/2_Pubblicazioni.py)", unsafe_allow_html=True)
        st.markdown("🎓 [Titoli & Certificazioni](pages/3_Titoli_Certificazioni.py)", unsafe_allow_html=True)
    with col3:
        st.markdown("💻 [Programmini (in)utili](pages/4_Programmini.py)", unsafe_allow_html=True)

else:
    st.divider()
    st.caption("Layout alternativo attivo (sempre minimal)")
    col_img, col_main = st.columns([1, 3], gap="large")
    with col_img:
        render_thumbs(IMMAGINI)
    with col_main:
        st.title("Hello, lettore! 👋")
        st.subheader("Dammi un buon voto! 😄")
        st.caption("Portfolio minimal & zen — layout alternativo")

    # After the two-column row: external links, CV, then internal links
    st.divider()
    st.markdown(
        """
        - 🎓 [Academia.edu](https://independent.academia.edu/FabianiUlisse)
        - 💻 [GitHub](https://github.com/Anisiel/ulix)
        """,
        unsafe_allow_html=True,
    )
    cv_path = Path("assets/Ulisse_Fabiani_CV.pdf")
    if cv_path.exists():
        st.download_button(
            "📄 Scarica il mio CV",
            data=cv_path.read_bytes(),
            file_name="Ulisse_Fabiani_CV.pdf",
            mime="application/pdf",
            key="cv_download_main",
        )

    st.divider()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("📈 [Grafici](pages/1_Grafici.py)", unsafe_allow_html=True)
    with col2:
        st.markdown("📚 [Pubblicazioni](pages/2_Pubblicazioni.py)", unsafe_allow_html=True)
        st.markdown("🎓 [Titoli & Certificazioni](pages/3_Titoli_Certificazioni.py)", unsafe_allow_html=True)
    with col3:
        st.markdown("💻 [Programmini (in)utili](pages/4_Programmini.py)", unsafe_allow_html=True)

    st.divider()
