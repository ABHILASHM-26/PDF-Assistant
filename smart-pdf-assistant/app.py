import streamlit as st
import pdfplumber
import spacy
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from gtts import gTTS
import tempfile
import os
from collections import Counter

nlp = spacy.load("en_core_web_sm")

if "theme" not in st.session_state:
    st.session_state.theme = "Light"

theme = st.session_state.theme
dark_mode = theme == "Dark"

def toggle_theme():
    st.session_state.theme = "Dark" if st.session_state.theme == "Light" else "Light"
    st.experimental_rerun()

bg_color = "#0e1117" if dark_mode else "#ffffff"
text_color = "#ffffff" if dark_mode else "#000000"
input_bg = "#262730" if dark_mode else "#f0f2f6"
button_color = "#1f77b4" if dark_mode else "#0056b3"
download_bg = "#1DB954" if dark_mode else "#0072E3"

st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {bg_color};
        color: {text_color};
    }}
    h1, h2, h3, h4, h5, h6, p, label, div {{
        color: {text_color} !important;
    }}
    .stTextInput input,
    .stTextArea textarea,
    .stSelectbox div[data-baseweb="select"],
    .stNumberInput input {{
        background-color: {input_bg} !important;
        color: {text_color} !important;
    }}
    .stRadio > div {{
        background-color: transparent !important;
    }}
    .stRadio div[role="radiogroup"] > div {{
        color: {text_color} !important;
        background-color: transparent !important;
        border-radius: 6px;
        padding: 4px;
    }}
    .stRadio div[role="radiogroup"] > div:hover {{
        background-color: rgba(255, 255, 255, 0.1);
    }}
    .stButton > button, .stDownloadButton > button {{
        background-color: {button_color};
        color: white !important;
        padding: 8px 16px;
        border-radius: 6px;
        border: none;
    }}
    .stDownloadButton > button {{
        background-color: {download_bg} !important;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.title("⚙️ Settings")
st.sidebar.button("Toggle Dark/Light Mode", on_click=toggle_theme)


st.title("Smart PDF Assistant")


uploaded_file = st.file_uploader("📤 Upload a PDF file", type="pdf")
text = ""

if uploaded_file:
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""

    st.subheader("📄 Extracted Text")
    st.write(text)

    doc = nlp(text)


    st.subheader("📝 Summary")
    sentences = list(doc.sents)
    summary = " ".join([str(sent) for sent in sentences[:5]])
    st.write(summary)

   
    st.subheader("📊 Top Keywords (Bar Chart)")
    keywords = [token.text.lower() for token in doc if token.is_alpha and not token.is_stop]
    keyword_freq = Counter(keywords)
    most_common = keyword_freq.most_common(20)

    if most_common:
        words, freqs = zip(*most_common)
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.barh(words[::-1], freqs[::-1], color="#1DB954" if dark_mode else "#0072E3")
        ax.set_xlabel("Frequency", color=text_color)
        ax.set_ylabel("Keywords", color=text_color)
        ax.tick_params(colors=text_color)
        ax.set_facecolor(bg_color)
        fig.patch.set_facecolor(bg_color)
        st.pyplot(fig)
    else:
        st.info("No keywords found.")

    
    st.subheader("Named Entities")
    named_entities = [(ent.text, ent.label_) for ent in doc.ents]
    if named_entities:
        st.write("Detected entities:")
        for text_, label_ in named_entities:
            st.markdown(f"- **{text_}** ({label_})")
    else:
        st.info("No named entities found.")

   
    st.subheader("🔊 Text-to-Speech")
    tts_text = st.text_area("Enter text for audio", summary)

    if st.button("🔈 Generate Audio"):
        try:
            tts = gTTS(tts_text)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
                tts.save(tmp_file.name)
                audio_file = tmp_file.name

            st.audio(audio_file, format="audio/mp3")
            with open(audio_file, "rb") as f:
                st.download_button("⬇️ Download Audio", f, file_name="speech.mp3")
            os.remove(audio_file)

        except Exception as e:
            st.error(f"Audio generation failed: {e}")

    
    st.subheader("📤 Export Options")
    st.download_button("Download Cleaned Text", text, file_name="cleaned_text.txt")
    st.download_button("Download Summary", summary, file_name="summary.txt")
