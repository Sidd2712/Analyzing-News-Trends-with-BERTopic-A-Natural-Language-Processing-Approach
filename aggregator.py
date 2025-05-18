import pandas as pd
from datetime import timedelta

from config import START_DATE, END_DATE, SOURCES, OUTPUT_CSV
from fetcher import fetch_rss_articles


def aggregate_articles():
    all_recs = []
    for src in SOURCES:
        name, url = src['name'], src['rss_url']
        current = START_DATE
        while current <= END_DATE:
            # dates
            recs = fetch_rss_articles(url, name, START_DATE, END_DATE)
            all_recs.extend(recs)
            break
    df = pd.DataFrame(all_recs)
    df.drop_duplicates(subset=["link"], inplace=True)
    df.to_csv(OUTPUT_CSV, index=False)
    print(f"✅ Saved {len(df)} articles across {len(SOURCES)} sources to {OUTPUT_CSV}")
