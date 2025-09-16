import pytest
from src.inference import predict_single, predict_batch

def test_predict_single():
    text = "I love this!"
    label, conf = predict_single(text)
    assert isinstance(label, str)
    assert 0.0 <= conf <= 1.0

def test_predict_batch():
    texts = ["I loved it", "This is awful"]
    results = predict_batch(texts)
    assert len(results) == 2
    for label, conf in results:
        assert isinstance(label, str)
        assert 0.0 <= conf <= 1.0

