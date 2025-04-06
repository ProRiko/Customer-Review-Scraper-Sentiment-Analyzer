import sys
import os

# Add src directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from scraper import get_trustpilot_reviews as get_reviews
from sentiment_analysis import analyze_sentiment
from visualize import plot_sentiments
import pandas as pd

def main():
    url = "https://www.trustpilot.com/review/amazon.com"  # Trustpilot Amazon Reviews
    reviews = get_reviews(url, max_pages=10)

    if reviews:
        df = pd.DataFrame(reviews, columns=['Review'])
        df.to_csv("data/reviews.csv", index=False)
        print("Reviews saved successfully!")
        
        sentiments = analyze_sentiment(df['Review'].tolist())
        print("Sentiment Analysis Results:", sentiments)
        plot_sentiments(sentiments)
    else:
        print("No reviews found!")

if __name__ == "__main__":
    main()
