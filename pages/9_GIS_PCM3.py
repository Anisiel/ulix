
import json
import folium
import streamlit as st
from streamlit_folium import st_folium

st.set_page_config(page_title="Mappa PCM - Distanze", layout="wide")
st.title("\U0001F4CD Mappa delle sedi PCM con scala di distanza")

# Carica i dati dal file JSON
with open("repo/sedi_pcm_con_distanze.json", "r", encoding="utf-8") as f:
    sedi = json.load(f)

# Funzione per convertire distanza in colore (verde -> rosso)
def distanza_to_color(d):
    if d <= 1:
        return "#2ECC71"  # verde
    elif d <= 3:
        return "#F7DC6F"  # giallo
    elif d <= 6:
        return "#F39C12"  # arancio
    else:
        return "#E74C3C"  # rosso

# Slider per filtrare le sedi per distanza
max_distanza = st.slider("\U0001F6E3️ Filtro distanza massima esclude le sedi sopra tot km", 0.0, 10.0, 10.0, 0.5)

# Crea la mappa centrata su Roma
m = folium.Map(location=[41.9, 12.5], zoom_start=12, control_scale=True)

# Aggiungi i marker con colore basato sulla distanza
for sede in sedi:
    
    distanza = sede.get("distanza_da_palazzo_chigi_km", 0)
    if distanza > max_distanza:
        continue

    lat = sede["lat"]
    lon = sede["lon"]
    nome = sede["nome"]
    colore = distanza_to_color(distanza)

# Marker speciale per Palazzo Chigi
folium.CircleMarker(
    location=[41.9029, 12.4823],
    radius=10,
    color="black",
    weight=2,
    fill=True,
    fill_color="red",
    fill_opacity=1,
    popup="📍 Palazzo Chigi"
).add_to(m)

# Marker colorati per le sedi
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
    ).add_to(m)




# Mostra la mappa in Streamlit
st_folium(m, width=1100, height=640)

# Espandi per visualizzare i dati
with st.expander("\U0001F4CB Vedi dati delle sedi visualizzate"):
    st.dataframe([s for s in sedi if s["distanza_da_palazzo_chigi_km"] <= max_distanza], use_container_width=True) 

st.markdown("""
*\*Legenda colori\**:
- Verde: distanza ≤ 1 km
- Giallo: distanza ≤ 3 km
- Arancio: distanza ≤ 6 km
- Rosso: distanza > 6 km
""")
