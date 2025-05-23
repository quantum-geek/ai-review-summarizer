
# AI Review Summarizer

A smart web app that uses AI to summarize customer reviews from e-commerce or service platforms. It helps users understand what people love, complain about, and feel overall—without reading hundreds of reviews.

## Features
- Scrape product reviews (Amazon, Yelp, etc.)
- Perform sentiment analysis
- Summarize pros, cons, and key topics
- Display results in a clean UI

## Tech Stack
- Python, BeautifulSoup, Hugging Face, Streamlit

## Project Idea: AI Review Summarizer
The goal is to build a simple AI-powered web app where users can paste a product or service review, and the app will:

Analyze the text

Predict whether the sentiment is positive or negative

Display the result clearly with a confidence score

It helps users quickly assess how a review "feels" — useful for shoppers, business owners, or researchers.


In this project, I : 
Created a project folder and virtual environment

Installed key Python packages (pandas, scikit-learn, streamlit, datasets)

Pulled real Amazon review data from Hugging Face (amazon_polarity)

Cleaned and preprocessed the review text

Trained a logistic regression sentiment classifier using TF-IDF

Wrapped the logic in analyzer.py for reuse

Built a Streamlit UI (app.py) to input reviews and display predictions

Enhanced the app to also show a confidence score