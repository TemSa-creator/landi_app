import streamlit as st

# Seitentitel & Layout
st.set_page_config(page_title="Landi – Dein Website-Bot", layout="centered")

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
    zielgruppe = st.text_input("🧑‍🤝‍🧑 Wer ist deine Zielgruppe?")
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
Starte jetzt ➜ Button
""")

        st.info("✅ Du kannst den Text einfach kopieren und in dein Website-Tool einfügen.")

# Fußbereich
st.markdown("---")
st.caption("Made with ❤️ by Sarah – powered by KI & Verkaufspsychologie")
import streamlit as st

# Seitentitel & Layout
st.set_page_config(page_title="Landi – Dein Website-Bot", layout="centered")

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
    zielgruppe = st.text_input("🧑‍🤝‍🧑 Wer ist deine Zielgruppe?")
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
Starte jetzt ➜ Button
""")

        st.info("✅ Du kannst den Text einfach kopieren und in dein Website-Tool einfügen.")

# Fußbereich
st.markdown("---")
st.caption("Made with ❤️ by Sarah – powered by KI & Verkaufspsychologie")
