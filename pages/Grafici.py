# grafici.py
import streamlit as st

st.set_page_config(page_title="Grafici avanzati", page_icon="📊", layout="wide")

st.title("📊 Portfolio – Grafici avanzati su dati meteo (Italia)")

st.markdown("""
Questa app mostra grafici che **Excel non realizza nativamente** (o solo con workaround complessi),
mettendo in evidenza **trasformazioni numeriche** (NumPy) e **interattività** (Plotly).

- Vai su **Pages → Grafici NumPy** per 3 grafici “NumPy-first”
- Vai su **Pages → Grafici Plotly** per 3 grafici interattivi

Carica il tuo file in `repo/grafici_speciali.xlsx` con un foglio (es. `Meteo`) e colonne:
**Data**, **Temperatura**, **Pioggia_mm**. In alternativa, la pagina genera **dati sintetici** realistici.
""")