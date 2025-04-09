from transformers import pipeline

# Load model once globally
sentiment_model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def get_sentiment_transformer(text):
    result = sentiment_model(text[:512])[0]
    label = result['label']
    return 1 if label == 'POSITIVE' else -1 if label == 'NEGATIVE' else 0