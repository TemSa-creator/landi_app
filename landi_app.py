import streamlit as st
import urllib.parse

st.set_page_config(page_title="Landi – Dein Website-Bot", layout="wide")

# Custom CSS für klares schwarzes Design
st.markdown(
    """
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

    .main-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #000000 !important;
        margin-bottom: 0.5rem;
    }

    .main-subtitle {
        font-size: 1.2rem;
        color: #000000 !important;
        margin-bottom: 2rem;
    }
    input, textarea, select {
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 1px solid #000000 !important;
        border-radius: 6px !important;
    }
    select, .stSelectbox div[data-baseweb="select"] > div {
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 1px solid #000000 !important;
        border-radius: 6px !important;
    }
    label, .stTextInput label, .stTextArea label, .stSelectbox label, .stRadio label {
        color: #000000 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

left, right = st.columns([1, 1])

with left:
    st.markdown('<div class="left-column"></div>', unsafe_allow_html=True)

with right:
    st.markdown("<div class='main-title'>👋 Willkommen bei Landi – deinem KI-Website-Bot</div>", unsafe_allow_html=True)
    st.markdown("<div class='main-subtitle'>Erstelle automatisch eine professionelle Verkaufsseite, Shop oder Website mit Domain 💡</div>", unsafe_allow_html=True)

    st.subheader("1️⃣ Was möchtest du bauen?")
    projekt_typ = st.selectbox("Wähle den Website-Typ:", ["Bitte wählen", "Landingpage", "Website", "Shop"])

    if projekt_typ != "Bitte wählen":
        st.subheader("2️⃣ Erkläre dein Projekt")

        beschreibung = st.text_area("🧠 Beschreibe deine Wunschseite (z. B. Stil, Zielgruppe, Inhalte):")

        zielgruppe = st.text_input("🧑‍🤝‍🧑 Wer ist deine Zielgruppe?")
        angebot = st.text_input("💡 Was bietest du an?")
        tonfall = st.selectbox("🌟 Wie soll der Text klingen?", ["locker", "seriös", "emotional", "inspirierend"])

        hauptfarbe = st.color_picker("🎨 Hauptfarbe", "#2f4d8c")
        sekundärfarbe = st.color_picker("🎨 Sekundärfarbe", "#ffffff")
        akzentfarbe = st.color_picker("🎨 Akzentfarbe", "#ff9900")

        schriftart = st.selectbox("🔤 Welche Schriftart möchtest du nutzen?", ["Segoe UI", "Arial", "Verdana", "Open Sans", "Roboto"])

        menupunkte = st.multiselect("📂 Welche Menüpunkte brauchst du?", ["Home", "Über uns", "Leistungen", "Blog", "Kontakt", "Produkte", "Shop"])

        seiteninhalte = {}
        for punkt in menupunkte:
            seiteninhalte[punkt] = st.text_area(f"📝 Inhalt für " + punkt, height=100)

        bilder = st.file_uploader("📸 Lade Bilder für deine Seite hoch (optional)", accept_multiple_files=True, type=["jpg", "jpeg", "png"])

        domain_typ = st.radio("🌐 Welche Domain soll verwendet werden?", ["Eigene Domain", "Domain über externen Anbieter kaufen", "Automatisch zugewiesene Domain nutzen"])
        if domain_typ == "Eigene Domain":
            benutzer_domain = st.text_input("🔑 Deine Wunsch-Domain (z. B. meine-seite.de)")
        elif domain_typ == "Domain über externen Anbieter kaufen":
            st.markdown("Du kannst eine Domain schnell & einfach bei [united-domains.de](https://www.united-domains.de/) prüfen und kaufen.")
        else:
            st.markdown("✅ Dir wird automatisch eine Domain zugewiesen, z. B. `landi-projekt123.webseite.ai`")

        if zielgruppe and angebot:
            st.subheader("3️⃣ Vorschau deiner Website")

            headline = f"So hilfst du {zielgruppe}, mit {angebot} in nur wenigen Tagen ihr Ziel zu erreichen."
            subheadline = f"Verwende unser {tonfall} System, um Ergebnisse zu erzielen, die wirklich zählen."
            cta = "Jetzt starten"

            bilder_html = ""
            if bilder:
                for bild in bilder:
                    bild_url = f"data:image/jpeg;base64,{(bild.read()).hex()}"
                    bilder_html += f'<img src="{bild_url}" style="width:100%;max-width:400px;margin-bottom:20px;"/>'

            html_vorschau = f"""
            <!DOCTYPE html>
            <html lang='de'>
            <head>
                <meta charset='UTF-8'>
                <meta name='viewport' content='width=device-width, initial-scale=1.0'>
                <title>{headline}</title>
                <style>
                    body {{ font-family: '{schriftart}', sans-serif; background: #f9f9f9; color: #000; padding: 2rem; }}
                    h1 {{ color: {hauptfarbe}; font-size: 2rem; }}
                    .cta {{ background-color: {akzentfarbe}; color: white; padding: 10px 20px; border-radius: 6px; text-decoration: none; display: inline-block; margin-top: 1rem; }}
                    nav ul {{ display: flex; gap: 1rem; list-style: none; padding: 0; }}
                    nav li {{ display: inline; }}
                    .inhalt {{ margin-top: 2rem; }}
                    footer {{ margin-top: 4rem; font-size: 0.8rem; color: #555; }}
                </style>
            </head>
            <body>
                <nav><ul>{''.join([f'<li>{punkt}</li>' for punkt in menupunkte])}</ul></nav>
                <h1>{headline}</h1>
                <p>{subheadline}</p>
                <a class='cta' href='#'>{cta}</a>
                {''.join([f'<div class="inhalt"><h2>{k}</h2><p>{v}</p></div>' for k, v in seiteninhalte.items()])}
                {bilder_html}
                <footer>
                    <p><a href='#'>Impressum</a> | <a href='#'>Datenschutz</a> | <a href='#'>AGB</a></p>
                </footer>
            </body>
            </html>
            """

            st.markdown("### 🌐 Vorschau deiner fertigen Website")
            st.code(html_vorschau, language="html")
            st.download_button("💾 HTML-Datei herunterladen", data=html_vorschau, file_name="landi-website.html")

            st.markdown("---")
            st.markdown("### 📦 So nutzt du deine Website ganz einfach")

            col1, col2 = st.columns(2)
            with col1:
                st.link_button("🔗 Carrd öffnen", "https://carrd.co/build")
                st.markdown("👉 Gehe auf Carrd, wähle ein leeres Template, klicke auf ➕ → Embed → HTML & füge den Code ein.")
            with col2:
                st.link_button("🔗 Tentary öffnen", "https://tentary.com/create")
                st.markdown("👉 In Tentary HTML einfügen oder Blöcke ersetzen.")

            st.link_button("🔗 Systeme.io starten", "https://systeme.io")
            st.markdown("👉 Melde dich an, wähle 'Funnel' → eigene Seite → HTML-Modul einfügen.")

            st.link_button("🔗 WordPress installieren", "https://wordpress.org/download/")
            st.markdown("👉 Lade HTML hoch oder nutze Page-Builder wie Elementor (kostenpflichtig). Hosting nötig.")

            st.caption("Made with ❤️ by Sarah – powered by KI & Verkaufspsychologie")
