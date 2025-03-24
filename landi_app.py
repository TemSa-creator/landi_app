import streamlit as st

st.set_page_config(page_title="Landi – Dein Website-Bot", layout="centered")

st.title("👋 Willkommen bei Landi – deinem KI-Homepage-Bot")

# Schritt 1: Nutzer auswählen lassen
st.subheader("Was möchtest du erstellen?")
option = st.selectbox("Wähle deinen Website-Builder:", ["Bitte wählen", "Systeme.io", "Carrd", "Dorik"])

# Schritt 2: Automatisch passenden Text anzeigen
if option == "Systeme.io":
    st.success("Systeme.io ist perfekt für Funnel. Hier dein Text-Template:")
    st.code("Headline: Gewinne täglich neue Kunden mit deinem Onlinekurs\nCTA: Jetzt gratis starten ➜")
elif option == "Carrd":
    st.success("Carrd ist minimalistisch & stylish. Hier dein Vorschlag:")
    st.code("<h1>Ich helfe dir, online Geld zu verdienen</h1>\n<p>Mit KI-Bots und deiner Expertise</p>")
elif option == "Dorik":
    st.success("Dorik ist super für moderne Websites. Hier dein Text:")
    st.code("Section 1: Über dich\nSection 2: Angebot\nSection 3: Kontaktformular")

if option != "Bitte wählen":
    st.info("👉 Du kannst die Texte einfach kopieren und in dein Website-Tool einfügen.")
