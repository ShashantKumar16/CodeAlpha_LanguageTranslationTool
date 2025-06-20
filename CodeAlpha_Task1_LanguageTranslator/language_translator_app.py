import streamlit as st
from deep_translator import GoogleTranslator

# List of supported languages (manually listed for simplicity)
supported_languages = [
    'english', 'urdu', 'hindi', 'french', 'german', 'spanish',
    'arabic', 'chinese (simplified)', 'russian', 'italian'
]

st.title("🌐 Language Translation Tool - CodeAlpha")
st.markdown("Translate text from one language to another using Deep Translator.")

# User input
text_to_translate = st.text_area("Enter text to translate:")

# Language selection
source_lang = st.selectbox("Source Language", supported_languages, index=supported_languages.index("english"))
target_lang = st.selectbox("Target Language", supported_languages, index=supported_languages.index("urdu"))

# Translate button
if st.button("Translate"):
    if not text_to_translate.strip():
        st.warning("Please enter some text.")
    else:
        try:
            translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text_to_translate)
            st.success("Translated Text:")
            st.write(translated)
        except Exception as e:
            st.error(f"Translation failed: {e}")
