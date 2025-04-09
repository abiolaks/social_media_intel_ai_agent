# Social Media intelligence Ai Agent

# 🤖 LinkedIn Engagement Intelligence Dashboard

This is an AI-powered Streamlit application that transforms LinkedIn post engagement into actionable business insights. It combines transformer-based sentiment analysis with GPT-4 powered summarization to deliver real-time visibility into how audiences interact with your posts.

---

## 🚀 Features

- 🔍 **Real-Time Engagement Feed**: Displays names, emails, and engagement types (like, comment, share).
- 🤖 **Transformer Sentiment Analysis**: Uses `distilbert-base-uncased-finetuned-sst-2-english` to detect post sentiment.
- 🧠 **LLM-Powered Insight Summarization**: GPT-4 generates executive-ready summaries of engagement trends.
- 📄 **Insight Export**: Export summarized insights to PDF.
- 📊 **Visual Dashboard**: View distribution of engagement types and sentiment over posts.

---

## 📂 Project Structure
```
linkedin_insights_demo/ 
├── app.py # Main Streamlit app 
├── components/ 
│ └── layout.py # UI layout, metrics, visualizations, GPT-4 insights 
├── data/ 
│ └── synthetic_data.py # Generates synthetic LinkedIn-like engagement data 
├── models/ 
│ └── sentiment.py # Transformer-based sentiment analysis 
├── .streamlit/ 
│ └── secrets.toml # Stores OpenAI API key 
├── requirements.txt 
└── env.yml
└── README.md
```

## 🛠 Setup Instructions

### 1. Clone the Repo

```
bash

git clone https://github.com/abiolaks/social_media_intel_ai_agent/linkedin-insights-demo.git
cd linkedin-insights-demo
```
2. Install Dependencies
```
bash

pip install -r requirements.txt
python -m textblob.download_corpora
python -m spacy download en_core_web_sm

```

3. Add OpenAI Key
Create a .streamlit/secrets.toml file:
[toml]
OPENAI_API_KEY = "your_openai_api_key"

4. Run the App
```
bash
streamlit run app.py
```
## 🧠 AI Models Used
### ➤ distilbert-base-uncased-finetuned-sst-2-english
- Transformer model trained for binary sentiment classification.
Offers strong accuracy with low latency, suitable for real-time apps.

### ➤ GPT-4 (via OpenAI API)
- Provides natural language summaries of trends and engagement data.

- Adds strategic layer of intelligence beyond raw numbers.

### 💼 Business Use Cases
- 📢 Marketing: Identify which messaging resonates and why.

- 🧲 Recruitment: Track performance of employer branding content.

- 🧠 Leadership: Stay informed on real-time employee/public sentiment.

### ☁️ Streamlit Cloud Deployment
- Push project to GitHub.

- Go to Streamlit Cloud → New App.

- Choose repo and entry point: app.py.

- Add OPENAI_API_KEY in Secrets.

Deploy and share the live link with stakeholders.

📄 License
MIT License

### ✨ Author
- Built with ❤️ by [abiolaks] 
