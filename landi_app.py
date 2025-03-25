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

# Rest des Codes bleibt gleich …
