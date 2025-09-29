# Use Python 3.10 (compatible with numpy==1.26.4)
FROM python:3.10-slim-bullseye

WORKDIR /app

# Minimal package install
RUN apt-get update || true \
    && apt-get install -y --no-install-recommends \
       ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

EXPOSE 5000

# Run Flask with Gunicorn
CMD ["gunicorn", "-w", "3", "-b", "0.0.0.0:5000", "app:app"]
