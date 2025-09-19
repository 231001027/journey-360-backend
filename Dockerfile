FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create a startup script
RUN echo '#!/bin/bash\npython -m uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}' > start.sh && chmod +x start.sh

# Expose port
EXPOSE 8000

# Use the startup script
CMD ["./start.sh"]
