# 🚀 Finetuned‑DistilBERT Sentiment Analyzer

Full‑stack sentiment analysis with DistilBERT: model fine‑tuning, REST API, and UI demo — all containerised and deployable.

---

## 📋 Table of Contents

1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Repo Structure](#repo-structure)  
4. [Setup & Installation](#setup--installation)  
5. [Usage](#usage)  
   - Running locally  
   - API Endpoints  
   - UI Demo  
   - Docker Deployment  
6. [Testing](#testing)  
7. [Model & Data](#model--data)  
8. [Deployment](#deployment)  
9. [Future Work](#future-work)  
10. [License](#license)  

---

## 1. Project Overview

This project aims to build a sentiment analysis system using a fine‑tuned DistilBERT model. It provides:

- A **model** for classifying text (single or batch) as positive/negative (or possibly neutral)  
- A **REST API** built with FastAPI to serve inference requests  
- A **frontend demo** using Streamlit to showcase live predictions  
- Containerization via Docker for ease of deployment  
- A live demo deployed on Hugging Face Spaces  

Ideal as a reference for end‑to‑end NLP pipelines: model → API → UI → deployment.

---

## 2. Features

- Fine‑tuned DistilBERT inference (locally stored model)  
- FastAPI endpoints:  
  - `GET /health` — health check  
  - `POST /predict` — single text input  
  - `POST /predict_batch` — multiple texts in one request  
- Streamlit UI for interactive demo (text input → sentiment output)  
- Dockerfile for building the app container  
- Basic unit tests to ensure core functionality  

---

## 3. Repo Structure

```
├── .devcontainer/            # Configuration for use in codespaces/devcontainer
├── api/                      # FastAPI application and related code
│   ├── main.py               # API routes
│   └── requirements.txt      # API‑specific dependencies
├── frontend/                 # Streamlit UI app
│   └── app.py                # Streamlit demo script
├── model/                    # Fine‑tuned model files (weights, tokenizer, etc.)
├── notebooks/                # Jupyter notebooks for training / experimentation
├── src/                      # Shared utilities, helper functions
├── tests/                    # Unit tests
├── Dockerfile                # To build the container image
└── README.md                 # This file
```

---

## 4. Setup & Installation

> These instructions assume you have **Python 3.8+** installed. Docker is optional if you want containerized deployment.

1. **Clone the repository**  
   ```bash
   git clone https://github.com/awaisimran32/Finetuned‑distilBert‑base‑sentiment‑analysis.git
   cd Finetuned‑distilBert‑base‑sentiment‑analysis
   ```

2. **Place your fine‑tuned model** into the `model/` directory  
   - Include model weights, tokenizer, config as needed.  
   - Alternatively, download a pre‑trained tokenizer + weights from Hugging Face and place here.

3. **Set up virtual environment**  
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # or .venv\Scripts\activate on Windows
   ```

4. **Install dependencies**  
   ```bash
   pip install -r api/requirements.txt
   pip install streamlit requests
   ```

---

## 5. Usage

### Running Locally

- **Start API**  
  ```bash
  uvicorn api.main:app --host 0.0.0.0 --port 8000
  ```

- **Access UI Demo**  
  ```bash
  streamlit run frontend/app.py
  ```
  Navigate to `http://localhost:8501` (default) to see the UI.

### API Endpoints

| Endpoint              | Method | Description                         | Payload                          |
|-----------------------|--------|-------------------------------------|----------------------------------|
| `GET /health`         | GET    | Health check                       | None                             |
| `POST /predict`       | POST   | Predict sentiment for single text | `{ "text": "Your input here" }` |
| `POST /predict_batch` | POST   | Predict for multiple texts        | `{ "texts": ["text1", "text2"] }`|

### Docker Deployment

```bash
docker build -t sentiment-app .
docker run -d -p 8000:8000 sentiment-app
```

---

## 6. Testing

```bash
pytest tests/
```

Covers:
- Prediction correctness  
- API route availability  
- Error handling  

---

## 7. Model & Data

- Model: Fine‑tuned **DistilBERT** (lightweight BERT variant)  
- Dataset: e.g. IMDB, SST‑2, or similar (mention which you used)  
- Preprocessing: Tokenization, truncation, handling class imbalance  
- Metrics: Accuracy, F1, Precision/Recall  

---

## 8. Deployment

- Deployed on **Hugging Face Spaces** using Docker  
- Demo link: *[insert live demo URL]*  

---

## 9. Future Work

- Add neutral sentiment class  
- Improve UI/UX  
- Add monitoring + retraining  
- Orchestrate with Kubernetes  
- Async batch processing  

---

## 10. License

```
MIT License
Copyright (c) 2025 Awais Imran
```

---

## ✅ Contact / Acknowledgements

- Author: [Awais Imran](https://github.com/awaisimran32)  
- Powered by Hugging Face, FastAPI, Streamlit, Docker, and open source contributors.  
