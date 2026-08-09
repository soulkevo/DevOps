# app.py
import os, signal, sys
from flask import Flask

VERSION = os.getenv("APP_VERSION", "1.0")
app = Flask(__name__)

@app.get("/")
def index():
    return f"привіт із контейнера, версія {VERSION}\n"

def bye(signum, frame):
    print("отримав SIGTERM, закриваюсь коректно", flush=True)
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGTERM, bye)
    app.run(host="0.0.0.0", port=8000)
