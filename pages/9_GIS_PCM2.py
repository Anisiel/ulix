

# ------------------------------------------------------------------------------
# 📍 Esempio GIS PCM 
# Questa pagina mostra un modulo GIS (Geographic Information System) realizzato in Python.
# Utilizza le librerie:
# - folium: per creare mappe interattive basate su Leaflet.js
# - streamlit-folium: per integrare le mappe Folium direttamente in Streamlit
# - json: per leggere dati strutturati con coordinate e attributi associati
#
# Il dataset contiene 10 sedi istituzionali legate alla Presidenza del Consiglio dei Ministri (PCM),
# con informazioni geografiche e fittizie (rischio sismico, distanza da Palazzo Chigi,
# tempo di percorrenza). I dati sono visualizzati su mappa con:
# - una **Heatmap** che rappresenta il rischio sismico in modo continuo (effetto raster)
# - marker puntuali opzionali per popup informativi
#
# Questo modulo dimostra come Python possa essere usato per unire visualizzazione,
# analisi e narrazione spaziale in modo semplice e immediato.
# ------------------------------------------------------------------------------



# =============================================================================
# 📌 Streamlit + Folium Heatmap (raster-like) sulle sedi PCM
# Fix: rimosso "Stamen Terrain" (causava "Custom tiles must have an attribution")
#      e sostituito con basemap sicure (OSM, CartoDB Positron, Esri World Imagery)
#
# Dipendenze:
#   pip install streamlit folium streamlit-folium
# Esecuzione:
#   streamlit run questo_file.py
# Dati:
#   repo/sedi_pcm.json con chiavi minime: nome, lat, lon
#   e campo numerico: rischio_sismico (1..5) per la Heatmap.
# =============================================================================

import os
import json
import streamlit as st
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium

# --------------------------- PAGE CONFIG ---------------------------
st.set_page_config(page_title="PCM - Mappa raster-like (Heatmap)", layout="wide")

st.title("🗺️ PCM — Mappa raster‑like (Heatmap) da dati JSON")
st.markdown(
    """
Questa pagina mostra una **mappa con effetto raster** (Heatmap) creata a partire dai punti nel JSON.
- Il **calore** deriva da **`rischio_sismico`** (scala 1–5).
- Sotto c’è una **basemap raster** (tile XYZ) con **attribuzioni corrette**.
- I **marker** (opzionali) mostrano popup/tooltip informativi.
"""
)

st.markdown("""
### 📍 Mappa delle sedi PCM

Questa pagina mostra un esempio di **GIS (Geographic Information System)** realizzato in Python.  
Un GIS consente di raccogliere, visualizzare e analizzare dati geolocalizzati—cioè legati a coordinate geografiche.  

In questo caso, utilizziamo Python per costruire una mappa interattiva delle sedi della **Presidenza del Consiglio dei Ministri (PCM)**, associando a ciascuna sede informazioni descrittive e un indice fittizio di **rischio sismico**.  

La mappa è composta da:
- una **Heatmap** che visualizza il rischio sismico come superficie continua (effetto raster);
- una **basemap raster** (OpenStreetMap, CartoDB, Esri) per il contesto cartografico;
- marker puntuali opzionali con popup informativi.

I dati sono strutturati in formato **JSON**, un linguaggio leggibile e flessibile.  
Se si parte da un file Excel o CSV, è possibile convertirlo in JSON usando strumenti online come:
- [ConvertCSV](https://www.convertcsvson.htm
- https://tableconvert.com/excel-to-json
- https://csvjson.com/csv2json

Il dataset include anche:
- `rischio_sismico`: indice fittizio di pericolosità (da 1 a 5);
- `distanza_da_palazzo_chigi_km`: distanza approssimativa in linea d’aria;
- `tempo_percorrenza_min`: tempo stimato di percorrenza.

Questi dati permettono di costruire mappe tematiche e visualizzazioni narrative che uniscono geografia e analisi.
""")

st.markdown("""
### 🧭 Le librerie spaziali in Python

Python offre un ecosistema ricco per l'analisi e la visualizzazione di dati geospaziali.  
Tra le librerie più utilizzate troviamo **GeoPandas** per la manipolazione di geometrie e shapefile, **Shapely** per operazioni spaziali, **PyDeck** per visualizzazioni 3D, e **Folium** per mappe interattive basate su Leaflet.js.  

Nel progetto attuale utilizziamo **Folium**, una libreria Python che consente di creare mappe interattive con pochi comandi.  
Folium si basa su Leaflet.js e permette di aggiungere:
- **Heatmap** per rappresentare fenomeni continui (effetto raster);
- marker, popup e layer tematici;
- basemap raster da provider affidabili (OSM, CartoDB, Esri).

Grazie all'integrazione con Streamlit tramite `streamlit-folium`, possiamo visualizzare direttamente le mappe nel sito, rendendo l'esperienza fluida e dinamica.
""")


# --------------------------- CARICAMENTO DATI ---------------------------
json_path = os.path.join("repo", "sedi_pcm.json")
if not os.path.exists(json_path):
    st.error(
        f"❌ File non trovato: `{json_path}`.\n"
        "Crea la cartella `repo` accanto a questo script e inserisci `sedi_pcm.json`."
    )
    st.stop()

try:
    with open(json_path, "r", encoding="utf-8") as f:
        sedi = json.load(f)
except Exception as e:
    st.error(f"❌ Errore nel parsing del JSON: {e}")
    st.stop()

required_keys = {"nome", "lat", "lon"}
bad = [i for i, s in enumerate(sedi) if not required_keys.issubset(s.keys())]
if bad:
    st.warning(f"⚠️ Righe prive delle chiavi minime {required_keys}: {bad[:8]}{' ...' if len(bad) > 8 else ''}")

# --------------------------- REGOLAZIONI VISIVE ---------------------------
with st.expander("🎚️ Regolazioni visive (opzionali)"):
    radius = st.slider("Raggio Heatmap (pixel)", 8, 60, 28, 2)
    blur = st.slider("Sfocatura Heatmap", 5, 35, 18, 1)
    min_opacity = st.slider("Opacità minima Heatmap", 0.0, 1.0, 0.35, 0.05)
    show_markers = st.checkbox("Mostra marker puntuali", value=True)

# --------------------------- MAPPA BASE ---------------------------
# Centro iniziale su Lazio/Centro Italia
m = folium.Map(location=[41.9, 12.5], zoom_start=7, control_scale=True)

# ✅ Basemap con attribuzioni corrette

# 1) OpenStreetMap (built-in): ha già attribution interna
folium.TileLayer('OpenStreetMap', name='OpenStreetMap').add_to(m)

# 2) CartoDB Positron (chiara)
folium.TileLayer(
    tiles='https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png',
    name='CartoDB Positron',
    attr='&copy; OpenStreetMap contributors &copy; CARTO',
    control=True
).add_to(m)

# 3) Esri World Imagery (satellitare)
folium.TileLayer(
    tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
    name='Esri World Imagery',
    attr='Tiles &copy; Esri — Source: Esri, Maxar, Earthstar Geographics, and the GIS User Community',
    control=True
).add_to(m)

# ⛔️ RIMOSSO:
# folium.TileLayer('Stamen Terrain', name='Terreno').add_to(m)
# Motivo: in molte installazioni non è un provider riconosciuto e viene trattato come "custom" senza attr → ValueError.

# --------------------------- PREPARAZIONE HEATMAP ---------------------------
heat_data = []
skipped = 0

for s in sedi:
    try:
        lat = float(s["lat"])
        lon = float(s["lon"])
    except Exception:
        skipped += 1
        continue

    # peso = rischio_sismico (default 3 se assente)
    rs = s.get("rischio_sismico", 3)
    try:
        peso = float(rs)
    except Exception:
        peso = 3.0

    # Mantieni il range sensato 0..5
    peso = max(0.0, min(5.0, peso))
    heat_data.append([lat, lon, peso])

if not heat_data:
    st.error("❌ Nessun dato valido per la Heatmap. Controlla lat/lon nel JSON.")
    st.stop()

if skipped > 0:
    st.info(f"ℹ️ Righe ignorate per coordinate non valide: {skipped}")

# Gradient (verde → giallo → arancio → rosso)
gradient = {
    0.00: '#2ECC71',
    0.40: '#F7DC6F',
    0.70: '#F39C12',
    1.00: '#E74C3C'
}

# --------------------------- HEATMAP (EFFETTO RASTER) ---------------------------
HeatMap(
    data=heat_data,
    radius=radius,
    blur=blur,
    max_zoom=10,
    min_opacity=min_opacity,
    max_val=5,                 # coerente con 1..5
    gradient=gradient,
    name="Heatmap rischio sismico"
).add_to(m)

# --------------------------- MARKER (OPZIONALI) ---------------------------
if show_markers:
    for s in sedi:
        try:
            lat = float(s["lat"])
            lon = float(s["lon"])
        except Exception:
            continue

        popup_html = folium.Popup(
            f"<b>{s.get('nome','(sconosciuto)')}</b><br>"
            f"Rischio sismico: {s.get('rischio_sismico', 'n.d.')}",
            max_width=260
        )

        folium.CircleMarker(
            location=[lat, lon],
            radius=5,
            color="black",
            weight=1,
            fill=True,
            fill_color="#ffffff",
            fill_opacity=0.7,
            tooltip=s.get("nome", ""),
            popup=popup_html
        ).add_to(m)

# --------------------------- CONTROLLI MAPPA ---------------------------
folium.LayerControl(collapsed=False).add_to(m)

# --------------------------- RENDER ---------------------------
st_folium(m, width=1100, height=640)

# --------------------------- TABELLA DATI ---------------------------
with st.expander("📋 Vedi dati caricati"):
    st.dataframe(sedi, use_container_width=True)