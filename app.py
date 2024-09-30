from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Threat Detection System is Running"

if __name__ == "__main__":
    app.run(debug=True)
