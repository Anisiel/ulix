# pages/01_Grafici_Plotly.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Grafici Plotly (non-Excel)", page_icon="🔷", layout="wide")
st.title("🔷 Grafici Plotly – oltre i limiti dei grafici Excel")

# --- Spiegazione iniziale -----------------------------------------------------
st.markdown("""
**Perché questi grafici qui e non in Excel?**
- **Rosa polare (barre polari)**: Excel non ha un grafico *bar‑polar* nativo; si simula con Radar e molte formattazioni, ma non è interattivo come qui.
- **Heatmap di densità 2D**: istogramma bidimensionale (bin automatici sulle due variabili) con scala colore e tooltip.
- **Superficie 3D interattiva**: rotazione/zoom/hover direttamente nel browser; l’esperienza 3D nel web per Excel è limitata.

<small>Fonti: [Tipi di grafici Excel](https://support.microsoft.com/en-us/office/available-chart-types-in-office-a6187218-807e-4103-9e0a-27cdb19afb90) ·
[Density heatmap Plotly](https://plotly.com/python-api-reference/generated/plotly.express.density_heatmap.html) ·
[3D Surface Plotly](https://plotly.com/python/3d-surface-plots/)</small>
""")

# --- Dati: tabella in testa (come richiesto) ---------------------------------
fp = "repo/grafici_speciali.xlsx"
df = pd.read_excel(fp)
df["Data"] = pd.to_datetime(df["Data"])

st.success(f"Dati caricati: {len(df)} righe  |  intervallo: {df['Data'].min().date()} → {df['Data'].max().date()}")
st.dataframe(df.head(20), use_container_width=True)

# ======================================================================================
# 1) HEATMAP DI DENSITÀ 2D (Temperatura vs Pioggia) – con controlli per renderla chiara
# ======================================================================================
st.subheader("1) Heatmap di densità 2D – Temperatura vs Pioggia")
st.caption("È un **istogramma 2D**: conta quanti giorni cadono in ciascun riquadro (Temperatura, Pioggia) e colora in base alla concentrazione.")

colA, colB, colC = st.columns([1,1,1])
nbx = colA.slider("N. bin su Temperatura (asse X)", 10, 100, 40, 5)
nby = colB.slider("N. bin su Pioggia (asse Y)", 10, 100, 40, 5)
rain_only = colC.checkbox("Solo giorni piovosi (> 0 mm)", True)

colD, colE = st.columns([1,2])
log_y = colD.checkbox("Scala log su Pioggia", True)
cmap = colE.selectbox("Palette colori", ["Viridis", "Plasma", "Turbo", "Cividis", "Magma"], index=0)

df_heat = df.copy()
if rain_only:
    df_heat = df_heat[df_heat["Pioggia_mm"] > 0]

fig_heat = px.density_heatmap(
    df_heat,
    x="Temperatura", y="Pioggia_mm",
    nbinsx=nbx, nbinsy=nby,
    color_continuous_scale=cmap,
    histfunc="count",
    labels={"Temperatura": "Temperatura [°C]", "Pioggia_mm": "Pioggia (mm)"},
    title="Densità dei giorni per coppia (Temperatura, Pioggia)"
)
if log_y:
    fig_heat.update_yaxes(type="log")

fig_heat.update_layout(coloraxis_colorbar_title="Conteggio")
st.plotly_chart(fig_heat, use_container_width=True)

with st.expander("ℹ️ Come leggere questa heatmap"):
    st.markdown("""
- **Cos’è**: una **mappa di densità** (o *2D histogram*). Divide il piano Temperatura‑Pioggia in **riquadri** (bin) e **conteggia** quanti giorni cadono in ogni riquadro. Il **colore** indica quanti sono (più scuro ⇒ più giorni).  
- **Perché la scala log su Pioggia?** Perché la pioggia è spesso **0 mm**: usando la scala log e/o filtrando “solo giorni piovosi” si separano meglio i valori piccoli da quelli grandi.  
- **Cosa capisco**: in quali **intervalli di temperatura** si concentrano i giorni **piovosi** e con quali **intensità**; puoi confrontare stagioni (filtrando per mesi, se vuoi estendere il codice).
- **Excel**: non dispone di un grafico **interattivo** equivalente fra i tipi standard; si può imitare con tabelle e formattazioni, ma senza hover/zoom nativi.  
  *Rif.*: Tipi di grafici disponibili in Office · API Plotly per density heatmap.  
""")

# ============================================================
# 2) ROSA POLARE DELLA PIOGGIA (barre polari) – non nativo in Excel
# ============================================================
st.subheader("2) Rosa polare della pioggia (mensile)")
st.caption("Somma mensile dei mm su coordinate polari (grafico non nativo in Excel).")

mappa_mesi = {i+1: m for i, m in enumerate(["Gen","Feb","Mar","Apr","Mag","Giu","Lug","Ago","Set","Ott","Nov","Dic"])}
g = (df.assign(Mese=df["Data"].dt.month)
       .groupby("Mese", as_index=False)["Pioggia_mm"].sum())
g["Mese"] = g["Mese"].map(mappa_mesi)

fig_polar = px.bar_polar(
    g, r="Pioggia_mm", theta="Mese",
    color="Pioggia_mm", color_continuous_scale="Blues",
    title="Pioggia totale per mese (rosa polare)"
)
fig_polar.update_layout(polar=dict(radialaxis=dict(showticklabels=True)))
st.plotly_chart(fig_polar, use_container_width=True)

# ============================================================
# 3) SUPERFICIE 3D INTERATTIVA (Calendario: Mese × Giorno)
# ============================================================
st.subheader("3) Superficie 3D – Temperatura media per Mese × Giorno")
st.caption("Griglia Mese × Giorno con temperatura media; rotazione/zoom/hover nel browser.")

df_cal = df.copy()
df_cal["Mese"] = df_cal["Data"].dt.month
df_cal["Giorno"] = df_cal["Data"].dt.day
z_pivot = df_cal.pivot_table(index="Mese", columns="Giorno", values="Temperatura", aggfunc="mean")
z = z_pivot.to_numpy()

fig_surf = go.Figure(data=go.Surface(
    z=z, x=z_pivot.columns.values, y=z_pivot.index.values, colorscale="RdBu_r"
))
fig_surf.update_layout(
    scene=dict(
        xaxis_title="Giorno del mese",
        yaxis_title="Mese",
        zaxis_title="T media [°C]"
    ),
    height=560,
    margin=dict(l=0, r=0, t=40, b=0),
    title="Superficie 3D (calendario): Mese × Giorno → Temperatura media"
)
st.plotly_chart(fig_surf, use_container_width=True)