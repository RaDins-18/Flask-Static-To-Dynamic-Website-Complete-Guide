# From flask library import the module Flask.
from flask import Flask

# Defining app
app = Flask(__name__)

# End point of website.
@app.route("/")

# A basic function for printing Hello, World!.
def hello_world():
    return "<p>Hello, World!</p>"

# We can create many routes.
@app.route("/radins")
def RaDins():
    return "<p>Hello, RaDin</p>"

# For running the server.
app.run(debug=True) # Throug debug=True argument we don't reload the server every time.