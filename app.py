import streamlit as st

st.set_page_config(page_title="Ulisse Portfolio", page_icon="🌱")

st.title("Hello, lettore! 👋")
st.subheader("Dammi un buon voto! 😄")

st.write("Ecco i miei titoli:")
st.markdown("- ✅ EIRSAF Full")
st.markdown("- ✅ EIPASS Progressive")

# Grafico semplice
import pandas as pd
import altair as alt

data = pd.DataFrame({
    'Anno': [2023, 2024, 2025],
    'Certificazioni': [1, 3, 5]
})

chart = alt.Chart(data).mark_line(point=True).encode(
    x='Anno',
    y='Certificazioni'
)

st.altair_chart(chart, use_container_width=True)