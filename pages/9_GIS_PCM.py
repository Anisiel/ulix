

# ------------------------------------------------------------------------------
# 📍 Esempio GIS PCM 
# Questa pagina mostra un modulo GIS (Geographic Information System) realizzato in Python.
# Utilizza le librerie:
# - folium: per creare mappe interattive basate su Leaflet.js
# - streamlit-folium: per integrare le mappe Folium direttamente in Streamlit
# - json: per leggere dati strutturati con coordinate e attributi associati
#
# Il dataset contiene "x" sedi istituzionali fittizie legate alla Presidenza del Consiglio dei Ministri (PCM),
# con informazioni geografiche e non reali (rischio sismico, distanza da Palazzo Chigi,
# tempo di percorrenza). I dati sono visualizzati su mappa con:
# - una Heatmap che rappresenta il rischio sismico in modo continuo (effetto raster)
# - marker puntuali opzionali per popup informativi
#
# Questo modulo dimostra come Python possa essere usato per unire visualizzazione,
# analisi e narrazione spaziale in modo semplice e immediato.
# ------------------------------------------------------------------------------

import os
import json
import streamlit as st
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium

# ---------------- CONFIGURAZIONE PAGINA ----------------
st.set_page_config(page_title="PCM - Mappe Heatmap e Distanze", layout="wide")
st.title("🗺️ Esempio di GIS con dati fittizi relativi alle sedi PCM")


st.markdown("""
### 📍 Lo spiegone...

Questa pagina mostra un esempio di **GIS (Geographic Information System)** realizzato in Python.  
Un GIS consente di raccogliere, visualizzare e analizzare dati geolocalizzati—cioè legati a coordinate geografiche.  

In questo caso, utilizziamo Python per costruire una mappa interattiva delle sedi della **Presidenza del Consiglio dei Ministri (PCM)**, associando a ciascuna sede informazioni descrittive e un indice **fittizio** di **rischio sismico**.  

La mappa è composta da:
- una **Heatmap** che visualizza il rischio sismico come superficie continua (effetto raster);
    - cos'è una Heatmap?        
        - Una Heatmap è una rappresentazione grafica che mostra la distribuzione di un fenomeno continuo usando colori.
        - Nel nostro caso ogni sede ha un valore di rischio sismico (da 1 a 5). La Heatmap prende questi punti e li “sfuma”, creando macchie colorate proporzionali al rischio.
        Il risultato è simile a una mappa raster, perché vedi una superficie continua con gradiente cromatico (verde → giallo → rosso).
    - Perchè serve?
        - E' utile perchè permette di percepire immediatamente le zone più critiche (rosse) e quelle più sicure (verdi), senza dover leggere ogni singolo marker.

e da:

- una **basemap raster** (OpenStreetMap, CartoDB, Esri) per il contesto cartografico;
    - cos'è una basemap raster?
        - Una basemap raster è una mappa di sfondo composta da tasselli (tiles) già renderizzati, che forniscono il contesto geografico.
            Esempi:
            - OpenStreetMap: stradale, dettagliata.
            - CartoDB Positron: chiara, ideale per sovrapporre dati.
            - Esri World Imagery: satellitare.
    - Perché serve? 
        - La Heatmap da sola non basta: senza una ***basemap*** non sapresti collocare spazialmente i punti di maggiore interesse. 
            La basemap permette di individuare il contesto geografico e di evidenziare eventuali punti di interesse ("marker).
""")

st.markdown("""
### 🧭 La struttura dei dati

I dati sono strutturati in formato **JSON**, un linguaggio leggibile e flessibile.  
Se si parte da un file Excel o CSV, è possibile convertirlo in JSON usando strumenti online come:
- https://tableconvert.com/csv-to-json (csv) oppure https://tableconvert.com/excel-to-json (xlsx)
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


############################################################
#                       LE MAPPE
############################################################
st.header(" Le due mappe di esempio: Heatmap e Distanze")


# ---------------- CARICAMENTO DATI ----------------
json_path = os.path.join("repo", "sedi_pcm_con_distanze.json")
with open(json_path, "r", encoding="utf-8") as f:
    sedi = json.load(f)

# ---------------- MAPPA 1: HEATMAP ----------------
st.subheader("🔥 Mappa1: Heatmap del rischio sismico")
# REGOLAZIONI VISIVE
with st.expander("🎛️ Regolazioni visive Heatmap"):
    radius = st.slider("Raggio Heatmap (pixel)", 8, 60, 28, 2)
    blur = st.slider("Sfocatura Heatmap", 5, 35, 18, 1)
    min_opacity = st.slider("Opacità minima Heatmap", 0.0, 1.0, 0.35, 0.05)
    show_markers = st.checkbox("Mostra marker puntuali", value=True)

# --------------------------- MAPPA BASE ---------------------------
# Centro iniziale su Lazio/Centro Italia
m1 = folium.Map(location=[41.9, 12.5], zoom_start=10, control_scale=True)

# Basemap con attribuzioni corrette
# 1) OpenStreetMap (built-in): ha già attribution interna
folium.TileLayer('OpenStreetMap', name='OpenStreetMap').add_to(m1)

# 2) CartoDB Positron (chiara)
folium.TileLayer(
    tiles='https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png',
    name='CartoDB Positron',
    attr='&copy; OpenStreetMap contributors &copy; CARTO',
    control=True
).add_to(m1)

# 3) Esri World Imagery (satellitare)
folium.TileLayer(
    tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
    name='Esri World Imagery',
    attr='Tiles &copy; Esri — Source: Esri, Maxar, Earthstar Geographics, and the GIS User Community',
    control=True
).add_to(m1)

# Heatmap
heat_data = []
for s in sedi:
    try:
        lat = float(s["lat"])
        lon = float(s["lon"])
        peso = float(s.get("rischio_sismico", 3))
        peso = max(0.0, min(5.0, peso))
        heat_data.append([lat, lon, peso])
    except:
        continue

# Scala colori (verde → giallo → arancio → rosso)
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
    max_val=5,
    gradient=gradient,
    name="Heatmap rischio sismico"
).add_to(m1)

# --------------------------- MARKER (OPZIONALI) ---------------------------
if show_markers:
    for s in sedi:
        try:
            lat = float(s["lat"])
            lon = float(s["lon"])
            popup_html = folium.Popup(
                f"<b>{s.get('nome','(sconosciuto)')}</b><br>Rischio sismico: {s.get('rischio_sismico', 'n.d.')}",
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
            ).add_to(m1)
        except:
            continue

# --------------------------- CONTROLLI MAPPA ---------------------------
folium.LayerControl(collapsed=False).add_to(m1)

# --------------------------- RENDER ---------------------------
st_folium(m1, width=1100, height=640)

st.divider()

# ---------------- MAPPA 2: DISTANZE ----------------
st.subheader("📍 Mappa2: scala di distanza da Palazzo Chigi")
max_distanza = st.slider("🚣‍♂️ Filtro distanza massima (km)", 0.0, 10.0, 10.0, 0.5)

# Centro iniziale su Lazio/Centro Italia
m2 = folium.Map(location=[41.9, 12.5], zoom_start=10, control_scale=True)

# Crea la mappa centrata su Roma il modo più semplice
m2 = folium.Map(location=[41.9, 12.5], zoom_start=12, control_scale=True)

# Marker Palazzo Chigi
folium.CircleMarker(
    location=[41.9029, 12.4823],
    radius=10,
    color="black",
    weight=2,
    fill=True,
    fill_color="red",
    fill_opacity=1,
    popup="📍 Palazzo Chigi"
).add_to(m2)

# Funzione colore
def distanza_to_color(d):
    if d <= 1:
        return "#2ECC71"
    elif d <= 3:
        return "#F7DC6F"
    elif d <= 6:
        return "#F39C12"
    else:
        return "#E74C3C"

# --------------------------- MARKER (OPZIONALI) ---------------------------
for sede in sedi:
    distanza = sede.get("distanza_da_palazzo_chigi_km", 0)
    if distanza > max_distanza:
        continue
    lat = sede["lat"]
    lon = sede["lon"]
    colore = distanza_to_color(distanza)
    popup = folium.Popup(f"""
        <b>{sede['nome']}</b><br>
        {sede['funzione']}<br>
        Accessibilità: {sede['accessibilita']}<br>
        Allerta: {sede['livello_allerta']}<br>
        Distanza: {sede['distanza_da_palazzo_chigi_km']} km<br>
        Tempo: {sede['tempo_percorrenza_min']} min<br>
        Rischio sismico: {sede['rischio_sismico']}
    """, max_width=300)
    folium.CircleMarker(
        location=[lat, lon],
        radius=6,
        color="black",
        weight=1,
        fill=True,
        fill_color=colore,
        fill_opacity=0.8,
        popup=popup
    ).add_to(m2)

# --------------------------- CONTROLLI MAPPA ---------------------------
folium.LayerControl(collapsed=False).add_to(m2)

# --------------------------- RENDER ---------------------------
st_folium(m2, width=1100, height=640)




# ---------------- DATI IN FORMA TABELLARE----------------
with st.expander("📋 Dati completi delle sedi"):
    st.dataframe(sedi, use_container_width=True)