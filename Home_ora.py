
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

# ---------- CSS minimale ----------
ACCENT = "#f59e0b"
CSS = f"""
<style>
.main .block-container {{
  max-width: 860px;
}}
.hero {{
  text-align: center;
  padding: 2rem 1rem 0.75rem 1rem;
}}
/* Logo molto piccolo, sopra al titolo */
.hero img.logo {{
  width: 24px;     /* ridotto ulteriormente */
  height: auto;
  border-radius: 8px;
}}
.hero h1 {{
  font-size: 2.25rem;
  line-height: 1.15;
  margin: 0.75rem 0 0.5rem 0;
}}
.hero p.lead {{
  font-size: 1.125rem;
  color: #4b5563;
  margin: 0 auto 1.5rem auto;
  max-width: 60ch;
}}

/* Row immagini piccole affiancate, minimal */
.img-row {{
  display: flex;
  gap: 0.75rem;
  justify-content: center;
  align-items: center;
  margin: 0.75rem 0 1.5rem 0;
  flex-wrap: wrap; /* per mobile va sotto */
}}
img-row img {{
  width: 140px;    /* piccole */
  height: auto;
  border-radius: 8px;
  object-fit: contain;
}}

.link-row {{
  display: flex;
  gap: 0.75rem;
  justify-content: center;
  margin: 1rem 0 1.5rem 0;
  flex-wrap: wrap;
}}
.link-row a {{
  padding: 0.5rem 0.9rem;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  text-decoration: none;
  color: #111827;
  background: #fff;
  font-size: 0.95rem;
}}
.link-row a:hover {{
  border-color: {ACCENT};
  box-shadow: 0 0 0 3px rgba(245, 158, 11, 0.15);
}}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# ---------- HERO con logo sopra al titolo ----------
logo_img = Path("assets/img/logo.jpg")
st.markdown('<div class="hero">', unsafe_allow_html=True)
if logo_img.exists():
    st.image(str(logo_img), caption=None)
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
    st.image(str(img1))
else:
    st.warning("Immagine non trovata: hero4.jpg")
if img2.exists():
    st.image(str(img2))
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

links_html = f"""
<div class="link-row">
  <a href="https://github.com/ulissefabiani" target="_blank" rel="noopenert.academia.edu/Ulisseademia.edu</a>
  {f'<a href="assets/Ulisse_F.pdfScarica il mio CV</a>' if cv_path.exists() else '<span style="color:#6b7280;">CV non trovato</span>'}
</div>
"""

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