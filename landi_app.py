import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Landi – Dein Website-Bot", layout="wide")

# CSS-Styling
st.markdown("""
<style>
.stApp {
    font-family: 'Segoe UI', sans-serif;
    background-color: #f4f8fc;
    color: #000000 !important;
}
.left-column {
    background-image: url('https://i.postimg.cc/FF8V1BLg/Design-ohne-Titel-2.gif');
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    height: 100vh;
    width: 100%;
}
input, textarea, select {
    background-color: #ffffff !important;
    color: #000000 !important;
    border: 1px solid #000000 !important;
    border-radius: 6px !important;
}
label, .stMarkdown, .stText, .stSubheader, .stCaption {
    color: #000000 !important;
}
.stLinkButton button, .stDownloadButton button, .stButton button {
    background-color: #ffffff !important;
    color: #000000 !important;
    border: 1px solid #000000 !important;
}
</style>
""", unsafe_allow_html=True)

left, right = st.columns([1, 1])

with left:
    st.markdown('<div class="left-column"></div>', unsafe_allow_html=True)

with right:
    st.markdown("<h1>👋 Willkommen bei Landi – deinem KI-Website-Bot</h1>", unsafe_allow_html=True)
    st.markdown("<p>Erstelle automatisch eine professionelle Verkaufsseite, Shop oder Website mit Domain 💡</p>", unsafe_allow_html=True)

    projekt_typ = st.selectbox("1️⃣ Was möchtest du bauen?", ["Bitte wählen", "Landingpage", "Website", "Shop"])

    if projekt_typ != "Bitte wählen":
        beschreibung = st.text_area("👋 Willkommens-Text auf der Startseite")
        zielgruppe = st.text_input("👥 Zielgruppe (optional)")
        angebot = st.text_input("💡 Was bietest du an?")
        tonfall = st.selectbox("🎯 Tonfall der Texte", ["locker", "seriös", "emotional", "inspirierend"])

        hauptfarbe = st.color_picker("Hauptfarbe", "#2f4d8c")
        sekundärfarbe = st.color_picker("Sekundärfarbe", "#ffffff")
        akzentfarbe = st.color_picker("Akzentfarbe", "#ff9900")

        schriftart = st.selectbox("Schriftart", ["Segoe UI", "Arial", "Verdana", "Open Sans", "Roboto"])
        st.markdown(f"<p style='font-family:{schriftart};font-size:18px;'>Beispieltext in {schriftart}</p>", unsafe_allow_html=True)

        template = st.selectbox("📐 Design-Template", ["Modern", "Elegant", "Clean", "Emotional"])

        menupunkte = st.multiselect("📂 Menüpunkte", ["Home", "Über uns", "Leistungen", "Blog", "Kontakt", "Produkte", "Shop"])
        seiteninhalte = {punkt: st.text_area(f"Inhalt für {punkt}", height=100) for punkt in menupunkte}

        bilder = st.file_uploader("📸 Bilder hochladen", accept_multiple_files=True, type=["jpg", "jpeg", "png"])

        hero_html = ""
        bilder_rest_html = ""
        if bilder:
            for i, bild in enumerate(bilder):
                bild_url = f"data:image/jpeg;base64,{(bild.read()).hex()}"
                if i == 0:
                    hero_html = f'<div style="text-align:center;margin-bottom:2rem;"><img src="{bild_url}" style="width:100%;max-width:700px;border-radius:10px;box-shadow:0 5px 20px rgba(0,0,0,0.1);"/></div>'
                else:
                    bilder_rest_html += f'<img src="{bild_url}" style="width:100%;max-width:400px;margin-bottom:20px;border-radius:6px;"/>'

        if beschreibung:
            headline = beschreibung
            subheadline = f"Verwende unser {tonfall} System, um Ergebnisse zu erzielen, die wirklich zählen."
            cta = "Jetzt starten"

            html_vorschau = f"""
            <!DOCTYPE html>
            <html lang='de'>
            <head>
            <meta charset='UTF-8'>
            <meta name='viewport' content='width=device-width, initial-scale=1.0'>
            <title>{headline}</title>
            <style>
            body {{ font-family: '{schriftart}', sans-serif; background: #f9f9f9; color: #000; padding: 2rem; }}
            h1 {{ color: {hauptfarbe}; font-size: 2.4rem; margin-bottom: 1rem; }}
            .cta {{ background-color: {akzentfarbe}; color: white; padding: 12px 24px; border-radius: 6px; text-decoration: none; display: inline-block; margin-top: 1.5rem; font-weight: bold; transition: background-color 0.3s ease; }}
            .cta:hover {{ background-color: #222; }}
            nav ul {{ display: flex; gap: 1rem; list-style: none; padding: 0; margin-bottom: 2rem; border-bottom: 1px solid #ccc; padding-bottom: 1rem; }}
            nav a {{ color: {hauptfarbe}; text-decoration: none; font-weight: 600; }}
            .inhalt {{ margin-top: 2rem; background: {sekundärfarbe}; padding: 1.5rem; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.05); }}
            footer {{ margin-top: 4rem; font-size: 0.8rem; color: #555; text-align: center; padding-top: 2rem; border-top: 1px solid #ccc; }}
            footer a {{ color: #000; text-decoration: underline; }}
            </style>
            </head>
            <body>
            {hero_html}
            <nav><ul>{''.join([f'<li><a href="#' + punkt.lower().replace(' ', '-') + '">' + punkt + '</a></li>' for punkt in menupunkte])}</ul></nav>
            <h1>{headline}</h1>
            <p>{subheadline}</p>
            <a class='cta' href='#'>{cta}</a>
            {''.join([f'<div class="inhalt" id="' + k.lower().replace(' ', '-') + '"><h2>' + k + '</h2><p>' + v + '</p></div>' for k, v in seiteninhalte.items()])}
            {bilder_rest_html}
            <footer>
            <p><a href='#'>Impressum</a> | <a href='#'>Datenschutz</a> | <a href='#'>AGB</a></p>
            </footer>
            </body>
            </html>
            """

            st.markdown("### 🌐 Live-Vorschau deiner Website")
            components.html(html_vorschau, height=900, scrolling=True)

            st.download_button("💾 HTML-Datei herunterladen", data=html_vorschau, file_name="landi-website.html", mime="text/html")

            st.markdown("---")
            st.markdown("### 📦 Anleitung zur Integration")
            st.link_button("🔗 Carrd öffnen", "https://carrd.co/build")
            st.link_button("🔗 Tentary öffnen", "https://tentary.com/create")
            st.link_button("🔗 Systeme.io starten", "https://systeme.io")
            st.link_button("🔗 WordPress installieren", "https://wordpress.org/download/")
            st.caption("Made with ❤️ by Sarah – powered by KI & Verkaufspsychologie")
