
import streamlit as st
import pandas as pd
import altair as alt

# Configura la pagina
st.set_page_config(page_title="Grafico Meteo Roma", page_icon="🌦")
st.title("🌦 Andamento Meteo Storico a Roma")

st.write(
    """
    Questa pagina visualizza i dati storici delle variabili meteo a Roma che sono stati scaricati da [Kaggle.com](https://www.kaggle.com/) che offre un [database gratuito di dati ambientali](https://www.kaggle.com/datasets/jarredpriester/rome-italy-weather-data?resource=download).
    I dati sono stati caricati in un file CSV nella cartella 'repo'.
    Il grafico mostra l'andamento meteo per la città di Roma, utilizzando temperatura media, massima, minima e precipitazioni (PRECIP).
    """
)

# Percorso del file CSV (salvalo in repo/)
file_path = "repo/Roma_weather.csv"

# Carica il dataset
df = pd.read_csv(file_path)

# Estrai l'anno dalla colonna DATA
df["YEAR"] = pd.to_datetime(df["DATA"], errors="coerce").dt.year

# Variabili meteo disponibili
variabili_meteo = ["TempMedia", "TempMAX", "TempMIN", "PRECIP"]

# Filtri interattivi
anni_disponibili = sorted(df["YEAR"].dropna().unique())
anno_inizio, anno_fine = st.select_slider(
    "Seleziona intervallo di anni",
    options=anni_disponibili,
    value=(anni_disponibili[0], anni_disponibili[-1])
)

variabili_selezionate = st.multiselect(
    "Variabili meteo da visualizzare",
    variabili_meteo,
    default=variabili_meteo
)

# Filtra il dataframe
df_filtrato = df[(df["YEAR"] >= anno_inizio) & (df["YEAR"] <= anno_fine)]

# Riorganizza i dati per Altair
df_melted = df_filtrato.melt(
    id_vars=["DATA"],
    value_vars=variabili_selezionate,
    var_name="Variabile",
    value_name="Valore"
)
df_melted.dropna(subset=["Valore"], inplace=True)

# Grafico interattivo
grafico = alt.Chart(df_melted).mark_line().encode(
    x="DATA:T",
    y="Valore:Q",
    color="Variabile:N"
).properties(
    width=800,
    height=400,
    title="Andamento delle variabili meteo a Roma"
)

st.altair_chart(grafico, use_container_width=True)

# Tabella dei dati filtrati
with st.expander("📋 Visualizza dati tabellari"):
    st.dataframe(df_filtrato[["DATA"] + variabili_selezionate].dropna())