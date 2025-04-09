import streamlit as st
import pandas as pd
import openai
from fpdf import FPDF
import tempfile
import os


def render_layout(df):
    st.subheader("🔍 Real-time Engagement Feed")
    st.dataframe(df[["Engager", "Email", "EngagementType", "Comment"]], height=200)

    st.markdown("### 📊 Key Engagement Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Posts", len(df["Post"].unique()))
    col2.metric("Unique Engagers", df["Email"].nunique())
    col3.metric("Avg Sentiment", round(df["Sentiment"].mean(), 2))

    st.markdown("### 📌 Sentiment by Post")
    st.dataframe(df[["Post", "Sentiment", "EngagementType"]])

    st.markdown("### 📈 Engagement Distribution")
    st.bar_chart(df["EngagementType"].value_counts())

    render_insights(df)


def render_insights(df):
    st.markdown("### 🧠 LLM-Generated Insights")

    sample = df[["Post", "EngagementType", "Sentiment"]].head(10).to_string(index=False)
    openai.api_key = st.secrets.get("OPENAI_API_KEY", "")

    if openai.api_key:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful business analyst.",
                    },
                    {
                        "role": "user",
                        "content": f"Give a short summary of what business insights we can get from this data:\n\n{sample}",
                    },
                ],
            )
            summary = response["choices"][0]["message"]["content"]
            st.write(summary)

            if st.button("📄 Export Insights to PDF"):
                export_to_pdf(summary)

        except Exception as e:
            st.warning(f"Could not generate GPT-4 summary: {e}")


def export_to_pdf(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in text.split("\n"):
        pdf.multi_cell(0, 10, line)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        pdf.output(tmp.name)
        with open(tmp.name, "rb") as f:
            st.download_button("Download PDF", f, file_name="insights.pdf")
