import streamlit as st

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

            if option == "Systeme.io":
                st.success("Systeme.io – Funnel-fokussierter Aufbau")
                st.code(f"""
Headline:
So hilfst du {zielgruppe}, mit {angebot} in nur wenigen Tagen ihr Ziel zu erreichen.

Subheadline:
Verwende unser {tonfall} System, um Ergebnisse zu erzielen, die wirklich zählen.

Call-to-Action:
👉 Jetzt kostenlos starten
""")

            elif option == "Carrd":
                st.success("Carrd – Minimalistische Onepager-Struktur")
                st.code(f"""
<h1>{angebot} für {zielgruppe}</h1>
<p>{tonfall.capitalize()} erklärt, damit deine Zielgruppe sofort versteht, worum es geht.</p>
<button>Jetzt starten</button>
""")

            elif option == "Dorik":
                st.success("Dorik – Moderne Website mit Sektionen")
                st.code(f"""
Section 1 – Über dich:
Ich helfe {zielgruppe}, durch {angebot} schneller ans Ziel zu kommen.

Section 2 – Warum du?
Weil ich einen {tonfall} Ansatz habe, der wirkt.

Section 3 – Call-to-Action:
Starte jetzt ➜ Button
""")

            elif option == "Tentary":
                st.success("Tentary – Verkaufsseiten & Mitgliederbereiche für digitale Produkte")
                st.code(f"""
Headline:
Erreiche {zielgruppe} mit deinem {angebot} auf einer smarten Verkaufsseite.

Subheadline:
Nutze einen {tonfall} Aufbau, der konvertiert.

CTA:
🚀 Starte jetzt mit Tentary
""")

            st.info("✅ Du kannst den Text einfach kopieren und in dein Website-Tool einfügen.")

            st.markdown("### 📋 Text kopieren oder speichern")
            copy_text = st.text_area("Dein generierter Text:", value=f"Headline:\nSo hilfst du {zielgruppe}, mit {angebot} in nur wenigen Tagen ihr Ziel zu erreichen.\n\nCTA:\n👉 Jetzt kostenlos starten", height=150)
            st.download_button("📥 Als .txt herunterladen", data=copy_text, file_name="website-text.txt")

            st.markdown("---")
            st.markdown("### 📄 Impressum, Datenschutz & AGBs")
            st.markdown("Du kannst die Vorlagen einfach anpassen – ersetze nur deine persönlichen Angaben:")

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
            st.markdown("### 🛒 Du willst deine Website oder dein Produkt verkaufen?")
            st.markdown("👉 Dann brauchst du eine einfache Verkaufsseite mit Bezahlfunktion – ganz ohne Technik-Stress.")
            st.markdown("**Wähle dein Tool & starte direkt:**")

            col1, col2, col3 = st.columns(3)
            with col1:
                st.link_button("🔗 Systeme.io", "https://systeme.io/?ref=DEIN-AFFILIATE-LINK")
            with col2:
                st.link_button("🔗 Carrd", "https://carrd.co/")
            with col3:
                st.link_button("🔗 Tentary", "https://www.tentary.com/?ref=DEIN-AFFILIATE-LINK")

            st.success("💡 BONUS: Wenn du eines der Tools über meinen Link nutzt, bekommst du eine exklusive Bot-Verkaufsseite als Vorlage von mir – gratis!")

    st.markdown("---")
    st.caption("Made with ❤️ by Sarah – powered by KI & Verkaufspsychologie")
