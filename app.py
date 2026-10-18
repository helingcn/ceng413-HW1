import os
from datetime import datetime, timezone

from flask import Flask, jsonify

app = Flask(__name__)

# Ayarlar ortam değişkenlerinden okunur; yoksa varsayılan değer kullanılır.
APP_NAME = os.environ.get("APP_NAME", "ceng413-app")
PORT = int(os.environ.get("PORT", "8080"))


@app.get("/")
def index():
    return jsonify(message=f"Hello from {APP_NAME}!")


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/time")
def current_time():
    return jsonify(utc=datetime.now(timezone.utc).isoformat())


if __name__ == "__main__":
    # 0.0.0.0: konteyner dışından gelen isteklere de cevap vermek için gerekli.
    app.run(host="0.0.0.0", port=PORT)
