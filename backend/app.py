
from flask import Flask, request, jsonify
from flask_cors import CORS
from pathlib import Path
import joblib
import re

app = Flask(__name__)
CORS(app)

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "phishing_model.joblib"

# Load the trained machine learning model
model = joblib.load(MODEL_PATH)


def analyze_email(email):
    prediction = model.predict([email])[0]

    probabilities = model.predict_proba([email])[0]
    classes = list(model.classes_)

    phishing_index = classes.index("phishing")
    phishing_probability = float(probabilities[phishing_index])

    risk_score = round(phishing_probability * 100)

    text = email.lower()

    checks = {
        "Suspicious link": bool(
            re.search(r"https?://|www\.", text)
        ),
        "Urgent language": any(
            word in text for word in [
                "urgent", "immediately", "act now",
                "account suspended", "verify now"
            ]
        ),
        "Requests sensitive information": any(
            phrase in text for phrase in [
                "password", "bank details",
                "credit card", "otp", "one-time password"
            ]
        ),
        "Prize or reward claim": any(
            phrase in text for phrase in [
                "you won", "claim your prize",
                "free gift", "lottery winner"
            ]
        ),
    }

    warning_signs = [
        name for name, found in checks.items() if found
    ]

    if prediction == "phishing":
        verdict = "Potential Phishing"
        advice = (
            "Do not click links or share sensitive information. "
            "Verify the sender through an official channel."
        )
    else:
        verdict = "Likely Legitimate"
        advice = (
            "The model classified this email as likely legitimate. "
            "Still verify the sender and links before trusting it."
        )

    return {
        "verdict": verdict,
        "prediction": prediction,
        "risk_score": risk_score,
        "warning_signs": warning_signs,
        "advice": advice,
        "model_type": "TF-IDF + Logistic Regression",
        "disclaimer": (
            "This is a beginner model trained on a small sample "
            "dataset. Its predictions are not proof that an email "
            "is safe or malicious."
        )
    }


@app.route("/")
def home():
    return jsonify({
        "message": "Phishing Email Detection ML API is running!"
    })


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "model_loaded": MODEL_PATH.exists()
    })


@app.route("/api/analyze", methods=["POST"])
def analyze():
    data = request.get_json(silent=True) or {}
    email = data.get("email", "")

    if not isinstance(email, str) or not email.strip():
        return jsonify({
            "error": "Please provide email text to analyze."
        }), 400

    if len(email) > 20000:
        return jsonify({
            "error": "Email text must be 20,000 characters or less."
        }), 400

    return jsonify(analyze_email(email))


if __name__ == "__main__":
    app.run(debug=True, port=5000)