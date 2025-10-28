from flask import Flask, request, jsonify
import joblib
import json
import pandas as pd

app = Flask(__name__)

# Model aur columns load karo
model = joblib.load('model.pkl')

# Columns file load karo (agar hai)
with open('columns.json', 'r') as f:
    columns = json.load(f)

# Home route
from flask import Flask, render_template_string

@app.route('/')
def home():
    with open("index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    return render_template_string(html_content)


# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # User input JSON me milega
        data = request.get_json()

        # DataFrame me convert karo
        df = pd.DataFrame([data])

        # Ensure all expected columns exist
        for col in columns:
            if col not in df.columns:
                df[col] = 0
        df = df[columns]

        # Predict
        pred = model.predict(df)[0]

        # Probability (agar available hai)
        proba = None
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(df)[0].max()

        # Response
        result = {
            "prediction": int(pred),
            "probability": float(proba) if proba is not None else None
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
