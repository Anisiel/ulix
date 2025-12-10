
# =============================================================================
# HOME_ORA — Pagina Home in stile "minimal landing"
# -----------------------------------------------------------------------------
# Essenziale, chiara: hero con illustrazione, headline, 1–2 CTA,
# tre sezioni (Visualizzazioni · Automazione · Pubblicazioni) con link alle pagine.
# =============================================================================

from pathlib import Path
import streamlit as st

# Evita doppie set_page_config (se il selettore l'ha già chiamata)
if not st.session_state.get("_page_config_done"):
    st.set_page_config(
        page_title="Ulisse Fabiani — Portfolio (Ora)",
        page_icon="🌞",
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
.hero svg {{
  width: 100%;
  max-width: 640px;
  height: auto;
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
.btn-row {{
  display: flex;
  gap: 0.75rem;
  justify-content: center;
  margin: 0.5rem 0 2rem 0;
}}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# ---------- HERO con illustrazione (SVG semplice tipo “sunrise”) ----------
hero_svg = """
<svg viewBox="0 0 800 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Sunrise illustration">
  <defs>
    <linearGradient id="sky" x1="0" x2="0" y1="0" y2="1">
      <stop offset="0%" stop-color="#fff7ed"/>
      <stop offset="100%" stop-color="#fde68a"/>
    </linearGradient>
    <linearGradient id="sun" x1="0" x2="0" y1="0" y2="1">
      <stop offset="0%" stop-color="#fffbeb"/>
      <stop offset="100%" stop-color="#f59e0b"/>
    </linearGradient>
  </defs>
  <!-- cielo -->
  <rect x="0" y="0" width="800" height="300" fill="url(#sky)"/>
  <!-- sole -->
  <circle cx="400" cy="180" r="50" fill="url(#sun)"/>
  <!-- raggi -->
  <g stroke="#f59e0b" stroke-width="4" stroke-linecap="round">
    <line x1="400" y1="90"  x2="400" y2="140"/>
    <line x1="330" y1="110" x2="370" y2="150"/>
    <line x1="470" y1="110" x2="430" y2="150"/>
    <line x1="310" y1="160" x2="360" y2="170"/>
    <line x1="490" y1="160" x2="440" y2="170"/>
  </g>
  <!-- orizzonte stilizzato -->
  <path d="M0 210 C 150 230, 250 220, 400 210 C 550 200, 650 220, 800 210 L 800 300 L 0 300 Z"
        fill="#fef3c7"/>
</svg>
"""

st.markdown(f'<div class="hero">{hero_svg}</div>', unsafe_allow_html=True)
st.markdown(
    """
<div class="hero">
  <h1>Portfolio di Ulisse Fabiani</h1>
  <p class="lead">Analisi dati, visualizzazioni interattive e automazione in Python.
  Una home essenziale, chiara e veloce da consultare.</p>
</div>
""",
    unsafe_allow_html=True,
)

# ---------- CTA centrali ----------
c1, c2, c3 = st.columns([1, 1, 1])
with c2:
    col_a, _, col_b = st.columns([1, 0.1, 1])
    with col_a:
        if st.button("Apri Grafici & Mappe", use_container_width=True, key="cta_grafici"):
            st.switch_page("pages/1_Grafici_plotly.py")
    with col_b:
        cv = Path("assets/Ulisse_Fabiani_CV.pdf")
        if cv.exists():
            st.download_button(
                "Scarica CV",
                data=cv.read_bytes(),
                file_name=cv.name,
                mime="application/pdf",
                use_container_width=True,
                key="cta_cv",
            )
        else:
            if st.button("Scarica CV", use_container_width=True, key="cta_cv_missing"):
                st.toast("CV non trovato: assets/Ulisse_Fabiani_CV.pdf", icon="⚠️")

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

# ---------- Link secondari ----------
col1, col2 = st.columns(2)
with col1:
    st.markdown("GitHub")
with col2:
    st.markdown("Academia.edu")

## ---------- Footer ----------
st.markdown(
    """
    <div style="text-align:center;color:#6b7280;padding: 1rem 0 2rem 0;">
      © Ulisse Fabiani · Portfolio in Python/Streamlit · Railway hosting
    </div>
    """,
    unsafe_allow_html=True,
)