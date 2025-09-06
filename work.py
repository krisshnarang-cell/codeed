import streamlit as st
import time
import openai
import os

translations = {
    "English": {
        "title": "TransformAI",
        "select_language": "Please select your language",
        "enter_text": "Enter your text here:",
        "choose_mode": "Choose output type:",
        "generate": "Generate",
        "output_types": ["Summary", "Quiz", "Test", "Video", "Audio", "Animation", "Translation"],
    },
    "Español": {
        "title": "TransformAI",
        "select_language": "Por favor seleccione su idioma",
        "enter_text": "Ingrese su texto aquí:",
        "choose_mode": "Elija tipo de salida:",
        "generate": "Generar",
        "output_types": ["Resumen", "Cuestionario", "Prueba", "Video", "Audio", "Animación", "Traducción"],
    },
}

st.set_page_config(page_title="TransformAI", layout="wide")

if "step" not in st.session_state:
    st.session_state.step = 0
if "lang" not in st.session_state:
    st.session_state.lang = None

title_css = """
<style>
#animated-title {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 80px;
    color: #0072C6;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    transition: all 3s ease;
    z-index: 9999;
}
#animated-title.shrink {
    font-size: 30px;
    top: 10px;
    left: 20px;
    transform: translate(0, 0);
}
#logo {
    position: fixed;
    top: 12px;
    left: 120px;
    height: 40px;
    display: none;
    z-index: 10000;
}
#logo.show {
    display: block;
}
</style>
"""

def show_animated_title(animate=False):
    st.markdown(title_css, unsafe_allow_html=True)
    if animate:
        st.markdown(
            """
            <h1 id="
