from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "This page is only for making a CI/CD pipeline and deploy it on docker hub"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)