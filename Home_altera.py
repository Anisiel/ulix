
import streamlit as st
from pathlib import Path
import base64

# =============================================================================
# STRUTTURA DELLA PAGINA — Home_altera.py (Versione Ricca)
# -----------------------------------------------------------------------------
# Questa pagina mostra una versione più elaborata del portfolio per la gestione delle immagini, ma più povera in relazione ai testi.
# Include una galleria immagini, link estesi e navigazione avanzata.
#
# Comandi principali:
# - `st.set_page_config(layout="wide")`: layout ampio e coerente
# - `st.columns(...)`: griglia per organizzare contenuti e link
# - `base64` + `data URI`: visualizzazione immagini senza richieste esterne
# - `st.download_button(...)`: pulsante per scaricare il CV
#
# Anche qui viene caricato `styles.css` per garantire coerenza visiva
# e mantenere il contenuto vicino alla sidebar.
# =============================================================================

# 🔗 Rimando alla pagina di organizzazione del sito
# Mostra la descrizione del progetto in alto a destra
col_left, col_right = st.columns([2, 3])  # proporzioni: sinistra più stretta
with col_right:
    with st.expander(" Info sul selettore e sul portfolio"):
        st.markdown("Vuoi sapere come è strutturato il sito e come funziona il selettore?")
        if st.button(" ***Organizzazione portfolio***"):
            st.switch_page("pages/0_Organizzazione_portfolio.py")

st.set_page_config(page_title="Ulisse Fabiani — Portfolio", page_icon="🌿", layout="wide")

# Intestazione colorata e centrale
st.markdown(
    """
    <div style='text-align:center;padding:2rem;background-color:#f0f2f6;border-radius:10px'>
        <h1 style='margin-bottom:0.2em'>🌟 Ulisse Fabiani</h1>
        <p style='font-size:1.2em'>Benvenuto nel mio portfolio interattivo — Home page versione ricca per la gestione delle immagini, ma più povera per la gestione dei testi</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Galleria immagini in griglia centrale
IMMAGINI = [
    {"src": "assets/img/hero.jpg", "note": "[Mocking Face](https://en.wikipedia.org/wiki/Joseph_Ducreux)"},
    {"src": "assets/img/hero2.jpg", "note": "[Le Discret](https://spencerart.ku.edu/art/collections-online/object/9141)"},
    {"src": "assets/img/hero3.jpg", "note": "[San Govanni Battista](https://it.wikipedia.org/wiki/San_Giovanni_Battista_(Leonardo))"},
]


def render_gallery(items):
    safe_items = [it for it in items if Path(it["src"]).exists()]
    if not safe_items:
        return
    st.markdown("###  Galleria")
    st.caption ("##### qui mostro solo le tre immagini in box che ne uniformano le dimensioni")
    cols = st.columns(3)
    for col, it in zip(cols, safe_items):

        with col:
    # costruisco un data URI così il browser non chiede /assets
            p = Path(it["src"])  
            ext = p.suffix.lower()  
            mime = "image/png" if ext == ".png" else "image/jpeg"  
            b64 = base64.b64encode(p.read_bytes()).decode() 
            uri = f"data:{mime};base64,{b64}" 

            st.markdown(
                f"<div class='thumb-box'><img src=\"{uri}\" class='gallery-thumb' /></div>",  
            unsafe_allow_html=True
            )
            if it.get("note"):
                st.caption(it["note"])

# Chiamata alla funzione
render_gallery(IMMAGINI)

# CSS per altezza immagini — posizionato DOPO la galleria
st.markdown("""
<style>
  /* ---- Configurazione rapida ---- */
  :root { --thumb-h: 120px; } /* cambia qui l'altezza delle miniature */

  /* Contenitore della miniatura */
  .thumb-box {
    height: var(--thumb-h);            /* stessa altezza per tutte */
    width: 100%;
    overflow: hidden;
    border-radius: 8px;
    background: #f2f2f2;               /* leggero sfondo "letterbox" */
    display: flex;                      /* centriamo l'immagine */
    align-items: center;
    justify-content: center;
  }

  /* Immagine dentro il contenitore */
  .thumb-box > img.gallery-thumb {
    max-width: 100%;
    max-height: 100%;
    width: auto;
    height: auto;
    object-fit: contain;                /* mostra tutta l'immagine (NO crop) */
    object-position: center;            /* centrata */
    display: block;
  }

  /* Bordo arrotondato coerente anche sull'immagine */
  .thumb-box > img.gallery-thumb { border-radius: 8px; }
</style>
""", unsafe_allow_html=True)

# Box informativi con link esterni
st.markdown("---")
st.markdown("### 🔗 Link utili")
st.markdown("Ecco alcuni link utili per saperne di più sulla mia attività all'Università e sulle risorse utilizzate per questo sito.")
col1, col2 = st.columns(2) 
with col1:
    st.markdown("📘 [Academia.edu](https://independent.academia.edu/FabianiUlisse)")
with col2:
    st.markdown("💻 [GitHub](https://github.com/Anisiel/ulix)") 
    st.markdown("💻 [Streamlit](https://streamlit.io/)")
    st.markdown("💻 [Streamlit](https://railway.com/)") 


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
    st.markdown("### 📊 Grafici & Mappe")
    st.page_link("pages/1_Grafici_plotly.py", label="📊 Grafici con Plotly")
    st.page_link("pages/2_Grafici_Altair_ECharts.py", label="🌐 Grafici con Echarts")
    st.page_link("pages/3_Grafici_Altair_Meteo.py", label="🌦️ Grafici Meteo con Altair")
    st.page_link("pages/9_GIS_PCM.py", label="🗺️ Mappe e dati spaziali")

with col2:
    st.markdown("### 🎓 Curriculum")
    st.page_link("pages/5_Titoli.py", label="🎓 Titoli di Studio")
    st.page_link("pages/6_Certificazioni.py", label="📜 Certificazioni")
    st.page_link("pages/7_Pubblicazioni.py", label="📖 Pubblicazioni")

with col3:
    st.markdown("### 🧰 Utility & Excel")
    st.page_link("pages/4_Programmini_(in)utili.py", label="🧪 Programmini (in)utili in DOS, Python e VBA")
    st.page_link("pages/10_crediti_contributi_pipeline.py", label="🧪 Crediti & contributi, un approccio integrato in Python")


st.divider()