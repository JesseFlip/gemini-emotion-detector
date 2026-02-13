import os
from pydantic import BaseModel, Field
from google import genai  # <--- The new modern import
from dotenv import load_dotenv

load_dotenv()

# Our data model stays exactly the same
class EmotionResponse(BaseModel):
    anger: float = Field(description="Score from 0 to 1")
    disgust: float = Field(description="Score from 0 to 1")
    fear: float = Field(description="Score from 0 to 1")
    joy: float = Field(description="Score from 0 to 1")
    sadness: float = Field(description="Score from 0 to 1")
    dominant_emotion: str = Field(description="The emotion with the highest score")

# Initialize the new Client (it automatically looks for GEMINI_API_KEY in .env)
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def emotion_detector(text: str) -> EmotionResponse:
    # New SDK syntax: client.models.generate_content
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Analyze the following text and provide a highly granular emotional score for each category (0.0 to 1.0). Text: {text}",
        config={
            "response_mime_type": "application/json",
            "response_schema": EmotionResponse,
        }
    )
    # The new SDK is smart: .parsed returns our Pydantic object directly!
    return response.parsed