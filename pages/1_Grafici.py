import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

st.set_page_config(page_title="Grafici avanzati", page_icon="📊")

st.title("Visualizzazioni con dati da Excel")

# Carica il file Excel
file_path = "repo/grafici_speciali.xlsx"
df = pd.read_excel(file_path, sheet_name=None, engine="openpyxl")

# --- Grafico a dispersione ---
st.subheader("📌 Grafico a dispersione")
disp = df["Dispersione"]
scatter = alt.Chart(disp).mark_circle(size=100).encode(
    x=alt.X("X", title="Variabile X"),
    y=alt.Y("Y", title="Variabile Y"),
    color="Categoria",
    tooltip=["X", "Y", "Categoria"]
).properties(title="Distribuzione delle categorie")
st.altair_chart(scatter, use_container_width=True)

# --- Heatmap interattiva ---
st.subheader("🔥 Heatmap interattiva")
st.markdown("Questa visualizzazione non è realizzabile in Excel perché richiede interattività e gradienti dinamici.")
heat = df["Heatmap"]
heatmap = alt.Chart(heat).mark_rect().encode(
    x=alt.X("Ora:O", title="Ora del giorno"),
    y=alt.Y("Giorno:O", title="Giorno della settimana"),
    color=alt.Color("Intensità:Q", scale=alt.Scale(scheme="reds")),
    tooltip=["Giorno", "Ora", "Intensità"]
).properties(title="Intensità attività settimanale")
st.altair_chart(heatmap, use_container_width=True)

# --- Grafico Radial ---
st.subheader("🧭 Grafico a raggi (Radial)")
st.markdown("Questo tipo di grafico non è supportato da Excel: richiede coordinate polari e trasformazioni geometriche.")
radial = df["Radial"]
radial["Angolo"] = radial.index * (360 / len(radial))
radial["Radiani"] = radial["Angolo"] * np.pi / 180
radial["X"] = radial["Valore"] * np.cos(radial["Radiani"])
radial["Y"] = radial["Valore"] * np.sin(radial["Radiani"])

radial_chart = alt.Chart(radial).mark_line(point=True).encode(
    x=alt.X("X", title="X"),
    y=alt.Y("Y", title="Y"),
    tooltip=["Categoria", "Valore"]
).properties(title="Distribuzione Radiale delle Attività")
st.altair_chart(radial_chart, use_container_width=True)