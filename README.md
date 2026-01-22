# CICD Demo

Simple FastAPI application with server-side rendering for CI/CD demonstration.

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
python3 app/server.py
```

Visit http://localhost:8000

## Docker

```bash
docker build -t cicd-demo .
docker run -p 8000:8000 cicd-demo
```