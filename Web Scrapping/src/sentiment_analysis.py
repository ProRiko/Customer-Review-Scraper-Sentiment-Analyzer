import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd

def analyze_sentiment(reviews):
    nltk.download('vader_lexicon')
    sia = SentimentIntensityAnalyzer()
    sentiments = {"Positive": 0, "Negative": 0, "Neutral": 0}
    
    for review in reviews:
        score = sia.polarity_scores(review)
        if score['compound'] > 0.05:
            sentiments["Positive"] += 1
        elif score['compound'] < -0.05:
            sentiments["Negative"] += 1
        else:
            sentiments["Neutral"] += 1
    
    return sentiments

if __name__ == "__main__":
    df = pd.read_csv("../data/reviews.csv")
    results = analyze_sentiment(df['Review'].tolist())
    print("Sentiment Analysis Results:", results)
