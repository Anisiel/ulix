import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Programmini (in)utili", page_icon="💻")
st.title("💻 Programmini (in)utili ⬇️")

st.markdown(
    """
Una raccolta di programmini (in)utili che ho scritto nel tempo, per esigenze d'ufficio (elenco cartelle, controllo .pdf) e per la mia personale gestione dei file.

- Programmini **🖥️ .bat** per il Prompt dei comandi di Windows (cmd.exe).  
  Si possono eseguire da `cmd` oppure con doppio clic (da cmd si leggono i messaggi (consigliato). Con il doppio click no (sarebbe necessario inserire `pause` nel codice)).

  - Uno script **🐍 Python (.py)** per il controllo di integrità dei file PDF, in versione base e avanzata (richiede Python + dipendenze).
    """,
    unsafe_allow_html=True
)

# =========================
#  ISTRUZIONI PER L'USO
# =========================
st.markdown("## 🔍 Cosa serve per far funzionare i Programmini (in)utili? ➡️")

st.markdown("""
**🖥️ Programmini da Prompt dei comandi (.bat):**
- **Opzione 1:** Doppio clic sul file `.bat` (consigliato aggiungere `pause` per vedere l’output).
- **Opzione 2:** Apri il **Prompt dei comandi**:
    - Premi `Win + R`, digita `cmd` e premi Invio.
    - Usa `cd` per spostarti nella cartella dove hai salvato il file (es. `cd C:\\Users\\Nome\\Downloads`).
    - Lancia il file digitando il nome (es. `elenca_cartelle.bat`).

**🐍 Script Python (.py):**
- Installa **Python**: [Scarica qui](👉 https://www.python.org/downloads/)
- Installa la dipendenza necessaria (pymupdf):
    ```bash
    pip install pymupdf
    ```
- Apri il file .py,  modifica il percorso nel file (blocco `MODIFICA QUI`) e lancia uno dei due script:
    ```bash
    python controlla_pdfs_approfondito.py
    ```
""")
# =========================


# --- Percorso cartella assets (pagina si trova in pages/)
ASSETS = Path(__file__).resolve().parents[1] / "assets"

def load_bytes(rel_path: str) -> bytes:
    p = ASSETS / rel_path
    return p.read_bytes()

def load_text(rel_path: str) -> str:
    p = ASSETS / rel_path
    return p.read_text(encoding="utf-8")

# =========================
#  CATALOGHIAMO I PROGRAMMI
# =========================
PROGRAMS = [
    {
        "categoria": "📂 File & Cartelle",
        "titolo": "Elenco cartelle (ricorsivo) → TXT",
        "file_rel": "bat/elenca_cartelle.bat",
        "descr": "Elenca tutte le cartelle e sottocartelle a partire da una radice e salva l’elenco in un file .txt.",
        "lingua": "bat"
    },
    {
        "categoria": "📂 File & Cartelle",
        "titolo": "Struttura ad albero (solo cartelle) → TXT",
        "file_rel": "bat/elenca_cartelle_struttura_albero.bat",
        "descr": "Usa `tree /a` per produrre una struttura ASCII ad albero (solo cartelle) e salvarla su file.",
        "lingua": "bat"
    },
    {
        "categoria": "🔎 Ricerca & Filtri",
        "titolo": "Elenco DOCX (ricorsivo) con esclusioni",
        "file_rel": "bat/elenco_docx.bat",
        "descr": "Cerca ricorsivamente i file .DOCX e salva i risultati.",
        "lingua": "bat"
    },
    {
        "categoria": "🔎 Ricerca & Filtri",
        "titolo": "Elenco XLSX (ricorsivo) con esclusioni",
        "file_rel": "bat/elenco_xlsx.bat",
        "descr": "Cerca ricorsivamente i file .XLSX e salva i risultati.",
        "lingua": "bat"
    },
    {
        "categoria": "🔎 Ricerca & Filtri",
        "titolo": "Elenco PDF (ricorsivo) con esclusioni",
        "file_rel": "bat/elenco_pdf.bat",
        "descr": "Cerca ricorsivamente i file .PDF e salva i risultati.",
        "lingua": "bat"
    },
    {
        "categoria": "🔎 Ricerca & Filtri",
        "titolo": "Elenco tutti i file (ricorsivo) senza esclusioni",
        "file_rel": "bat/elenco_tutti.bat",
        "descr": "Cerca ricorsivamente tutti i file e salva i risultati.",
        "lingua": "bat"
    },
    {
        "categoria": "🔁 Backup & Sync",
        "titolo": "Backup/Sync con Robocopy (dry-run)",
        "file_rel": "bat/backup_robocopy.bat",
        "descr": "Esegue una copia/sincronizzazione robusta con Robocopy; parte in **dry-run** (`/L`), poi togli `/L` per eseguire davvero.",
        "lingua": "bat"
    },
    {
        "categoria": "🧹 Pulizia",
        "titolo": "Cancella file più vecchi di N giorni",
        "file_rel": "bat/pulizia_vecchi_file.bat",
        "descr": "Usa `forfiles` per eliminare file oltre una certa età e poi prova a rimuovere cartelle rimaste vuote.",
        "lingua": "bat"
    },
    {
        "categoria": "🚀 Automazione",
        "titolo": "Avvio Multi‑App",
        "file_rel": "bat/avvio_multiapp.bat",
        "descr": "Avvia più applicazioni in sequenza; facoltativi piccoli `timeout` tra un avvio e l’altro.",
        "lingua": "bat"
    },
    {
        "categoria": "📄 PDF Tools base (Python)",
        "titolo": "Controlla PDF non leggibili (PyMuPDF), controllo base",
        "file_rel": "python/controlla_pdfs.py",
        "descr": "Controlla se i PDF si aprono o meno. Report su file .txt.",
        "lingua": "python"
    },
        {
        "categoria": "📄 PDF Tools avanzato (Python)",
        "titolo": "Controlla PDF non leggibili (PyMuPDF), controllo approfondito",
        "file_rel": "python/controlla_pdfs_approfondito.py",
        "descr": "Controlla: PDF cifrati (password vuota), 0 pagine, caricamento 1ª pagina. Report su file .txt.",
        "lingua": "python"
    },
]

# =======
# RENDER PER SCARICARE I PROGRAMMI
# =======
st.markdown("—")
st.subheader("Scarica i programmini")

# Raggruppa per categoria
from collections import defaultdict
by_cat = defaultdict(list)
for p in PROGRAMS:
    by_cat[p["categoria"]].append(p)

for categoria in by_cat:
    st.markdown(f"### {categoria}")
    for p in by_cat[categoria]:
        cols = st.columns([0.75, 0.25])
        with cols[0]:
            st.markdown(f"**{p['titolo']}**  \n{p['descr']}")
        with cols[1]:
            try:
                data = load_bytes(p["file_rel"])
                file_name = Path(p["file_rel"]).name
                st.download_button(
                    label="⬇️ Scarica",
                    data=data,
                    file_name=file_name,
                    mime="text/plain" if p["lingua"] in ("bat", "python") else "application/octet-stream",
                    use_container_width=True
                )
            except FileNotFoundError:
                st.error(f"File mancante: `{p['file_rel']}`")

        with st.expander("Mostra codice"):
            try:
                code = load_text(p["file_rel"])
                st.code(code, language=p["lingua"])
            except FileNotFoundError:
                st.warning("Aggiungi il file nella cartella `assets/` per vederlo qui.")

st.markdown("---")
st.caption(
    "Suggerimenti: i .bat si eseguono con doppio clic o da `cmd`. Per lo script Python devi avere installato Python e le dipendenze (pymupdf) "
    "e modifica il percorso di input nel file (blocco `MODIFICA QUI`)."
)