# SOC Dashboard

A lightweight Security Operations Center dashboard built with Flask.

## Features
- Alert overview by severity
- Recent security events
- Source/destination IP visibility
- REST API at `/api/alerts`
- Health check at `/health`
- Railway/Gunicorn-ready deployment

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:8080`.

> The included data is synthetic demonstration data. Do not use it as real incident telemetry.
