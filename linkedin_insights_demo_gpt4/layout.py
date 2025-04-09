import streamlit as st
import pandas as pd

def render_layout(df):
    st.subheader("🔍 Real-time Engagement Feed")
    st.dataframe(df[['Engager', 'Email', 'EngagementType', 'Comment']], height=200)

    st.markdown("### 📊 Key Engagement Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Posts", len(df['Post'].unique()))
    col2.metric("Unique Engagers", df['Email'].nunique())
    col3.metric("Avg Sentiment", round(df['Sentiment'].mean(), 2))

    st.markdown("### 📌 Sentiment by Post")
    st.dataframe(df[['Post', 'Sentiment', 'EngagementType']])

    st.markdown("### 📈 Engagement Distribution")
    st.bar_chart(df['EngagementType'].value_counts())