import streamlit as st
import pandas as pd
import json
from pathlib import Path

# Imposta la configurazione della pagina con titolo e icona
st.set_page_config(page_title="Titoli Universitari", page_icon="🎓")

# Titolo principale della pagina
st.title("🎓 Titoli Universitari")

# Messaggio finale
st.success("📌 Puoi cliccare sui link nella tabella per visualizzare i badge, oppure usare il menu a tendina per navigare tra i titoli.")


st.divider()
# ============================
# Sezione tabellare compatta
# ============================
st.subheader("📋 Tabella riepilogativa dei titoli")
# Creazione di una tabella compatta


# Percorso del file JSON
json_path = "assets/titoli/titoli.json"



try:
    with open(json_path, "r", encoding="utf-8") as f:
        titoli_data = json.load(f)
except FileNotFoundError:
    st.error(f"File JSON non trovato: {json_path}")
    st.stop()

# Loop sui titoli
for i, titolo in enumerate(titoli_data):
    st.markdown(f"**{titolo['Titolo']}** — 📅 {titolo['Data']}")
    cols = st.columns(2)

    # Bottone Badge
    with cols[0]:
        badge_path = titolo.get("Badge")
        if badge_path and badge_path != "--" and Path(badge_path).exists():
            with open(badge_path, "rb") as f:
                st.download_button(
                    label="🔗 Badge (PDF)",
                    data=f,
                    file_name=Path(badge_path).name,
                    mime="application/pdf",
                    key=f"badge_{i}",
                    type="primary",
                )
        else:
            st.caption("Badge: non disponibile")

    # Bottone Tesi
    with cols[1]:
        tesi_path = titolo.get("Tesi")
        if tesi_path and tesi_path != "--" and Path(tesi_path).exists():
            with open(tesi_path, "rb") as f:
                st.download_button(
                    label="📄 Tesi (PDF)",
                    data=f,
                    file_name=Path(tesi_path).name,
                    mime="application/pdf",
                    key=f"tesi_{i}",
                )
        else:
            st.caption("Tesi: non disponibile")

st.divider()
# ============================
# Sezione interattiva con selectbox
# ============================

st.subheader("📚 Seleziona un titolo per visualizzare i dettagli")

opzioni_titoli = [
    "📘 Dottorato in Ingegneria delle Infrastrutture e dei Trasporti",
    "📕 Laurea VO in Lettere Classiche (indirizzo Topografico)",
    "📗 Laurea Triennale in Scienze dei Servizi Giuridici (informatica giuridica)",
    "📒 Master I livello in Sistemi Informativi Territoriali e Telerilevamento",
    "📙 Master I livello per insegnamento in istituti secondari",
    "📘 Esperto nella Normativa e nella Contrattualistica del lavoro - 1500 ore"
]

scelta = st.selectbox("Scegli un titolo:", opzioni_titoli)

if scelta == opzioni_titoli[0]:
    with st.expander(opzioni_titoli[0], expanded=True):
        st.markdown("- Titolo accademico di terzo livello conseguito presso istituto universitario")
        st.markdown("- 📅 Data: 20-02-2009")
        with open("assets/titoli/dottorato_infrastrutture.pdf", "rb") as f:
            st.download_button("🔗 Scarica Badge", f, file_name="dottorato_infrastrutture.pdf")
#        with open("assets/titoli/dottorato_infrastrutture_tesi.pdf", "rb") as f:
#            st.download_button("📄 Scarica Tesi", f, file_name="dottorato_infrastrutture_tesi.pdf")

elif scelta == opzioni_titoli[1]:
    with st.expander(opzioni_titoli[1], expanded=True):
        st.markdown("- Laurea vecchio ordinamento con indirizzo topografico")
        st.markdown("- 📅 Data: 12-07-2002")
        with open("assets/titoli/laurea_vecchio_ordinamento.pdf", "rb") as f:
            st.download_button("🔗 Scarica Badge", f, file_name="laurea_vecchio_ordinamento.pdf")
#        with open("assets/titoli/laurea_vecchio_ordinamento_tesi.pdf", "rb") as f:
#            st.download_button("📄 Scarica Tesi", f, file_name="laurea_vecchio_ordinamento_tesi.pdf")

elif scelta == opzioni_titoli[2]:
    with st.expander(opzioni_titoli[2], expanded=True):
        st.markdown("- Laurea triennale in ambito informatico-giuridico")
        st.markdown("- 📅 Data: 05-07-2016")
        with open("assets/titoli/laurea_triennale.pdf", "rb") as f:
            st.download_button("🔗 Scarica Badge", f, file_name="laurea_triennale.pdf")
#        with open("assets/titoli/laurea_triennale_tesi.pdf", "rb") as f:
#           st.download_button("📄 Scarica Tesi", f, file_name="laurea_triennale_tesi.pdf")

elif scelta == opzioni_titoli[3]:
    with st.expander(opzioni_titoli[3], expanded=True):
        st.markdown("- Master I livello in Sistemi Informativi Territoriali e Telerilevamento")
        st.markdown("- 📅 Data: 22-11-2004")
        with open("assets/titoli/master_sistemi_informativi.pdf", "rb") as f:
            st.download_button("🔗 Scarica Badge", f, file_name="master_sistemi_informativi.pdf")
 #       with open("assets/titoli/master_sistemi_informativi_tesi.pdf", "rb") as f:
 #           st.download_button("📄 Scarica Tesi", f, file_name="master_sistemi_informativi_tesi.pdf")

elif scelta == opzioni_titoli[4]:
    with st.expander(opzioni_titoli[4], expanded=True):
        st.markdown("- Master I livello per insegnamento in istituti secondari")
        st.markdown("- 📅 Data: 27-10-2022")
        with open("assets/titoli/master_insegnamento.pdf", "rb") as f:
            st.download_button("🔗 Scarica Badge", f, file_name="master_insegnamento.pdf")
#        with open("assets/titoli/master_insegnamento_tesi.pdf", "rb") as f:
#           st.download_button("📄 Scarica Tesi", f, file_name="master_insegnamento_tesi.pdf")

elif scelta == opzioni_titoli[5]:
    with st.expander(opzioni_titoli[5], expanded=True):
        st.markdown("- Esperto nella Normativa e nella Contrattualistica del lavoro - 1500 ore")
        st.markdown("- 📅 Data: 27-11-2014")
        with open("assets/titoli/Esperto_Normativa.pdf", "rb") as f:
            st.download_button("🔗 Scarica Badge", f, file_name="Esperto_Normativa.pdf")
        # La tesi non è disponibile
        st.caption("📄 Tesi: non disponibile")


st.divider()

# ============================
# Sezione dettagliata con expander
# ============================
st.subheader("📦 Dettagli completi dei titoli")

for i, titolo in enumerate(titoli_data):
    with st.expander(f"{titolo['Titolo']}", expanded=False):
        st.markdown(f"- 📅 Data: {titolo['Data']}")

        # Bottone Badge
        badge_path = titolo.get("Badge")
        if badge_path and badge_path != "--" and Path(badge_path).exists():
            with open(badge_path, "rb") as f:
                st.download_button(
                    label="🔗 Scarica Badge (PDF)",
                    data=f,
                    file_name=Path(badge_path).name,
                    mime="application/pdf",
                    key=f"badge_exp_{i}",
                    type="primary",
                )
        else:
            st.caption("Badge: non disponibile")

        # Bottone Tesi
        tesi_path = titolo.get("Tesi")
        if tesi_path and tesi_path != "--" and Path(tesi_path).exists():
            with open(tesi_path, "rb") as f:
                st.download_button(
                    label="📄 Scarica Tesi (PDF)",
                    data=f,
                    file_name=Path(tesi_path).name,
                    mime="application/pdf",
                    key=f"tesi_exp_{i}",
                )
        else:
            st.caption("Tesi: non disponibile")