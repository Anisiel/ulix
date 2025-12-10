
# =============================================================================
# HOME_ORA — Pagina Home in stile "minimal landing"
# ----------------------------------------------------------------------------- 
# Essenziale, chiara: hero con immagine, headline, 3 sezioni con link.
# =============================================================================

from pathlib import Path
import streamlit as st

# Evita doppie set_page_config (se il selettore l'ha già chiamata)
logo_path = Path("assets/img/logo.jpg")  # <-- immagine icona
if not st.session_state.get("_page_config_done"):
    st.set_page_config(
        page_title="Ulisse Fabiani — Portfolio (Ora)",
        page_icon=str(logo_path) if logo_path.exists() else "🌞",  # usa immagine come icona
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.session_state["_page_config_done"] = True

# ---------- CSS minimale ----------
ACCENT = "#f59e0b"  # ambra/ocra
CSS = f"""
<style>
.main .block-container {{
  max-width: 860px;
}}
.hero {{
  text-align: center;
  padding: 2rem 1rem 1rem 1rem;
}}
.hero img {{
  width: 100%;
  max-width: 640px;
  height: auto;
  border-radius: 8px;
}}
.hero h1 {{
  font-size: 3rem;
  line-height: 1.1;
  margin: 1rem 0 0.5rem 0;
}}
.hero p.lead {{
  font-size: 1.125rem;
  color: #4b5563; /* gray-600 */
  margin: 0 auto 1.5rem auto;
  max-width: 60ch;
}}
.img-row {{
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
  margin: 0.5rem 0 2rem 0;
}}
.img-row img {{
  width: 100%;
  max-width: 420px;
  height: auto;
  border-radius: 8px;
}}
.link-row {{
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
  margin: 0.5rem 0 1.5rem 0;
}}
.link-row a {{
  display: inline-block;
  padding: 0.625rem 1rem;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  text-decoration: none;
  color: #111827;
  background: #fff;
}}
.link-row a:hover {{
  border-color: {ACCENT};
  box-shadow: 0 0 0 3px rgba(245, 158, 11, 0.15);
}}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# ---------- HERO con immagine ----------
hero_img = Path("assets/img/hero4.jpg")
st.markdown('<div class="hero">', unsafe_allow_html=True)
if hero_img.exists():
    st.image(str(hero_img), caption=None, use_container_width=False)
else:
    st.info("Immagine hero non trovata: assets/img/hero4.jpg")

st.markdown(
    """
  <h1>Portfolio di Ulisse Fabiani</h1>
  <p class="lead">Analisi dati, visualizzazioni interattive e automazione in Python.
  Una home essenziale, chiara e veloce da consultare.</p>
""",
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

# ---------- Al posto della CTA: due immagini ----------
img1 = Path("assets/img/hero4.jpg")
img2 = Path("assets/img/hero5.jpg")
row_html = '<div class="img-row">'
st.markdown(row_html, unsafe_allow_html=True)
if img1.exists():
    st.image(str(img1), use_container_width=False)
else:
    st.warning("Immagine non trovata: assets/img/hero4.jpg")
if img2.exists():
    st.image(str(img2), use_container_width=False)
else:
    st.warning("Immagine non trovata: assets/img/hero5.jpg")
st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# ---------- Sezioni con link alle pagine ----------
colA, colB, colC = st.columns(3)

with colA:
    st.subheader("Visualizzazioni")
    st.caption("Grafici interattivi con Plotly, Altair ed ECharts.")
    if st.button("Plotly", use_container_width=True, key="v_plotly"):
        st.switch_page("pages/1_Grafici_plotly.py")
    if st.button("Echarts & Altair", use_container_width=True, key="v_echarts_altair"):
        st.switch_page("pages/2_Grafici_Altair_Echarts.py")
    if st.button("Meteo con Altair", use_container_width=True, key="v_meteo"):
        st.switch_page("pages/3_Grafici_Altair_Meteo.py")
    if st.button("Mappe GIS/PCM", use_container_width=True, key="v_gis"):
        st.switch_page("pages/9_GIS_PCM.py")

with colB:
    st.subheader("Automazione")
    st.caption("Script Python, utility e integrazione con Excel/VBA.")
    if st.button("Programmini (in)utili", use_container_width=True, key="a_prog"):
        st.switch_page("pages/4_Programmini_(in)utili.py")
    if st.button("Excel & Progetti VBA", use_container_width=True, key="a_excel_vba"):
        st.switch_page("pages/8_Excel_Progetti_VBA.py")

with colC:
    st.subheader("Pubblicazioni")
    st.caption("Selezione di lavori e attività accademiche.")
    if st.button("Pubblicazioni", use_container_width=True, key="p_pubblicazioni"):
        st.switch_page("pages/7_Pubblicazioni.py")
    if st.button("Titoli di Studio", use_container_width=True, key="p_titoli"):
        st.switch_page("pages/5_Titoli.py")
    if st.button("Certificazioni", use_container_width=True, key="p_certificazioni"):
        st.switch_page("pages/6_Certificazioni.py")

st.divider()

# ---------- Link secondari (GitHub · Academia · CV) ----------
cv_path = Path("assets/Ulisse_Fabiani_CV.pdf")
links_html = f"""
<div class="link-row">
  https://github.com/ulissefabianiGitHub</a>
  <a href="https://independent.academia.edu/UlisseFabiani" target="_blank"s/Ulisse_Fabiani_CV.pdfScarica il mio CV</a>" if cv_path.exists() else "<span style='color:#6b7280;'>CV non trovato</span>"
</div>
"""
st.markdown(links_html, unsafe_allow_html=True)

## ---------- Footer ----------
st.markdown(
    """
    <div style="text-align:center;color:#6b7280;padding: 1rem 0 2rem 0;">
      © Ulisse Fabiani · Portfolio in Python/Streamlit · Railway hosting
    </div>
       """,
    unsafe_allow_html=True,
)