FROM python:3.10-slim-bullseye

# Set working directory
WORKDIR /app

# Install minimal system dependencies
RUN apt-get update || true \
    && apt-get install -y --no-install-recommends \
       ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Copy Python dependencies first (for caching layers)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code, templates, and static files
COPY app.py .
COPY templates/ ./templates/
COPY static/ ./static/

# Expose Flask app port
EXPOSE 5000

# Run Flask using Gunicorn (multi-worker production server)
CMD ["gunicorn", "-w", "3", "-b", "0.0.0.0:5000", "app:app"]
