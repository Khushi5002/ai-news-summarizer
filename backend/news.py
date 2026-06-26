import requests
import os
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def get_news(topic):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": topic,
        "searchIn": "title,description",
        "apiKey": NEWS_API_KEY,
        "language": "en",
        "sortBy": "relevancy",
        "pageSize": 5

    }
    response = requests.get(url, params=params)
    data = response.json()

    articles = []
    for article in data.get("articles", []):
        articles.append({
            "title": article["title"],
            "description": article["description"],
            "url": article["url"],
            "source": article["source"]["name"]
        })
    return articles