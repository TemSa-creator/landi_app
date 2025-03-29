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

    label, .stSelectbox label, .stTextInput label, .stTextArea label, .stRadio label, .css-1cpxqw2, .css-1v0mbdj, .css-1y4p8pa {
        color: #000000 !important;
    }

    .stSelectbox > div,
    .stTextInput > div > input,
    .stTextArea > div > textarea {
        background-color: #ffffff !important;
        color: #000000 !important;
        border-radius: 6px;
        border: 1px solid #c6d4f2;
    }

    .stButton button, .stDownloadButton button, .stLinkButton button {
        border-radius: 8px;
        font-weight: 600;
        padding: 0.6rem 1.2rem;
        background-color: #2f4d8c;
        color: #ffffff !important;
        border: none;
    }

    .stLinkButton button:hover, .stButton button:hover {
        background-color: #1e3364;
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

        zielgruppe = st.text_input("🧑‍🤝‍🧑 Wer ist deine Zielgruppe?")
        angebot = st.text_input("💡 Was bietest du an?")
        tonfall = st.selectbox("🌟 Wie soll der Text klingen?", ["locker", "seriös", "emotional", "inspirierend"])

        produkte = []
        if projekt_typ == "Shop":
            st.subheader("🍬 Produkte hinzufügen")
            for i in range(1, 4):
                produktname = st.text_input(f"Produkt {i} Name", key=f"produkt_{i}")
                produktpreis = st.text_input(f"Produkt {i} Preis (z. B. 29,99 €)", key=f"preis_{i}")
                if produktname and produktpreis:
                    produkte.append((produktname, produktpreis))

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

            st.markdown("#### 💻 Vorschau deiner Seite:")
            st.markdown(f"### {headline}")
            st.markdown(f"<p style='color:#000000;font-size:18px;'>{subheadline}</p>", unsafe_allow_html=True)
            st.markdown(f"<button style='background-color:#2f4d8c;border:none;color:white;padding:10px 20px;border-radius:6px;margin-top:10px;'>{cta}</button>", unsafe_allow_html=True)

            if projekt_typ == "Shop" and produkte:
                st.markdown("#### 🍬 Produkte in deinem Shop:")
                for name, preis in produkte:
                    st.markdown(f"**{name}** – {preis}")

            if st.button("✅ Ja, diesen Vorschlag übernehmen"):
                st.success("Super! Du kannst den Text jetzt unten speichern oder kopieren.")

            st.markdown("### 📋 Text kopieren oder speichern")
            full_text = f"Headline:
{headline}

Subheadline:
{subheadline}

CTA:
{cta}"
            st.text_area("Dein generierter Text:", value=full_text, height=150)
            st.download_button("📅 Als .txt herunterladen", data=full_text, file_name="website-text.txt")

            st.markdown("---")
            st.markdown("### 📄 Impressum, Datenschutz & AGBs")
            impressum = """
Impressum
Angaben gemäß § 5 TMG:
Max Mustermann
Musterstraße 123
12345 Musterstadt
Deutschland
E-Mail: max@example.com
Telefon: +49 123 4567890
"""
            datenschutz = """
Datenschutzerklärung
Wir nehmen den Schutz deiner persönlichen Daten sehr ernst. Personenbezogene Daten werden vertraulich und entsprechend der gesetzlichen Datenschutzvorschriften behandelt.

Verantwortlich:
Max Mustermann, max@example.com
"""
            agb = """
Allgemeine Geschäftsbedingungen (AGB)
1. Geltungsbereich: Diese AGB gelten für alle Bestellungen über unseren Online-Shop.
2. Vertragspartner: Der Kaufvertrag kommt zustande mit Max Mustermann.
... (weiter anpassbar)
"""
            st.text_area("📌 Impressum (bitte anpassen)", value=impressum, height=150)
            st.text_area("📌 Datenschutzerklärung (bitte anpassen)", value=datenschutz, height=200)
            st.text_area("📌 AGBs (bitte anpassen)", value=agb, height=200)

            st.markdown("---")
            st.markdown("### 🛎 Jetzt verkaufen oder starten?")
            col1, col2 = st.columns(2)
            with col1:
                st.link_button("🔗 Carrd öffnen", "https://carrd.co/build")
            with col2:
                st.link_button("🔗 Tentary öffnen", "https://tentary.com/create")

    st.markdown("---")
st.caption("Made with ❤️ by Sarah – powered by KI & Verkaufspsychologie")
