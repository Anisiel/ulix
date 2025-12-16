
# =============================================================================
# HOME_ORA — Pagina Home in stile "minimal landing"
# =============================================================================

from pathlib import Path
import streamlit as st

# Configurazione pagina (icona rimane emoji, NON il logo)
if not st.session_state.get("_page_config_done"):
    st.set_page_config(
        page_title="Ulisse Fabiani — Portfolio (Ora)",
        page_icon="🌞",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.session_state["_page_config_done"] = True

# ---------- Carica CSS esterno ----------
css_path = Path("assets/stylehora.css")
if css_path.exists():
    st.markdown(f"<style>{css_path.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)
else:
    st.warning("File CSS non trovato: assets/stylehora.css")

# ---------- HERO con logo sopra al titolo ----------
logo_img = Path("assets/img/logo.jpg")
st.markdown('<div class="hero">', unsafe_allow_html=True)

# Mostra il logo come <img class="logo"> per applicare la regola CSS (24px)
if logo_img.exists():
    st.markdown(
        f'{logo_img.as_posix()}',
        unsafe_allow_html=True
    )
else:
    st.warning("Logo non trovato: assets/img/logo.jpg")
    
st.markdown(
    """
<h1>Portfolio di Ulisse Fabiani</h1>
<p class="lead">Analisi dati, visualizzazioni interattive e automazione in Python.
Una home essenziale, chiara e veloce da consultare.</p>
""",
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)


# ---------- Due immagini affiancate sotto il titolo ----------
img1 = Path("assets/img/hero4.jpg")
img2 = Path("assets/img/hero5.jpg")

st.markdown('<div class="img-row">', unsafe_allow_html=True)

if img1.exists():
    st.markdown(
        f'{img1.as_posix()}',
        unsafe_allow_html=True
    )
else:
    st.warning("Immagine non trovata: hero4.jpg")

if img2.exists():
    st.markdown(
        f'{img2.as_posix()}',
        unsafe_allow_html=True
    )
else:
       st.warning("Immagine non trovata: hero5.jpg")
st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# ---------- Sezioni con link alle pagine ----------
colA, colB, colC = st.columns(3)
with colA:
    st.subheader("Visualizzazioni")
    st.caption("Grafici interattivi con Plotly, Altair ed ECharts.")
    if st.button("Plotly", use_container_width=True): st.switch_page("pages/1_Grafici_plotly.py")
    if st.button("Echarts & Altair", use_container_width=True): st.switch_page("pages/2_Grafici_Altair_Echarts.py")
    if st.button("Meteo con Altair", use_container_width=True): st.switch_page("pages/3_Grafici_Altair_Meteo.py")
    if st.button("Mappe GIS/PCM", use_container_width=True): st.switch_page("pages/9_GIS_PCM.py")

with colB:
    st.subheader("Automazione")
    st.caption("Script Python, utility e integrazione con Excel/VBA.")
    if st.button("Programmini (in)utili", use_container_width=True): st.switch_page("pages/4_Programmini_(in)utili.py")
    if st.button("Excel & Progetti VBA", use_container_width=True): st.switch_page("pages/8_Excel_Progetti_VBA.py")

with colC:
    st.subheader("Pubblicazioni")
    st.caption("Selezione di lavori e attività accademiche.")
    if st.button("Pubblicazioni", use_container_width=True): st.switch_page("pages/7_Pubblicazioni.py")
    if st.button("Titoli di Studio", use_container_width=True): st.switch_page("pages/5_Titoli.py")
    if st.button("Certificazioni", use_container_width=True): st.switch_page("pages/6_Certificazioni.py")

st.divider()



# ---------- Link secondari ----------
cv_path = Path("assets/Ulisse_Fabiani_CV.pdf")

stst.write("### Link utili")
st.link_button("GitHub", "https://github.com/ulissefabiani")

if cv_path.exists():
    st.link_button("Scarica il mio CV", cv_path.as_posix())
else:
    st.caption("CV non trovato")

st.markdown(links_html, unsafe_allow_html=True)

# ---------- Footer ----------
st.markdown(
    """
    <div style="text-align:center;color:#6b7280;padding: 1rem 0 2rem 0;">
      © Ulisse Fabiani · Portfolio in Python/Streamlit · Railway hosting
    </div>
    """,
    unsafe_allow_html=True,
)
