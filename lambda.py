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
import streamlit as st
import time
import openai
import os

# --- Language translations for UI ---
translations = {
    "English": {
        "title": "TransformAI",
        "select_language": "Please select your language",
        "enter_text": "Enter your text here:",
        "choose_mode": "Choose output type:",
        "generate": "Generate",
        "output_types": ["Summary", "Quiz", "Test", "Video", "Audio", "Animation", "Translation"]
    },
    "Español": {
        "title": "TransformAI",
        "select_language": "Por favor seleccione su idioma",
        "enter_text": "Ingrese su texto aquí:",
        "choose_mode": "Elija tipo de salida:",
        "generate": "Generar",
        "output_types": ["Resumen", "Cuestionario", "Prueba", "Video", "Audio", "Animación", "Traducción"]
    },
    # Add more languages here...
}

st.set_page_config(page_title="TransformAI", layout="wide")

# Placeholder to control dynamic content
placeholder = st.empty()

# Step 1: Show big centered title with CSS animation using st.markdown
def show_big_title():
    placeholder.markdown(
        """
        <style>
        .big-title {
            font-size: 80px;
            text-align: center;
            margin-top: 30vh;
            transition: all 2s ease;
            color: #0072C6;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        </style>
        <h1 class="big-title" id="main-title">TransformAI</h1>
        """,
        unsafe_allow_html=True,
    )

# Step 2: Animate title to top-left and shrink font
def animate_title_top_left():
    placeholder.markdown(
        """
        <style>
        #main-title {
            font-size: 30px !important;
            position: fixed !important;
            top: 10px !important;
            left: 20px !important;
            color: #0072C6;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            transition: all 1.5s ease;
        }
        </style>
        <h1 id="main-title">TransformAI</h1>
        """,
        unsafe_allow_html=True,
    )

# Step 3: Show language selector centered with styled container
def show_language_selector(ui_texts):
    st.markdown(
        """
        <style>
        .centered-container {
            display: flex;
            justify-content: center;
            margin-top: 30vh;
            flex-direction: column;
            align-items: center;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .stSelectbox > div {
            min-width: 250px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    with st.container():
        st.markdown(f"<div class='centered-container'><h3>{ui_texts['select_language']}</h3></div>", unsafe_allow_html=True)
        lang = st.selectbox("", list(translations.keys()), key="language_select")
    return lang

# Step 4: Show main input form with localized UI
def show_main_form(ui_texts):
    st.text_area(ui_texts["enter_text"], height=200, key="input_text")
    output_type = st.selectbox(ui_texts["choose_mode"], ui_texts["output_types"], key="output_type")
    generate_clicked = st.button(ui_texts["generate"])
    return generate_clicked, output_type

# Build OpenAI prompt based on language, text, and output type
def build_prompt(language, input_text, output_type):
    if output_type.lower() in ["summary", "resumen"]:
        return f"Summarize the following text in {language}:\n\n{input_text}"
    elif output_type.lower() in ["quiz", "cuestionario"]:
        return f"Create a quiz with 5 questions based on the following text in {language}:\n\n{input_text}"
    elif output_type.lower() == "test":
        return f"Generate a test with 5 multiple choice questions from this text in {language}:\n\n{input_text}"
    elif output_type.lower() == "video":
        return f"Provide a script for a short educational video in {language} based on this text:\n\n{input_text}"
    elif output_type.lower() == "audio":
        return f"Create an audio narration script in {language} for this text:\n\n{input_text}"
    elif output_type.lower() == "animation":
        return f"Describe an animation storyboard in {language} that explains the following content:\n\n{input_text}"
    elif output_type.lower() in ["translation", "traducción"]:
        return f"Translate the following text to {language}:\n\n{input_text}"
    else:
        return input_text

# Main app logic
def main():
    openai.api_key = os.getenv("KEY")
    # 1. Show big title
    show_big_title()
    time.sleep(3)

    # 2. Animate to top-left
    animate_title_top_left()

    # 3. Show language selector
    ui_texts = translations["English"]  # Default UI texts
    lang = show_language_selector(ui_texts)

    # Wait for user to pick a language
    if lang:
        ui_texts = translations.get(lang, translations["English"])
        st.markdown("<br><br>", unsafe_allow_html=True)  # add space after language selector

        # 4. Show main form with inputs
        generate_clicked, output_type = show_main_form(ui_texts)

        # When generate button clicked
        if generate_clicked:
            input_text = st.session_state.get("input_text", "").strip()
            if not input_text:
                st.error("Please enter some text!")
                return

            prompt = build_prompt(lang, input_text, output_type)

            with st.spinner("Generating AI output..."):
                try:
                    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": "You are a helpful assistant."},
                            {"role": "user", "content": prompt}
                        ],
                        max_tokens=500,
                        temperature=0.7,
                    )
                    ai_output = response['choices'][0]['message']['content']
                    st.markdown("### AI Output")
                    st.write(ai_output)
                except Exception as e:
                    st.error(f"OpenAI API error: {e}")

if __name__ == "__main__":
    main()
import streamlit as st
import time
import openai
import os

# Language translations
translations = {
    "English": {
        "title": "TransformAI",
        "select_language": "Please select your language",
        "enter_text": "Enter your text here:",
        "choose_mode": "Choose output type:",
        "generate": "Generate",
        "output_types": ["Summary", "Quiz", "Test", "Video", "Audio", "Animation", "Translation"]
    },
    "Español": {
        "title": "TransformAI",
        "select_language": "Por favor seleccione su idioma",
        "enter_text": "Ingrese su texto aquí:",
        "choose_mode": "Elija tipo de salida:",
        "generate": "Generar",
        "output_types": ["Resumen", "Cuestionario", "Prueba", "Video", "Audio", "Animación", "Traducción"]
    },
    # Add more languages here...
}

st.set_page_config(page_title="TransformAI", layout="wide")

def show_animated_title():
    # This CSS animates the title from center big to top-left small
    st.markdown(
        """
        <style>
        @keyframes moveAndShrink {
            0% {
                font-size: 80px;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                position: fixed;
                color: #0072C6;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
            100% {
                font-size: 30px;
                top: 10px;
                left: 20px;
                transform: translate(0, 0);
                position: fixed;
                color: #0072C6;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
        }
        #animated-title {
            animation-name: moveAndShrink;
            animation-duration: 3s;
            animation-fill-mode: forwards;
            position: fixed;
        }
        </style>
        <h1 id="animated-title">TransformAI</h1>
        """,
        unsafe_allow_html=True,
    )

def show_language_selector(ui_texts):
    st.markdown(
        """
        <style>
        .centered-container {
            display: flex;
            justify-content: center;
            margin-top: 30vh;
            flex-direction: column;
            align-items: center;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .stSelectbox > div {
            min-width: 250px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    with st.container():
        st.markdown(f"<div class='centered-container'><h3>{ui_texts['select_language']}</h3></div>", unsafe_allow_html=True)
        lang = st.selectbox("", list(translations.keys()), key="language_select")
    return lang

def show_main_form(ui_texts):
    st.text_area(ui_texts["enter_text"], height=200, key="input_text")
    output_type = st.selectbox(ui_texts["choose_mode"], ui_texts["output_types"], key="output_type")
    generate_clicked = st.button(ui_texts["generate"])
    return generate_clicked, output_type

def build_prompt(language, input_text, output_type):
    if output_type.lower() in ["summary", "resumen"]:
        return f"Summarize the following text in {language}:\n\n{input_text}"
    elif output_type.lower() in ["quiz", "cuestionario"]:
        return f"Create a quiz with 5 questions based on the following text in {language}:\n\n{input_text}"
    elif output_type.lower() == "test":
        return f"Generate a test with 5 multiple choice questions from this text in {language}:\n\n{input_text}"
    elif output_type.lower() == "video":
        return f"Provide a script for a short educational video in {language} based on this text:\n\n{input_text}"
    elif output_type.lower() == "audio":
        return f"Create an audio narration script in {language} for this text:\n\n{input_text}"
    elif output_type.lower() == "animation":
        return f"Describe an animation storyboard in {language} that explains the following content:\n\n{input_text}"
    elif output_type.lower() in ["translation", "traducción"]:
        return f"Translate the following text to {language}:\n\n{input_text}"
    else:
        return input_text

def main():
    openai.api_key = os.getenv("KEY")

    # 1. Show animated title
    show_animated_title()

    # 2. Wait 3 seconds for animation to complete
    time.sleep(3)

    # 3. Clear screen by rerunning with st.experimental_rerun not possible here,
    # so we use placeholder to overwrite content
    st.experimental_rerun()

if __name__ == "__main__":
    # Use session_state to track where we are in the flow
    if "step" not in st.session_state:
        st.session_state.step = 0

    if st.session_state.step == 0:
        # Show animated title and advance step after 3s
        show_animated_title()
        time.sleep(3)
        st.session_state.step = 1
        st.experimental_rerun()

    elif st.session_state.step == 1:
        # Show language selector
        ui_texts = translations["English"]
        lang = show_language_selector(ui_texts)

        if lang:
            st.session_state.lang = lang
            st.session_state.step = 2
            st.experimental_rerun()

    elif st.session_state.step == 2:
        # Show form with chosen language UI
        ui_texts = translations.get(st.session_state.lang, translations["English"])
        generate_clicked, output_type = show_main_form(ui_texts)

        if generate_clicked:
            input_text = st.session_state.get("input_text", "").strip()
            if not input_text:
                st.error("Please enter some text!")
            else:
                prompt = build_prompt(st.session_state.lang, input_text, output_type)
                with st.spinner("Generating AI output..."):
                    try:
                        response = openai.ChatCompletion.create(
                            model="gpt-3.5-turbo",
                            messages=[
                                {"role": "system", "content": "You are a helpful assistant."},
                                {"role": "user", "content": prompt}
                            ],
                            max_tokens=500,
                            temperature=0.7,
                        )
                        ai_output = response['choices'][0]['message']['content']
                        st.markdown("### AI Output")
                        st.write(ai_output)
                    except Exception as e:
                        st.error(f"OpenAI API error: {e}")
import streamlit as st
import openai
import os

# --- Translation dictionary ---
translations = {
    "English": {
        "title": "TransformAI",
        "select_language": "Please select your language",
        "enter_text": "Enter your text here:",
        "choose_mode": "Choose output type:",
        "generate": "Generate",
        "output_types": ["Summary", "Quiz", "Test", "Video", "Audio", "Animation", "Translation"]
    },
    "Español": {
        "title": "TransformAI",
        "select_language": "Por favor seleccione su idioma",
        "enter_text": "Ingrese su texto aquí:",
        "choose_mode": "Elija tipo de salida:",
        "generate": "Generar",
        "output_types": ["Resumen", "Cuestionario", "Prueba", "Video", "Audio", "Animación", "Traducción"]
    },
    # Add other languages here...
}

# Set page config
st.set_page_config(page_title="TransformAI", layout="wide")

# Initialize session state steps
if "step" not in st.session_state:
    st.session_state.step = 0
if "lang" not in st.session_state:
    st.session_state.lang = None

# Function to embed animated title with CSS + JS timer to notify Streamlit
def animated_title_with_js():
    st.markdown(
        """
        <style>
        #title {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 80px;
            color: #0072C6;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            animation: moveAndShrink 3s forwards;
            z-index: 9999;
        }
        @keyframes moveAndShrink {
            from {
                font-size: 80px;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
            }
            to {
                font-size: 30px;
                top: 10px;
                left: 20px;
                transform: translate(0, 0);
            }
        }
        /* Logo style */
        #logo {
            position: fixed;
            top: 12px;
            left: 120px;
            height: 40px;
            display: none; /* hidden initially */
            z-index: 10000;
        }
        </style>
        <h1 id="title">TransformAI</h1>
        <img id="logo" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Streamlit_logo.svg/1200px-Streamlit_logo.svg.png" alt="Logo"/>
        
        <script>
        // When animation ends, send message to Streamlit
        const title = document.getElementById('title');
        const logo = document.getElementById('logo');

        title.addEventListener('animationend', () => {
            // Show logo after animation
            logo.style.display = 'block';
            // Send event to Streamlit to update session state
            window.parent.postMessage({type: 'animation_done'}, '*');
        });
        </script>
        """,
        unsafe_allow_html=True,
    )

# Function to show language selector
def show_language_selector(ui_texts):
    st.markdown(
        """
        <style>
        .centered-container {
            display: flex;
            justify-content: center;
            margin-top: 30vh;
            flex-direction: column;
            align-items: center;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .stSelectbox > div {
            min-width: 250px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    with st.container():
        st.markdown(f"<div class='centered-container'><h3>{ui_texts['select_language']}</h3></div>", unsafe_allow_html=True)
        lang = st.selectbox("", list(translations.keys()), key="language_select")
    return lang

# Show main input form
def show_main_form(ui_texts):
    text = st.text_area(ui_texts["enter_text"], height=200, key="input_text")
    output_type = st.selectbox(ui_texts["choose_mode"], ui_texts["output_types"], key="output_type")
    generate_clicked = st.button(ui_texts["generate"])
    return generate_clicked, text, output_type

# Build prompt for OpenAI
def build_prompt(language, input_text, output_type):
    if output_type.lower() == "summary":
        return f"Summarize this text in {language}:\n\n{input_text}"
    elif output_type.lower() == "quiz":
        return f"Create a quiz with 5 questions based on this text in {language}:\n\n{input_text}"
    elif output_type.lower() == "test":
        return f"Generate a test with 5 multiple-choice questions from this text in {language}:\n\n{input_text}"
    elif output_type.lower() == "video":
        return f"Write a script for a short educational video in {language} based on this text:\n\n{input_text}"
    elif output_type.lower() == "audio":
        return f"Write an audio narration script in {language} for this text:\n\n{input_text}"
    elif output_type.lower() == "animation":
        return f"Describe an animation storyboard in {language} explaining this content:\n\n{input_text}"
    elif output_type.lower() == "translation":
        return f"Translate this text to {language}:\n\n{input_text}"
    else:
        return input_text

# JS message listener to detect animation completion
def js_message_listener():
    st.components.v1.html(
        """
        <script>
        window.addEventListener("message", (event) => {
            if (event.data.type && event.data.type === "animation_done") {
                window.parent.postMessage({streamlit_animation_done: true}, "*");
            }
        });
        </script>
        """,
        height=0,
        width=0,
    )

def main():
    openai.api_key = os.getenv("KEY")  # Make sure your environment variable is set

    # Step 0: Show animated title + logo
    if st.session_state.step == 0:
        animated_title_with_js()
        js_message_listener()
        # Wait for JS to send message to update step
        # Streamlit does not allow bidirectional JS <-> Python messaging easily,
        # so we'll use a workaround with st.experimental_get_query_params and user interaction

        # To detect the JS message in Streamlit, user needs to interact (e.g., press a button)
        # Alternatively, instruct user to click "Continue" to proceed after animation:
        if st.button("Continue"):
            st.session_state.step = 1
            st.experimental_rerun()

    # Step 1: Language selection
    elif st.session_state.step == 1:
        ui_texts = translations["English"]
        lang = show_language_selector(ui_texts)
        if lang:
            st.session_state.lang = lang
            st.session_state.step = 2
            st.experimental_rerun()

    # Step 2: Main input and output
    elif st.session_state.step == 2:
        ui_texts = translations.get(st.session_state.lang, translations["English"])
        generate_clicked, input_text, output_type = show_main_form(ui_texts)

        if generate_clicked:
            if not input_text.strip():
                st.error("Please enter some text!")
            else:
                prompt = build_prompt(st.session_state.lang, input_text, output_type)
                with st.spinner("Generating AI output..."):
                    try:
                        response = openai.ChatCompletion.create(
                            model="gpt-3.5-turbo",
                            messages=[
                                {"role": "system", "content": "You are a helpful assistant."},
                                {"role": "user", "content": prompt},
                            ],
                            max_tokens=500,
                            temperature=0.7,
                        )
                        output = response["choices"][0]["message"]["content"]
                        st.markdown("### AI Output")
                        st.write(output)
                    except Exception as e:
                        st.error(f"OpenAI API error: {e}")

if __name__ == "__main__":
    main()
