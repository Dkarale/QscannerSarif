"""
Minimal demo app used only to exercise the vulnerable dependencies pinned in
requirements.txt for QScanner SCA (code) + image scan reproduction testing.
"""
import yaml
import requests
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "QScanner vulnerable-app demo"


@app.route("/load-config")
def load_config():
    # Demo call exercising PyYAML (kept simple; not meant for real use).
    with open("config.yaml") as f:
        return str(yaml.load(f, Loader=yaml.FullLoader))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
