from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained Random Forest model
model = joblib.load('random_forest_model.pkl')  # Make sure this file exists

@app.route('/')
def home():
    return "Welcome to the Threat Detection System"

@app.route('/detect', methods=['POST'])
def detect_threat():
    data = request.json
    threat_indicator = data.get('threat_indicator')

    # Feature extraction based on the threat indicator
    features = []

    # Customize the features based on the threat_indicator
    if threat_indicator == "malicious_ip":
        features = [1, 0, 1]  # Example features for a malicious IP
    elif threat_indicator == "safe_ip":
        features = [0, 1, 0]  # Example features for a safe IP
    else:
        return jsonify({"error": "Unknown threat indicator"}), 400

    # Check if the number of features is correct
    if len(features) != 3:  # Ensure this matches your model's expected input
        return jsonify({"error": "Invalid number of features"}), 400

    # Predict using the Random Forest model
    prediction = model.predict([features])[0]

    result = "Threat Detected" if prediction == 1 else "No Threat Detected"
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
