import json
import os
import pandas as pd
from fetcher import fetch_articles

def load_config():
    with open("config/aggregator_config.json", "r") as f:
        return json.load(f)["sources"]

def run_scraper():
    all_articles = []

    sources = load_config()
    for source in sources:
        print(f"🔍 Fetching from: {source['name']}")
        articles = fetch_articles(source)
        all_articles.extend(articles)

    if not os.path.exists("output"):
        os.makedirs("output")

    df = pd.DataFrame(all_articles)
    output_path = "output/phalgam_attack_articles.csv"
    df.to_csv(output_path, index=False)
    print(f"✅ Scraped {len(df)} articles. Saved to {output_path}")

if __name__ == "__main__":
    run_scraper()
