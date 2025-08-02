 📄 Smart PDF Assistant

Smart PDF Assistant is an intelligent, interactive Streamlit-based application that allows users to upload PDF documents and perform various NLP and visualization tasks. 
The app enables keyword extraction, named entity recognition, text summarization, text-to-speech conversion, metadata extraction, and matplotlib-based data visualization.

 Features

PDF Text Extraction using `pdfplumber`
Named Entity Recognition using `spaCy`
Keyword Extraction using TF-IDF & POS filtering
Text Summarization using Sumy (or alternative fallback logic)
Metadata & Link Extraction
Text-to-Speech (Downloadable Audio in `.mp3`)
Matplotlib Graph for keyword frequency visualization
Dark / Light Themes

 Built With

- Python
- Streamlit
- pdfplumber
- spaCy
- matplotlib
- wordcloud
- gTTS (Google Text-to-Speech)
- pyttsx3 (Offline TTS)
- Python-docx
- scikit-learn

Getting Started

git clone https://github.com/ABHILASHM-26/PDF-Assistant.git
cd PDF-Assistant
Create a virtual environment :
python -m venv venv
source venv/bin/activate 

Install dependencies:
  pip install -r requirements.txt
  
Run the App :
  streamlit run main.py

 Example Use Cases

Analyze research papers or eBooks

Extract insights from business reports

Convert sections of PDFs to audio

Visualize term importance using bar charts

I deployed this project in streamlit community as an app :
  Everyone can access it [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://smart-pdf-assistant-abhilashm.streamlit.app/)

Developed By :

Abhilash M

GitHub: [ABHILASHM-26](https://github.com/ABHILASHM-26)

LinkedIn: [linkedin.com/in/abhilashm](https://www.linkedin.com/in/abhilashmellacheruvu/)

Email: abhilashm9585@gmail.com
