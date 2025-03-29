import streamlit as st
import urllib.parse

st.set_page_config(page_title="Landi – Dein Website-Bot", layout="wide")

# Custom CSS für blaues, klares Design
st.markdown(
    """
    <style>
    .stApp {
        font-family: 'Segoe UI', sans-serif;
        background-color: #f4f8fc;
        color: #0f1e3c !important;
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
        color: #0f1e3c !important;
        margin-bottom: 0.5rem;
    }

    .main-subtitle {
        font-size: 1.2rem;
        color: #2f4d8c !important;
        margin-bottom: 2rem;
    }

    label, .stSelectbox label, .stTextInput label, .stTextArea label {
        color: #0f1e3c !important;
    }

    .stSelectbox > div,
    .stTextInput > div > input,
    .stTextArea > div > textarea {
        background-color: #ffffff !important;
        color: #0f1e3c !important;
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
    st.markdown("<div class='main-subtitle'>Erstelle automatisch eine professionelle Verkaufsseite mit Abo-Anbindung, KI-Bots & mehr 💡</div>", unsafe_allow_html=True)

    st.subheader("1️⃣ Wähle dein Website-Tool")
    option = st.selectbox(
        "Mit welchem Website-Baukasten möchtest du arbeiten?",
        ["Bitte wählen", "Systeme.io", "Carrd", "Dorik", "Tentary"]
    )

    if option != "Bitte wählen":
        st.subheader("2️⃣ Erkläre dein Projekt")

        zielgruppe = st.text_input("🧑‍🤝‍🧑 Wer ist deine Zielgruppe?")
        angebot = st.text_input("💡 Was bietest du an?")
        tonfall = st.selectbox("🌟 Wie soll der Text klingen?", ["locker", "seriös", "emotional", "inspirierend"])

        if zielgruppe and angebot:
            st.subheader("3️⃣ Vorschau deiner Website")

            headline = f"So hilfst du {zielgruppe}, mit {angebot} in nur wenigen Tagen ihr Ziel zu erreichen."
            subheadline = f"Verwende unser {tonfall} System, um Ergebnisse zu erzielen, die wirklich zählen."
            cta = "👉 Jetzt Abo starten"

            with st.container():
                st.markdown("#### 💻 Vorschau deiner Seite:")
                st.markdown(f"### {headline}")
                st.markdown(f"<p style='color:#2f4d8c;font-size:18px;'>{subheadline}</p>", unsafe_allow_html=True)
                st.markdown(f"<a href='https://www.checkout-ds24.com/product/599133' target='_blank'><button style='background-color:#2f4d8c;border:none;color:white;padding:10px 20px;border-radius:6px;margin-top:10px;'>Jetzt Abo starten</button></a>", unsafe_allow_html=True)

            if st.button("✅ Ja, diesen Vorschlag übernehmen"):
                st.success("Super! Du kannst den Text jetzt unten speichern oder kopieren.")

            st.markdown("### 📋 Text kopieren oder speichern")
            full_text = f"Headline:\n{headline}\n\nSubheadline:\n{subheadline}\n\nCTA:\n{cta}"
            st.text_area("Dein generierter Text:", value=full_text, height=150)
            st.download_button("📅 Als .txt herunterladen", data=full_text, file_name="website-text.txt")

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
            st.markdown("### 🛎 Jetzt verkaufen oder starten?")
            st.markdown("Starte direkt mit deinem Abo-Link oder nutze einen Website-Baukasten deiner Wahl.")

            col1, col2 = st.columns(2)
            with col1:
                st.link_button("🔗 Carrd öffnen", "https://carrd.co/build")
            with col2:
                st.link_button("🔗 Tentary öffnen", "https://tentary.com/create")

            st.markdown("### 🌐 Oder direkt loslegen:")
            st.link_button("🚀 Abo jetzt starten (Digistore24)", "https://www.checkout-ds24.com/product/599133")

    st.markdown("---")
    st.caption("Made with ❤️ by Sarah – powered by KI & Verkaufspsychologie")
