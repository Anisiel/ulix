import streamlit as st
import folium
from streamlit_folium import st_folium
import json
import os

st.set_page_config(page_title="Esempio GIS PCM", layout="wide")


# ------------------------------------------------------------------------------
# 📍 Esempio GIS PCM 
# Questa pagina mostra un modulo GIS (Geographic Information System) realizzato in Python.
# Utilizza le librerie:
# - folium: per creare mappe interattive basate su Leaflet.js
# - streamlit-folium: per integrare le mappe Folium direttamente in Streamlit
# - json: per leggere dati strutturati con coordinate e attributi associati
#
# Il dataset contiene 10 sedi istituzionali legate alla Presidenza del Consiglio dei Ministri (PCM),
# con informazioni geografiche, funzionali e fittizie (livello di allerta, distanza da Palazzo Chigi,
# tempo di percorrenza). I dati sono visualizzati su mappa con marker colorati in base al livello di allerta.
#
# Questo modulo dimostra come Python possa essere usato per unire visualizzazione, analisi e narrazione spaziale.
# ------------------------------------------------------------------------------


st.markdown("""
### 📍 Mappa delle sedi PCM

Questa pagina mostra un esempio di **GIS (Geographic Information System)** realizzato in Python.  
Un GIS consente di raccogliere, visualizzare e analizzare dati geolocalizzati—cioè legati a coordinate geografiche.  
In questo caso, utilizziamo Python per costruire una mappa interattiva delle sedi della **Presidenza del Consiglio dei Ministri (PCM)**, associando a ciascuna sede informazioni descrittive e numeriche.

I dati sono strutturati in formato **JSON**, un linguaggio leggibile e flessibile.  
Se si parte da un file Excel o CSV, è possibile convertirlo in JSON usando strumenti online come:
- [ConvertCSV](https://www.convertcsv.com/csv-to-json.htm)
- [TableConvert](https://tableconvert.com/excel-to-json)
- [CSVJSON](https://csvjson.com/csv2json)

Il dataset include anche:
- `livello_allerta`: indice fittizio di criticità (da 1 a 5).
- `distanza_da_palazzo_chigi_km`: distanza approssimativa in linea d’aria.
- `tempo_percorrenza_min`: tempo stimato di percorrenza.

Questi dati permettono di costruire mappe tematiche, filtri dinamici e visualizzazioni narrative che uniscono geografia, funzione e tensione operativa.
""")

st.markdown("""
### 🧭 Le librerie spaziali in Python

Python offre un ecosistema ricco per l'analisi e la visualizzazione di dati geospaziali.  
Tra le librerie più utilizzate troviamo **GeoPandas** per la manipolazione di geometrie e shapefile, **Shapely** per operazioni spaziali, **PyDeck** per visualizzazioni 3D, e **Folium** per mappe interattive basate su Leaflet.js.  
Questi strumenti permettono di unire analisi tecnica, visualizzazione e narrazione spaziale in modo accessibile e potente.

### 🗺️ Folium: mappe interattive con semplicità

Nel progetto attuale utilizziamo **Folium**, una libreria Python che consente di creare mappe interattive con pochi comandi.  
Folium si basa su Leaflet.js e permette di aggiungere marker, popup, layer tematici e stili personalizzati.  
Grazie all'integrazione con Streamlit tramite `streamlit-folium`, possiamo visualizzare direttamente le mappe nel sito, rendendo l'esperienza fluida e dinamica.
""")

# Percorso al file JSON
json_path = os.path.join("repo", "sedi_pcm.json")

# Carica dati
with open(json_path, "r", encoding="utf-8") as f:
    sedi = json.load(f)

# Crea mappa
mappa = folium.Map(location=[41.5000, 13.0000], zoom_start=8)

# Colori per livello allerta
colori = {1: "verde", 2: "verde chiaro", 3: "giallo", 4: "arancione", 5: "rosso"}

# Aggiungi marker
for sede in sedi:
    popup = f"""
    <b>{sede['nome']}</b><br>
    {sede['funzione']}<br>
    Accessibilità: {sede['accessibilita']}<br>
    Allerta: {sede['livello_allerta']}<br>
    Distanza: {sede['distanza_da_palazzo_chigi_km']} km<br>
    Tempo: {sede['tempo_percorrenza_min']} min<br>
    Note: {sede['note']}
    """
    folium.CircleMarker(
        location=[sede["lat"], sede["lon"]],
        radius=6,
        color=colori.get(sede["livello_allerta"], "gray"),
        fill=True,
        fill_opacity=0.7,
        popup=popup
    ).add_to(mappa)

# Mostra mappa
st_folium(mappa, width=900)




