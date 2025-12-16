
from pathlib import Path
import streamlit as st

# Configurazione pagina
if not st.session_state.get("_page_config_done"):
    st.set_page_config(
        page_title="Ulisse Fabiani — Portfolio (Ora)",
        page_icon="🌞",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.session_state["_page_config_done"] = True

# Rimando alla pagina di organizzazione del sito
# Mostra la descrizione del progetto in alto a destra
col_left, col_right = st.columns([2, 3])  # proporzioni: sinistra più stretta
with col_right:
    with st.expander("📘 Info sul selettore e sul portfolio"):
        st.markdown("Vuoi sapere come è strutturato il sito e come funziona il selettore?")
        if st.button("👉 ***Organizzazione portfolio***"):
            st.switch_page("pages/0_Organizzazione_portfolio.py")

# ---------- HERO LOGO ----------
logo_img = Path("assets/img/logo1.png")
# Logo piccolo
if logo_img.exists():
    col1, col2, col3 = st.columns([1, 3, 1])  # colonna centrale più larga
    with col2:
        st.image(str(logo_img), width=84)
else:
    st.warning("Logo non trovato")

st.divider()
st.write("## Portfolio di Ulisse Fabiani")
st.caption("Analisi dati, visualizzazioni interattive e automazione in Python.")

# ---------- Due immagini affiancate ----------
img1 = Path("assets/img/hero4.jpg")
img2 = Path("assets/img/hero5.jpg")

col1, col2 = st.columns(2, gap="small")
with col1:
    if img1.exists():
        st.image(str(img1), width=500)
    else:
        st.warning("Immagine non trovata: hero4.jpg")

with col2:
    if img2.exists():
        st.image(str(img2), width=500)
    else:
        st.warning("Immagine non trovata: hero5.jpg")

st.divider()

# ---------- Sezioni con link alle pagine ----------
colA, colB, colC = st.columns(3)

with colA:
    st.subheader("Visualizzazioni")
    st.caption("Grafici interattivi con Plotly, Altair ed ECharts.")
    if st.button("Plotly", use_container_width=True):
        st.switch_page("pages/1_Grafici_plotly.py")
    if st.button("Echarts & Altair", use_container_width=True):
        st.switch_page("pages/2_Grafici_Altair_Echarts.py")
    if st.button("Meteo con Altair", use_container_width=True):
        st.switch_page("pages/3_Grafici_Altair_Meteo.py")
    if st.button("Mappe GIS/PCM", use_container_width=True):
        st.switch_page("pages/9_GIS_PCM.py")

with colB:
    st.subheader("Automazione")
    st.caption("Script Python, utility e integrazione con Excel/VBA.")
    if st.button("Programmini (in)utili", use_container_width=True):
        st.switch_page("pages/4_Programmini_inutili.py")
    if st.button("Excel & Progetti VBA", use_container_width=True):
        st.switch_page("pages/8_Excel_Progetti_VBA.py")

with colC:
    st.subheader("Pubblicazioni")
    st.caption("Selezione di lavori e attività accademiche.")
    if st.button("Pubblicazioni", use_container_width=True):
        st.switch_page("pages/7_Pubblicazioni.py")
    if st.button("Titoli di Studio", use_container_width=True):
        st.switch_page("pages/5_Titoli.py")
    if st.button("Certificazioni", use_container_width=True):
        st.switch_page("pages/6_Certificazioni.py")

st.divider()

# ---------- Link utili ----------
cv_path = Path("assets/titoli/Ulisse_Fabiani_CV.pdf")
st.write("### Link utili")

col1, col2, col3  = st.columns([1,2,1])
with col1:
    st.link_button("GitHub", "https://github.com/Anisiel/ulix")
    st.link_button("Academia.Edu", "https://independent.academia.edu/FabianiUlisse")

with col2:
    if cv_path.exists():
        st.link_button("Scarica il mio CV", cv_path.as_posix())
    else:
        st.caption("CV non trovato")


# ---------- Footer ----------
st.markdown(
    """
    <div style="text-align:center;color:#6b7280;padding: 1rem 0 2rem 0;">
      © Ulisse Fabiani · Portfolio in Python/Streamlit · Railway hosting
    </div>
    """,
    unsafe_allow_html=True,
)