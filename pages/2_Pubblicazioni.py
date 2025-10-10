import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Pubblicazioni", page_icon="📚")
st.title("Pubblicazioni")

# Pulsante per il profilo generale
ACADEMIA_URL = "https://independent.academia.edu/FabianiUlisse"
st.link_button("📚 Vai al mio profilo su Academia.edu", ACADEMIA_URL)

st.divider()

# Elenco con link diretti alle pubblicazioni
st.markdown(
    """
    - [**Spatial research and geomatic resources applied to the archaeology of the Farafra Oasis**](https://www.academia.edu/5109115/Spatial_research_and_geomatic_resources_applied_to_the_archaeology_of_the_Farafra_Oasis)
    1 [**Titolo pubblicazione 2**](https://www.academia.edu/link_pubblicazione_2)
    1 [**   M. G. CRESPI, FABIANI U. . Metodologie geomatiche per la referenziazione delle informazioni archeologiche. In Atlas of Ancient Rome. Biography and Portraits of the City a cura di A. Carandini, Mondadori Electa Roma 2012, tradotto in The Atlas of Ancient Rome: Biography and Portraits of the City Princeton University Press, Princeton 2017.**]()
    2 [**   P. CARAFA, M. G. CRESPI, M. T. D’ALESSIO, FABIANI U.. L'utilizzo delle tecnologie geomatiche e la Forma Urbis: un nuovo approccio. In Bullettino della Commissione Archeologica Comunale di Roma, CXII 2011.**](https://www.academia.edu/5109115/Spatial_research_and_geomatic_resources_applied_to_the_archaeology_of_the_Farafra_Oasis)
    3 [**   FABIANI U., G. LUCARINI. Risorse geomatiche applicate all'indagine archeologica nell'Oasi di Farafra. In Rivista di Scienze Preistoriche, LX - 2010, 331-347.**]()
    4.[**   B. E. BARICH, M. G. CRESPI,   FABIANI U., G. LUCARINI. Tecniche geomatiche applicate alla ricerca archeologica   in ambienti   desertici: il caso della Missione Archeologica Italiana nell'Oasi di Farafra (Egitto). 13º Conferenza ASITA (Federazione delle Associazioni Scientifiche per le Informazioni Territoriali e Ambientali). Bari (Italia), Dicembre 2009.**]()
    5.[**   B. E. BARICH, M. G. CRESPI, FABIANI U., G. LUCARINI, (in press) Geomatics resources for archeological survey in desert areas - Someprospects from Farafra Oasis. Dakhleh Oasis Project Sixth International Conference. New Perspectives on the Western Desert of Egypt. Università del Salento - Monash University - New York University, Lecce (Italia), Settembre 2009.**]()
    6.[**	FABIANI U., F. FRAIOLI (2010). Sull’allineamento del Tempio di Venere e Roma. In: AIAC XVII CONGRESSO INTERNAZIONALE DIARCHEOLOGIA CLASSICA.ROMA, 22-26 SETTEMBRE 2008.**] (http://www.fastionline.org/docs/FOLDER-it-2010-193.pdf)
    7.[**	F. CATALLI, FABIANI U., A. MAZZONI, P. PACCHIAROTTI (2009). Regio XIV, Transtiberim. Nuovi dati per la ricostruzione del paesaggio urbano antico. In: AIAC XVII Congresso Internazionale di Archeologia Classica. ROMA, 22-26 SETTEMBRE 2008.**](http://www.fastionline.org/docs/FOLDER-it-2009-163.pdf)
    8.[**	V. BAIOCCHI,  FABIANI U.,  A.  MAZZONI,  G.  PIETRANTONIO,  F.  RIGUZZI  (2008).  Morphological  updating  on  the  basis  of  integrated DTMs: study on the Albano and Nemi craters. JOURNAL OF APPLIED GEODESY, vol. 2, ISSN: 1862-9016.**]()
    9.[**	V. BAIOCCHI, M. ANZIDEI, A. ESPOSITO, FABIANI U., G. PIETRANTONIO, F. RIGUZZI  (2007). Intégrer bathymétrie et lidar.GÉOMATIQUE EXPERT, ISSN: 1620 4859.**]()
    10.[**	BAIOCCHI V, FABIANI U., MAZZONI A, PIETRANTONIO G, RIGUZZI F (2007). Integrated DTM of the Albano and Nemi craters (central Italy) permit morphological updates. JOURNAL OF VOLCANOLOGY AND GEOTHERMAL RESEARCH, ISSN: 0377-0273.**]()
    11.[**	D. COLMANO, M. CRESPI, FABIANI U., W. MAIER, M. ZEBISCH (2007). Quality assessment of commercially available DEMs in mountain areas ”. In: 27° Earsel Symposium, Bolzano 8-9 giugno 2007.**]()
    12.[**	M. G. CRESPI, FABIANI U., F. FRATARCANGELI, F. GIANNONE (2007). Orthorectification of high resolution satellite imagery for land management in high mountain area: the impact of DEM accuracy. In: Workshop: Applied Remote Sensing in Mountain Regions. EURAC, Bolzano, Italy, 01-02 Febraury 2007.**]()
    13.[**	M. G. CRESPI, L. DE VENDICTIS, FABIANI U., L. LUZIETTI, A. MAZZONI (2006). The archaeological information system of theunderground of rome: a challenging proposal for the next future. ARCHAEOLOGICAL COMPUTING NEWSLETTER, ISSN: 0952-3332.**]()
    14.[**	V. BAIOCCHI, F. DEL GUZZO, D. DOMINICI, FABIANI U., A. LA NAVE (2006). Utilisation des images satellites àhaute résolution pour lasurveillance d’une zone côtière. GÉOMATIQUE EXPERT, ISSN: 1620 4859.**]()
    15.[**	V. BAIOCCHI, M. ANZIDEI, FABIANI U., A. ESPOSITO, G. PIETRANTONIO, F. RIGUZZI (2006). Integrazione di rilievi batimetrici e laser scanner aereo nell’area dei Colli Albani. In: ASITA. BOLZANO, 14-17 NOVEMBRE 2006.**]()
    16.[**	V. BAIOCCHI, FABIANI U., M. MEZZAPESA, P. SABURRI (2006). Metodi e modelli di trasformazione di coordinate e di datum per ilterritorio nazionale. In: ATTI 10 CONFERENZA NAZIONALE ASITA. BOLZANO, 14-17 NOVEMBRE 2006.**]()
    17.[**	M. G. CRESPI, L. DE VENDICTIS, FABIANI U., L. LUZIETTI, A. MAZZONI (2006). Applicazioni nel campo del posizionamento di precisione in tempo reale supportato da una rete di stazioni permanenti GNSS: Resnap GPS e l’esperienza nel Lazio. In: ASITA. BOLZANO, 14-18 NOVEMBRE.**]()
    18.[**	V. BAIOCCHI, M. G. CRESPI, FABIANI U., P. MACCIACCHERA, M. NEGRETTI, P. ZATELLI (2005). Implementation of datumtransformations for the italian territory in grass: methodology, problems and experiments. GEOMATICS WORKBOOKS, vol. 5, ISSN: 1591-092X.**]()
    19.[**  M. G. CRESPI, L. DE, VENDICTIS, FABIANI U., L. LUZIETTI, A, MAZZONI (2005). The Archaeological information system of theunderground of Rome: a challenging proposal for the next future. In XX CIPA International Symposium Torino 27 settembre - 01 ottobre 2005.**]()
    20.[**	M. G. CRESPI, L. DE VENDICTIS, FABIANI U., L. LUZIETTI, A. MAZZONI (2005). Un sistema informativo territoriale globale per la gestione dei dati di scavo di Roma: una proposta operativa. In: Convegno Nazionale SIFET (Società Fotogrammetria e Topografia) Mondello (Palermo) dal 29/06 al 01/07  2005.**]()
    21.[**	M. G. CRESPI, T. FABIANI, FABIANI U., U. FILOSCIA (2005). Trasformazione di datum e sistemi cartografici per file di cartografia numerica: la conversione della cartografia di Roma dal sistema GAUSS-BOAGA al sistema UTM-WGS84-ETRF89. In: ASITA. CATANIA, 15-18NOVEMBRE.**]()
    22.[**	V. BAIOCCHI, FABIANI U., L.LISO, S. MASCIA, E. TANGA (2005). Studio della possibilità di applicazione della “smart station” permonitoraggi ambientali. In: ASITA. CATANIA, 14-17 NOVEMBRE 2005.**]()
    23.[**  M. G. CRESPI, L. DE VENDICTIS, FABIANI U., A. MAZZONI (2005). Integration of GPS kinematic surveys and orthorectified high resolution satellite imagery for roads cadastre purposes. In: Workshop on 3D Digital Imaging and Modeling. Padova, 17-18 May 2005.**]()
    24.[**	FABIANI U. (2003). Il percorso della via Valeria antica nel territorio di Aequa. AEQUA, vol. 13, ISSN: 1825-9804.**]()
    25.[**  FABIANI U. (2002). I due miliari XXXVIII della Valeria ad Arsoli. AEQUA, vol. 11, ISSN: 1825-9804.**]()  
    """,
    unsafe_allow_html=True
)

# Pulsante per scaricare elenco completo
pubs_path = Path("assets/pubblicazioni.pdf")
if pubs_path.exists():
    st.download_button(
        "⬇️ Scarica elenco completo",
        data=pubs_path.read_bytes(),
        file_name=pubs_path.name,
        mime="application/pdf"
    )
else:
    st.caption("Carica il file `assets/pubblicazioni.pdf` per attivare il download.")