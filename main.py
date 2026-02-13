from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from logic import emotion_detector, EmotionResponse
import os

app = FastAPI(title="Modern Emotion Detector")

# 1. THE HOME ROUTE (Must be at the top)
@app.get("/")
async def read_index():
    # Make sure index.html is actually inside a folder named 'static'
    return FileResponse('static/index.html')

# 2. THE API ROUTE
@app.get("/emotionDetector", response_model=EmotionResponse)
async def detect_emotion(textToAnalyze: str):
    if not textToAnalyze.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    return emotion_detector(textToAnalyze)

# 3. THE STATIC MOUNT (Must be at the bottom)
# This handles CSS/JS files inside the static folder
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")
