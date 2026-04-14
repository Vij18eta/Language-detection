from pathlib import Path

from flask import Flask, jsonify, send_file
from flask_cors import CORS

BASE_DIR = Path(__file__).resolve().parent.parent
INDEX_FILE = BASE_DIR / "index.html"

app = Flask(__name__, static_folder=str(BASE_DIR), static_url_path="")
CORS(app)


@app.route("/")
def home():
    return send_file(INDEX_FILE)


@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "app": "LinguaScope AI",
        "frontend": "static-browser-app"
    })


if __name__ == "__main__":
    app.run(debug=True)
