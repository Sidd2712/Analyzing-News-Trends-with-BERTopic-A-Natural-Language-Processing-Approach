import pandas as pd
from bertopic import BERTopic


# Optional: for interactive visualization
import plotly.io as pio
pio.renderers.default = "browser"  # opens in default browser

# Step 1: Load your CSV
df = pd.read_csv("output/phalgam_attack_articles.csv")

# Step 2: Ensure 'text' column exists and is non-empty
df["text"] = df["text"].fillna("").astype(str)
texts = df["text"].tolist()

# Step 3: Run BERTopic
topic_model = BERTopic()
topics, probs = topic_model.fit_transform(texts)

# Step 4: Show top topics
print("\n📌 Top topics:")
print(topic_model.get_topic_info().head(10))

# Step 5 (optional): Visualize
topic_model.visualize_topics().show()
