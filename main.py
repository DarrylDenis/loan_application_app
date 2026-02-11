from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os

from preprocessing import clean_raw_data
from features import add_credit_history_features
from config import MODEL_PATH


app = Flask(__name__)


if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError("Model file not found. Train the model first.")

model = joblib.load(MODEL_PATH)

@app.route("/")
def home():
    return jsonify({"message": "Loan Default Prediction API is running"})


@app.route("/predict", methods=["POST"])
def predict():

    try:
        data = request.get_json()

        
        input_df = pd.DataFrame([data])

        
        input_df = clean_raw_data(input_df)
        input_df = add_credit_history_features(input_df)

        
        prediction = model.predict(input_df)[0]
        probability = model.predict_proba(input_df)[0][1]

        response = {
            "prediction": int(prediction),
            "default_probability": round(float(probability), 4)
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
