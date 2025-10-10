import streamlit as st
from pathlib import Path
import base64

BASE_DIR = Path(__file__).resolve().parent
IMMAGINI = [
    {"src": "assets/hero.jpg",  "note": "Mocking Face"},
    {"src": "assets/hero2.jpg", "note": "Le Discret"},
    {"src": "assets/hero3.jpg", "note": "San Govanni Battista"},
]

def to_data_uri(p: Path) -> str:
    data = p.read_bytes()
    ext = p.suffix.lower()
    mime = "image/jpeg" if ext in (".jpg", ".jpeg") else "image/png"
    b64 = base64.b64encode(data).decode()
    return f"data:{mime};base64,{b64}"

def render_gallery_html(items, cols=3, height=240):
    # Prepara i data URI
    enriched = []
    for it in items:
        p = (BASE_DIR / it["src"]).resolve()
        if p.exists():
            enriched.append({**it, "uri": to_data_uri(p)})
    if not enriched:
        st.info("Nessuna immagine trovata.")
        return

    st.markdown("### 🎨 Galleria", unsafe_allow_html=True)

    # CSS (class match corretta: gallery-thumb)
    st.markdown(f"""
    <style>
    .thumb-box {{
        width: 100%;
        height: {height}px;
        overflow: hidden;
        border-radius: 8px;
        background: #eee;
    }}
    .thumb-box > img.gallery-thumb {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
    }}
    </style>
    """, unsafe_allow_html=True)

    # Griglia a righe
    for i in range(0, len(enriched), cols):
        row = enriched[i:i+cols]
        columns = st.columns(len(row), gap="small")
        for col, it in zip(columns, row):
            with col:
                st.markdown(
                f"<div class='thumb-box'><img src=\"{it['uri']}\" class='gallery-thumb' /></div>",
                unsafe_allow_html=True
                )
                if it.get("note"):
                    st.caption(it["note"])

render_gallery_html(IMMAGINI, cols=3, height=240)
