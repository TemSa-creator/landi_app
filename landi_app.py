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

# Der Rest des Codes bleibt unverändert ...
