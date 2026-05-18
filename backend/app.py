from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load model and encoder
model = joblib.load("backend/risk_model.pkl")
label_encoder = joblib.load("backend/label_encoder.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        print("Received data:", data)

        # Validate and extract data
        co = float(data.get("CO"))
        ch4 = float(data.get("CH4"))
        h2s = float(data.get("H2S"))
        o2 = float(data.get("O2"))

        features = np.array([[co, ch4, h2s, o2]])

        prediction = model.predict(features)[0]
        risk_level = label_encoder.inverse_transform([prediction])[0]

        print("Predicted risk level:", risk_level)
        return jsonify({"risk_level": risk_level})

    except Exception as e:
        print("Prediction error:", str(e))
        return jsonify({"error": "Prediction failed", "details": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
