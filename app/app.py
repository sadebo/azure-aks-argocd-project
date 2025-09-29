from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello from Flask running on AKS with ArgoCD 🚀"

@app.route("/healthz")
def healthz():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
