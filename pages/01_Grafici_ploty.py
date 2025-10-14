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
# 1bis) Line chart: Temperatura nel tempo
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


# Modifica: marker colorati per fascia (niente linee)
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

# Modifica: aggiungo solo i marker alla figura principale
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

# 2) Scatter plot: Temperatura vs Pioggia
st.subheader("2) Relazione Temperatura vs Pioggia")
fig_scatter = px.scatter(
    df, x="Temperatura", y="Pioggia_mm",
    title="Temperatura vs Pioggia",
    opacity=0.6
)
st.plotly_chart(fig_scatter, use_container_width=True)

st.markdown("""
**Perché qui è meglio di Excel**  
- **Selezione lasso/box** direttamente sul grafico per isolare gruppi di punti o outlier.  
- **Hover** con valori precisi e zoom fluido per scoprire pattern che su grafici statici si perdono.  
- Puoi estendere facilmente con **colorazioni per categoria** o **assi logaritmici** senza formule.
""")



# 2) Temperatura (linea) + Pioggia (punti) nel tempo  # Modifica
st.subheader("2) Temperatura (linea) + Pioggia (punti) nel tempo")  # Modifica

import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Modifica: ordine per Data
df = df.sort_values("Data").reset_index(drop=True)  # Modifica

# Modifica: CATEGORIE ROBUSTE (derivate dal numero, indipendenti dal testo in Excel)
fasce_bins   = [-1e9, 5, 20, 1e9]  # <5, 5-20, >20
fasce_labels = ["Freddo (<5°C)", "Mite (5-20°C)", "Caldo (>20°C)"]  # ASCII semplice  # Modifica
df["FasciaTemp_plot"] = pd.cut(df["Temperatura"], bins=fasce_bins, labels=fasce_labels,
                               include_lowest=True, right=True)  # Modifica

# Modifica: mappa colori coerente
color_map = {
    "Freddo (<5°C)": "#1f77b4",   # blu
    "Mite (5-20°C)": "#ff7f0e",   # arancio
    "Caldo (>20°C)": "#d62728"    # rosso
}

# Modifica: interruttore scala log per pioggia
log_rain = st.checkbox("Scala log sulla pioggia (asse destro)", value=True)  # Modifica

# Modifica: figura con doppi assi
fig_combo = make_subplots(specs=[[{"secondary_y": True}]])

# --- Linea della Temperatura (asse sinistro) ---
fig_combo.add_trace(
    go.Scatter(
        x=df["Data"], y=df["Temperatura"],
        mode="lines",
        line=dict(color="#7f7f7f", width=2),
        name="Temperatura [°C]"
    ),
    secondary_y=False
)

# --- Punti di Pioggia (asse destro), colorati per FasciaTemp_plot ---

# 1) Line chart: Temperatura nel tempo
st.subheader("1) Andamento della temperatura")

# Modifica: ordino per data
df = df.sort_values("Data").reset_index(drop=True)  # Modifica

# Modifica: verifica presenza colonna 'FasciaTemp' in Excel
if "FasciaTemp" not in df.columns:
    st.error("Nel file Excel manca la colonna 'FasciaTemp'. Aggiungila e ricarica la pagina.")
else:
    # Modifica: normalizzo le etichette per la mappatura colori (tolleranza trattino lungo, spazi, maiuscole)
    def _norm(s):
        return str(s).strip().lower().replace("–", "-").replace("—", "-")
    df["_fascia_norm"] = df["FasciaTemp"].map(_norm)

    # Modifica: colori desiderati per le 3 fasce standard (fallback automatico per categorie extra)
    import plotly.express as px
    fixed_map = {
        _norm("Freddo (<5°C)"): "#1f77b4",
        _norm("Mite (5-20°C)"): "#ff7f0e",
        _norm("Caldo (>20°C)"): "#d62728",
    }
    uniq = [v for v in df["_fascia_norm"].dropna().unique().tolist()]
    palette = px.colors.qualitative.Set2 + px.colors.qualitative.Pastel
    auto_map = {k: palette[i % len(palette)] for i, k in enumerate(uniq) if k not in fixed_map}
    color_map = {**auto_map, **fixed_map}  # Modifica

    # Modifica: linea base grigia
    fig_line = px.line(df, x="Data", y="Temperatura", title="Temperatura giornaliera")
    fig_line.update_traces(line=dict(color="#7f7f7f", width=2))
    fig_line.update_xaxes(rangeslider_visible=True)

    # Modifica: marker colorati per fascia EXCEL (niente linee)
    # -> una traccia per categoria, così ottieni la legenda pulita
    import plotly.graph_objects as go
    # recupero un'etichetta "umana" per ciascuna fascia normalizzata
    label_by_norm = (df.dropna(subset=["_fascia_norm"])
                       .groupby("_fascia_norm")["FasciaTemp"].first().to_dict())

    for k in uniq:
        g = df[df["_fascia_norm"] == k]
        if g.empty:
            continue
        fig_line.add_trace(
            go.Scatter(
                x=g["Data"], y=g["Temperatura"],
                mode="markers",
                marker=dict(size=5, color=color_map.get(k, "#7f7f7f"), line=dict(width=0)),
                name=label_by_norm.get(k, k)  # legenda usa il testo Excel
            )
        )

    st.plotly_chart(fig_line, use_container_width=True)







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