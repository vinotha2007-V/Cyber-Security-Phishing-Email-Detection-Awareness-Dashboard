
import pandas as pd
from pathlib import Path

path = (
    Path(__file__).resolve().parent.parent
    / "dataset"
    / "public_emails.csv"
)

print("Reading dataset headers...")

df = pd.read_csv(path, nrows=5, low_memory=False)

print("\nColumn names:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head().to_string())

print("\nDataset label samples:")
for col in df.columns:
    if "label" in col.lower() or "class" in col.lower() or "type" in col.lower():
        print(f"\n{col}:")
        print(pd.read_csv(path, usecols=[col], nrows=20)[col].tolist())