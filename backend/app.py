from flask import Flask, request, jsonify
from flask_cors import CORS
from news import get_news
from summarizer import summarize_articles
import os
from dotenv import load_dotenv
load_dotenv('../.env')
app = Flask(__name__)
CORS(app)
@app.route("/")
def home():
    return jsonify({"message": "AI News Summarizer API is running!"})
@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json()
    topic = data.get("topic", "")
    if not topic:
        return jsonify({"error": "Please provide a topic"}), 400
    # Step 1 - Fetch news articles
    articles = get_news(topic)
    if not articles:
        return jsonify({"error": "No articles found for this topic"}), 404
    # Step 2 - Summarize using Gemini AI
    summaries = summarize_articles(articles)
    return jsonify({
        "topic": topic,
        "summaries": summaries
    })
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug_mode = os.environ.get("FLASK_DEBUG", "True") == "True"
    app.run(debug=debug_mode, host="0.0.0.0", port=port)