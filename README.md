# Threat Detection System

The Threat Detection System is a Flask-based web application that uses a machine learning model (Random Forest) to detect potential security threats based on threat indicators like IP addresses. This project is designed to mimic a system that could be used by a Security Operations Center (SOC) for identifying potential security risks.

## Features

- Detects potential security threats based on predefined indicators (like IP addresses).
- Trained Random Forest machine learning model for threat classification.
- Flask web application with a REST API for easy integration.
- Deployed on Heroku for cloud-based access.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/ashwadh21/threat-detection-system.git
cd threat-detection-system
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Step 1: Running the Flask server
Once the dependencies are installed, you can run the Flask server:

bash
Copy code
python app.py
The app will run locally at http://127.0.0.1:5000/.

API Endpoints
1. Home Route
URL: /
Method: GET
Description: Returns a simple welcome message indicating that the system is running.
Example Response:
json
Copy code
"Welcome to the Threat Detection System"
2. Threat Detection Route
URL: /detect

Method: POST

Content-Type: application/json

Description: Accepts a JSON object containing a threat_indicator and returns a classification result (either "Threat Detected" or "No Threat Detected").

Payload:

json

{
  "threat_indicator": "malicious_ip"
}
Example Response for Threat Detected:

json
{
  "result": "Threat Detected"
}
Example Response for Safe Event:

json
{
  "result": "No Threat Detected"
}
Testing the System
To test the system locally, use a tool like curl or Postman to make requests to the /detect endpoint.

Testing with curl:
For a malicious IP:

bash

curl -X POST http://127.0.0.1:5000/detect -H "Content-Type: application/json" -d '{"threat_indicator": "malicious_ip"}'
For a safe IP:

bash

curl -X POST http://127.0.0.1:5000/detect -H "Content-Type: application/json" -d '{"threat_indicator": "safe_ip"}'
Testing with Postman:
Open Postman.
Select POST as the method.
Set the URL as http://127.0.0.1:5000/detect.
Under the Body tab, select raw and JSON format.
Provide the JSON input (e.g., {"threat_indicator": "malicious_ip"}) and send the request.
