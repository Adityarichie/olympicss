from flask import Flask, render_template, redirect, url_for, request
import requests


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=2119)
