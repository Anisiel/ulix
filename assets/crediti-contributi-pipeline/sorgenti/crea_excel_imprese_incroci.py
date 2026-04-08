import json
import os
import pandas as pd
from collections import defaultdict

# =========================================================
# PERCORSI
# =========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_DB = os.path.join(BASE_DIR, "db_unico.json")

OUTPUT_FOLDER = os.path.join(BASE_DIR, "incroci_contributi_crediti")
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

OUTPUT_XLSX = os.path.join(
    OUTPUT_FOLDER,
    "imprese_crediti_contributi.xlsx"
)

# =========================================================
# CARICAMENTO DATABASE JSON
# =========================================================

with open(FILE_DB, "r", encoding="utf-8") as f:
    db = json.load(f)

# =========================================================
# STRUTTURA info:
# - per ogni impresa (CF)
# - elenco di:
#   - crediti (per categoria → anni)
#   - contributi (per categoria → anni)
#   - contributi diretti (>0, per categoria → anni)
# =========================================================

info = {}

for cf, categorie in db.items():

    denominazione = None

    crediti = defaultdict(set)
    contributi = defaultdict(set)
    contributi_diretti = defaultdict(set)

    for categoria, records in categorie.items():
        for r in records:

            denominazione = r.get("denominazione", denominazione)
            anno = r.get("anno")
            tipo = r.get("tipo")

            # -------------------------
            # CREDITI
            # -------------------------
            if tipo == "credito":
                nome = r.get("categoria", "Credito non specificato")
                crediti[nome].add(anno)

            # -------------------------
            # CONTRIBUTI (NON DIRETTI)
            # -------------------------
            elif tipo == "contributo":
                nome = r.get("categoria", "Contributo non specificato")
                contributi[nome].add(anno)

            # -------------------------
            # CONTRIBUTI DIRETTI
            # consideriamo SOLO importi > 0
            # -------------------------
            elif tipo == "contributi diretti":
                if float(r.get("importo", 0.0)) > 0:
                    nome = r.get("categoria", "Contributo diretto")
                    contributi_diretti[nome].add(anno)

    info[cf] = {
        "denominazione": denominazione,
        "crediti": crediti,
        "contributi": contributi,
        "contributi_diretti": contributi_diretti
    }

# =========================================================
# COSTRUZIONE DATAFRAME DI BASE (MATRICE INCROCIO)
# =========================================================

def format_dettaglio(d):
    """
    Trasforma un dizionario:
    {categoria: {anni}}
    in stringa leggibile:
    categoria (anno1, anno2)
    """
    parti = []
    for nome, anni in d.items():
        anni_str = ", ".join(map(str, sorted(anni)))
        parti.append(f"{nome} ({anni_str})")
    return " · ".join(parti)

rows = []

for cf, d in info.items():

    ha_crediti = bool(d["crediti"])
    ha_contributi = bool(d["contributi"])
    ha_contributi_diretti = bool(d["contributi_diretti"])

    rows.append({
        "Codice Fiscale": cf,
        "Denominazione": d["denominazione"],

        "Crediti": "SI" if ha_crediti else "NO",
        "Contributi": "SI" if ha_contributi else "NO",
        "Contributi Diretti": "SI" if ha_contributi_diretti else "NO",

        "Dettaglio Crediti":
            format_dettaglio(d["crediti"]) if ha_crediti else "",

        "Dettaglio Contributi":
            format_dettaglio(d["contributi"]) if ha_contributi else "",

        "Dettaglio Contributi Diretti":
            format_dettaglio(d["contributi_diretti"])
            if ha_contributi_diretti else "",

        "Numero Casi":
            sum([ha_crediti, ha_contributi, ha_contributi_diretti])
    })

df_all = pd.DataFrame(rows)


# =========================================================
# FOGLIO 0
# LEGENDA - SPIEGAZIONE DEL CONTENUTO DEL FILE EXCEL
# =========================================================

# Ogni elemento della lista sarà una riga del foglio Excel.
legenda_testi = [

    "LEGENDA DEL FILE \"imprese_crediti_contributi.xlsx\"",

    "",

    "Questo file Excel è generato automaticamente dal sistema a partire "
    "dal database unificato (db_unico.json) che comprende CREDITI, "
    "CONTRIBUTI e CONTRIBUTI DIRETTI.",

    "Il file ha lo scopo di fornire, in un unico strumento, una visione "
    "strutturata, verificabile e analitica di tutte le erogazioni "
    "concesse alle imprese, sia in forma tabellare sia in forma aggregata.",

    "",
    "Il file è suddiviso in più fogli, ciascuno con una funzione precisa. "
    "I fogli NON devono essere modificati manualmente: in caso di modifica "
    "dei file Excel di input, il file va rigenerato tramite "
    "launch_excel.exe.",

    "",
    "DESCRIZIONE DEI FOGLI CONTENUTI NEL FILE",
    "------------------------------------------------------------",

    "",
    "FOGLIO: MATRICE_INCROCIO",

    "Questo foglio contiene una riga per ciascuna impresa presente "
    "nel database. Per ogni impresa viene indicato se ha beneficiato "
    "di CREDITI, CONTRIBUTI e/o CONTRIBUTI DIRETTI (valori SI/NO), "
    "insieme a un dettaglio testuale che indica per quali misure "
    "e per quali anni.",

    "Con questo foglio si risponde alla domanda: "
    "\"Quali imprese hanno beneficiato di quali tipologie di aiuto "
    "e in quali anni?\"",

    "",
    "FOGLI: CREDITI_CONTRIBUTI, CREDITI_CONTRIBUTIDIRETTI, "
    "CONTRIBUTI_CONTRIBUTIDIRETTI",

    "Questi fogli rappresentano sottoinsiemi della matrice generale "
    "e mostrano solo le imprese che ricadono contemporaneamente "
    "in due tipologie di aiuto (ad esempio crediti e contributi).",

    "Con questi fogli si risponde alla domanda: "
    "\"Quali imprese rientrano in specifiche combinazioni di misure?\"",

    "",
    "FOGLIO: STATISTICHE_BASE_POPOLAZIONE",

    "Questo foglio fornisce una descrizione quantitativa della popolazione "
    "di imprese presente nel database: numero totale di imprese, "
    "distribuzione per tipologia di aiuto (crediti, contributi, diretti), "
    "combinazioni tra tipologie e copertura temporale degli anni presenti.",

    "Con questo foglio si risponde alla domanda: "
    "\"Quante imprese sono coinvolte e come sono distribuite rispetto "
    "alle diverse tipologie di aiuto?\"",

    "",
    "FOGLIO: STATISTICHE_BASE_PER_MISURA",

    "Questo foglio analizza ogni singola MISURA (ad esempio credito carta, "
    "contributo copie vendute, contributi diretti) e ne riporta l'importo "
    "totale erogato, il numero di imprese beneficiarie, gli anni di "
    "copertura e indicatori statistici sintetici (media, mediana, massimo).",

    "Con questo foglio si risponde alla domanda: "
    "\"Qual è il peso economico reale di ciascuna misura e "
    "quanto è diffusa tra le imprese?\"",

    "",
    "FOGLIO: STATISTICHE_BASE_TEMPORALI_PER_MISURA",

    "Questo foglio presenta le stesse misure analizzate su base ANNUALE. "
    "Per ogni anno e per ciascuna misura vengono indicati il numero "
    "di imprese beneficiarie e gli importi complessivi.",

    "Con questo foglio si risponde alla domanda: "
    "\"Come evolvono nel tempo le singole misure "
    "e in quali anni hanno maggiore impatto?\"",

    "",
    "FOGLIO: SINTESI_PER_IMPRESA",

    "Questo foglio riporta, per ciascuna impresa, l'importo totale "
    "ricevuto suddiviso per macrotipologia: CREDITI, CONTRIBUTI e "
    "CONTRIBUTI DIRETTI, oltre al totale complessivo.",

    "Con questo foglio si risponde alla domanda: "
    "\"Quanto ha ricevuto complessivamente ciascuna impresa "
    "e da quali tipologie di aiuto?\"",

    "",
    "NOTE FINALI",

    "Il file rappresenta una base di analisi e controllo. "
    "I valori presenti sono coerenti con i report Word "
    "generati dal sistema e con i file di log presenti "
    "nella cartella log/.",

    "In caso di dubbi, anomalie o verifiche, il foglio "
    "STATISTICHE_BASE_PER_MISURA e i file di log costituiscono "
    "il principale riferimento di controllo."
]

# Creiamo un DataFrame a una colonna
df_legenda = pd.DataFrame(
    {"Legenda": legenda_testi}
)

# =========================================================
# FOGLIO 1
# STATISTICHE_BASE_POPOLAZIONE
# =========================================================

pop_stats = []

tot = len(df_all)

pop_stats.append(("Numero totale imprese", tot))
pop_stats.append(("Imprese con almeno un credito",
                  (df_all["Crediti"] == "SI").sum()))
pop_stats.append(("Imprese con almeno un contributo",
                  (df_all["Contributi"] == "SI").sum()))
pop_stats.append(("Imprese con almeno un contributo diretto",
                  (df_all["Contributi Diretti"] == "SI").sum()))

pop_stats.append(("Imprese con crediti + contributi",
                  ((df_all["Crediti"] == "SI") &
                   (df_all["Contributi"] == "SI")).sum()))

pop_stats.append(("Imprese con crediti + contributi diretti",
                  ((df_all["Crediti"] == "SI") &
                   (df_all["Contributi Diretti"] == "SI")).sum()))

pop_stats.append(("Imprese con tutte le tipologie",
                  ((df_all["Crediti"] == "SI") &
                   (df_all["Contributi"] == "SI") &
                   (df_all["Contributi Diretti"] == "SI")).sum()))

pop_stats.append(("Solo crediti",
                  ((df_all["Crediti"] == "SI") &
                   (df_all["Contributi"] == "NO") &
                   (df_all["Contributi Diretti"] == "NO")).sum()))

pop_stats.append(("Solo contributi",
                  ((df_all["Crediti"] == "NO") &
                   (df_all["Contributi"] == "SI") &
                   (df_all["Contributi Diretti"] == "NO")).sum()))

pop_stats.append(("Solo contributi diretti",
                  ((df_all["Crediti"] == "NO") &
                   (df_all["Contributi"] == "NO") &
                   (df_all["Contributi Diretti"] == "SI")).sum()))

# ---- intervallo anni ----
anni_presenti = set()

for categorie in db.values():
    for records in categorie.values():
        for r in records:
            if r.get("anno"):
                anni_presenti.add(r["anno"])

if anni_presenti:
    pop_stats.append(("Anno minimo", min(anni_presenti)))
    pop_stats.append(("Anno massimo", max(anni_presenti)))

df_pop = pd.DataFrame(
    pop_stats,
    columns=["Indicatore", "Valore"]
)

# =========================================================
# FOGLIO 2
# STATISTICHE_BASE_PER_MISURA
# =========================================================

# struttura lunga:
# una riga = (cf, tipo, misura, anno, importo)

records_lunghi = []

for cf, categorie in db.items():
    for records in categorie.values():
        for r in records:

            tipo = r.get("tipo")
            misura = r.get("categoria", "non specificata")
            anno = r.get("anno")

            if tipo == "credito":
                importo = float(r.get("credito", 0.0))

            elif tipo == "contributo":
                importo = float(r.get("importo", 0.0))

            elif tipo == "contributi diretti":
                importo = float(r.get("importo", 0.0))
                if importo <= 0:
                    continue
                # normalizziamo la misura
                misura = "Contributi Diretti"

            else:
                continue

            records_lunghi.append({
                "CF": cf,
                "Tipo": tipo,
                "Misura": misura,
                "Anno": anno,
                "Importo": importo
            })

df_long = pd.DataFrame(records_lunghi)

# raggruppamento per misura
righe_misura = []

for (tipo, misura), g in df_long.groupby(["Tipo", "Misura"]):

    anni = g["Anno"].dropna()

    importi_per_impresa = (
        g.groupby("CF")["Importo"].sum()
    )

    righe_misura.append({
        "Misura": misura,
        "Tipo": tipo,
        "Anno minimo": int(anni.min()),
        "Anno massimo": int(anni.max()),
        "Importo totale": importi_per_impresa.sum(),
        "Imprese uniche": importi_per_impresa.count(),
        "Media per impresa": importi_per_impresa.mean(),
        "Mediana": importi_per_impresa.median(),
        "Importo massimo singola impresa": importi_per_impresa.max()
    })

df_misure = pd.DataFrame(righe_misura)

# =========================================================
# FOGLIO 3
# STATISTICHE_BASE_TEMPORALI_PER_MISURA
# =========================================================

righe_temporali = []

# Raggruppiamo per Anno + Tipo + Misura
for (anno, tipo, misura), g in df_long.groupby(
    ["Anno", "Tipo", "Misura"]
):

    # Importi totali per impresa (in quell'anno, per quella misura)
    importi_per_impresa = (
        g.groupby("CF")["Importo"].sum()
    )

    numero_imprese = importi_per_impresa.count()
    importo_totale = importi_per_impresa.sum()

    # Evitiamo divisioni strane (per sicurezza)
    importo_medio = (
        importo_totale / numero_imprese
        if numero_imprese > 0 else 0
    )

    righe_temporali.append({
        "Anno": int(anno),
        "Misura": misura,
        "Tipo": tipo,
        "Imprese beneficiarie": numero_imprese,
        "Importo totale": importo_totale,
        "Importo medio": importo_medio
    })

df_temporale = pd.DataFrame(righe_temporali)

# Ordinamento logico:
# prima per Anno, poi per Tipo, poi per Misura
df_temporale = df_temporale.sort_values(
    ["Anno", "Tipo", "Misura"]
)

# =========================================================
# FOGLIO 4
# SINTESI_PER_IMPRESA
# =========================================================

righe_impresa = []

# Raggruppiamo tutti i record per impresa (CF)
for cf, g_impresa in df_long.groupby("CF"):

    # Recuperiamo la denominazione dall'oggetto info,
    # che è la fonte "ufficiale" delle anagrafiche
    denominazione = info.get(cf, {}).get("denominazione", "")

    # -------------------------
    # TOTALE CREDITI
    # -------------------------
    tot_crediti = (
        g_impresa[g_impresa["Tipo"] == "credito"]["Importo"].sum()
    )

    # -------------------------
    # TOTALE CONTRIBUTI (NON DIRETTI)
    # -------------------------
    tot_contributi = (
        g_impresa[g_impresa["Tipo"] == "contributo"]["Importo"].sum()
    )

    # -------------------------
    # TOTALE CONTRIBUTI DIRETTI
    # -------------------------
    tot_diretti = (
        g_impresa[g_impresa["Tipo"] == "contributi diretti"]["Importo"].sum()
        if "contributi diretti" in g_impresa["Tipo"].values
        else 0.0
    )

    # -------------------------
    # TOTALE COMPLESSIVO
    # -------------------------
    totale = tot_crediti + tot_contributi + tot_diretti

    righe_impresa.append({
        "Codice Fiscale": cf,
        "Denominazione": denominazione,
        "Totale crediti": tot_crediti,
        "Totale contributi": tot_contributi,
        "Totale contributi diretti": tot_diretti,
        "Totale complessivo": totale
    })

df_sintesi = pd.DataFrame(righe_impresa)

# Ordiniamo per totale complessivo decrescente:
# molto utile per lettura e controlli
df_sintesi = df_sintesi.sort_values(
    "Totale complessivo",
    ascending=False
)

# =========================================================
# FILTRI INCROCI
# =========================================================

df_cred_contr = df_all[
    (df_all["Crediti"] == "SI") &
    (df_all["Contributi"] == "SI")
]

df_cred_contr_dir = df_all[
    (df_all["Crediti"] == "SI") &
    (df_all["Contributi Diretti"] == "SI")
]

df_contr_contr_dir = df_all[
    (df_all["Contributi"] == "SI") &
    (df_all["Contributi Diretti"] == "SI")
]

# =========================================================
# SCRITTURA EXCEL FINALE
# =========================================================

with pd.ExcelWriter(OUTPUT_XLSX, engine="openpyxl") as writer:

    # --- fogli già esistenti ---
    df_all.to_excel(writer, sheet_name="Matrice_Incrocio", index=False)
    df_cred_contr.to_excel(writer, sheet_name="Crediti_Contributi", index=False)
    df_cred_contr_dir.to_excel(
        writer, sheet_name="Crediti_ContributiDiretti", index=False)
    df_contr_contr_dir.to_excel(
        writer, sheet_name="Contributi_ContributiDiretti", index=False)

    # --- NUOVI FOGLI BASE ---
    
    df_legenda.to_excel(
    writer,
    sheet_name="LEGENDA",
    index=False
    )

    df_pop.to_excel(
        writer,
        sheet_name="STATBASE_POPDB",
        index=False
    )

    df_misure.to_excel(
        writer,
        sheet_name="STATBASE_PERMISURA",
        index=False
    )

    df_temporale.to_excel(
    writer,
    sheet_name="STATBASE_TEMP_PERMISURA",
    index=False
    )
    
    df_sintesi.to_excel(
    writer,
    sheet_name="SINTESI_PERIMPRESA",
    index=False
    )

print("Excel creato:", OUTPUT_XLSX)