
import pandas as pd
import joblib
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "dataset" / "emails.csv"
MODEL_PATH = BASE_DIR / "models" / "phishing_model.joblib"
REPORT_PATH = BASE_DIR / "models" / "evaluation_report.txt"

# Load dataset
print("Loading dataset...")
df = pd.read_csv(DATA_PATH)

# Clean dataset
df = df.dropna(subset=["text", "label"])
df["text"] = df["text"].astype(str).str.strip()
df["label"] = df["label"].astype(str).str.strip().str.lower()

df = df[df["label"].isin(["phishing", "legitimate"])]
df = df[df["text"].str.len() > 0]
df = df.drop_duplicates(subset=["text"]).reset_index(drop=True)

print("Dataset size:", len(df))
print("\nClass counts:")
print(df["label"].value_counts())

if df["label"].nunique() != 2:
    raise ValueError(
        "Dataset must contain both phishing and legitimate labels."
    )

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    df["text"],
    df["label"],
    test_size=0.20,
    random_state=42,
    stratify=df["label"]
)

# Build machine learning pipeline
model = Pipeline([
    (
        "tfidf",
        TfidfVectorizer(
            lowercase=True,
            ngram_range=(1, 2),
            max_features=5000,
            sublinear_tf=True
        )
    ),
    (
        "classifier",
        LogisticRegression(
            max_iter=1000,
            class_weight="balanced",
            random_state=42
        )
    )
])

# Train model
print("\nTraining model...")
model.fit(X_train, y_train)

# Evaluate model
print("\nEvaluating model...")
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

report = classification_report(
    y_test,
    predictions,
    labels=["legitimate", "phishing"],
    zero_division=0
)

matrix = confusion_matrix(
    y_test,
    predictions,
    labels=["legitimate", "phishing"]
)

print("\nTest Accuracy:", round(accuracy * 100, 2), "%")
print("\nClassification Report:")
print(report)

print("\nConfusion Matrix:")
print(matrix)

# Create models folder if needed
MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)

# Save trained model
joblib.dump(model, MODEL_PATH)

# Save evaluation report
with open(REPORT_PATH, "w", encoding="utf-8") as file:
    file.write("PHISHING EMAIL DETECTION - MODEL EVALUATION\n")
    file.write("=" * 45 + "\n\n")
    file.write(f"Dataset size: {len(df)}\n")
    file.write(f"Training samples: {len(X_train)}\n")
    file.write(f"Testing samples: {len(X_test)}\n")
    file.write(f"Test accuracy: {accuracy * 100:.2f}%\n\n")
    file.write("Classification Report:\n")
    file.write(report)
    file.write("\nConfusion Matrix:\n")
    file.write(str(matrix))
    file.write(
        "\n\nConfusion matrix label order: "
        "legitimate, phishing\n"
    )

print("\nModel saved successfully:")
print(MODEL_PATH)

print("\nEvaluation report saved successfully:")
print(REPORT_PATH)

print("\nTraining and evaluation completed!")