# pages/02_Grafici_Altair_ECharts.py
# ==================================
# Seconda pagina: due grafici con due librerie diverse:
#  - ALTair: Linea Temperatura + Punti Pioggia con doppio asse e selezione intervallo (overview+detail)
#  - pyecharts: Calendar heatmap dei mm/giorno su un anno
# ----------------------------------
# Dipendenze: streamlit, pandas, altair, pyecharts, streamlit-echarts5, openpyxl




import os
import streamlit as st
import pandas as pd
import altair as alt
from pyecharts.charts import Calendar
from pyecharts import options as opts
from streamlit_echarts5 import st_pyecharts  # componente Streamlit ↔ ECharts

st.markdown("""
Questa pagina mostra grafici che **Excel non realizza nativamente** (o solo con workaround complicati tipo duplicare dati, formattazioni complesse, macro Vba),
mettendo in evidenza due librerie che permettono di creare grafici dinamici (Altair e ECharts).
I grafici sono identici a quelli realizzati con Plotly, permettendo cosi di confrontare le librerie.
Clicca qui per visualizzare la prima pagina: [Grafici di Plotly](pages/1_Grafici_plotly.py).

Tutti grafici sono realizzati a partire da dati presenti su un file excel caricato in `repo/grafici_speciali.xlsx`. 
            Colonne native: **Data**, **Temperatura**, **Pioggia_mm**. Colonne calcolate: **FasciaTemp** e **ClassePioggia**.
""")

# ---------- [STEP 1] Config pagina ----------
st.set_page_config(page_title="Altair + ECharts", page_icon="📊", layout="wide")
st.title("📊 Grafici speciali con Altair + ECharts")

# ---------- [STEP 2] Caricamento dati da Excel ----------
# Usa lo stesso file della pagina Plotly; prova prima il path "repo/", poi locale
FILE_CANDIDATES = ["repo/grafici_speciali.xlsx", "grafici_speciali.xlsx"]
file_path = next((p for p in FILE_CANDIDATES if os.path.exists(p)), FILE_CANDIDATES[0])

df = pd.read_excel(file_path, engine="openpyxl")
df["Data"] = pd.to_datetime(df["Data"])
st.success(f"Dati caricati: {len(df)} righe da `{file_path}`")
st.dataframe(df.head(), use_container_width=True)

st.divider()

# =========================================================
# GRAFICO A) ALTair — Linea Temperatura + Punti Pioggia
#  - Obiettivo: mostrare Temperatura nel tempo (linea) e i giorni di pioggia (punti)
#  - Extra: doppio asse Y (indipendente) e selezione intervallo con riquadro di overview
#  - Altair: layering + resolve_scale(y='independent') + selection interval
#    Riferimenti:
#       - Assi indipendenti (dual axis via layer): altair user guide  ➜ vedi cite
#       - Selezioni/brush: Altair selections notebook                ➜ vedi cite
# =========================================================

st.subheader("A) Altair — Linea (Temperatura) + Punti (Pioggia)")
# [A1] Prepara subset per i soli giorni con pioggia > 0 (punti verdi)
rain = df[df["Pioggia_mm"] > 0].copy()

# [A2] Definisci selezione intervallo sull'asse X (tempo)
brush = alt.selection_interval(encodings=["x"])  # l'utente trascina per filtrare il pannello sopra

# [A3] Base temporale
base = alt.Chart(df).encode(x=alt.X("Data:T", title="Data"))

# [A4] Linea temperatura (asse Y sinistro)
line = base.mark_line(color="#1f77b4").encode(
    y=alt.Y("Temperatura:Q", title="Temperatura [°C]"),
    tooltip=["yearmonthdate(Data):T", "Temperatura:Q"]
)

# [A5] Punti pioggia (asse Y destro, indipendente)
pts = alt.Chart(rain).mark_point(size=50, color="#2ca02c", opacity=0.9).encode(
    x="Data:T",
    y=alt.Y("Pioggia_mm:Q", title="Pioggia [mm]"),
    tooltip=["yearmonthdate(Data):T", "Pioggia_mm:Q"]
)

# [A6] Componi "pannello superiore": applica il filtro della selezione e usa assi Y indipendenti
upper = (alt.layer(line, pts)
         .transform_filter(brush)
         .resolve_scale(y='independent')  # <<< doppio asse (sinistra=°C, destra=mm)
         .properties(height=280))

# [A7] "pannello inferiore" (overview): piccola area su temperatura per selezionare l’intervallo
lower = (base.mark_area(color="#c7c7c7")
         .encode(y=alt.Y("Temperatura:Q", title=None))
         .add_params(brush)
         .properties(height=60))

# [A8] Metti insieme (overview + dettaglio)
altair_chart = alt.vconcat(upper, lower).resolve_scale(x='shared')

st.altair_chart(altair_chart, use_container_width=True)

st.caption(
    "Altair consente assi indipendenti in grafici sovrapposti e selezioni (brush) "
    "per filtrare dinamicamente il pannello principale. "
    "Vedi doc su `resolve_scale` e selezioni Altair."
)

st.divider()

# =========================================================
# GRAFICO B) pyecharts — Calendar Heatmap dei mm/giorno
#  - Obiettivo: visualizzare i mm di pioggia per ogni giorno su un calendario annuale
#  - pyecharts ha un tipo 'Calendar' pronto all'uso; Streamlit ↔ ECharts con streamlit-echarts5
#    Riferimenti: galleria pyecharts e componente Streamlit             ➜ vedi cite
# =========================================================

st.subheader("B) ECharts (pyecharts) — Calendar heatmap della pioggia")

# [B1] Seleziona l'anno da mostrare (se i dati coprono più anni)
years = sorted(df["Data"].dt.year.unique())
year = st.selectbox("Scegli anno", years, index=0)

# [B2] Prepara i dati (lista di [data_str, valore]) per il calendario dell'anno scelto
df_y = (df[df["Data"].dt.year == year]
        .assign(day=lambda d: d["Data"].dt.strftime("%Y-%m-%d")))
data_calendar = df_y.groupby("day")["Pioggia_mm"].sum().reset_index().values.tolist()

# [B3] Costruisci il calendario con pyecharts
cal = (
    Calendar(init_opts=opts.InitOpts(width="1000px", height="320px"))
    .add("", data_calendar, calendar_opts=opts.CalendarOpts(range_=str(year)))
    .set_global_opts(
        title_opts=opts.TitleOpts(title=f"Pioggia giornaliera — {year}"),
        visualmap_opts=opts.VisualMapOpts(  # scala colori continua basata sui mm
            max_=float(df_y["Pioggia_mm"].max() or 0.0), is_piecewise=False
        ),
        tooltip_opts=opts.TooltipOpts(formatter="{c} mm"),
    )
)

# [B4] Render in Streamlit (component)
st_pyecharts(cal, height="340px")

st.caption(
    "Il calendario heatmap di ECharts/pyecharts è un grafico non nativo in Excel; "
    "il componente `streamlit-echarts5` lo integra in Streamlit."
)