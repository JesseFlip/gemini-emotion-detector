import streamlit as st
import pandas as pd
from logic import emotion_detector

# Page Configuration
st.set_page_config(page_title="Gemini Emotion AI", page_icon="🎭", layout="centered")

# Custom CSS for a modern look
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    stTextArea textarea { background-color: #161b22; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎭 Gemini Emotion Detector")
st.write("Analyze text sentiment using Google Gemini 2.5 Flash.")

# User Input
text_input = st.text_area("What's on your mind?", placeholder="Type something here...", height=150)

if st.button("Analyze Emotions", use_container_width=True):
    if text_input.strip():
        with st.spinner("Gemini is thinking..."):
            try:
                # Call our existing logic
                result = emotion_detector(text_input)
                
                # Layout columns for the result
                col1, col2 = st.columns([1, 1])
                
                with col1:
                    st.subheader(f"Dominant: {result.dominant_emotion.upper()}")
                    # Prepare data for the chart
                    chart_data = pd.DataFrame({
                        "Emotion": ["Anger", "Disgust", "Fear", "Joy", "Sadness"],
                        "Score": [result.anger, result.disgust, result.fear, result.joy, result.sadness]
                    })
                    st.bar_chart(chart_data.set_index("Emotion"))

                with col2:
                    st.json(result.model_dump()) # Shows the raw data neatly
                    
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter some text first!")
