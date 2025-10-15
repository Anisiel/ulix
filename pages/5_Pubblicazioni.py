import streamlit as st
import pandas as pd
from pathlib import Path

# Configura la pagina
st.set_page_config(page_title="Pubblicazioni", page_icon="📚")
st.title("📚 Pubblicazioni")

st.markdown("""
In fondo alla pagina puoi scaricare l'elenco completo delle mie pubblicazioni oppure stampare la pagina.
""", unsafe_allow_html=True)

# Pulsante per il profilo su Academia.edu
ACADEMIA_URL = "https://independent.academia.edu/FabianiUlisse"
st.link_button("🔗 Vai al mio profilo su Academia.edu", ACADEMIA_URL)

st.divider()

# Percorso del file CSV
file_path = Path("repo/pubblicazioni.csv")

if file_path.exists():
    # Leggi il CSV
    df = pd.read_csv(file_path, sep=";", encoding="utf-8")
    
    # Filtri interattivi
    anni = sorted(df["ANNO"].dropna().unique())
    anno_sel = st.multiselect("Filtra per anno", anni, default=anni)
    
    temi = sorted(df["TEMA"].dropna().unique())
    tema_sel = st.multiselect("Filtra per tema", temi, default=temi if temi else [])
    
    # Applica filtri
    df_filtrato = df[(df["ANNO"].isin(anno_sel)) & (df["TEMA"].isin(tema_sel) if tema_sel else True)]
    
    # Mostra tabella
    st.dataframe(df_filtrato, use_container_width=True)
    
    # Mostra pubblicazioni in formato leggibile
    st.markdown("# 📖 Elenco dettagliato")
    for _, row in df_filtrato.iterrows():
        st.markdown(f"""
        **{row['AUTORI']}**  
        *{row['TITOLO']}*  
        {row['ARTICOLO RIVISTA [AR] / ARTICOLO LIBRO [AL]']}  
        **Anno:** {row['ANNO']}  
        🔗 [Link]({row['LINK']})
        ---
        """, unsafe_allow_html=True)
else:
    st.warning("⚠️ Impossibile trovare il file delle pubblicazioni. Carica `repo/pubblicazioni.csv`.")

# Download PDF se disponibile
pdf_path = Path("assets/papers/pubblicazioni.pdf")
if pdf_path.exists():
    st.download_button(
        "⬇️ Scarica elenco completo",
        data=pdf_path.read_bytes(),
        file_name=pdf_path.name,
        mime="application/pdf"
    )
else:
    st.caption("📄 Carica il file `assets/papers/pubblicazioni.pdf` per attivare il download.")

st.divider()

# Pulsante stampa
st.markdown("""
<button onclick="window.print()" style="padding:8px 16px; font-size:16px;">
🖨️ Stampa questa pagina
</button>
""", unsafe_allow_html=True)