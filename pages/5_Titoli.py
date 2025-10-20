import streamlit as st
import pandas as pd

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


# Dati dei titoli
data = {
    "Titolo": [
        "Dottorato in Ingegneria delle Infrastrutture e dei Trasporti",
        "Laurea Vecchio Ordinamento in Lettere Classiche (indirizzo Topografico)",
        "Laurea Triennale in Scienze dei Servizi Giuridici in Informatica Giuridica",
        "Master I livello in Sistemi Informativi Territoriali e Telerilevamento - 1650 ore",
        "Master I livello per insegnamento in istituti secondari",
        "Esperto nella Normativa e nella Contrattualistica del lavoro - 1500 ore"

    ],
    "Data": [
        "20-02-2009",
        "12-07-2002",
        "22-11-2004",
        "05-07-2016",
        "27-10-2022",
        "27-11-2014"
    ],
    "Nome e Livello europeo": [
        "Dottorato - Livello 8",
        "Laurea VO - Livello 7",
        "Triennale - livello 6",
        "Master I livello - Livello 7",
        "Master I livello - Livello 7"
        "Esperto - Livello 6"
    ],
    "Badge": [
        "[PDF](assets/cert/dottorato_infrastrutture.pdf)",
        "[PDF](assets/cert/laurea_vecchio_ordinamento.pdf)",
        "[PDF](assets/cert/laurea_triennale.pdf)",
        "[PDF](assets/cert/master_sistemi_informativi.pdf)",
        "[PDF](assets/cert/master_insegnamento.pdf)",
        "[PDF](assets/cert/Esperto_Normativa.pdf)"
    ],
    "Tesi": [
        "[PDF](assets/cert/dottorato_infrastrutture_tesi.pdf)",
        "[PDF](assets/cert/laurea_vecchio_ordinamento_tesi.pdf)",
        "[PDF](assets/cert/laurea_triennale_tesi.pdf)",
        "[PDF](assets/cert/master_sistemi_informativi_tesi.pdf)",
        "[PDF](assets/cert/master_insegnamento_tesi.pdf)",
        "--"
    ]
}

# Mostra la tabella con link
df = pd.DataFrame(data)
st.markdown(df.to_markdown(index=False), unsafe_allow_html=True)

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
        st.markdown("""
        - Titolo accademico di terzo livello conseguito presso istituto universitario  
        - 📅 Data: 20-02-2009  
        - 🔗 [Visualizza badge](assets/cert/dottorato_infrastrutture.pdf)
        - 📄 [Visualizza tesi](assets/cert/dottorato_infrastrutture_tesi.pdf)
        """)

elif scelta == opzioni_titoli[1]:
    with st.expander(opzioni_titoli[1], expanded=True):
        st.markdown("""
        - Laurea vecchio ordinamento con indirizzo topografico  
        - 📅 Data: 12-07-2002  
        - 🔗 [Visualizza badge](assets/cert/laurea_vecchio_ordinamento.pdf)
        - 📄 [Visualizza tesi](assets/cert/laurea_vecchio_ordinamento_tesi.pdf
        """)

elif scelta == opzioni_titoli[2]:
    with st.expander(opzioni_titoli[2], expanded=True):
                    
        st.markdown("""
        - Laurea triennale in ambito informatico-giuridico  
        - 📅 Data: 05-07-2016  
        - 🔗 [Visualizza badge](assets/cert/laurea_triennale.pdf)
        - 📄 [Visualizza tesi](assets/cert/laurea_triennale_tesi.pdf)
        """)

elif scelta == opzioni_titoli[3]:
    with st.expander(opzioni_titoli[3], expanded=True):
                    
        st.markdown("""
        - Master I livello in Sistemi Informativi Territoriali e Telerilevamento 
        - 📅 Data: 22-11-2004
        - 🔗 [Visualizza badge](assets/cert/master_sistemi_informativi.pdf)
        - 📄 [Visualizza tesi](assets/cert/master_sistemi_informativi_tesi.pdf)
        """)

elif scelta == opzioni_titoli[4]:
    with st.expander(opzioni_titoli[4], expanded=True):
                    
        st.markdown("""
        - Master I livello per insegnamento in istituti secondari 
        - 📅 Data: 27-10-2022
        - 🔗 [Visualizza badge](assets/cert/master_insegnamento.pdf)
        - 📄 [Visualizza tesi](assets/cert/master_insegnamento_tesi.pdf)
        """)

elif scelta == opzioni_titoli[5]:
    with st.expander(opzioni_titoli[5], expanded=True):
                    
        st.markdown("""
        - Esperto nella Normativa e nella Contrattualistica del lavoro - 1500 ore 
        - 📅 Data: 27-11-2014
        - 🔗 [Visualizza badge](assets/cert/Esperto_Normativa.pdf)
        - 📄 [Visualizza tesi](assets/cert/Esperto_Normativa_diploma.pdf)
        """)

st.divider()
# ============================
# Sezione dettagliata con expander
# ============================
st.subheader("📦 Dettagli completi dei titoli")

for titolo, data, file, emoji in zip(
    data["Titolo"],
    data["Data"],
    data["Badge"],
    ["📘", "📕", "📗", "📒", "📙", 📘]
):
    with st.expander(f"{emoji} {titolo}", expanded=False):
        st.markdown(f"""
        - 📅 Data: {data}  
        - 🔗 {file}
        """)


        *Esperto nella Normativa e nella Contrattualistica del lavoro** - 27/11/2014 - [Visualizza cert.](assets/cert/Esperto_Normativa.pdf) - [Visualizza diploma](assets/cert/Esperto_Normativa_diploma.pdf)