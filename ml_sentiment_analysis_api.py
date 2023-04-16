from fastapi import FastAPI, Depends
from pydantic import BaseModel
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

app = FastAPI()

class TextData(BaseModel):
    text: str


def get_sentiment_analysis_pipeline():
    tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
    model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
    sentiment_pipeline = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
    return sentiment_pipeline


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, query_param: str = None):
    return {"item_id": item_id, "query_param": query_param}


@app.post("/analyze_sentiment")
def analyze_sentiment(data: TextData, sentiment_pipeline: pipeline = Depends(get_sentiment_analysis_pipeline)):
    result = sentiment_pipeline(data.text)
    return result
