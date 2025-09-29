import os
import redis
from flask import Flask, render_template

app = Flask(__name__)

# Redis connection
redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = int(os.getenv("REDIS_PORT", "6379"))
r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route("/")
def index():
    # Increment a counter in Redis
    visits = r.incr("page_visits")
    return render_template("index.html", visits=visits)

@app.route("/healthz")
def healthz():
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
