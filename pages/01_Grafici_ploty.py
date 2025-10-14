# pages/01_Grafici_Plotly.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Grafici Plotly", page_icon="🔷", layout="wide")
st.title("🔷 Grafici interattivi con Plotly")

# Carica dati
file_path = "repo/grafici_speciali.xlsx"
df = pd.read_excel(file_path)
df["Data"] = pd.to_datetime(df["Data"])

st.success(f"Dati caricati: {len(df)} righe")
st.dataframe(df.head(), use_container_width=True)

# ===========================
# 1) Line chart: Temperatura nel tempo
# ===========================
st.subheader("1) Andamento della temperatura")

fig_line = px.line(df, x="Data", y="Temperatura", title="Temperatura giornaliera")

# (facilita l'esplorazione: zoom temporale con cursore)
fig_line.update_xaxes(rangeslider_visible=True)

st.plotly_chart(fig_line, use_container_width=True)

# ===========================
# 1bis) Line chart: Temperatura nel tempo colorata per fascia
# ===========================
st.subheader("1) Andamento della temperatura con variazione dei colori")

 # verifica presenza colonna 'FasciaTemp' in Excel
if "FasciaTemp" not in df.columns:
    st.error("Nel file Excel manca la colonna 'FasciaTemp'. Aggiungila e ricarica la pagina.")
else:
    #  normalizzo le etichette per la mappatura colori (tolleranza trattino lungo, spazi, maiuscole)
    def _norm(s):
        return str(s).strip().lower().replace("-", "-").replace("—", "-")
    df["_fascia_norm"] = df["FasciaTemp"].map(_norm)


#  linea base neutra (grigio) + slider temporale
fig_line = px.line(
    df, x="Data", y="Temperatura",
    title="Temperatura giornaliera"
)
fig_line.update_traces(line=dict(color="#7f7f7f", width=2))  # grigio
fig_line.update_xaxes(rangeslider_visible=True)              #  slider

#  marker colorati per fascia (niente linee)
color_map = {
    "Freddo (<5°C)": "#1f77b4",   # blu
    "Mite (5-20°C)": "#ff7f0e",   # arancio
    "Caldo (>20°C)": "#d62728"    # rosso
}
fig_pts = px.scatter(  # Modifica
    df, x="Data", y="Temperatura", color="FasciaTemp",
    color_discrete_map=color_map,
    opacity=0.9
)

#  aggiungo solo i marker alla figura principale
for tr in fig_pts.data:
    tr.mode = "markers"                   # solo marker (NO linee)
    tr.marker.update(size=5, line=dict(width=0))
    fig_line.add_trace(tr)

st.plotly_chart(fig_line, use_container_width=True)

st.markdown("""
**Perché qui è meglio di Excel**  
- **Interattivo**: interazione tra zoom, pan e **cursore temporale** per scorrere velocemente i periodi.  
- **Hover**:  Quando **passi il mouse** sulla linea o sui puntini, compaiono **tooltip** con data e valore esatto, senza dover formattare etichette a mano.  
- **Esporta** con un click (icona fotocamera) e possibilità di aggiungere altre serie via codice.
""")


# ===========================
# 2) Istogramma: Pioggia per classe (da Excel)
# ===========================
st.subheader("2) Distribuzione della pioggia per classe")

# STEP 1: Controllo che la colonna ClassePioggia esista
if "ClassePioggia" not in df.columns:
    st.error("Nel file Excel manca la colonna 'ClassePioggia'. Aggiungila e ricarica la pagina.")
else:
    # STEP 2: Raggruppo per classe e conto i giorni
    rain_class = df.groupby("ClassePioggia").size().reset_index(name="Conteggio")

    # STEP 3: Ordino le classi in modo logico
    ordine = ["Nessuna pioggia", "Debole (0-2 mm)", "Moderata (2-10 mm)", "Forte (>10 mm)"]
    rain_class["ClassePioggia"] = pd.Categorical(rain_class["ClassePioggia"], categories=ordine, ordered=True)
    rain_class = rain_class.sort_values("ClassePioggia")

    # STEP 4: Creo il grafico a barre colorate per intensità
    fig_hist = px.bar(
        rain_class,
        x="ClassePioggia",
        y="Conteggio",
        color="ClassePioggia",  # Colore per categoria
        color_discrete_map={
            "Nessuna pioggia": "#d9d9d9",   # grigio chiaro
            "Debole (0-2 mm)": "#90caf9",   # azzurro
            "Moderata (2-10 mm)": "#42a5f5",# blu medio
            "Forte (>10 mm)": "#0d47a1"     # blu scuro
        },
        title="Distribuzione dei giorni per classe di pioggia",
        labels={"ClassePioggia": "Classe di pioggia", "Conteggio": "Numero di giorni"}
    )

    # STEP 5: Layout pulito
    fig_hist.update_layout(showlegend=False, margin=dict(l=10, r=10, t=60, b=10))

    # STEP 6: Mostro il grafico
    st.plotly_chart(fig_hist, use_container_width=True)

    # Spiegazione per il portfolio
    st.markdown("""
    **Perché è meglio di Excel:**  
    - Colori coerenti per **classi definite in Excel** (nessuna formula complessa nel grafico).  
    - Interattivo: hover, zoom, esportazione.  
    - Facile aggiornare le soglie: basta cambiare la formula in Excel.
    """)


# ===========================
# 2)bis Scatter plot: Temperatura + Pioggia (punti) nel tempo
# ===========================
# 2) Temperatura (linea) + Pioggia (punti) nel tempo
st.subheader("2) Temperatura (linea) + Pioggia (punti) nel tempo")

# Import per grafico con doppi assi
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# STEP 1: Ordino i dati per Data (evita "zig-zag" della linea)
df = df.sort_values("Data").reset_index(drop=True)

# STEP 2: Creo una figura con due assi Y (sinistra = Temperatura, destra = Pioggia)
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
# Modifica: elimino i punti con pioggia zero
rain = df[df["Pioggia_mm"] > 0]               # Modifica
fig.add_trace(
    go.Scatter(
        x=rain["Data"], y=rain["Pioggia_mm"],  # Modifica
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
    plot_bgcolor="#ffffff"                     # sfondo bianco pulito (opzionale)
)
fig.update_xaxes(title_text="Data", rangeslider=dict(visible=True))

# STEP 6: Assi Y
fig.update_yaxes(title_text="Temperatura [°C]", secondary_y=False)

# Modifica: disattivo griglia e zeroline dell'asse destro (pioggia)
#           così la griglia viene solo dall'asse sinistro ed è sempre "coerente"
fig.update_yaxes(
    title_text="Pioggia (mm)",
    showgrid=False,            # Modifica: niente griglia sull'asse destro
    zeroline=False,            # Modifica: niente "linea dello zero" a destra
    secondary_y=True
)

# Modifica: imposto una griglia leggera solo sull'asse sinistro (opzionale ma consigliato)
fig.update_yaxes(
    showgrid=True, gridcolor="rgba(0,0,0,0.08)", zeroline=False,  # Modifica
    secondary_y=False
)

# STEP 7: Mostro il grafico
st.plotly_chart(fig, use_container_width=True)

# Nota per il portfolio
st.markdown("""
**Perché qui è meglio di Excel**  
- Grafico **con due assi Y** (sinistro e destro) non nativo in Excel.  
- **Filtraggio automatico** dei soli giorni con pioggia (>0) per evitare punti inutili.
- Manteniamo l'interattività: zoom, pan, slider temporale e tooltip.
""")


# 3) Polar bar: Pioggia totale per mese
st.subheader("3) Rosa polare della pioggia mensile")
df["Mese"] = df["Data"].dt.month
rain_month = df.groupby("Mese")["Pioggia_mm"].sum().reset_index()
mesi = ["Gen","Feb","Mar","Apr","Mag","Giu","Lug","Ago","Set","Ott","Nov","Dic"]
rain_month["MeseNome"] = rain_month["Mese"].map({i+1: m for i,m in enumerate(mesi)})

fig_polar = px.bar_polar(
    rain_month, r="Pioggia_mm", theta="MeseNome",
    color="Pioggia_mm", color_continuous_scale="Blues",
    title="Pioggia totale per mese"
)
st.plotly_chart(fig_polar, use_container_width=True)

st.markdown("""
**Perché qui è meglio di Excel**  
- **Tipo di grafico non nativo** in Excel (la vera **bar‑polar**): niente workaround con Radar o formattazioni complesse.  
- **Coordinate polari reali** con hover, colori continui e interazione.  
- Comunica bene **stagionalità/direzioni** in modo più immediato rispetto a una barra “lineare”.
""")