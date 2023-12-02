import requests
from flask import Flask, render_template, url_for, redirect
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return redirect(url_for("desktop"))

@app.route("/desktop", methods=["GET"])
def desktop():
    with open("teste.json") as f:
        data = f.read()
    spaces = json.loads(data)
    return render_template("desktop.html", spaces=spaces)

if __name__ == '__main__':
    app.run(debug=True)