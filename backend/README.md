# 🛡️ Cyber Security – Phishing Email Detection & Awareness Dashboard

## 📌 Project Overview

The **Phishing Email Detection & Awareness Dashboard** is a machine learning-based cybersecurity project designed to analyze email text and identify potential phishing attempts.

The application uses Natural Language Processing (NLP) and machine learning techniques to classify emails as potentially phishing or legitimate. It also provides risk information, warning signs, and safety recommendations to improve cybersecurity awareness.

## 🎯 Objectives

* Detect potential phishing emails using machine learning.
* Classify email text into phishing or legitimate categories.
* Display risk scores and suspicious warning signs.
* Provide safety advice to help users recognize phishing attempts.
* Demonstrate the practical application of AI and cybersecurity.

## ✨ Key Features

* 🤖 **Machine Learning-Based Detection** – Analyzes email text using a trained ML model.
* 📧 **Email Classification** – Predicts whether an email is potentially phishing or legitimate.
* ⚠️ **Risk Assessment** – Displays a risk score for analyzed emails.
* 🔍 **Warning Signs** – Highlights potential suspicious indicators.
* 🛡️ **Security Awareness** – Provides recommendations for safer email practices.
* 📊 **Model Evaluation** – Generates an evaluation report containing accuracy, classification metrics, and a confusion matrix.
* 💻 **Interactive Dashboard** – Provides a web interface for testing email samples.

## 🧰 Technologies Used

* **Frontend:** React.js, Vite, JavaScript, HTML, CSS
* **Backend:** Python, Flask, Flask-CORS
* **Machine Learning:** Scikit-learn, Logistic Regression
* **Natural Language Processing:** TF-IDF Vectorization
* **Data Processing:** Pandas
* **Model Storage:** Joblib
* **Dataset:** Prepared email text dataset with phishing and legitimate labels

## 🏗️ Project Architecture

```text
Cyber-Security-Phishing-Email-Detection-Awareness-Dashboard/
│
├── backend/
│   ├── app.py
│   ├── train_model.py
│   ├── prepare_dataset.py
│   └── inspect_dataset.py
│
├── frontend/
│   └── React + Vite application
│
├── dataset/
│   ├── public_emails.csv
│   └── emails.csv
│
├── models/
│   ├── phishing_model.joblib
│   └── evaluation_report.txt
│
└── README.md
```

## ⚙️ How It Works

1. The user enters email text in the dashboard.
2. The frontend sends the email text to the Flask backend.
3. The backend processes the text using the trained machine learning pipeline.
4. The model predicts the email category.
5. The dashboard displays the prediction, risk score, warning signs, and safety advice.
6. The model evaluation report provides metrics for assessing performance on a test dataset.

## 🚀 Installation and Setup

### Prerequisites

Install the following:

* Python 3
* Node.js and npm
* Visual Studio Code

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd Cyber-Security-Phishing-Email-Detection-Awareness-Dashboard
```

Replace the repository URL with your actual GitHub repository URL.

### 2. Install Backend Dependencies

From the project root directory, run:

```bash
python -m pip install flask flask-cors pandas scikit-learn joblib
```

### 3. Start the Backend

```bash
python backend/app.py
```

Keep this terminal running.

### 4. Install Frontend Dependencies

Open a second terminal:

```bash
cd frontend
npm install
```

### 5. Start the Frontend

```bash
npm run dev
```

Open the local URL displayed by Vite in your browser. For example:

```text
http://localhost:5174/
```

The port may differ depending on your local setup.

## 🧪 Model Training and Evaluation

To train the model using the prepared dataset, run the following command from the project root:

```bash
python backend/train_model.py
```

The training script evaluates the model and saves:

* `models/phishing_model.joblib` – Trained machine learning pipeline.
* `models/evaluation_report.txt` – Test accuracy, classification report, and confusion matrix.

The actual performance should be verified using the generated evaluation report.

## 🔐 Security Notes

* Do not use real confidential emails or sensitive personal information for testing.
* Treat model predictions as indicators, not as a guarantee that an email is safe or malicious.
* Verify suspicious links and sender addresses independently.
* Keep dependencies updated and avoid exposing secrets in source code.
* Large datasets and generated model files may be better managed separately from Git if repository size becomes an issue.

## 🔮 Future Enhancements

* Add URL and attachment analysis.
* Improve detection of previously unseen phishing patterns.
* Add user authentication and secure scan history.
* Introduce visual analytics for prediction results.
* Deploy the application to a cloud platform.
* Add more diverse and well-documented email datasets.
* Evaluate precision, recall, F1-score, and false-positive rates on independent data.

## ⚠️ Disclaimer

This project is developed for educational purposes and cybersecurity awareness. Machine learning predictions may contain false positives and false negatives. Do not rely on this application as the only method for determining whether an email is safe.

## 👩‍💻 Author

**Vinotha**

Cybersecurity | Machine Learning | Python | React.js

## ⭐ Acknowledgment

This project demonstrates how machine learning and natural language processing can be applied to email security and phishing awareness.
