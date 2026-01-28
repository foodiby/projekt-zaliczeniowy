from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return f"<h1>Serwer działa!</h1><p>Kontener zbudowany automatycznie przez GitHub Actions.</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)