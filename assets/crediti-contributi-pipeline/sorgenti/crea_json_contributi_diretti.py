import os
import json
import pandas as pd
import re
from datetime import datetime

# =========================================================
# PERCORSI
# =========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXCEL_DIR = os.path.join(BASE_DIR, "excel")
LOG_DIR = os.path.join(BASE_DIR, "log")

os.makedirs(LOG_DIR, exist_ok=True)

INPUT_EXCEL = os.path.join(EXCEL_DIR, "contributi Diretti.xlsx")
OUTPUT_JSON = os.path.join(BASE_DIR, "db_contributi_diretti.json")
LOG_FILE = os.path.join(LOG_DIR, "log_contributi_diretti.txt")

# =========================================================
# FUNZIONI
# =========================================================

def pulisci_cf(val):
    if val is None:
        return None
    return str(val).replace("_x000D_", "").replace("\n", "").replace("\r", "").strip()

def cf_valido(cf):
    if not cf:
        return False
    if re.match(r"^EST\d{2}_.+", cf):
        return True
    return len(cf) in (11, 16)

def split_testate(val):
    if pd.isna(val):
        return []
    return [t.strip() for t in str(val).split("-") if t.strip()]

def riga_valida(row):
    if pd.isna(row.get("N.")):
        return False
    if not str(row["N."]).isdigit():
        return False
    if str(row.get("Denominazione", "")).lower() in ("totale", "totali"):
        return False
    return True

def converti_importo(val):
    if pd.isna(val):
        return 0.0
    if isinstance(val, (int, float)):
        return float(val)
    s = str(val).strip()
    if "," in s:
        s = s.replace(".", "").replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return 0.0

# =========================================================
# LETTURA EXCEL
# =========================================================

df = pd.read_excel(INPUT_EXCEL)
df = df.iloc[:-1]
df = df[df.apply(riga_valida, axis=1)]

# colonne "Anno XXXX"
anno_cols = [c for c in df.columns if isinstance(c, str) and c.startswith("Anno")]
anno_map = {c: int(re.search(r"\d{4}", c).group()) for c in anno_cols}

# print(df[anno_cols].dtypes)
# print(df[anno_cols].head(5))

# =========================================================
# CONVERSIONE IMPORTI (UNA SOLA VOLTA)
# =========================================================

for col in anno_cols:
    df[col] = df[col].apply(converti_importo)

# =========================================================
# COSTRUZIONE JSON
# =========================================================

db = {}
righe = 0

for _, row in df.iterrows():

    cf = pulisci_cf(row.get("Codice Fiscale"))
    if not cf_valido(cf):
        continue

    db.setdefault(cf, {}).setdefault("contributi_diretti", [])

    for col, anno in anno_map.items():
        db[cf]["contributi_diretti"].append({
            "tipo": "contributi diretti",
            "categoria": row.get("Categoria"),
            "anno": anno,
            "denominazione": row.get("Denominazione"),
            "testate": split_testate(row.get("Testata")),
            "solo_digitale": str(row.get("Solo digitale", "")).lower() == "solo digitale",
            "importo": row[col],
            "fonte": "contributi Diretti.xlsx"
        })
        righe += 1

# =========================================================
# SALVATAGGIO JSON
# =========================================================

with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
#   print("MAX IMPORTI:")
#    print(df[anno_cols].max())
    json.dump(db, f, ensure_ascii=False, indent=2)

# =========================================================
# LOG DI CONFRONTO EXCEL vs JSON
# =========================================================

from collections import defaultdict

log_path = LOG_FILE

# ---- Aggregazione JSON ----
# json_aggr = defaultdict(lambda: {"imprese": set(), "totale": 0.0})

# for cf, blocco in db.items():
#    for r in blocco["contributi_diretti"]:
#        key = (r["categoria"], r["anno"])
#        json_aggr[key]["imprese"].add(cf)
#        json_aggr[key]["totale"] += r["importo"]

json_aggr = defaultdict(lambda: {
    "imprese": set(),
    "imprese_zero": set(),
    "totale": 0.0
})

for cf, blocco in db.items():
    for r in blocco["contributi_diretti"]:
        key = (r["categoria"], r["anno"])
        json_aggr[key]["imprese"].add(cf)

        if r["importo"] == 0:
            json_aggr[key]["imprese_zero"].add(cf)
        else:
            json_aggr[key]["totale"] += r["importo"]

# ---- Aggregazione EXCEL ----
excel_aggr = defaultdict(lambda: {"imprese": set(), "totale": 0.0})

for _, row in df.iterrows():
    cf = pulisci_cf(row["Codice Fiscale"])
    if not cf_valido(cf):
        continue

    for col, anno in anno_map.items():
        if row[col] != 0:
            key = (row["Categoria"], anno)
            excel_aggr[key]["imprese"].add(cf)
            excel_aggr[key]["totale"] += row[col]

# ---- Scrittura log ----
with open(log_path, "w", encoding="utf-8") as log:

    log.write("LOG CONFRONTO CONTRIBUTI DIRETTI – EXCEL vs JSON\n")
    log.write(f"Data: {datetime.now():%d/%m/%Y %H:%M}\n")
    log.write("=" * 70 + "\n\n")

    tutte_le_chiavi = sorted(set(excel_aggr) | set(json_aggr))

    for categoria, anno in tutte_le_chiavi:

        ex = excel_aggr.get((categoria, anno), {"imprese": set(), "totale": 0.0})
        js = json_aggr.get((categoria, anno), {"imprese": set(), "totale": 0.0})

        log.write(f"CATEGORIA: {categoria} – ANNO {anno}\n")
        log.write("-" * 70 + "\n")

#        log.write(f"Imprese Excel: {len(ex['imprese'])}\n")
#        log.write(f"Imprese JSON : {len(js['imprese'])}\n")

#        log.write(f"Totale Excel: {ex['totale']:,.2f} €\n")
#        log.write(f"Totale JSON : {js['totale']:,.2f} €\n")

#        if (
#            len(ex["imprese"]) == len(js["imprese"])
#            and abs(ex["totale"] - js["totale"]) < 0.01
#        ):
#            log.write("➥ CONFRONTO: ✔ OK\n")
#        else:
#            log.write("➥ CONFRONTO: DIFFERENZA\n")

        log.write(f"Imprese Excel: {len(ex['imprese'])}\n")

        num_json = len(js["imprese"])
        num_zero = len(js["imprese_zero"])

        if num_zero > 0:
            log.write(
                f"Imprese JSON : {num_json} (di cui {num_zero} a zero)\n"
            )
        else:
            log.write(f"Imprese JSON : {num_json}\n")

        log.write(f"Totale Excel: {ex['totale']:,.2f} €\n")
        log.write(f"Totale JSON : {js['totale']:,.2f} €\n")

        if (
            len(ex["imprese"]) == (num_json - num_zero)
            and abs(ex["totale"] - js["totale"]) < 0.01
        ):
            log.write("CONFRONTO: ✔ OK\n")
        else:
            log.write("CONFRONTO:  DIFFERENZA\n")

        log.write("\n")

# =========================================================

print("JSON generato:", OUTPUT_JSON)
print("LOG generato:", LOG_FILE)