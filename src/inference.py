from functools import lru_cache
from typing import List, Tuple
import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import logging

logger = logging.getLogger(__name__)

MODEL_DIR = "model"  #change this if your model path is different
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

@lru_cache(maxsize=1)
def load_model_and_tokenizer(model_dir: str = MODEL_DIR):
    """
    Loads tokenizer and model from local directory or HF model id.
    Cached so repeated imports are fast.
    """
    logger.info("Loading tokenizer and model from %s", model_dir)
    tokenizer = AutoTokenizer.from_pretrained(model_dir)
    model = AutoModelForSequenceClassification.from_pretrained(model_dir)
    model.to(DEVICE)
    model.eval()
    return tokenizer, model

def preprocess(texts: List[str], tokenizer, max_length: int = 256):
    return tokenizer(
        texts,
        padding=True,
        truncation=True,
        max_length=max_length,
        return_tensors="pt",
    )

def predict_batch(texts: List[str]) -> List[Tuple[str, float]]:
    """
    Predict a batch of texts. Returns list of (label, confidence) where confidence is probability of predicted label.
    """
    if not isinstance(texts, list):
        raise ValueError("texts must be a list of strings")

    tokenizer, model = load_model_and_tokenizer()
    inputs = preprocess(texts, tokenizer)
    # move to device
    inputs = {k: v.to(DEVICE) for k, v in inputs.items()}

    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits  # shape (batch, num_labels)
        probs = F.softmax(logits, dim=-1)
        confs, preds = torch.max(probs, dim=-1)  # highest prob per sample

    # get label mapping if present in model config
    labels = None
    config = getattr(model, "config", None)
    if config and hasattr(config, "id2label"):
        id2label = config.id2label
        labels = [id2label[int(p.item())] for p in preds]
    else:
        # fallback: 0 -> NEGATIVE, 1 -> POSITIVE
        labels = ["NEGATIVE" if p.item() == 0 else "POSITIVE" for p in preds]

    results = []
    for label, conf in zip(labels, confs):
        results.append((label, float(conf.item())))
    return results

def predict_single(text: str) -> Tuple[str, float]:
    return predict_batch([text])[0]
