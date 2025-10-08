import streamlit as st
from pathlib import Path  # servirà per CV e per check immagini

st.set_page_config(page_title="Ulisse Fabiani", page_icon="🌱", layout="wide")  #  wide = allineamento a sinistra

# [MODIFICA] —— Parametri modificabili facilmente ——————————————————————————
STAMP_WIDTH = 120          # “francobollo” (px). Provare anche 80, 96, 120...
GRID_COLS   = 5           # quante immagini per riga

# Elenco immagini (aggiungerne/rimuoverne senza rompere nulla).
# "note" è una riga opzionale: se stringa vuota, NON viene mostrata.
IMMAGINI = [
    {"src": "assets/hero.jpg",  "note": "Mocking Face"},          # es.: "note": "Foto 2025, estate"
    {"src": "assets/hero2.jpg", "note": "Le Discret"},          # lasciare "" per non visualizzare nulla
    {"src": "assets/hero3.jpg", "note": "San Govanni Battista"},
]
# ————————————————————————————————————————————————————————————————————————

# helper minimal per visualizzare le immagini come francobolli
def render_thumbs(items, width=STAMP_WIDTH, cols=GRID_COLS):
    # mostra solo quelle che ESISTONO nel repo (assets), così non va in errore se mancano
    safe_items = [it for it in items if Path(it["src"]).exists()]
    if not safe_items:
        return

    for i in range(0, len(safe_items), cols):
        row = safe_items[i : i + cols]
        columns = st.columns(len(row), gap="small")
        for col, it in zip(columns, row):
            with col:
                st.image(it["src"], width=width)
                if it.get("note"):              # se vuoto, non mostra nulla
                    st.caption(it["note"])

# ──────────────────────────────────────────────────────────────────────────
# Titolo/testo SOPRA l’immagine
st.header("Ulisse Fabiani — Portfolio")     # titolo minimal
st.title("Hello, lettore! 👋")
st.subheader("Dammi un buon voto! 😄")

# HERO / COPERTINA (francobolli, allineati a sinistra, anche più immagini)
render_thumbs(IMMAGINI)                      # rende i “francobolli”

st.caption("Portfolio minimal & zen — fatto con Python + Streamlit")

st.divider()

# LINK RAPIDI (interni ed esterni)
col1, col2, col3 = st.columns(3)

with col1:
    # Link interno a una pagina della app
    st.page_link("pages/1_Grafici.py", label="📈 Grafici")

with col2:
    st.page_link("pages/2_Pubblicazioni.py", label="📚 Pubblicazioni")
    st.page_link("pages/3_Titoli_Certificazioni.py", label="🎓 Titoli & Certificazioni")

with col3:
    st.page_link("pages/3_Titoli_Certificazioni.py", label="💻 Programmini (in)utili")

st.divider()


st.markdown(
    f"""
    - 🎓 [Academia.edu](https://independent.academia.edu/FabianiUlisse)
    - 💻 [GitHub]("https://github.dev/Anisiel/ulix")
    """,
    unsafe_allow_html=True,
)

# Download CV (se carico il file)
cv_path = Path("assets/Ulisse_Fabiani_CV.pdf")
if cv_path.exists():
    st.download_button(
        "📄 Scarica il mio CV",
        data=cv_path.read_bytes(),  # leggo i byte direttamente
        file_name="Ulisse_Fabiani_CV.pdf",
        mime="application/pdf",
    )

# ——————————————————————————————————————————————————————————————
# Layout alternativo (OPZIONALE): lo attivo mettendo True
ALT_LAYOUT = False
if ALT_LAYOUT:
    st.divider()
    st.caption("Layout alternativo attivo (sempre minimal)")

    col_img, col_main = st.columns([1, 3], gap="large")
    with col_img:
        render_thumbs(IMMAGINI)  # immagini a sinistra
    with col_main:
        st.header("Ulisse Fabiani — Portfolio")
        st.title("Hello, lettore! 👋")
        st.subheader("Dammi un buon voto! 😄")
     #   st.caption("Portfolio minimal & zen — layout alternativo") # in mezzo al testo

     # Footer fisso in basso a sinistra, dentro il frame principale
DESKTOP_LEFT_OFFSET = "14rem"   # quanto spostare a destra per non coprire la sidebar su desktop
MOBILE_LEFT_OFFSET  = "0.75rem" # margine sinistro su schermi piccoli

st.markdown(
    f"""
    <style>
    /* Aggiungo un po' di spazio in fondo per evitare che il footer copra elementi cliccabili */
    .block-container {{ padding-bottom: 3.25rem; }}

    /* Footer fisso */
    .ulix-footer {{
        position: fixed;
        bottom: 0.6rem;
        left: {MOBILE_LEFT_OFFSET};
        padding: 6px 10px;
        font-size: 0.9rem;
        color: #666;
        background: transparent;  /* resta minimal */
        z-index: 9999;
    }}

    /* Su viewport più larghi sposto il footer a destra per non sovrapporre la sidebar */
    @media (min-width: 992px) {{
        .ulix-footer {{
            left: {DESKTOP_LEFT_OFFSET};
        }}
    }}
    </style>

    <div class="ulix-footer">Portfolio minimal &amp; zen — fatto con Python + Streamlit</div>
    """,
    unsafe_allow_html=True,
)
