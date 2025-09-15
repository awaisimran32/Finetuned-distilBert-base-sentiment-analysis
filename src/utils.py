# src/utils.py
import logging
from typing import List, Tuple

logger = logging.getLogger(__name__)

def format_prediction(pred: Tuple[str, float]) -> dict:
    label, conf = pred
    return {"sentiment": label, "confidence": round(conf, 4)}

def format_batch(preds: List[Tuple[str, float]]):
    return [format_prediction(p) for p in preds]
