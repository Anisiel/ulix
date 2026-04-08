import os
import json
import pandas as pd
import re
from datetime import datetime

# =========================================================
# CONFIGURAZIONE PERCORSI RELATIVI PER TEST
# =========================================================
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# CARTELLA = r"C:\Users\ufabiani\Downloads\bd\excel"
# OUTPUT_JSON = r"C:\Users\ufabiani\Downloads\bd\db_crediti.json"

# LOG_DIR = os.path.join(BASE_DIR, "log")
# os.makedirs(LOG_DIR, exist_ok=True)
# LOG_FILE = os.path.join(LOG_DIR, "log_crediti.txt")
# LOG_CF_INVALIDI = os.path.join(LOG_DIR, "log_crediti_cf_invalidi.txt")


# =========================================================
# CONFIGURAZIONE PERCORSI ASSOLUTI
# =========================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # per lanciare i programmi da qualsiasi cartella

CARTELLA = os.path.join(BASE_DIR, "excel")
OUTPUT_JSON = os.path.join(BASE_DIR, "db_crediti.json")

LOG_DIR = os.path.join(BASE_DIR, "log")
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "log_crediti.txt")
LOG_CF_INVALIDI = os.path.join(LOG_DIR, "log_invalidi_crediti.txt")




# Svuota il log CF invalidi ad ogni esecuzione
# il log dei crediti viene scritto SOLO alla fine
with open(LOG_CF_INVALIDI, "w", encoding="utf-8") as f:
    f.write("LOG CODICI FISCALI INVALIDI\n")
    f.write("======================================\n\n")

# =========================================================
# NORMALIZZA_CF (controllo 11 o 16 caratteri alfanumerici, sempre stringa)
# =========================================================
def normalizza_cf(val):
    """
    Normalizza e valida Codice Fiscale / Partita IVA.
    - Mantiene gli zeri iniziali
    - Rimuove .0 / ,0 finali dovuti all'importazione Excel
    - Rimuove caratteri non alfanumerici
    - Converte tutto in stringa uppercase
    - Accetta SOLO:
        • 11 cifre (P.IVA)
        • 16 caratteri alfanumerici (CF persone fisiche)
    """
    if val is None:
        return None

    s = str(val).strip()

    # remove .0 or ,0 from float-converted Excel values
    if s.endswith(".0") or s.endswith(",0"):
        s = s[:-2]

    # keep only allowed characters
    s = re.sub(r"[^A-Za-z0-9]", "", s)
    s = s.upper()

    # partita IVA: 11 cifre
    if len(s) == 11 and s.isdigit():
        return s

    # codice fiscale persona: 16 alfanumerico
    if len(s) == 16 and s.isalnum():
        return s

    return None


# =========================================================
# Reset del file JSON ad ogni esecuzione
# =========================================================
if os.path.exists(OUTPUT_JSON):
    os.remove(OUTPUT_JSON)
# Ricrea un database vuoto
db = {}


# =========================================================
# FUNZIONI UTILI
# =========================================================
def estrai_anno(nome):
    """Estrae anno nel formato 20XX dal nome file o foglio."""
    m = re.search(r"(20\d{2})", nome)
    return int(m.group(1)) if m else None

def analizza_nome_file(nome_file):
    """
    Dato un file tipo 'credito carta.xlsx', estrae:
    tipo = credito
    categoria = carta
    """
    base = os.path.splitext(nome_file)[0].lower()
    # Regex corretta
    parti = re.split(r"[_\s]+", base)
    tipo = parti[0] if len(parti) > 0 else "sconosciuto"
    categoria = parti[1] if len(parti) > 1 else "generico"
    return tipo, categoria


# =========================================================
# CARICAMENTO JSON ESISTENTE (SE PRESENTE)
# =========================================================
db = {}
if os.path.exists(OUTPUT_JSON):
    with open(OUTPUT_JSON, "r", encoding="utf-8") as f:
        db = json.load(f)

# Per salvare i conteggi dichiarati negli Excel
excel_dati = {}   # struttura: {categoria: {anno: {imprese: X, totale: Y}}}


# =========================================================
# LETTURA DEI FILE EXCEL
# =========================================================
for file in os.listdir(CARTELLA):

# Ignora file temporanei di Excel
    if file.startswith("~$"):
        continue

#  Analizza SOLO i file che iniziano con "credito"
    if not file.lower().startswith("credito"):
        continue

# Accetta solo .xlsx o .xls
    if not file.lower().endswith((".xlsx", ".xls")):
        continue

    tipo, categoria = analizza_nome_file(file)
    percorso_file = os.path.join(CARTELLA, file)

    xls = pd.ExcelFile(percorso_file)

    for foglio in xls.sheet_names:

        anno = estrai_anno(foglio) or estrai_anno(file)

        df = pd.read_excel(percorso_file, sheet_name=foglio, dtype=str)

        df.columns = [str(c).strip().lower() for c in df.columns]

        # -------------------------
        # CALCOLO IMPRESE DA EXCEL
        # -------------------------

        colA = df.columns[0]   # colonna "N."
        colA_values = df[colA].astype(str).str.strip().str.lower()

        # Trova "totali" o "totale"
        idx_totali = colA_values[colA_values.str.contains("total")].index

        if len(idx_totali) > 0:
            riga_totali = idx_totali[0]
            riga_imprese = riga_totali - 1
            try:
                numero_imprese_excel = int(float(str(df.iloc[riga_imprese][colA]).replace(",", ".")))
            except:
                numero_imprese_excel = None
        else:
            numero_imprese_excel = None

        # -------------------------
        # CALCOLO TOTALE DA EXCEL
        # -------------------------

        col_credito_excel = next((c for c in df.columns if "credito" in c), None)
        totale_excel = None

        if col_credito_excel:
            try:
                valori_credito = pd.to_numeric(df[col_credito_excel], errors="coerce")
                totale_excel = float(valori_credito.dropna().iloc[-1])
            except:
                totale_excel = None

        # -------------------------
        # SALVA I DATI DELL’EXCEL
        # -------------------------
        excel_dati.setdefault(categoria, {})
        excel_dati[categoria].setdefault(anno, {
            "imprese": numero_imprese_excel,
            "totale": totale_excel
        })

        # -------------------------
        # IDENTIFICA COLONNE DATI REALI
        # -------------------------
        col_cf = next((c for c in df.columns if "codice" in c and "fiscale" in c), None)
        col_den = next((c for c in df.columns if "denominazione" in c), None)
        col_cred = next((c for c in df.columns if "credito" in c and "concesso" in c), None)

        if not (col_cf and col_den and col_cred):
            print(f" Colonne mancanti in: {file} / {foglio}")
            print(df.columns)
            continue

        # -------------------------
        # RIGHE VALIDE: dalla seconda alla penultima
        # -------------------------
        df_valid = df.iloc[:-1]

        for _, r in df_valid.iterrows():
            cf_raw = r[col_cf]                     # valore letto dalla cella
            cf = normalizza_cf(cf_raw)             # normalizzazione CF

            if not cf:
                # mostra errore a schermo
                print(f" CF INVALIDO: {cf_raw}  in file {file}, foglio {foglio}")

                # scrivi nel log
                with open(LOG_CF_INVALIDI, "a", encoding="utf-8") as flog:
                    flog.write(f"{file} / {foglio} → CF non valido: {cf_raw}\n")

                continue   # NON inserire nel JSON

            denominazione = str(r[col_den]).strip()

            try:
                credito = float(str(r[col_cred]).replace(",", "."))
            except:
                continue  # salta riga sporca

            # -------------------------
            #  COSTRUISCI JSON
            # -------------------------

            if cf not in db:
                db[cf] = {}

            if categoria not in db[cf]:
                db[cf][categoria] = []

            db[cf][categoria].append({
                "tipo": tipo,
                "categoria": categoria,
                "anno": anno,
                "denominazione": denominazione,
                "credito": credito,
                "fonte": f"{file}/{foglio}"
            })


# =========================================================
# SALVATAGGIO JSON
# =========================================================
with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
    json.dump(db, f, indent=4, ensure_ascii=False)


# =========================================================
# GENERAZIONE DUE LOG
# =========================================================

# Calcolo statistiche dal JSON
stat = {}  # {categoria: {anno: {"imprese": set(), "totale": float}}}

for cf, categorie in db.items():
    for categoria, records in categorie.items():
        for record in records:
            anno = record["anno"]
            credito = record["credito"]

            stat.setdefault(categoria, {})
            stat[categoria].setdefault(anno, {"imprese": set(), "totale": 0})

            stat[categoria][anno]["imprese"].add(cf)
            stat[categoria][anno]["totale"] += credito

# Scrittura log con data di creazione
with open(LOG_FILE, "w", encoding="utf-8") as log:

    log.write("LOG CREDITI – riepilogo annuale per categoria\n")
    oggi = datetime.now().strftime("%d/%m/%Y %H:%M")
    log.write(f"Data di creazione del log: {oggi}\n")
    log.write("============================================================\n\n")
    
    for categoria in sorted(stat.keys()):
        for anno in sorted(stat[categoria].keys()):

            json_imprese = len(stat[categoria][anno]["imprese"])
            json_totale = stat[categoria][anno]["totale"]

            imp_excel = excel_dati[categoria][anno]["imprese"]
            tot_excel = excel_dati[categoria][anno]["totale"]

            ok_imp = (json_imprese == imp_excel)
            ok_tot = (tot_excel is not None and abs(json_totale - tot_excel) < 0.01)

            log.write(f"CATEGORIA: {categoria.upper()} – ANNO {anno}\n")
            log.write("------------------------------------------------------------\n")

            log.write(f"Imprese JSON: {json_imprese}\n")
            log.write(f"Imprese Excel: {imp_excel}\n")
            log.write(f"➥ Coerenza imprese: {'✔ OK' if ok_imp else ' DIFFERENZA'}\n\n")

            log.write(f"Credito totale JSON: {json_totale:,.2f} €\n")
            log.write(f"Credito totale Excel: {tot_excel:,.2f} €\n")
            log.write(f"➥ Coerenza credito: {'✔ OK' if ok_tot else ' DIFFERENZA'}\n\n")

            if ok_imp and ok_tot:
                log.write("✔ Dati perfettamente coerenti con Excel\n")
            else:
                log.write(" Attenzione: differenze rilevate\n")

            log.write("\n\n")

print(" JSON generato correttamente:", OUTPUT_JSON)
print(" LOG generato correttamente:", LOG_FILE)
print(" LOG CF INVALIDI generato:", LOG_CF_INVALIDI)