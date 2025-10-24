import streamlit as st
from pathlib import Path  # servirà per CV e per check immagini

# =============================================================================
# STRUTTURA DELLA PAGINA — Home.py (Versione Minimal)
# -----------------------------------------------------------------------------
# Questa pagina mostra una versione semplice e "zen" del portfolio.
# Il layout è diviso in due colonne:
# - A sinistra: immagini in formato "francobollo"
# - A destra: contenuto testuale, link e navigazione
#
# Comandi principali:
# - `st.set_page_config(layout="wide")`: layout allineato a sinistra
# - `st.columns(...)`: struttura a due colonne
# - `st.markdown(...)`: titoli, link e testo
# - `st.download_button(...)`: pulsante per scaricare il CV
#
# Il file `styles.css` viene caricato per mantenere il layout stabile
# e vicino alla sidebar, evitando centrature automatiche.
# =============================================================================

# 🔗 Rimando alla pagina di organizzazione del sito
# Mostra la descrizione del progetto in alto a destra
col_left, col_right = st.columns([2, 3])  # proporzioni: sinistra più stretta
with col_right:
    with st.expander("📘 Info sul selettore e sul portfolio"):
        st.markdown("Vuoi sapere come è strutturato il sito e come funziona il selettore?")
        if st.button("👉 ***Organizzazione portfolio***"):
            st.switch_page("pages/0_Organizzazione_portfolio.py")                

st.set_page_config(page_title="Ulisse Fabiani", page_icon="🌱", layout="wide")  #  wide = allineamento a sinistra

# Titolo principale: mostrato una sola volta, indipendentemente dal layout in modo da stare in alto
st.markdown(
	"""
	<div style='line-height:1.05'>
		<h1>Ulisse Fabiani </h1>
		<div class='subtitle'>Benvenuto nel mio portfolio interattivo versione Home minimal & zen, come piace a me </div>
	</div>
	""",
	unsafe_allow_html=True,
)

# --- Stili CSS per migliorare la responsiveness ---------------------------------
try:
	css_path = Path("assets/styles.css")
	if css_path.exists():
		st.markdown(f"<style>{css_path.read_text()}</style>", unsafe_allow_html=True)
except Exception:
	# fall back: niente CSS esterno se qualcosa va storto
	pass

# —— Parametri modificabili facilmente ——————————————————————————
STAMP_WIDTH = 180          # “francobollo” (px). Provare anche 80, 96, 120...
GRID_COLS   = 3           # quante immagini per riga

# Elenco immagini (aggiungerne/rimuoverne senza rompere nulla).
# "note" è una riga opzionale: se stringa vuota, NON viene mostrata.
IMMAGINI = [
	{"src": "assets/img/hero.jpg",  "note": "Mocking Face"},
	{"src": "assets/img/hero2.jpg", "note": "Le Discret"},
	{"src": "assets/img/hero3.jpg", "note": "San Govanni Battista"},
]

# helper minimal per visualizzare le immagini come francobolli
def render_thumbs(items, width=STAMP_WIDTH, cols=GRID_COLS):
	# mostra solo quelle che ESISTONO nel repo (assets), così non va in errore se mancano
	safe_items = [it for it in items if Path(it["src"]).exists()]
	if not safe_items:
		return

	for i in range(0, len(safe_items), cols):
		row = safe_items[i : i + cols]
		columns = st.columns(len(row), gap="small")
		for col, it in zip(columns, row):
			with col:
				st.image(it["src"], use_container_width=True)
				if it.get("note"):
					st.caption(it["note"])

# Single active layout (keep only this)
st.divider()

col_img, col_main, col_extra = st.columns([1, 3, 1], gap="large")
with col_img:
	render_thumbs(IMMAGINI)  # immagini in colonna sinistra	
with col_main: # testi in colonna centrale
	st.subheader("Hello, lettore! 👋")
	st.markdown("""
	#### A sinistra tre immagini ironiche che raccontano la mia personalità...
	#### ...A destra un ritratto "personale" che mi accompagna da sempre😄
	""")

	
	st.caption("Portfolio interamente programmato in python no wordpress")



with col_extra:
    # 🔧 MODIFICA: aggiunta immagine extra a destra del testo
    extra_img_path = "assets/img/hero1.jpg"
    if Path(extra_img_path).exists():
        st.image(extra_img_path, caption="[Ulisse su Wikipedia](https://it.wikipedia.org/wiki/Ulisse)", use_container_width=True)


# Dopo le immagini  ci sono i link esterni, interni e poi il link al CV
st.divider()
# Link esterni in colonna e non affiancati
st.markdown(
	"""
	<div style='display:flex;gap:1.2rem;align-items:center;'>
	  <div style='display:flex;gap:.5rem;align-items:center;'>🎓<a href='https://independent.academia.edu/FabianiUlisse' target='_blank' rel='noreferrer'>Academia.edu</a></div>
	  <div style='display:flex;gap:.5rem;align-items:center;'>💻<a href='https://github.com/Anisiel/ulix' target='_blank' rel='noreferrer'>GitHub</a></div>
	</div>
	""",
	unsafe_allow_html=True,
)

# Download CV
cv_path = Path("assets/Ulisse_Fabiani_CV.pdf")
if cv_path.exists():
	st.markdown("<div style='margin-top:0.6rem'></div>", unsafe_allow_html=True)
	st.download_button(
		"🧾❗  Scarica il mio CV",
		data=cv_path.read_bytes(),
		file_name="Ulisse_Fabiani_CV.pdf",
		mime="application/pdf",
		key="cv_download_home",
	)

st.divider()
# Link interni alle pagine affiancati e non in colonna
col1, col2, col3 = st.columns(3)

with col1:
	st.markdown("### 📊 Grafici")
	if st.button("📊 Grafici con Plotly"):
		st.switch_page("pages/1_Grafici_plotly.py")
	if st.button("🌐 Grafici con Echarts"):
		st.switch_page("pages/2_Grafici_Altair_Echarts.py")
	if st.button("🌦️ Grafici Meteo con Altair"):
   		st.switch_page("pages/3_Grafici_Altair_Meteo.py")
		   
with col2:
	st.markdown("### 🎓 Curriculum")
	if st.button("🎓 Titoli di Studio"):
		st.switch_page("pages/5_Titoli.py")
	if st.button("📜 Certificazioni"):
		st.switch_page("pages/6_Certificazioni.py")
	if st.button("📖 Pubblicazioni"):
		st.switch_page("pages/7_Pubblicazioni.py")

with col3:
	st.markdown("### 🧰 Utility & Excel")
	if st.button("🧪 Programmini (in)utili"):
		st.switch_page("pages/4_Programmini_(in)utili.py")
	if st.button("📂 Excel & Progetti VBA"):
		st.switch_page("pages/8_Excel_Progetti_VBA.py")

st.divider()
