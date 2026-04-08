import os
import json
import pandas as pd
import re
from datetime import datetime

# =========================================================
# CONFIGURAZIONE PERCORSI RELATIVI PER TEST
# =========================================================
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# EXCEL_DIR = os.path.join(BASE_DIR, "excel")
# OUTPUT_JSON = os.path.join(BASE_DIR, "db_contributi.json")

# LOG_DIR = os.path.join(BASE_DIR, "log")
# os.makedirs(LOG_DIR, exist_ok=True)
# LOG_FILE = os.path.join(LOG_DIR, "log_contributi.txt")
# LOG_CF_INVALIDI = os.path.join(LOG_DIR, "log_contributi_cfinvalidi.txt")


# =========================================================
# CONFIGURAZIONE PERCORSI (ASSOLUTI)
# =========================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # per lanciare i programmi da qualsiasi cartella

EXCEL_DIR = os.path.join(BASE_DIR, "excel")
OUTPUT_JSON = os.path.join(BASE_DIR, "db_contributi.json")

LOG_DIR = os.path.join(BASE_DIR, "log")
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "log_contributi.txt")
LOG_CF_INVALIDI = os.path.join(LOG_DIR, "log_invalidi_contributi.txt")


# Svuota il log CF invalidi ad ogni esecuzione
with open(LOG_CF_INVALIDI, "w", encoding="utf-8") as f:
    f.write("LOG CODICI FISCALI INVALIDI (CONTRIBUTI)\n")
    f.write("======================================\n\n")

# =========================================================
# PULISCI_CF → rimuove _x000D_, newline, carriage return
# =========================================================
def pulisci_cf(raw):
    if raw is None:
        return None
    s = str(raw)
    s = s.replace("_x000D_", "")
    s = s.replace("\r", "")
    s = s.replace("\n", "")
    return s.strip()


# =========================================================
# NORMALIZZA_CF
# =========================================================
def normalizza_cf(val):
    """
    Normalizza e valida CF / P.IVA.
    """
    if val is None:
        return None

    s = str(val).strip()

    # Rimuovi .0 o ,0
    if s.endswith(".0") or s.endswith(",0"):
        s = s[:-2]

    # Solo alfanumerico
    s = re.sub(r"[^A-Za-z0-9]", "", s).upper()

    # P.IVA → 11 cifre
    if len(s) == 11 and s.isdigit():
        return s

    # CF persona → 16 alfanumerico
    if len(s) == 16 and s.isalnum():
        return s

    return None


# =========================================================
# Reset JSON contributi
# =========================================================
if os.path.exists(OUTPUT_JSON):
    os.remove(OUTPUT_JSON)

db = {}
excel_info = {}     # {categoria: {anno: {imprese, totale}}}


# =========================================================
# FUNZIONI UTILI
# =========================================================
def estrai_anno(nome):
    m = re.search(r"(20\d{2})", nome)
    return int(m.group(1)) if m else None


# =========================================================
# LETTURA FILE EXCEL CONTRIBUTI
# =========================================================
for file in os.listdir(EXCEL_DIR):

    if file.startswith("~$"):
        continue

    # Solo file che iniziano con contributo
    if not file.lower().startswith("contributo"):
        continue

    if not file.lower().endswith(".xlsx"):
        continue

    # categoria = seconda parola
    base = os.path.splitext(file)[0].lower()
    parti = re.split(r"[_\s]+", base)
    categoria = parti[1] if len(parti) > 1 else "generico"

    percorso = os.path.join(EXCEL_DIR, file)
    xls = pd.ExcelFile(percorso)

    for foglio in xls.sheet_names:

        anno = estrai_anno(foglio) or estrai_anno(file)
        if not anno:
            continue

        # IMPORTANTE: leggere tutto come stringa
        df = pd.read_excel(percorso, sheet_name=foglio, dtype=str)

        df.columns = [str(c).strip().lower() for c in df.columns]

        # colonne obbligatorie
        col_n = df.columns[0]
        col_cf = next((c for c in df.columns if "codice" in c and "fiscale" in c), None)
        col_den = next((c for c in df.columns if "denominazione" in c), None)
        col_imp = next((c for c in df.columns if "importo concesso" in c), None)

        if not (col_cf and col_den and col_imp):
            print(f"⚠ Colonne mancanti in: {file} / {foglio}")
            print(df.columns)
            continue

        # trova riga totale
        colA_values = df[col_n].astype(str).str.lower()
        idx_tot = colA_values[colA_values.str.contains("total")].index

        if len(idx_tot) == 0:
            print(f"Riga TOTALI non trovata: {file} / {foglio}")
            continue

        riga_totali = idx_tot[0]

        # numero imprese excel
        try:
            n_imprese = int(float(df[col_n].iloc[riga_totali - 1].replace(",", ".")))
        except:
            n_imprese = None

        # totale excel
        try:
            tot_excel = float(str(df[col_imp].iloc[riga_totali]).replace(",", "."))
        except:
            tot_excel = None

        excel_info.setdefault(categoria, {})
        excel_info[categoria][anno] = {
            "imprese": n_imprese,
            "totale": tot_excel
        }

        # righe valide
        df_valid = df.iloc[:riga_totali]

        for _, r in df_valid.iterrows():

            cf_raw = pulisci_cf(r[col_cf])
            cf = normalizza_cf(cf_raw)

            if not cf:
                print(f" CF INVALIDO: {cf_raw}  in file {file}, foglio {foglio}")
                with open(LOG_CF_INVALIDI, "a", encoding="utf-8") as flog:
                    flog.write(f"{file} / {foglio} → CF non valido: {cf_raw}\n")
                continue

            denominazione = str(r[col_den]).strip()

            try:
                importo = float(str(r[col_imp]).replace(",", "."))
            except:
                continue

            if cf not in db:
                db[cf] = {}

            if categoria not in db[cf]:
                db[cf][categoria] = []

            db[cf][categoria].append({
                "tipo": "contributo",
                "categoria": categoria,
                "anno": anno,
                "denominazione": denominazione,
                "importo": importo,
                "fonte": f"{file}/{foglio}"
            })


# =========================================================
# SALVA JSON
# =========================================================
with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
    json.dump(db, f, indent=4, ensure_ascii=False)


# =========================================================
# LOG CONTRIBUTI
# =========================================================
stats = {}

for cf, cats in db.items():
    for categoria, records in cats.items():
        for rec in records:
            anno = rec["anno"]
            imp = rec["importo"]

            stats.setdefault(categoria, {})
            stats[categoria].setdefault(anno, {"imprese": set(), "totale": 0})

            stats[categoria][anno]["imprese"].add(cf)
            stats[categoria][anno]["totale"] += imp

with open(LOG_FILE, "w", encoding="utf-8") as log:

    log.write("LOG CONTRIBUTI – riepilogo annuale per categoria\n")
    oggi = datetime.now().strftime("%d/%m/%Y %H:%M")
    log.write(f"Data creazione: {oggi}\n")
    log.write("============================================================\n\n")

    for categoria in sorted(stats.keys()):
        for anno in sorted(stats[categoria].keys()):
            imp_json = len(stats[categoria][anno]["imprese"])
            tot_json = stats[categoria][anno]["totale"]

            imp_excel = excel_info[categoria][anno]["imprese"]
            tot_excel = excel_info[categoria][anno]["totale"]

            ok_imp = (imp_json == imp_excel)
            ok_tot = (tot_excel is not None and abs(tot_json - tot_excel) < 0.01)

            log.write(f"CATEGORIA: {categoria.upper()} – ANNO {anno}\n")
            log.write("------------------------------------------------------------\n")
            log.write(f"Imprese JSON: {imp_json}\n")
            log.write(f"Imprese Excel: {imp_excel}\n")
            log.write(f"➥ Coerenza imprese: {'✔ OK' if ok_imp else '❌ DIFFERENZA'}\n\n")

            log.write(f"Totale JSON: {tot_json:,.2f} €\n")
            log.write(f"Totale Excel: {tot_excel:,.2f} €\n")
            log.write(f"➥ Coerenza totale: {'✔ OK' if ok_tot else '❌ DIFFERENZA'}\n\n\n")

print("JSON contributi generato:", OUTPUT_JSON)
print("LOG contributi generato:", LOG_FILE)
print("LOG CF INVALIDI generato:", LOG_CF_INVALIDI)