import json
import folium
from folium import Map, CircleMarker
import json
import os

# Costruisce il percorso al file JSON contenente le sedi PCM
json_path = os.path.join("repo", "sedi_pcm_con_distanze.json")

# Carica i dati dal file JSON
with open("sedi_pcm_con_distanze.json", "r", encoding="utf-8") as f:
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

# Crea la mappa centrata su Roma
m = Map(location=[41.9, 12.5], zoom_start=12)

# Aggiungi i marker con colore basato sulla distanza
for sede in sedi:
    lat = sede["lat"]
    lon = sede["lon"]
    nome = sede["nome"]
    distanza = sede.get("distanza_da_palazzo_chigi_km", 0)
    colore = distanza_to_color(distanza)

    popup_text = f"<b>{nome}</b><br>Distanza: {distanza} km"
    CircleMarker(
        location=[lat, lon],
        radius=7,
        color="black",
        weight=1,
        fill=True,
        fill_color=colore,
        fill_opacity=0.8,
        popup=folium.Popup(popup_text, max_width=250)
    ).add_to(m)

# Salva la mappa in HTML
m.save("mappa_distanze_pcm.html")
