# -*- coding: utf-8 -*-
import streamlit as st
from analyzer import predict_sentiment

st.set_page_config(page_title="AI Review Sentiment Analyzer", layout="centered")

st.title("AI Review Sentiment Analyzer")
st.markdown("Paste a product review below and let the AI determine whether it's positive or negative.")

user_input = st.text_area("Enter your review:", height=200)

if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter a review first.")
    else:
        prediction, confidence = predict_sentiment(user_input)
        result_msg = f"Predicted Sentiment: {prediction.capitalize()} (Confidence: {confidence * 100:.1f}%)"
        if prediction == "positive":
            st.success(result_msg)
        else:
            st.error(result_msg)