# Use slim Python image
FROM python:3.10-slim-bullseye

# Set working dir
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Expose Flask port
EXPOSE 5000

# Run Flask with Gunicorn for production
CMD ["gunicorn", "-w", "3", "-b", "0.0.0.0:5000", "app:app"]
