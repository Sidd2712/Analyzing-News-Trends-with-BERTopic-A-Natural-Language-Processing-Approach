# Information Retrieval & Extraction (IRE) Project  
## Topic Modeling on News Articles about the Pahalgam Attack

---

### Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Dataset](#dataset)
4. [Project Structure](#project-structure)
5. [Installation](#installation)
6. [Usage](#usage)
7. [Results & Visualisations](#results--visualisations)
8. [Acknowledgements](#acknowledgements)

---

## Overview
This project demonstrates an end‑to‑end **Information Retrieval & Extraction** pipeline for uncovering latent themes in news coverage of the **Pahalgam attack**.

* **Data Acquisition** — Scrape multiple RSS feeds to collect relevant news stories.
* **Data Storage** — Serialize the raw items to `output/phalgam_attack_articles.csv`.
* **Topic Modeling** — Apply **[BERTopic](https://maartengr.github.io/BERTopic/)** to generate interpretable topics from article summaries.
* **Interactive Exploration** — Render Plotly‑based dashboards for deeper insight.

> *Why BERTopic?*  It leverages transformer embeddings, UMAP for dimensionality reduction and HDBSCAN for density‑based clustering, delivering coherent topics with minimal tuning.

---

## Features
- 🔎 **Automated RSS Scraper** – configurable sources & date range filters.
- 🗂️ **Clean CSV Output** – duplicate removal, stop‑word filtering & Unicode normalisation.
- 🧠 **BERTopic Pipeline** – one‑line `fit_transform` or fully customisable components.
- 📊 **Interactive HTML Visuals** – explore topics, their probabilities & representative terms.
- 🛠️ **Modular Codebase** – clear separation of scrape → prepare → model → visualise steps.

---

## Dataset
| Column | Description |
| `title` | Headline of the news article |
| `link`  | Original URL |
| `published` | Publication timestamp (UTC) |
| `summary` | Extracted summary/description text |
| `source` | RSS feed identifier |

<details>
<summary>Sample Record</summary>

```json
{
  "title": "Militants attack convoy in Pahalgam, casualties feared",
  "link": "https://news.example.com/article123",
  "published": "2025‑05‑14T10:07:00Z",
  "summary": "Several security personnel were injured when militants opened fire on…",
  "source": "Example News RSS"
}
```
</details>

---

## Project Structure
```
├── output/
│   ├── phalgam_attack_articles.csv
├── config/
│   └── aggregator_config.json/             # RSS Links
├── aggregator.py
|── main.py 
├── bert.py      
├── fetcher.py      
└── requirements.txt     
└── README.md               # you are here
```

---

## Installation
```bash
# Clone the repo
$ git clone https://github.com/<your‑user>/pahalgam‑bertopic.git
$ cd pahalgam‑bertopic

# Create env & install deps
$ pip install requirements.txt

## Usage
```bash
# 1️ Scrape latest articles (edit sources in src/scrape_rss.py)
$ python main.py

# 2 Run topic modelling
$ python bert.py

# 4️⃣ Launch interactive visualisations (opens browser tab)
$ python src/visualise.py
```


Contributions are welcome — feel free to open issues or pull requests.

---

## Contributing
1. Fork the repo & create your branch: `git checkout -b feature/foo`
2. Commit your changes: `git commit -m 'Add foo'`
3. Push to the branch: `git push origin feature/foo`
4. Open a Pull Request


## Acknowledgements
- [Maarten Grootendorst](https://github.com/MaartenGr) for **BERTopic**
- [Plotly](https://plotly.com/python/) for interactive charts
- RSS feeds from `The Hindu`, `Indian Express`, `Times of India`, and other reputable outlets

---

> *Developed with ❤️ by [Siddharth](https://github.com/Sidd2712) – May 2025*

