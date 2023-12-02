import requests
from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return redirect(url_for("desktop"))

@app.route("/desktop", methods=["GET"])
def desktop():
    return render_template("desktop.html")

@app.route("/desktop/liminal", methods=["GET"])
def liminal():
    spaces = requests.get("http://localhost:8080/spaces").json()
    return render_template("liminal.html", spaces=spaces)

if __name__ == '__main__':
    app.run(debug=True)