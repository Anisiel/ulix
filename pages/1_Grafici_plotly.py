## pages/01_Grafici_plotly.py
# ==================================
# Prima pagina: tre grafici con la libreria Plotly
#  ======================================================
# STEP 0: IMPORT – cosa fanno
# - streamlit as st: UI web reattiva per titoli, tabelle, grafici (API ref: https://docs.streamlit.io/develop/api-reference)  
# - pandas as pd: gestione dati tabellari; read_excel per caricare xlsx (https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) 
# - plotly.express as px: API alto livello* (grafici rapidi: line/scatter/imshow/bar_polar) (https://plotly.com/python/plotly-express/)
# - plotly.graph_objects as go: API basso livello** (controllo fine, doppi assi, unione tracce) (https://plotly.com/python-api-reference/plotly.graph_objects.html)
# - make_subplots: crea figure con sottoplot/assi secondari (https://plotly.com/python-api-reference/generated/plotly.subplots.make_subplots.html)
# *API Alto livello si intende: API di alto livello (Plotly Express, px) → pochi parametri, grafici immediati.
#   Ideale per linee, scatter, heatmap: una riga, hai già figure pronte, con mapping automatico dei campi del DataFrame (colori, etichette, legende).
# **API Basso livello si intende: API di basso livello (plotly.graph_objects, go) → molti parametri, controllo fine.
#   Serve quando devi combinare tipi di grafico, usare assi secondari o subplots arbitrari con make_subplots.
# ======================================================

import streamlit as st
import pandas as pd
import plotly.express as px

import plotly.graph_objects as go
from plotly.subplots import make_subplots

#======================================================
# STEP A: Configurazione base dell’app Streamlit e titolo
# - set_page_config: imposta titolo, icona e layout (wide = tutta larghezza)
# - st.title: intestazione principale
# ======================================================
st.set_page_config(page_title="Grafici Plotly", page_icon="📊", layout="wide")
st.title("📊 Grafici interattivi con Plotly utilizzando dati meteo inventati")

st.markdown("""
Questa pagina mostra grafici che **Excel non realizza nativamente** (o solo con metodi complicati tipo duplicare dati, formattazioni complesse, macro Vba),
mettendo in evidenza l'**interattività** di Plotly. 

I grafici sono realizzati a partire dai dati di un file excel che è caricato in `repo/grafici_speciali.xlsx`. 
Colonne native: **Data**, **Temperatura**, **Pioggia_mm**. Colonne calcolate: **FasciaTemp** e **ClassePioggia**.
  
Usa ***il selettore e i comandi in alto a destra*** di ciascun grafico per vedere le potenzialità delle librerie python
""")
# ======================================================
# STEP B: Caricamento dati da Excel e preparazione
# - Legge il file Excel
# - Converte 'Data' in datetime per funzioni temporali/slider
# - Mostra info di servizio + anteprima tabellare
# ======================================================
file_path = "repo/grafici_speciali.xlsx"
df = pd.read_excel(file_path)
df["Data"] = pd.to_datetime(df["Data"])

st.success(f"Dati caricati: {len(df)} giorni (1 anno) dal file `{file_path}`")
st.dataframe(df.head(), use_container_width=True)

# ===========================
# 1) Line chart: Temperatura nel tempo
# ===========================
st.subheader("1) Andamento della temperatura")

# STEP 1: Linea semplice della temperatura giornaliera
# - X: Data, Y: Temperatura
fig_line = px.line(df, x="Data", y="Temperatura", title="Temperatura giornaliera")

# STEP 2: Attiva il range slider temporale sotto l'asse X
# - Facilita l’esplorazione nel tempo
fig_line.update_xaxes(rangeslider_visible=True)

# STEP 3: Visualizza il grafico
st.plotly_chart(fig_line, use_container_width=True)
st.divider()
# ===========================
# 1bis) Line chart: Temperatura nel tempo colorata per fascia
# ===========================
st.subheader("1bis) Andamento della temperatura con variazione dei colori")

# STEP 1: Verifica che esista la colonna 'FasciaTemp' in Excel
# - La colorazione per fascia dipende da questa colonna
if "FasciaTemp" not in df.columns:
    st.error("Nel file Excel manca la colonna 'FasciaTemp'. Aggiungila e ricarica la pagina.")
else:
    # STEP 2: (Opzionale) Normalizzazione etichette per mappatura colori
    # - Utile se in Excel compaiono varianti (spazi, maiuscole, trattini lunghi)
    # - Qui la teniamo per eventuali controlli/debug.
    def _norm(s):
        return str(s).strip().lower().replace("-", "-").replace("—", "-")
    df["_fascia_norm"] = df["FasciaTemp"].map(_norm)

# STEP 3: Linea base neutra (grigio) + slider
# - La linea grigia dà la tendenza continua
fig_line = px.line(
    df, x="Data", y="Temperatura",
    title="Temperatura giornaliera"
)
fig_line.update_traces(line=dict(color="#7f7f7f", width=2))  # grigio
fig_line.update_xaxes(rangeslider_visible=True)              #  slider

# marker colorati per fascia (niente linee)
color_map = {
    "Freddo (<5°C)": "#1f77b4",   # blu
    "Mite (5-20°C)": "#ff7f0e",   # arancio
    "Caldo (>20°C)": "#d62728"    # rosso
}
# scatter plot per i punti colorati
fig_pts = px.scatter(  
    df, x="Data", y="Temperatura", color="FasciaTemp",
    color_discrete_map=color_map,
    opacity=0.9
)

# STEP 5: Unisco i marker colorati alla linea base
# - Converto le tracce scatter in “solo marker” e le aggiungo alla figura principal
for tr in fig_pts.data:
    tr.mode = "markers"                   # solo marker (NO linee)
    tr.marker.update(size=5, line=dict(width=0))
    fig_line.add_trace(tr)

# STEP 6: Visualizza il grafico combinato (linea grigia + puntini colorati)
st.plotly_chart(fig_line, use_container_width=True)

# Perché qui è meglio di Excel
st.markdown("""
**Perché qui è meglio di Excel**  
- **Interattivo**: interazione tra zoom, pan e **cursore temporale** per scorrere velocemente i periodi.  
- **Hover**:  Quando **passi il mouse** sulla linea o sui puntini, compaiono **tooltip** con data e valore esatto, senza dover formattare etichette a mano.  
- **Esporta** con un click (icona fotocamera) e possibilità di aggiungere altre serie via codice.
""")
st.divider()
# ===========================
# 1ter) Scatter plot: Temperatura + Pioggia (punti) nel tempo
# ===========================
st.subheader("1ter) Temperatura (linea) + Pioggia (punti) nel tempo")

# STEP 1: Ordino i dati per Data (evita "zig-zag" della linea)
df = df.sort_values("Data").reset_index(drop=True)

# STEP 2: Creo una figura con due assi Y 
# - sinistra  = Temperatura [°C] (linea)
# - destra    = Pioggia (mm)     (punti)
#   (Qui usiamo go + make_subplots perché px non gestisce direttamente il doppio asse)
fig = make_subplots(specs=[[{"secondary_y": True}]])

# STEP 3: Aggiungo la linea della Temperatura (asse sinistro)
fig.add_trace(
    go.Scatter(
        x=df["Data"], y=df["Temperatura"],
        mode="lines",
        line=dict(color="#1f77b4", width=2),   # linea blu
        name="Temperatura [°C]"
    ),
    secondary_y=False
)

# STEP 4: Filtro i soli giorni con Pioggia > 0 e aggiungo i puntini (asse destro)
# - Applico un filtro cosi si evita di mostrare tanti puntini a zero che “sporcano” il grafico
rain = df[df["Pioggia_mm"] > 0]             # filtro
fig.add_trace(
    go.Scatter(
        x=rain["Data"], y=rain["Pioggia_mm"],  
        mode="markers",
        marker=dict(size=6, color="#2ca02c"),  # puntini verdi
        name="Pioggia (mm)"
    ),
    secondary_y=True
)

# STEP 5: Titolo, legenda e slider orizzontale per lo zoom
fig.update_layout(
    title="Temperatura e Pioggia nel tempo",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
    margin=dict(l=10, r=10, t=60, b=10),
    plot_bgcolor="#ffffff"                     # sfondo bianco
)
fig.update_xaxes(title_text="Data", rangeslider=dict(visible=True))

# STEP 6: Assi Y e gestione griglia
# - Asse sinistro (Temperatura): griglia leggera
# - Asse destro  (Pioggia)     : nessuna griglia/zeroline per evitare “sfasamenti”
fig.update_yaxes(title_text="Temperatura [°C]", secondary_y=False)
fig.update_yaxes(
    title_text="Pioggia (mm)",
    showgrid=False,            # niente griglia sull'asse destro
    zeroline=False,            # niente "linea dello zero" a destra
    secondary_y=True
)
# Asse sinistro (Temperatura) con una griglia leggera 
fig.update_yaxes(
    showgrid=True, gridcolor="rgba(0,0,0,0.08)", zeroline=False,  
    secondary_y=False
)

# STEP 7: Mostro il grafico
st.plotly_chart(fig, use_container_width=True)

# Perché qui è meglio di Excel
st.markdown("""
**Perché qui è meglio di Excel**  
- Grafico **con due assi Y** (sinistro e destro) non nativo in Excel.  
- **Filtraggio automatico** dei soli giorni con pioggia (>0) per evitare punti inutili.
- Manteniamo l'interattività: zoom, pan, slider temporale e tooltip.
""")
st.divider()
# ===========================
# 3) Calendario grafico (Heatmap): Pioggia giornaliera
# ===========================
st.subheader("2) Heatmap calendario della pioggia")

# STEP 1: Creo colonne per Mese e Giorno
df["Mese"] = df["Data"].dt.month
df["Giorno"] = df["Data"].dt.day

# STEP 2: Creo una tabella pivot (Mese = righe, Giorno = colonne, valore = Pioggia_mm)
pivot = df.pivot_table(index="Mese", columns="Giorno", values="Pioggia_mm", aggfunc="sum")

# STEP 3: Creo la heatmap con Plotly
fig_heat = px.imshow(
    pivot,
    color_continuous_scale="Blues",
    labels=dict(color="Pioggia (mm)"),
    title="Distribuzione giornaliera della pioggia per mese"
)

# STEP 4: Aggiorno assi con etichette leggibili
mesi = ["Gen","Feb","Mar","Apr","Mag","Giu","Lug","Ago","Set","Ott","Nov","Dic"]
fig_heat.update_yaxes(title="Mese", tickvals=list(range(0,12)), ticktext=mesi)
fig_heat.update_xaxes(title="Giorno del mese")

# STEP 5: Mostro il grafico
st.plotly_chart(fig_heat, use_container_width=True)

# Perché qui è meglio di Excel
st.markdown("""
**Perché qui è meglio di Excel:**  
- Excel non ha un **grafico calendario interattivo**.  
- Qui puoi **vedere subito stagionalità e giorni estremi** con una scala colore.  
- Passa il mouse (hover) dinamico: passa il mouse e leggi il valore preciso.
""")
st.divider()
# ===========================
# 4) Polar bar: Pioggia totale per mese
# ===========================
st.subheader("3) Rosa polare della pioggia mensile")

# STEP 1: Aggrego i mm per mese e preparo etichette
df["Mese"] = df["Data"].dt.month
rain_month = df.groupby("Mese")["Pioggia_mm"].sum().reset_index()
mesi = ["Gen","Feb","Mar","Apr","Mag","Giu","Lug","Ago","Set","Ott","Nov","Dic"]
rain_month["MeseNome"] = rain_month["Mese"].map({i+1: m for i,m in enumerate(mesi)})

# STEP 2: Creo il grafico a barre polari (non nativo in Excel)
# - r     = raggio (mm totali)
# - theta = angolo (mese)
# - color = intensità colore continua
fig_polar = px.bar_polar(
    rain_month, r="Pioggia_mm", theta="MeseNome",
    color="Pioggia_mm", color_continuous_scale="Blues",
    title="Pioggia totale per mese"
)

# STEP 3: Visualizzo il grafico
st.plotly_chart(fig_polar, use_container_width=True)

# Perché qui è meglio di Excel
st.markdown("""
**Perché qui è meglio di Excel**  
- **Tipo di grafico non nativo** in Excel(non ha un grafico predefinito, ma simili, tipo Radar o Grafici a ragnatela): nessun controllo di lunghezza, spessore delle barre, colori continui... ): necessarie formattazioni complesse.  
- **Coordinate polari reali** con hover, colori continui e interazione.  
- Comunica bene **stagionalità/direzioni** in modo più immediato rispetto a una barra “lineare”.
""")