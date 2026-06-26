# AI News Summarizer

A web app that fetches live news articles on any topic and summarizes them using AI — so you can get the gist of what's happening without reading five different articles.

**Live demo:** _coming soon_
**Backend repo / API:** _coming soon_

---

## What it does

1. You type a topic (e.g. "artificial intelligence", "cricket", "markets")
2. The backend fetches the latest related articles via **NewsAPI**
3. Each article is summarized in 2–3 sentences using **Google's Gemini API**
4. The frontend displays clean, readable summary cards with links to the full articles

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript (vanilla, no framework) |
| Backend | Python, Flask |
| News data | [NewsAPI](https://newsapi.org/) |
| AI summarization | [Google Gemini API](https://ai.google.dev/) (`gemini-2.5-flash`) |
| Hosting | Render |

---

## Architecture

```
User enters topic
       │
       ▼
  Frontend (HTML/CSS/JS)
       │  fetch() POST /summarize
       ▼
  Backend (Flask API)
       │
       ├──► NewsAPI        (fetch articles for topic)
       │
       └──► Gemini API     (summarize each article)
       │
       ▼
  JSON response → rendered as cards on frontend
```

---

## Project Structure

```
ai-news-summarizer/
│
├── backend/
│   ├── app.py            # Flask app & /summarize route
│   ├── news.py            # NewsAPI integration
│   ├── summarizer.py       # Gemini API integration
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── .env                   # API keys (not committed)
├── .gitignore
└── README.md
```

---

## Running it locally

### 1. Clone the repo
```bash
git clone https://github.com/Khushi5002/ai-news-summarizer.git
cd ai-news-summarizer
```

### 2. Set up the backend
```bash
cd backend
pip install -r requirements.txt
```

### 3. Add your API keys
Create a `.env` file in the **project root** (one level above `backend/`) with:
```
NEWS_API_KEY=your_newsapi_key_here
GEMINI_API_KEY=your_gemini_key_here
```
- Get a free NewsAPI key at [newsapi.org](https://newsapi.org/)
- Get a free Gemini API key at [ai.google.dev](https://ai.google.dev/)

### 4. Run the backend
```bash
python app.py
```
The API will run at `http://127.0.0.1:5000`.

### 5. Run the frontend
Open `frontend/index.html` directly in your browser (or use a tool like VS Code's Live Server extension).

---

## API Reference

### `POST /summarize`

**Request body:**
```json
{ "topic": "technology" }
```

**Response:**
```json
{
  "topic": "technology",
  "summaries": [
    {
      "title": "Article title",
      "summary": "2-3 sentence AI-generated summary.",
      "source": "Source name",
      "url": "https://..."
    }
  ]
}
```

---

## Why I built this

I wanted a project that touched the full stack — a real frontend, a real backend, calls to external APIs, and actual AI/ML usage (LLM-based summarization) — without going into multi-agent complexity. This project let me practice connecting a third-party data API (NewsAPI) with an LLM API (Gemini) through a clean Flask backend, and handling real-world issues like environment variables, CORS, and API rate limits.

---

## Possible future improvements

- Batch all articles into a single Gemini call instead of one call per article (reduces API usage and avoids rate limits)
- Add caching so repeated searches for the same topic don't re-call the APIs
- Add a loading skeleton UI instead of a plain status message
- Deploy frontend and backend together with a custom domain