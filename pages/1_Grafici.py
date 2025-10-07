import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="Grafici", page_icon="📈")

st.title("Grafici di esempio")
st.write("Un grafico minimalista come demo:")

# Dati fittizi (sostituisci con i tuoi)
df = pd.DataFrame({
    "Anno": [2023, 2024, 2025],
    "Certificazioni": [1, 3, 5],
})

chart = (
    alt.Chart(df)
    .mark_line(point=True)
    .encode(
        x=alt.X("Anno:O", title="Anno"),
        y=alt.Y("Certificazioni:Q", title="Numero certificazioni"),
        tooltip=["Anno", "Certificazioni"],
    )
)

st.altair_chart(chart, use_container_width=True)

st.info(
    "Suggerimento: puoi caricare i tuoi dati (CSV/Excel) nella cartella del repo e "
    "leggerli con pandas per creare grafici reali."
)
