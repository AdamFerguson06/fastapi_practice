from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

sentiment_analysis = pipeline("sentiment-analysis")

class TextData(BaseModel):
    text: str

@app.post("/analyze_sentiment")
def analyze_sentiment(data: TextData):
    result = sentiment_analysis(data.text)
    return result
