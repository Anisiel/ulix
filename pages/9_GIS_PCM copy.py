# Importa le librerie necessarie
import streamlit as st
import folium
from folium import FeatureGroup, LayerControl
from folium.plugins import Search
from streamlit_folium import st_folium
import json
import os

# Imposta il titolo della pagina e il layout largo
st.set_page_config(page_title="Esempio GIS PCM", layout="wide")

# ------------------------------------------------------------------------------
# 📍 Esempio GIS PCM 
# Questa pagina mostra un modulo GIS realizzato in Python (Folium + Streamlit).
# ------------------------------------------------------------------------------

st.markdown("""
### 📍 Mappa delle sedi PCM
... (testo introduttivo invariato) ...
""")

st.markdown("""
### 🧭 Le librerie spaziali in Python
... (testo introduttivo invariato) ...
""")

# --------------------------- CARICAMENTO DATI ---------------------------
json_path = os.path.join("repo", "sedi_pcm.json")
with open(json_path, "r", encoding="utf-8") as f:
    sedi = json.load(f)

# --------------------------- COLORI & UTILS ---------------------------
colori_allerta = {
    1: "#2ECC71",  # verde
    2: "#A9DFBF",  # verde chiaro
    3: "#F7DC6F",  # giallo
    4: "#F39C12",  # arancione
    5: "#E74C3C"   # rosso
}

def colore_distanza_km(d):
    """Restituisce un colore in base alla distanza (stessa logica che usavi coi pulsanti)."""
    if d < 5:
        return "#3498DB"  # blu
    elif d < 15:
        return "#1ABC9C"  # verde acqua
    else:
        return "#9B59B6"  # viola

# --------------------------- MENU (SE DESIDERI) ---------------------------
# ✅ MODIFICA: puoi mantenere il selectbox per evidenziare una sede con il marker blu.
#    Se invece vuoi TUTTO dentro mappa, commenta le due righe seguenti.
nomi_sedi = [s["nome"] for s in sedi]
sede_selezionata = st.selectbox("Seleziona una sede da evidenziare (marker blu):", nomi_sedi)

# 🔁 SOSTITUISCE i pulsanti esterni:
# tema_distanza = st.button("Visualizza mappa per distanza da Palazzo Chigi")
# tema_allerta = st.button("Visualizza mappa per livello di allerta")
# Con LayerControl e due FeatureGroup dentro mappa (vedi sotto).

# --------------------------- CREAZIONE MAPPA ---------------------------
mappa = folium.Map(location=[41.5000, 13.0000], zoom_start=8)

# --------------------------- FEATURE GROUPS (MENÙ DENTRO MAPPA) ---------------------------
# ✅ MODIFICA: creiamo 3 layer:
# 1) "Sedi - Allerta" (colore per livello_allerta)
# 2) "Sedi - Distanza" (colore per distanza)
# 3) "Sede selezionata" (marker blu opzionale)
fg_allerta = FeatureGroup(name="Sedi - Allerta", overlay=True, show=True)
fg_distanza = FeatureGroup(name="Sedi - Distanza", overlay=True, show=False)
fg_selezionata = FeatureGroup(name="Sede selezionata", overlay=True, show=True)

# Lista di Feature per GeoJSON (serve al Search)
features_geojson = []

# --------------------------- AGGIUNTA MARKER ---------------------------
for sede in sedi:
    # Popup HTML
    popup_html = folium.Popup(f"""
    <b>{sede['nome']}</b><br>
    {sede['funzione']}<br>
    Accessibilità: {sede['accessibilita']}<br>
    Allerta: {sede['livello_allerta']}<br>
    Distanza: {sede['distanza_da_palazzo_chigi_km']} km<br>
    Tempo: {sede['tempo_percorrenza_min']} min<br>
    Note: {sede['note']}
    """, max_width=300)

    # Marker per layer "Allerta"
    folium.CircleMarker(
        location=[sede["lat"], sede["lon"]],
        radius=7,
        color="black",
        weight=1,
        fill=True,
        fill_color=colori_allerta.get(sede["livello_allerta"], "gray"),
        fill_opacity=0.9,
        popup=popup_html,
        tooltip=f"{sede['nome']} • Allerta {sede['livello_allerta']}"
    ).add_to(fg_allerta)

    # Marker per layer "Distanza"
    folium.CircleMarker(
        location=[sede["lat"], sede["lon"]],
        radius=7,
        color="black",
        weight=1,
        fill=True,
        fill_color=colore_distanza_km(sede["distanza_da_palazzo_chigi_km"]),
        fill_opacity=0.9,
        popup=popup_html,
        tooltip=f"{sede['nome']} • {sede['distanza_da_palazzo_chigi_km']} km"
    ).add_to(fg_distanza)

    # Costruiamo anche la Feature per GeoJSON (ricerca per nome)
    features_geojson.append({
        "type": "Feature",
        "properties": {
            "nome": sede["nome"],
            "funzione": sede["funzione"]
        },
        "geometry": {
            "type": "Point",
            "coordinates": [sede["lon"], sede["lat"]]
        }
    })

# --------------------------- MARKER SEDE SELEZIONATA ---------------------------
# ✅ MODIFICA: evidenziamo la sede selezionata (se hai mantenuto il selectbox)
sede_info = next((s for s in sedi if s["nome"] == sede_selezionata), None)
if sede_info:
    folium.Marker(
        location=[sede_info["lat"], sede_info["lon"]],
        popup=f"<b>{sede_info['nome']}</b>",
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(fg_selezionata)

# Aggiungiamo i layer alla mappa
fg_allerta.add_to(mappa)
fg_distanza.add_to(mappa)
fg_selezionata.add_to(mappa)

# --------------------------- RICERCA DENTRO MAPPA ---------------------------
# ✅ MODIFICA: aggiungiamo un Search box sulla mappa (cerca per "nome")
geojson_data = {
    "type": "FeatureCollection",
    "features": features_geojson
}

# Creiamo un layer GeoJson (non visibile come layer singolo, ma utilizzato da Search)
geojson_layer = folium.GeoJson(
    geojson_data,
    name="Indice sedi (ricerca)",
    tooltip=folium.GeoJsonTooltip(fields=["nome", "funzione"], aliases=["Nome:", "Funzione:"])
).add_to(mappa)

# Search per proprietà 'nome'
Search(
    layer=geojson_layer,
    geom_type='Point',
    search_label='nome',
    placeholder='Cerca sede…',
    collapsed=False,        # se True, diventa una lente che si espande al click
    position='topleft'
).add_to(mappa)

# --------------------------- CONTROLLI MAPPA ---------------------------
# ✅ MODIFICA: menù LayerControl dentro mappa
LayerControl(position='topright', collapsed=False).add_to(mappa)

# (Opzionale) altri controlli utili:
# from folium.plugins import Fullscreen, MeasureControl
# Fullscreen(position='topleft').add_to(mappa)
# MeasureControl(position='topleft', primary_length_unit='kilometers').add_to(mappa)

# --------------------------- VISUALIZZAZIONE MAPPA ---------------------------
st.markdown("### 🗺️ Mappa interattiva delle sedi PCM")
st_folium(mappa, width=1000, height=600)

# --------------------------- VISUALIZZAZIONE TABELLA ---------------------------
st.markdown("""
            ### 📋 Tabella delle sedi PCM
            ###### ***scorrere verso destra per visualizzare tutte le colonne***
             """)
st.dataframe(sedi)
