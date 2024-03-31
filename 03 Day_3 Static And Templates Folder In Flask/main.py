from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Through render_template module we can serve html pages on the server from templates folder.
    return render_template("home.html")

@app.route("/about")
def about():
    # We can also serve variables with the html pages through render_template module.
    # Like: myName variable
    myName = "RaDin Alvi"
    return render_template("about.html", name=myName)

app.run(debug=True)