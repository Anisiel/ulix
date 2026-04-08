import os
import json
from datetime import datetime
from collections import defaultdict

# =========================================================
# PERCORSI
# =========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FILE_CREDITI = os.path.join(BASE_DIR, "db_crediti.json")
FILE_CONTRIBUTI = os.path.join(BASE_DIR, "db_contributi.json")
FILE_CONTRIBUTI_DIRETTI = os.path.join(BASE_DIR, "db_contributi_diretti.json")
FILE_UNICO = os.path.join(BASE_DIR, "db_unico.json")

LOG_DIR = os.path.join(BASE_DIR, "log")
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "log_unito.txt")

# =========================================================
# FUNZIONE MERGE DATABASE
# =========================================================

def merge_database(*db_list):
    """
    Unisce più database con chiave = codice fiscale.
    Ogni CF contiene categorie → liste di record.
    """
    db = {}

    for sorgente in db_list:
        for cf, categorie in sorgente.items():
            db.setdefault(cf, {})
            for cat, records in categorie.items():
                db[cf].setdefault(cat, [])
                db[cf][cat].extend(records)

    return db

# =========================================================
# CARICAMENTO FILE JSON
# =========================================================

def carica_json(path):
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

db_crediti = carica_json(FILE_CREDITI)
db_contributi = carica_json(FILE_CONTRIBUTI)
db_contributi_diretti = carica_json(FILE_CONTRIBUTI_DIRETTI)

# =========================================================
# UNIONE DATABASE
# =========================================================

db_unito = merge_database(
    db_crediti,
    db_contributi,
    db_contributi_diretti
)

# =========================================================
# SALVATAGGIO DATABASE UNICO
# =========================================================

with open(FILE_UNICO, "w", encoding="utf-8") as f:
    json.dump(db_unito, f, indent=4, ensure_ascii=False)

# =========================================================
# COSTRUZIONE STATISTICHE LOG
# =========================================================

stats = defaultdict(lambda: defaultdict(lambda: {
    "imprese": set(),
    "totale": 0.0
}))

# insiemi per analisi finali
cf_crediti = set()
cf_contributi = set()
cf_contributi_diretti = set()

for cf, categorie in db_unito.items():

    ha_crediti = False
    ha_contributi = False
    ha_contributi_diretti = False

    for categoria, records in categorie.items():
        for rec in records:

            anno = rec["anno"]
            tipo = rec.get("tipo", "sconosciuto")

            # =========================
            # CREDITI
            # =========================
            if tipo == "credito":
                valore = float(rec.get("credito", 0.0))
                categoria_log = f"credito {categoria}"

                stats[categoria_log][anno]["imprese"].add(cf)
                stats[categoria_log][anno]["totale"] += valore
                ha_crediti = True

            # =========================
            # CONTRIBUTI (NON DIRETTI)
            # =========================
            elif tipo == "contributo":
                valore = float(rec.get("importo", 0.0))
                categoria_log = f"contributo {categoria}"

                stats[categoria_log][anno]["imprese"].add(cf)
                stats[categoria_log][anno]["totale"] += valore
                ha_contributi = True

            # =========================
            # CONTRIBUTI DIRETTI
            #  SOLO SE importo > 0
            # =========================
            elif tipo == "contributi diretti":
                valore = float(rec.get("importo", 0.0))

            # contiamo SOLO contributi diretti con importo positivo
                if valore > 0:
                    categoria_log = f"contributi diretti {categoria}"

                    stats[categoria_log][anno]["imprese"].add(cf)
                    stats[categoria_log][anno]["totale"] += valore
                    ha_contributi_diretti = True

    if ha_crediti:
        cf_crediti.add(cf)
    if ha_contributi:
        cf_contributi.add(cf)
    if ha_contributi_diretti:
        cf_contributi_diretti.add(cf)

# =========================================================
# CALCOLO TOTALI ANNUALI CONTRIBUTI DIRETTI
# (da db_contributi_diretti.json)
# =========================================================

totali_annuali_diretti = defaultdict(float)

for _, dati_cf in db_contributi_diretti.items():
    if "contributi_diretti" not in dati_cf:
        continue

    for rec in dati_cf["contributi_diretti"]:
        if rec.get("tipo") == "contributi diretti":
            anno = rec.get("anno")
            importo = float(rec.get("importo", 0))

            if importo > 0:
                totali_annuali_diretti[anno] += importo

# =========================================================
# SCRITTURA LOG
# =========================================================

with open(LOG_FILE, "w", encoding="utf-8") as log:

    log.write("LOG DATABASE UNIFICATO – CREDITI + CONTRIBUTI + CONTRIBUTI DIRETTI\n")
    log.write("=" * 60 + "\n")
    log.write(f"Data generazione: {datetime.now():%d/%m/%Y %H:%M}\n")
    log.write("=" * 60 + "\n\n")

    log.write(f"Totale imprese censite: {len(db_unito)}\n\n")

    categorie_trovate = sorted(stats.keys())

    log.write("Categorie presenti nel database unificato:\n")
    for cat in categorie_trovate:
        log.write(f"- {cat}\n")
    log.write("\n")

    log.write("=" * 60 + "\n")
    log.write("DETTAGLIO PER CATEGORIA E ANNO\n")
    log.write("=" * 60 + "\n\n")

    for cat in categorie_trovate:
        log.write(f"CATEGORIA: {cat.upper()}\n")
        log.write("-" * 40 + "\n")

        for anno in sorted(stats[cat].keys()):
            numero_imprese = len(stats[cat][anno]["imprese"])
            totale = stats[cat][anno]["totale"]

            log.write(f"Anno {anno}\n")
            log.write(f" - Imprese coinvolte: {numero_imprese}\n")

        #    if cat.startswith("contributi diretti"):
        #        log.write(f" - Totale contributi diretti: {totale:,.2f} €\n\n")
        #    else:
        #        log.write(f" - Totale importi: {totale:,.2f} €\n\n")


            if cat.startswith("contributi diretti"):
                log.write(f" - Imprese beneficiarie (importo > 0): {numero_imprese}\n")
                log.write(f" - Totale contributi diretti: {totale:,.2f} €\n\n")
            else:
                log.write(f" - Totale importi: {totale:,.2f} €\n\n")    
        
        log.write("\n")

    # =====================================================
    # SEZIONI FINALI RICHIESTE
    # =====================================================

    log.write("=" * 60 + "\n")
    log.write("ANALISI TRASVERSALI IMPRESE\n")
    log.write("=" * 60 + "\n\n")

    int_1 = cf_crediti & cf_contributi
    log.write("IMPRESE CHE PRENDONO CREDITI E CONTRIBUTI\n")
    log.write(f"Totale: {len(int_1)}\n\n")

    int_2 = cf_crediti & cf_contributi_diretti
    log.write("IMPRESE CHE PRENDONO CREDITI E CONTRIBUTI DIRETTI\n")
    log.write(f"Totale: {len(int_2)}\n\n")

    int_3 = cf_contributi & cf_contributi_diretti
    log.write("IMPRESE CHE PRENDONO CONTRIBUTI E CONTRIBUTI DIRETTI\n")
    log.write(f"Totale: {len(int_3)}\n\n")

# =========================================================
# FINE
# =========================================================

print(" JSON unificato creato:", FILE_UNICO)
print(" Log unificato creato :", LOG_FILE)