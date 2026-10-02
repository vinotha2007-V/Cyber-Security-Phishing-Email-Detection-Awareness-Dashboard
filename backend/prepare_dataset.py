
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_PATH = BASE_DIR / "dataset" / "public_emails.csv"
OUTPUT_PATH = BASE_DIR / "dataset" / "emails.csv"

MAX_PER_CLASS = 25000
CHUNK_SIZE = 20000

collected = {
    "legitimate": [],
    "phishing": []
}

# For this dataset: 0 = legitimate, 1 = phishing
label_map = {
    "0": "legitimate",
    "0.0": "legitimate",
    "1": "phishing",
    "1.0": "phishing"
}

for chunk in pd.read_csv(
    INPUT_PATH,
    usecols=["body", "label"],
    chunksize=CHUNK_SIZE,
    low_memory=False
):
    chunk = chunk.rename(columns={"body": "text"})
    chunk = chunk.dropna(subset=["text", "label"])

    chunk["text"] = chunk["text"].astype(str).str.strip()
    chunk["label"] = (
        chunk["label"].astype(str).str.strip().str.lower()
    )
    chunk["label"] = chunk["label"].map(label_map)

    chunk = chunk.dropna(subset=["label"])
    chunk = chunk[chunk["text"].str.len() > 0]
    chunk = chunk.drop_duplicates(subset=["text"])

    for label in ["legitimate", "phishing"]:
        current_count = sum(
            len(part) for part in collected[label]
        )
        remaining = MAX_PER_CLASS - current_count

        if remaining > 0:
            rows = chunk[chunk["label"] == label].head(remaining)
            if not rows.empty:
                collected[label].append(rows[["text", "label"]])

    print({
        label: sum(len(part) for part in parts)
        for label, parts in collected.items()
    })

    if all(
        sum(len(part) for part in collected[label]) >= MAX_PER_CLASS
        for label in collected
    ):
        break

frames = [
    part
    for parts in collected.values()
    for part in parts
]

if not frames or any(not collected[label] for label in collected):
    raise ValueError(
        "Could not collect both classes. Check dataset label values."
    )

df = pd.concat(frames, ignore_index=True)
df = df.drop_duplicates(subset=["text"])
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

print("\nFinal counts:")
print(df["label"].value_counts())

df.to_csv(OUTPUT_PATH, index=False)
print(f"\nSaved prepared dataset: {OUTPUT_PATH}")
print(f"Total emails: {len(df)}")