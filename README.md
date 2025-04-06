# Customer Review Scraper & Sentiment Analyzer 🕵️‍♂️📊

This project uses Python to scrape customer reviews from websites like Amazon or Trustpilot using Selenium. It then applies sentiment analysis using NLTK to classify reviews as Positive, Negative, or Neutral, and generates a sentiment distribution graph for visualization.

---

## 🚀 Features

- 🔍 Scrapes product reviews from a given URL
- 🤖 Performs sentiment analysis using VADER (NLTK)
- 📈 Visualizes the sentiment results in a pie chart
- 🗃️ Saves reviews and sentiment data as a CSV file

---

## 🛠️ Tech Stack

- Python 3.x
- Selenium
- NLTK
- Pandas
- Matplotlib

---

## 📁 Folder Structure

project/ │ 
├── main.py # Main driver script 

├── data/ 
  │ └── reviews.csv # CSV file containing scraped reviews 

├── src/  
  ├── scraper.py # Web scraper logic using Selenium │ 
  ├── sentiment_analysis.py# Sentiment analysis logic 
  │ └── visualize.py # Graph generation logic


---

## ⚙️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/ProRiko/review-sentiment-analyzer.git
   cd review-sentiment-analyzer
2. Install the required packages:
  pip install -r requirements.txt

3. Download NLTK data:
import nltk
nltk.download('vader_lexicon')

4. Run the scraper:
python main.py

🧪 Sample Output
CSV File: data/reviews.csv
Sentiment Pie Chart: sentiment_graph.png
Console Output: Number of positive, negative, and neutral reviews.
