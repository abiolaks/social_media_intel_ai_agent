import streamlit as st
import pandas as pd
from transformers import pipeline
from components.layout import render_layout
from models.sentiment import get_sentiment_transformer
from data.synthetic_data import generate_synthetic_data

st.set_page_config(page_title="LinkedIn Post Intelligence", layout="wide")

st.title("🤖 LinkedIn Post Engagement Intelligence Dashboard")

# Load or generate data
df = generate_synthetic_data(100)

# Apply sentiment transformer
df['Sentiment'] = df['Post'].apply(get_sentiment_transformer)

# Render layout
render_layout(df)