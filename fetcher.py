import feedparser
import datetime
from bs4 import BeautifulSoup

def clean_summary(html_summary):
    soup = BeautifulSoup(html_summary, "html.parser")
    text = soup.get_text().strip()
    return text

def fetch_articles(source):
    feed = feedparser.parse(source['url'])
    articles = []

    for entry in feed.entries:
        title = entry.get("title", "")
        raw_summary = entry.get("summary", "")
        summary = clean_summary(raw_summary)
        published = entry.get("published", "")
        link = entry.get("link", "")

        #no summary
        if not summary or summary.startswith("http"):
            summary = title  

        article = {
            "source": source['name'],
            "title": title,
            "summary": summary,
            "link": link,
            "published": published,
            "fetched_on": datetime.datetime.now().isoformat(),
            "text": f"{title}. {summary}"
        }
        articles.append(article)

    return articles
