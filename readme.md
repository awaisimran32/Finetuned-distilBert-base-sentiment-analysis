# DistilBert Sentiment Analysis

**End-to-end demo** of a fine-tuned DistilBert model for sentiment analysis — packaged as an API and demo UI.

## Features
- Fine-tuned DistilBert inference (local `model/` folder)
- FastAPI endpoints:
  - `GET /health`
  - `POST /predict` (single text)
  - `POST /predict_batch` (list of texts)
- Streamlit demo (frontend/app.py)
- Dockerfile for reproducible deployment
- Basic unit tests

## Repo layout
(see README in repo root for layout)

## Quick start (local)
1. Put your fine-tuned Hugging Face Transformer model in `./model/`
2. Create a virtualenv and install deps:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r api/requirements.txt
pip install streamlit requests

