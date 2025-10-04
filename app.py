import streamlit as st
from googletrans import Translator
from gtts import gTTS

st.set_page_config(page_title="Language Translator", page_icon="🌐")
st.title("🌐 Language Translation Tool")

text_input = st.text_area("Enter text to translate:")

languages = {
    "English": "en",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta"
}

source_lang = st.selectbox("Source Language", list(languages.keys()))
target_lang = st.selectbox("Target Language", list(languages.keys()))

if st.button("Translate"):
    translator = Translator()
    translated = translator.translate(text_input, src=languages[source_lang], dest=languages[target_lang])
    st.success(f"Translated Text: {translated.text}")

    tts = gTTS(translated.text, lang=languages[target_lang])
    tts.save("translated_audio.mp3")
    audio_file = open("translated_audio.mp3", "rb")
    st.audio(audio_file.read(), format="audio/mp3")
