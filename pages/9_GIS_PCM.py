# Importa le librerie necessarie
import streamlit as st
import folium
from streamlit_folium import st_folium
import json
import os

# Imposta il titolo della pagina e il layout largo
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


# --------------------------- CARICAMENTO DATI ---------------------------
# Costruisce il percorso al file JSON contenente le sedi PCM
json_path = os.path.join("repo", "sedi_pcm.json")

# Apre e carica il file JSON
with open(json_path, "r", encoding="utf-8") as f:
    sedi = json.load(f)

# --------------------------- MENU A TENDINA ---------------------------
# ✅ MODIFICA: aggiunta menu per selezionare una sede specifica
nomi_sedi = [s["nome"] for s in sedi]  # Estrae i nomi delle sedi
sede_selezionata = st.selectbox("Seleziona una sede da visualizzare sulla mappa:", nomi_sedi)

# Pulsanti per visualizzare mappe tematiche
tema_distanza = st.button("Visualizza mappa per distanza da Palazzo Chigi")
tema_allerta = st.button("Visualizza mappa per livello di allerta")

# Colori per livello allerta
colori_allerta = {
    1: "#2ECC71",  # verde
    2: "#A9DFBF",  # verde chiaro
    3: "#F7DC6F",  # giallo
    4: "#F39C12",  # arancione
    5: "#E74C3C"   # rosso
}

# --------------------------- CREAZIONE MAPPA ---------------------------
# Crea mappa
mappa = folium.Map(location=[41.5000, 13.0000], zoom_start=8)

# --------------------------- AGGIUNTA MARKER ---------------------------
# Cicla su tutte le sedi per aggiungere marker tematici
for sede in sedi:
   # Costruisce il contenuto del popup con informazioni dettagliate
    popup = folium.Popup (f"""
    <b>{sede['nome']}</b><br>
    {sede['funzione']}<br>
    Accessibilità: {sede['accessibilita']}<br>
    Allerta: {sede['livello_allerta']}<br>
    Distanza: {sede['distanza_da_palazzo_chigi_km']} km<br>
    Tempo: {sede['tempo_percorrenza_min']} min<br>
    Note: {sede['note']}
    """, max_width=300)

   # Determina il colore del marker in base al tema selezionato
    colore = colori_allerta.get(sede["livello_allerta"], "gray")

    if tema_distanza:
        # colore in base alla distanza
        distanza = sede["distanza_da_palazzo_chigi_km"]
        if distanza < 5:
            colore = "#3498DB"  # blu
        elif distanza < 15:
            colore = "#1ABC9C"  # verde acqua
        else:
            colore = "#9B59B6"  # viola

    elif tema_allerta:
        # colore in base al livello di allerta
        colore = colori_allerta.get(sede["livello_allerta"], "gray")

# --------------------------- MARKER SEDE SELEZIONATA ---------------------------
# aggiunta marker blu per la sede selezionata
sede_info = next((s for s in sedi if s["nome"] == sede_selezionata), None)
if sede_info:
    folium.Marker(
        location=[sede_info["lat"], sede_info["lon"]],
        popup=f"<b>{sede_info['nome']}</b>",
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(mappa)

# --------------------------- VISUALIZZAZIONE MAPPA ---------------------------
# Mostra la mappa interattiva
st.markdown("### 🗺️ Mappa interattiva delle sedi PCM")
st_folium(mappa, width=1000, height=600)

# --------------------------- VISUALIZZAZIONE TABELLA ---------------------------
# aggiunta tabella interattiva con i dati delle sedi
st.markdown("""
            ### 📋 Tabella delle sedi PCM
            ###### ***scorrere verso destra per visualizzare tutte le colonne***
             """)
st.dataframe(sedi)