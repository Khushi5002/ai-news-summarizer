import os
from google import genai
from dotenv import load_dotenv

load_dotenv('../.env')

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def summarize_articles(articles):
    summaries = []

    for article in articles:
        title = article.get("title", "No title")
        description = article.get("description", "")

        if not description:
            summaries.append({
                "title": title,
                "summary": "No content available to summarize.",
                "url": article.get("url", ""),
                "source": article.get("source", "")
            })
            continue

        prompt = f"""
        Summarize this news article in 2-3 clear sentences for a general audience.
        Title: {title}
        Content: {description}
        Give only the summary, nothing else.
        """

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            summary = response.text.strip()
        except Exception as e:
            summary = "Could not generate summary at this time."
            print(f"Gemini error for '{title}': {e}")

        summaries.append({
            "title": title,
            "summary": summary,
            "url": article.get("url", ""),
            "source": article.get("source", "")
        })

    return summaries