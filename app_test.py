import streamlit as st
from pathlib import Path  # servirà per CV e per check immagini

st.set_page_config(page_title="Ulisse Fabiani", page_icon="🌱", layout="wide")  #  wide = allineamento a sinistra

# Titolo principale: mostrato una sola volta, indipendentemente dal layout in modo da stare in alto
st.markdown(
    """
    <div style='line-height:1.05'>
        <h1>Ulisse Fabiani — Portfolio</h1>
        <div class='subtitle'>Hello, lettore! 👋 • Questo è un esempio creato da me nel mese di ottobre 2025 per mostrare le competenze informatiche </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- Stili CSS per migliorare la responsiveness ---------------------------------
try:
    css_path = Path("assets/styles.css")
    if css_path.exists():
        st.markdown(f"<style>{css_path.read_text()}</style>", unsafe_allow_html=True)
# file rimosso: contenuto spostato in appmultipages.py

# Nota: per motivi di sicurezza del repository non elimino fisicamente
# il file ma lo lascio vuoto come marker. Se vuoi che venga effettivamente
# rimosso dal repository, dammi il permesso e lo cancello.
    # fall back: niente CSS esterno se qualcosa va storto
