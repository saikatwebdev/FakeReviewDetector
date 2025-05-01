
from flask import Flask, request, jsonify, send_from_directory
import joblib

app = Flask(__name__)
model = joblib.load("fake_review_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/styles.css")
def css():
    return send_from_directory(".", "styles.css")

@app.route("/script.js")
def js():
    return send_from_directory(".", "script.js")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    review = data["review"]
    vec = vectorizer.transform([review])
    prediction = model.predict(vec)[0]
    result = "Fake Review" if prediction == 1 else "Real Review"
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
