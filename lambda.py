import streamlit as st
import openai 
import os
st.title("TransformAI")
openai.api_key=os.getenv("KEY")
lang=st.selectbox("Choose language:",["English",
        "हिंदी",           # Hindi
        "Español",         # Spanish
        "Français",        # French
        "Deutsch",         # German
        "中文",             # Chinese
        "日本語",           # Japanese
        "한국어",           # Korean
        "Русский",         # Russian
        "اردو",            # Urdu
        "বাংলা",           # Bengali
        "తెలుగు",         # Telugu
        "தமிழ்",           # Tamil
        "ગુજરાતી",         # Gujarati
        "मराठी",           # Marathi
        "ਪੰਜਾਬੀ",          # Punjabi
        "ಕನ್ನಡ",           # Kannada
        "मारवाड़ी",        # Marwari
        "O‘zbekcha",       # Uzbek
        "ქართული",         # Georgian
        "العربية",         # Arabic
        "Türkçe",          # Turkish
        "ภาษาไทย",         # Thai
        "فارسی",           # Persian
        "Shqip",           # Albanian
        "Nederlands",      # Dutch
        "Svenska",         # Swedish
        "Italiano",        # Italian
        "Việt",            # Vietnamese
        "ລາວ"              # Lao
])
txt=st.text_area("paste your text here")
outpt=st.selectbox(
    "Choose output type:",
    ["Summary", "Quiz", "Test", "Video", "Audio", "Animation", "Translation"])
if st.button("Generate"):
    st.write(f"Language: {lang}")
    st.write(f"Output type: {outpt}")
    st.write("This is where the AI output will appear")
    from streamlit_lottie import st_lottie
import requests
from PIL import Image

# --- Config ---
st.set_page_config(page_title="TransformAI", layout="wide")

# --- Load logo ---
def load_logo():
    try:
        logo = Image.open("logo.png")  # replace with your local file path or URL download logic
        return logo
    except Exception as e:
        return None

# --- Load Lottie animation from URL ---
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
# --- Display header with logo and title ---
def display_header():
    logo = load_logo()
    col1, col2 = st.columns([1, 8])
    with col1:
        if logo:
            st.image(logo, width=80)
        else:
            st.write("🏢")  # fallback emoji or text
    with col2:
        st.markdown("<h1 style='margin-bottom: 0;'>TransformAI</h1>", unsafe_allow_html=True)

# --- Main app ---
def main():
    display_header()

    # Show animation
    lottie_animation = load_lottie_url("https://assets3.lottiefiles.com/packages/lf20_qp1q7mct.json")
    if lottie_animation:
        st_lottie(lottie_animation, height=150)