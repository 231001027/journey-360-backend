#!/bin/bash
# Use PORT environment variable or default to 8000
PORT=${PORT:-8000}
echo "Starting server on port $PORT"
python -m uvicorn app.main:app --host 0.0.0.0 --port $PORT
