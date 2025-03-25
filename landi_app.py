import streamlit as st
import urllib.parse

st.set_page_config(page_title="Landi – Dein Website-Bot", layout="wide")

# Custom CSS für zweispaltiges Layout mit Roboter links und Text rechts
st.markdown(
    """
    <style>
    .stApp {
        font-family: 'Segoe UI', sans-serif;
        background-color: #ffffff;
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
        font-size: 1.1rem;
        color: #000000 !important;
        margin-bottom: 2rem;
    }

    label, .css-1cpxqw2, .css-1v0mbdj, .css-10trblm, .css-1y4p8pa, .css-1r6slb0, .css-1c7y2kd, .css-1aehpvj, .css-1kyxreq, .css-1fcdlh3 {
        color: #000000 !important;
    }

    .stSelectbox > div,
    .stTextInput > div > input,
    .stTextArea > div > textarea {
        background-color: #ffffff !important;
        color: #000000 !important;
    }

    .stMarkdown, .stText, .stSubheader, .stCaption, .stSuccess, .stInfo, .stDownloadButton, .stLinkButton, .stCode {
        color: #000000 !important;
    }

    .stAlert .stAlert-success {
        background-color: #e6f4ea !important;
        color: #000000 !important;
    }

    .stButton button, .stDownloadButton button, .stLinkButton button {
        border-radius: 8px;
        font-weight: bold;
        padding: 0.6rem 1.2rem;
        color: #ffffff !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

left, right = st.columns([1, 1])

with left:
    st.markdown('<div class="left-column"></div>', unsafe_allow_html=True)

with right:
    st.markdown("<div class='main-title'>👋 Willkommen bei Landi – deinem KI-Homepage-Bot</div>", unsafe_allow_html=True)
    st.markdown("<div class='main-subtitle'>Erstelle in wenigen Sekunden eine verkaufsstarke Website für dein Business 💡</div>", unsafe_allow_html=True)

    st.subheader("1️⃣ Wähle dein Website-Tool")
    option = st.selectbox(
        "Mit welchem Website-Baukasten möchtest du arbeiten?",
        ["Bitte wählen", "Systeme.io", "Carrd", "Dorik", "Tentary"]
    )

    if option != "Bitte wählen":
        st.subheader("2️⃣ Erzähl mir mehr über dein Projekt")

        zielgruppe = st.text_input("🧑‍🤝‍🧑 Wer ist deine Zielgruppe?")
        angebot = st.text_input("💡 Was bietest du an?")
        tonfall = st.selectbox("🎯 Wie soll der Text klingen?", ["locker", "seriös", "emotional", "inspirierend"])

        if zielgruppe and angebot:
            st.subheader("3️⃣ Dein fertiger Website-Text")

            headline = f"So hilfst du {zielgruppe}, mit {angebot} in nur wenigen Tagen ihr Ziel zu erreichen."
            subheadline = f"Verwende unser {tonfall} System, um Ergebnisse zu erzielen, die wirklich zählen."
            cta = "👉 Jetzt kostenlos starten"

            st.code(f"""
Headline:
{headline}

Subheadline:
{subheadline}

Call-to-Action:
{cta}
""")

            st.markdown("### 📋 Text kopieren oder speichern")
            full_text = f"Headline:\n{headline}\n\nSubheadline:\n{subheadline}\n\nCTA:\n{cta}"
            st.text_area("Dein generierter Text:", value=full_text, height=150)
            st.download_button("📥 Als .txt herunterladen", data=full_text, file_name="website-text.txt")

            st.markdown("---")
            st.markdown("### 📄 Impressum, Datenschutz & AGBs")
            impressum = """
Impressum\nAngaben gemäß § 5 TMG:\nMax Mustermann\nMusterstraße 123\n12345 Musterstadt\nDeutschland\nE-Mail: max@example.com\nTelefon: +49 123 4567890
"""
            datenschutz = """
Datenschutzerklärung\nWir nehmen den Schutz deiner persönlichen Daten sehr ernst. Personenbezogene Daten werden vertraulich und entsprechend der gesetzlichen Datenschutzvorschriften behandelt.\n\nVerantwortlich:\nMax Mustermann, max@example.com
"""
            agb = """
Allgemeine Geschäftsbedingungen (AGB)\n1. Geltungsbereich: Diese AGB gelten für alle Bestellungen über unseren Online-Shop.\n2. Vertragspartner: Der Kaufvertrag kommt zustande mit Max Mustermann.\n... (weiter anpassbar)
"""
            st.text_area("📌 Impressum (bitte anpassen)", value=impressum, height=150)
            st.text_area("📌 Datenschutzerklärung (bitte anpassen)", value=datenschutz, height=200)
            st.text_area("📌 AGBs (bitte anpassen)", value=agb, height=200)

            st.markdown("---")
            st.markdown("### 🛒 Du willst deine Website oder dein Produkt verkaufen?")
            st.markdown("👉 Dann brauchst du eine einfache Verkaufsseite mit Bezahlfunktion – ganz ohne Technik-Stress.")
            st.markdown("**Wähle dein Tool & starte direkt mit Vorlage:**")

            carrd_url = "https://carrd.co/build"
            tentary_url = "https://tentary.com/create"

            col1, col2 = st.columns(2)
            with col1:
                st.link_button("🔗 Carrd öffnen", carrd_url)
            with col2:
                st.link_button("🔗 Tentary öffnen", tentary_url)

    st.markdown("---")
    st.caption("Made with ❤️ by Sarah – powered by KI & Verkaufspsychologie")
