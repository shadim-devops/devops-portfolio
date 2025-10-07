
from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.get("/")
def root():
    return jsonify({
        "app": "devops-portfolio",
        "message": "Hello from Flask on Kubernetes!",
    })

@app.get("/health")
def health():
    return jsonify({"status": "ok"})

@app.get("/metrics")
def metrics():
    # Placeholder for Prometheus metrics;
    # integrate prometheus_client if you want real metrics.
    return "custom_app_metric 1\n", 200, {"Content-Type": "text/plain; version=0.0.4"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    app.run(host="0.0.0.0", port=port)
