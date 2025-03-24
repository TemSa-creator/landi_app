import streamlit as st

st.set_page_config(page_title="Landi – Dein Website-Bot", layout="centered")

# Neuer Style: Hintergrund + transparente UI + moderne Elemente
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://i.postimg.cc/nrk0fr2z/DALL-E-2025-03-03-09-12-01-A-small-cute-AI-robot-working-in-an-office-with-big-expressive-eyes-a.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Transparenter Bereich mit Stil */
    .main > div {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    }

    h1, h2, h3, h4 {
        color: #222;
        font-weight: 700;
    }

    p, label, .stMarkdown {
        color: #333;
        font-size: 1.05rem;
    }

    textarea, input, select {
        border-radius: 12px !important;
        padding: 0.5rem;
    }

    .stButton button {
        border-radius: 12px;
        background-color: #3b82f6;
        color: white;
        font-weight: bold;
        padding: 0.6rem 1.2rem;
        border: none;
    }

    .stDownloadButton button {
        border-radius: 12px;
        background-color: #10b981;
        color: white;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("👋 Willkommen bei Landi – deinem KI-Homepage-Bot")
st.markdown("Erstelle in wenigen Sekunden eine verkaufsstarke Website für dein Business 💡")

# Tool-Auswahl
st.subheader("1️⃣ Wähle dein Website-Tool")
option = st.selectbox(
    "Mit welchem Website-Baukasten möchtest du arbeiten?",
    ["Bitte wählen", "Systeme.io", "Carrd", "Dorik"]
)

# Sobald ein Tool gewählt ist:
if option != "Bitte wählen":
    st.subheader("2️⃣ Erzähl mir mehr über dein Projekt")

    # Eingaben vom Nutzer
    zielgruppe = st.text_input("🧑‍🧑‍ Wer ist deine Zielgruppe?")
    angebot = st.text_input("💡 Was bietest du an?")
    tonfall = st.selectbox("🎯 Wie soll der Text klingen?", ["locker", "seriös", "emotional", "inspirierend"])

    # Wenn beide Felder ausgefüllt sind
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
Starte jetzt ➔ Button
""")

        st.info("✅ Du kannst den Text einfach kopieren und in dein Website-Tool einfügen.")

        # Copy-Textfeld + Download
        st.markdown("### 📋 Text kopieren oder speichern")
        copy_text = st.text_area("Dein generierter Text:", value=f"Headline:\nSo hilfst du {zielgruppe}, mit {angebot} in nur wenigen Tagen ihr Ziel zu erreichen.\n\nCTA:\n👉 Jetzt kostenlos starten", height=150)
        st.download_button("📅 Als .txt herunterladen", data=copy_text, file_name="website-text.txt")

        # Tentary Empfehlung
        st.markdown("---")
        st.markdown("### 🛒 Du willst deine Website oder dein Produkt verkaufen?")

        st.markdown("👉 Dann brauchst du eine einfache Verkaufsseite mit Bezahlfunktion – ganz ohne Technik-Stress.")
        st.markdown("**Ich empfehle dir Tentary:** Schnell, easy & ideal für digitale Produkte, Kurse und Bots!")

        st.link_button("🚀 Jetzt mit Tentary starten", "https://www.tentary.com/?ref=DEIN-AFFILIATE-LINK")

        st.success("💡 BONUS: Wenn du Tentary über meinen Link nutzt, bekommst du eine exklusive Bot-Verkaufsseite als Vorlage von mir – gratis!")

# Fußbereich
st.markdown("---")
st.caption("Made with ❤️ by Sarah – powered by KI & Verkaufspsychologie")
