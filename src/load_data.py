from datasets import load_dataset
import pandas as pd
import os

def get_sample_reviews(n=500):
    print("📦 Downloading dataset...")
    dataset = load_dataset("amazon_polarity", split=f"train[:{n}]")
    df = pd.DataFrame(dataset)

    # Map 0 => negative, 1 => positive
    df["label"] = df["label"].map({0: "negative", 1: "positive"})
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/sample_reviews.csv", index=False, encoding="utf-8")
    print(f"✅ Saved {len(df)} reviews to data/sample_reviews.csv")

if __name__ == "__main__":
    get_sample_reviews()
