
"""
controlla_pdfs_approfondito.py
------------------------------
Scansione ricorsiva di una cartella per individuare PDF corrotti / non leggibili.

Criteri di 'leggibilità':
  - Il PDF si apre SENZA eccezioni.
  - NON richiede password (oppure il file è decriptabile con password vuota).
  - Ha almeno 1 pagina.
  - (Opzionale) La prima pagina si carica correttamente e consente una lettura basilare.

Dipendenze:
    pip install pymupdf
"""

import os
import fitz  # PyMuPDF


def check_pdf_readability(pdf_path, deep=False):
    """
    Ritorna True se il PDF è 'leggibile' secondo i criteri sopra.
    deep=False  -> controllo leggero e veloce.
    deep=True   -> carica la prima pagina ed effettua una lettura basilare (più lento, ma più affidabile).
    """
    try:
        # Context manager: il file viene sempre chiuso correttamente
        with fitz.open(pdf_path) as doc:
            # PDF cifrato? Prova l'autenticazione con password vuota; se fallisce, per noi non è 'leggibile'.
            if doc.is_encrypted and not doc.authenticate(""):
                return False

            # Deve avere almeno una pagina
            if doc.page_count <= 0:
                return False

            if not deep:
                return True

            # Controllo 'approfondito': carica la prima pagina e prova a leggere del testo.
            # (Se è un PDF immagine-only, il testo potrebbe essere vuoto: l'importante è che il caricamento non fallisca.)
            page = doc.load_page(0)
            _ = page.get_text("text")
            return True

    except Exception:
        # Qualsiasi eccezione (I/O, parsing, formato) => non leggibile
        return False


def find_corrupted_pdfs(root_folder, deep=False):
    """
    Scorre ricorsivamente root_folder e ritorna la lista dei PDF non leggibili
    (ovvero quelli per cui check_pdf_readability(...) è False).
    """
    corrupted = []
    for foldername, _subfolders, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.lower().endswith(".pdf"):
                pdf_path = os.path.join(foldername, filename)
                if not check_pdf_readability(pdf_path, deep=deep):
                    corrupted.append(pdf_path)
    return corrupted


def main():
    # =========================================================
    # MODIFICA QUI I PARAMETRI IN BASE ALLE TUE ESIGENZE
    #  - root_folder : cartella da analizzare (PERCORSO REALE)
    #  - out_file    : report di output (percorso file .txt)
    #  - deep_check  : True per controllo approfondito (carica 1ª pagina), False per controllo veloce
    # =========================================================
    root_folder = r"C:\Users\ufabiani\Downloads\scuole"  # <<< INSERISCI QUI IL TUO PERCORSO
    out_file    = "pdf_non_validi_controllo_approfondito.txt"                   # puoi mettere un percorso assoluto se preferisci
    deep_check  = False                                  # metti True se vuoi il controllo approfondito

    if not os.path.isdir(root_folder):
        print(f"Errore: la cartella non esiste o non è accessibile: {root_folder}")
        return

    corrupted_pdfs = find_corrupted_pdfs(root_folder, deep=deep_check)

    # Scrive il report (un percorso per riga)
    with open(out_file, "w", encoding="utf-8") as f:
        for pdf in corrupted_pdfs:
            f.write(pdf + "\n")

    print(
        f"Controllo completato.\n"
        f"  Radice: {root_folder}\n"
        f"  Controllo approfondito: {deep_check}\n"
        f"  PDF non leggibili: {len(corrupted_pdfs)}\n"
        f"  Report: {os.path.abspath(out_file)}"
    )


if __name__ == "__main__":
    main()
