from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    env = os.environ.get("APP_ENV", "développement")
    return f"<h1>Flask fonctionne !</h1><p>Environnement : {env}</p>"

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)