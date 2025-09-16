import streamlit as st
import requests
import json
from typing import List

st.set_page_config(page_title="DisitlBert Sentiment Analyzer Demo", layout="centered")

API_URL = st.secrets.get("api_url", "http://localhost:8000")

st.title("DistilBert Sentiment Analysis Demo")
st.markdown("Type a sentence and get sentiment prediction from your fine-tuned Distil Bert model.")

text = st.text_area("Enter text", value="I love this product. It works great!")

if st.button("Analyze"):
    if not text.strip():
        st.warning("Enter some text first")
    else:
        try:
            res = requests.post(f"{API_URL}/predict", json={"text": text}, timeout=10)
            res.raise_for_status()
            out = res.json()
            st.write("**Prediction**")
            st.json(out)
            st.progress(int(out.get("confidence", 0) * 100))
        except Exception as e:
            st.error(f"Request failed: {e}")
            st.write("Make sure the API is running at", API_URL)

st.markdown("---")
st.markdown("For batch demo, provide multiple lines and press **Analyze Batch**")

batch_text = st.text_area("Batch texts (one per line)", value="I loved it!\nIt was very scary.")
if st.button("Analyze Batch"):
    texts = [t.strip() for t in batch_text.splitlines() if t.strip()]
    if not texts:
        st.warning("Add at least one line")
    else:
        try:
            res = requests.post(f"{API_URL}/predict_batch", json={"texts": texts}, timeout=20)
            res.raise_for_status()
            out = res.json()
            for i, o in enumerate(out):
                st.write(f"**{i+1}.** {texts[i]}")
                st.json(o)
        except Exception as e:
            st.error(f"Request failed: {e}")

