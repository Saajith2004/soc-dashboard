from flask import Flask, jsonify, render_template
from datetime import datetime, timezone
import os

app = Flask(__name__)

ALERTS = [
    {"id":"ALT-1042","severity":"Critical","type":"Brute Force","source":"185.220.101.42","destination":"10.0.0.15","status":"Investigating","time":"2 min ago"},
    {"id":"ALT-1041","severity":"High","type":"Suspicious PowerShell","source":"10.0.0.24","destination":"10.0.0.8","status":"Open","time":"8 min ago"},
    {"id":"ALT-1040","severity":"Medium","type":"Port Scan","source":"172.16.4.91","destination":"10.0.0.0/24","status":"Triaged","time":"21 min ago"},
    {"id":"ALT-1039","severity":"High","type":"Malware Detected","source":"10.0.0.31","destination":"cdn-example.net","status":"Contained","time":"34 min ago"},
    {"id":"ALT-1038","severity":"Low","type":"Failed Login","source":"10.0.0.55","destination":"10.0.0.5","status":"Closed","time":"1 hr ago"},
]

@app.route("/")
def index():
    counts = {"Critical":0, "High":0, "Medium":0, "Low":0}
    for alert in ALERTS:
        counts[alert["severity"]] += 1
    return render_template("index.html", alerts=ALERTS, counts=counts)

@app.route("/health")
def health():
    return jsonify(status="ok", service="soc-dashboard",
                   timestamp=datetime.now(timezone.utc).isoformat())

@app.route("/api/alerts")
def alerts():
    return jsonify(ALERTS)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
