from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import logging
from src.inference import predict_single, predict_batch
from src.utils import format_prediction, format_batch

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("api")

app = FastAPI(title="XLnet Sentiment Analysis API", version="1.0")

class TextItem(BaseModel):
    text: str

class BatchText(BaseModel):
    texts: List[str]
    top_k: Optional[int] = None

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/predict")
def predict(item: TextItem):
    if not item.text:
        raise HTTPException(status_code=400, detail="text is required")
    label, conf = predict_single(item.text)
    return format_prediction((label, conf))

@app.post("/predict_batch")
def predict_batch_endpoint(batch: BatchText):
    if not batch.texts:
        raise HTTPException(status_code=400, detail="texts must be a non-empty list")
    results = predict_batch(batch.texts)
    return format_batch(results)

# Quick root
@app.get("/")
def root():
    return {"message": "Xlnet Sentiment Analysis API - see /docs for interactive UI"}
