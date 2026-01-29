from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Wersja 2.0!</h1><p>Właśnie przetestowałem automatyczną aktualizację.</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)