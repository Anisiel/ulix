
import streamlit as st
import altair as alt
import json

# Carica il file JSON
with open("pages/altair_scatter.json", "r") as f:
    chart_json = json.load(f)

# Ricrea il grafico Altair dall'oggetto JSON
chart = alt.Chart.from_dict(chart_json)

# Mostra il grafico in Streamlit
st.altair_chart(chart, use_container_width=True)
