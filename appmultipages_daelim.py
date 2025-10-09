import streamlit as st
from pathlib import Path  # servirà per CV e per check immagini

st.set_page_config(page_title="Ulisse Fabiani", page_icon="🌱", layout="wide")  #  wide = allineamento a sinistra

# Titolo principale: mostrato una sola volta, indipendentemente dal layout in modo da stare in alto
st.markdown(
	"""
	<div style='line-height:1.05'>
		<h1>Ulisse Fabiani — Portfolio</h1>
		<div class='subtitle'>Hello, lettore! 👋 • Questo è un esempio creato da me nel mese di ottobre 2025 per mostrare le competenze informatiche </div>
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

# [MODIFICA] —— Parametri modificabili facilmente ——————————————————————————
STAMP_WIDTH = 120          # “francobollo” (px). Provare anche 80, 96, 120...
GRID_COLS   = 5           # quante immagini per riga

# Elenco immagini (aggiungerne/rimuoverne senza rompere nulla).
# "note" è una riga opzionale: se stringa vuota, NON viene mostrata.
IMMAGINI = [
	{"src": "assets/hero.jpg",  "note": "Mocking Face"},          # es.: "note": "Foto 2025, estate"
	{"src": "assets/hero2.jpg", "note": "Le Discret"},          # lasciare "" per non visualizzare nulla
	{"src": "assets/hero3.jpg", "note": "San Govanni Battista"},
]
# ————————————————————————————————————————————————————————————————————————

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
					# usare un <img class='gallery-thumb'> per poter targettare
					# solamente le immagini della galleria con il CSS
					# usare st.image per assicurare la corretta visualizzazione
					# aggiungiamo anche un attributo alt tramite markdown vicino
					st.image(it["src"], use_container_width=True)
					if it.get("note"):              # se vuoto, non mostra nulla
						st.caption(it["note"])

# ──────────────────────────────────────────────────────────────────────────

# (I link e il download del CV sono ora mostrati subito DOPO le immagini,
#  per restare visibili sotto la galleria; il blocco viene inserito più
#  in basso nel codice.)

# ——————————————————————————————————————————————————————————————
# Layout alternativo (OPZIONALE): lo attivo mettendo True/False
ALT_LAYOUT = True

if not ALT_LAYOUT:
	# Titolo/testo SOPRA l’immagine
  #  st.header("Ulisse Fabiani — Portfolio")     # se lo inserisco qui appare di lato alle immagini
	st.title("Hello, lettore! 👋")
	st.subheader("Dammi un buon voto! 😄")

	# HERO / COPERTINA (francobolli, allineati a sinistra, anche più immagini)
	render_thumbs(IMMAGINI)                      # rende i “francobolli”

	# Separator before external links
	st.divider()

	# 1) External links inline (icon + link)
	st.markdown(
		"""
		<div style='display:flex;gap:1.2rem;align-items:center;'>
		  <div style='display:flex;gap:.5rem;align-items:center;'>🎓<a href='https://independent.academia.edu/FabianiUlisse' target='_blank' rel='noreferrer'>Academia.edu</a></div>
		  <div style='display:flex;gap:.5rem;align-items:center;'>💻<a href='https://github.com/Anisiel/ulix' target='_blank' rel='noreferrer'>GitHub</a></div>
		</div>
		""",
		unsafe_allow_html=True,
	)
	# Download CV slightly detached and with a playful icon
	cv_path = Path("assets/Ulisse_Fabiani_CV.pdf")
	if cv_path.exists():
		st.markdown("<div style='margin-top:0.6rem'></div>", unsafe_allow_html=True)
		st.download_button(
			"📄 Scarica il mio CV",
			data=cv_path.read_bytes(),
			file_name="Ulisse_Fabiani_CV.pdf",
			mime="application/pdf",
			key="cv_download_1",
		)

	st.divider()
	# Internal page links (affiancati)
	col1, col2, col3 = st.columns(3)

	with col1:
		st.markdown("📈 [Grafici](pages/1_Grafici.py)", unsafe_allow_html=True)

	with col2:
		st.markdown("📚 [Pubblicazioni](pages/2_Pubblicazioni.py)", unsafe_allow_html=True)
		st.markdown("🎓 [Titoli & Certificazioni](pages/3_Titoli_Certificazioni.py)", unsafe_allow_html=True)

	with col3:
		st.markdown("💻 [Programmini (in)utili](pages/4_Programmini.py)", unsafe_allow_html=True)
    

else:
	st.divider()
	st.caption("Layout alternativo attivo (sempre minimal)")

	col_img, col_main = st.columns([1, 3], gap="large")
	with col_img:
		render_thumbs(IMMAGINI)  # immagini a sinistra
		# (left column only contains images)
	with col_main:
		  #  st.header("Ulisse Fabiani — Portfolio")     # se lo inserisco qui appare di lato alle immagini
		st.title("Hello, lettore! 👋")
		st.subheader("Dammi un buon voto! 😄")
		st.caption("Portfolio minimal & zen — layout alternativo")

	# After the two-column row, render links (full-width): external, internal, then CV
	st.divider()
	# External links
	st.markdown(
		"""
		<div style='display:flex;gap:1.2rem;align-items:center;'>
		  <div style='display:flex;gap:.5rem;align-items:center;'>🎓<a href='https://independent.academia.edu/FabianiUlisse' target='_blank' rel='noreferrer'>Academia.edu</a></div>
		  <div style='display:flex;gap:.5rem;align-items:center;'>💻<a href='https://github.com/Anisiel/ulix' target='_blank' rel='noreferrer'>GitHub</a></div>
		</div>
		""",
		unsafe_allow_html=True,
	)

	# Download CV slightly detached and with a playful icon
	cv_path = Path("assets/Ulisse_Fabiani_CV.pdf")
	if cv_path.exists():
		st.markdown("<div style='margin-top:0.6rem'></div>", unsafe_allow_html=True)
		st.download_button(
			"📄 Scarica il mio CV",
			data=cv_path.read_bytes(),
			file_name="Ulisse_Fabiani_CV.pdf",
			mime="application/pdf",
			key="cv_download_2",
		)

	st.divider()
	# Internal page links (affiancati)
	col1, col2, col3 = st.columns(3)

	with col1:
		st.markdown("📈 [Grafici](pages/1_Grafici.py)", unsafe_allow_html=True)

	with col2:
		st.markdown("📚 [Pubblicazioni](pages/2_Pubblicazioni.py)", unsafe_allow_html=True)
		st.markdown("🎓 [Titoli & Certificazioni](pages/3_Titoli_Certificazioni.py)", unsafe_allow_html=True)

	with col3:
		st.markdown("💻 [Programmini (in)utili](pages/4_Programmini.py)", unsafe_allow_html=True)

	st.divider()
