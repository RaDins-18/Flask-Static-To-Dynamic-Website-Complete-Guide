# A Simple And Basic Bootstrap Website.

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/inner-page.html")
def inner_page():
    return render_template("inner-page.html")

@app.route("/portfolio-details.html")
def portfolio_details():
    return render_template("portfolio-details.html")

app.run(debug=True)