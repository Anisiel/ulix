"""
controlla_pdfs.py
-------------
Scandisce una cartella ricorsivamente e individua i PDF "non leggibili":
- un PDF è considerato "leggibile" se si apre correttamente e ha almeno 1 pagina;
- in caso contrario viene segnalato come "corrotto/non leggibile".

Dipendenze:
    pip install pymupdf   # modulo 'fitz'

Output:
    Crea un file di testo 'pdf_non_validi.txt' con l'elenco dei PDF problematici.

Nota:
    Questo è un controllo 'leggero'. Per danni più nascosti o PDF protetti da password,
    vedi la versione "robusta" più in basso.
"""

import os
import fitz  # PyMuPDF


def check_pdf_readability(pdf_path: str) -> bool:
    """
    Torna True se il PDF si apre e ha almeno una pagina, altrimenti False.
    - Usa un 'try/except' per intercettare errori di apertura (file danneggiati, permessi, ecc.).
    - Chiude il documento anche in caso di eccezione, grazie al context manager.
    """
    try:
        # Apri il documento in modo sicuro: il context manager chiude il file automaticamente
        with fitz.open(pdf_path) as doc:
            # Se il conteggio pagine è > 0 lo consideriamo 'leggibile' (controllo di base)
            return doc.page_count > 0
    except Exception:
        # Qualsiasi errore di apertura / parsing -> NON leggibile
        return False


def find_corrupted_pdfs(root_folder: str) -> list[str]:
    """
    Cammina ricorsivamente 'root_folder' e verifica tutti i .pdf.
    Restituisce la lista dei path ritenuti non leggibili.
    """
    corrupted_pdfs: list[str] = []

    # os.walk restituisce (cartella_corrente, sottocartelle, file_nella_cartella)
    for foldername, _subfolders, filenames in os.walk(root_folder):
        for filename in filenames:
            # Confronto case-insensitive per estensione .pdf
            if filename.lower().endswith(".pdf"):
                pdf_path = os.path.join(foldername, filename)

                # Se il PDF non supera il controllo di base, aggiungilo alla lista
                if not check_pdf_readability(pdf_path):
                    corrupted_pdfs.append(pdf_path)

    return corrupted_pdfs


def main() -> None:
    """
    Punto di ingresso:
    - imposta la cartella radice (MODIFICA QUI se necessario),
    - lancia la scansione,
    - salva su file 'pdf_non_validi.txt' l'elenco dei PDF problematici,
    - stampa un riepilogo a video.
    """
    root_folder = r"C:\Users\ufabiani\Downloads\scuole"

    corrupted_pdfs = find_corrupted_pdfs(root_folder)

    # Scrive un file di testo con un PDF per riga
    with open("pdf_non_validi.txt", "w", encoding="utf-8") as f:
        for pdf in corrupted_pdfs:
            f.write(f"{pdf}\n")

    print(
        f"Controllo completato. "
        f"Trovati {len(corrupted_pdfs)} file PDF corrotti o non leggibili."
    )


if __name__ == "__main__":
    main()