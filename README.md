
# Fake Review Detector

This is a simple web application that detects fake reviews using a machine learning model trained on synthetic data. The app is built using Python (Flask) for the backend and HTML/CSS/JavaScript for the frontend.

## Features

- Input any review text and check if it is fake or real.
- Lightweight, clean interface.
- Powered by a Logistic Regression model and TF-IDF vectorization.

## Getting Started

### Prerequisites

Install the required Python packages:

```bash
pip install flask joblib scikit-learn
```

### Running the App

1. Unzip the project folder.
2. Open a terminal and navigate to the project directory.
3. Run the Flask app:

```bash
python app.py
```

4. Open your browser and go to `http://127.0.0.1:5000`.

## Project Structure

```
fake_review_detector/
│
├── app.py                  # Flask backend
├── fake_review_model.pkl   # Trained Logistic Regression model
├── vectorizer.pkl          # TF-IDF vectorizer
├── fake_reviews_dataset.csv  # Sample dataset
├── index.html              # Frontend HTML
├── styles.css              # CSS styling
└── script.js               # JavaScript for frontend logic
```

## Dataset

- The dataset contains 500 synthetic reviews (250 real, 250 fake) with basic phrases for demonstration purposes.

## Note

This app is a demo using synthetic data. For real-world applications, you'd need a large, labeled dataset of real and fake reviews.

