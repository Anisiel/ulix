
# =============================================================================
# HOME_ORA — Pagina Home in stile "minimal landing"
# -----------------------------------------------------------------------------
# Obiettivo: una home essenziale con hero centrale, messaggio chiaro e 1-2 CTA.
# - Tipografia grande, tanto spazio bianco, pochi link (principale + secondario)
# - Evita distrazioni: niente gallerie, niente menu complessi
# - CTA porta alle sezioni principali del portfolio
# =============================================================================

import os
from pathlib import Path
import streamlit as st

# Evita doppie set_page_config: chiamala solo se non già impostata dal selettore
if not st.session_state.get("_page_config_done"):
    st.set_page_config(
        page_title="Ulisse Fabiani — Portfolio (Ora)",
        page_icon="🌞",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.session_state["_page_config_done"] = True

# --- Piccolo stamp di versione per capire cosa è online ---
commit = os.getenv("RAILWAY_GIT_COMMIT_SHA", "local")
branch = os.getenv("RAILWAY_GIT_BRANCH", "unknown")
st.caption(f"Build: {commit[:7]} · Branch: {branch}")

# --- CSS minimale per hero centrato, palette neutra con accento ---
ACCENT = "#f59e0b"  # ambra / ocra
CSS = f"""
<style>
/* restringe il container per un look più "landing" */
.main .block-container {{
  max-width: 860px;
}}

/* Hero centrale */
.hero {{
  text-align: center;
  padding: 6rem 1rem 3rem 1rem;
}}
.hero h1 {{
  font-size: 3rem;
  line-height: 1.1;
  margin: 0 0 1rem 0;
}}
.hero p.lead {{
  font-size: 1.25rem;
  color: #4b5563; /* gray-600 */
  margin: 0 auto 2rem auto;
  max-width: 48ch;
}}

/* CTA (se usata in HTML) */
.btn {{
  display: inline-block;
  padding: 0.8rem 1.2rem;
  border-radius: 8px;
  font-weight: 600;
  text-decoration: none;
}}
.btn-primary {{
  background: {ACCENT};
  color: white;
}}
.btn-secondary {{
  background: transparent;
  color: #374151; /* gray-700 */
  border: 2px solid #d1d5db; /* gray-300 */
}}

/* Sezione features */
.features h3 {{
  margin-bottom: 0.5rem;
}}
.features p {{
  color: #6b7280; /* gray-500 */
}}

/* Footer minimale */
.footer {{
  text-align: center;
  color: #6b7280;
  padding: 2rem 0 4rem 0;
}}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# --- HERO ---
st.markdown(
    """
    <div class="hero">
      <h1>Portfolio di Ulisse Fabiani</h1>
      <p class="lead">Soluzioni di analisi dati, visualizzazione interattiva e automazione in Python.
      Una home essenziale, chiara e veloce da consultare.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- CTA (centrate) ---
cta_col1, cta_col2, cta_col3 = st.columns([1, 1, 1])
with cta_col2:
    c1, csp, c2 = st.columns([1, 0.1, 1])

    with c1:
        if st.button("Apri Grafici & Mappe", use_container_width=True):
            st.switch_page("pages/1_Grafici_plotly.py")

    with c2:
        # Se presente, mostra subito il download del CV; altrimenti un toast
        cv = Path("assets/Ulisse_Fabiani_CV.pdf")
        if cv.exists():
            st.download_button(
                "Scarica CV",
                data=cv.read_bytes(),
                file_name=cv.name,
                mime="application/pdf",
                use_container_width=True,
            )
        else:
            if st.button("Scarica CV", use_container_width=True):
                st.toast("CV non trovato in assets/Ulisse_Fabiani_CV.pdf", icon="⚠️")

# --- Features sintetiche (3 card) ---
st.write("")
colA, colB, colC = st.columns(3)
with colA:
    st.markdown("### Visualizzazioni")
    st.markdown("Grafici interattivi con Plotly, Altair ed ECharts. Focus su insight chiari.")
with colB:
    st.markdown("### Automazione")
    st.markdown("Script Python per ETL, pulizia dati e integrazione con Excel/VBA.")
with colC:
    st.markdown("### Pubblicazioni")
    st.markdown("Selezione di lavori accademici e progetti reali (link alle pagine dedicate).")

st.divider()

# --- Link secondari minimali ---
col1, col2 = st.columns(2)
with col1:
    st.markdown("GitHub")
with col2:
    st.markdown("Academia.edu")

## --- Footer ---
st.markdown(
    """
    <div class="footer">© Ulisse Fabiani · Portfolio in Python/Streamlit · Railway hosting</div>
    """,
    unsafe_allow_html=True,
)