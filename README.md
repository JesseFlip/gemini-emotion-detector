# 🎭 Gemini Emotion Detector

A modern, full-stack AI application that performs granular emotional sentiment analysis on text using **Google Gemini 1.5 Flash**. 

Built with a focus on speed, type safety, and clean UI, this project demonstrates a transition from legacy NLP libraries to state-of-the-art Generative AI.

## 🚀 Key Features
* **AI Engine:** Leverages Gemini 1.5 Flash for high-speed, contextual sentiment analysis.
* **Structured Data:** Uses **Pydantic** to ensure AI responses follow a strict schema (Anger, Disgust, Fear, Joy, Sadness).
* **Modern UI:** Responsive dashboard built with **Streamlit** and real-time data visualization via native charts.
* **Fast Environment:** Managed with **uv** for lightning-fast, reproducible dependency management.

## 🛠 Tech Stack
* **Language:** Python 3.10+
* **AI SDK:** `google-genai`
* **Frontend:** Streamlit
* **Package Manager:** uv

## 📦 Installation & Setup

1. **Clone the repo:**
   ```bash
   git clone [https://github.com/JesseFlip/gemini-emotion-detector.git]
   cd gemini-emotion-detector
Install dependencies (via uv):

Bash
uv sync
Set up your API Key:
Create a .env file and add your Google AI Studio key:

Plaintext
GEMINI_API_KEY=your_api_key_here
Run the app:

Bash
uv run streamlit run app.py
Created by Jesse Flippen during a transition into the tech sector using Gemini as a guide to write most of the code and troubleshoot errors. 

Screenshot

![Screenshot of a web application titled "Gemini Emotion Detector" showing a sentiment analysis of the text "I will provide solutions!" The results identify "Joy" as the dominant emotion with a score of 0.85, visualized by a bar chart and a JSON data snippet.](emotion_screenshot.png)



