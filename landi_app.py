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
        background-image: url('https://i.postimg.cc/nrk0fr2z/DALL-E-2025-03-03-09-12-01-A-small-cute-AI-robot-working-in-an-office-with-big-expressive-eyes-a.jpg');
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

    .stTextInput > div > input,
    .stSelectbox > div,
    .stTextArea > div > textarea {
        background-color: #fff;
        color: #000 !important;
    }

    .stMarkdown, .stText, .stSubheader, .stCaption, .stSuccess, .stInfo, .stDownloadButton, .stLinkButton, .stCode, .css-1cpxqw2 {
        color: #000 !important;
    }

    .stButton button, .stDownloadButton button, .stLinkButton button {
        border-radius: 8px;
        font-weight: bold;
        padding: 0.6rem 1.2rem;
        color: #fff !important;
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
        ["Bitte wählen", "Systeme.io", "Carrd", "Dorik"]
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

            st.info("✅ Du kannst den Text einfach kopieren und in dein Website-Tool einfügen.")

            st.markdown("### 📋 Text kopieren oder speichern")
            copy_text = st.text_area("Dein generierter Text:", value=f"Headline:\nSo hilfst du {zielgruppe}, mit {angebot} in nur wenigen Tagen ihr Ziel zu erreichen.\n\nCTA:\n👉 Jetzt kostenlos starten", height=150)
            st.download_button("📥 Als .txt herunterladen", data=copy_text, file_name="website-text.txt")

            st.markdown("---")
            st.markdown("### 🛒 Du willst deine Website oder dein Produkt verkaufen?")
            st.markdown("👉 Dann brauchst du eine einfache Verkaufsseite mit Bezahlfunktion – ganz ohne Technik-Stress.")
            st.markdown("**Ich empfehle dir Tentary:** Schnell, easy & ideal für digitale Produkte, Kurse und Bots!")
            st.link_button("🚀 Jetzt mit Tentary starten", "https://www.tentary.com/?ref=DEIN-AFFILIATE-LINK")
            st.success("💡 BONUS: Wenn du Tentary über meinen Link nutzt, bekommst du eine exklusive Bot-Verkaufsseite als Vorlage von mir – gratis!")

    st.markdown("---")
    st.caption("Made with ❤️ by Sarah – powered by KI & Verkaufspsychologie")
