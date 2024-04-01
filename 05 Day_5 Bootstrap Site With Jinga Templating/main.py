from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/about.html")
def about_page():
    return render_template("about.html")

navigation = [{"href":"article.html", "caption":"First list item"},
              {"href":"article.html", "caption":"Second list item"},
              {"href":"article.html", "caption":"Third list item"},
              {"href":"article.html", "caption":"Fourth list item"},
              {"href":"article.html", "caption":"Fifth list item"}
            ]

@app.route("/article.html")
def article_page():
    return render_template("article.html", navigation=navigation)

@app.route("/contact.html")
def contact_page():
    return render_template("contact.html")

@app.route("/privacy-policy.html")
def privacy_policy_page():
    return render_template("privacy-policy.html")

@app.route("/terms-conditions.html")
def terms_conditions_page():
    return render_template("terms-conditions.html")

@app.route("/travel.html")
def travel_page():
    return render_template("travel.html")

@app.route("/404.html")
def page_404():
    return render_template("404.html")

app.run(debug=True, host="127.0.0.1")


# Jinja is used to add python code into html.

# Bootstrap website with jinja template.
# In jinja templating.

# Instead of linking files from static folder like this:
# <!-- <link rel="stylesheet" href="static/plugins/bootstrap/bootstrap.min.css"> -->

# We link files like this:
# <link rel="stylesheet" href="{{ url_for('static', filename='plugins/bootstrap/bootstrap.min.css') }}">
# It is more effective.

# We can use a list of dictionary items in html like this:
#        <!DOCTYPE html>
#        <html lang="en">
#        <head>
#            <title>My Webpage</title>
#        </head>
#        <body>
#            <ul id="navigation">
#            {% for item in navigation %}
#                <li><a href="{{ item.href }}">{{ item.caption }}</a></li>
#            {% endfor %}
#            </ul>

#            <h1>My Webpage</h1>
#            {{ a_variable }}

#            {# a comment #}
#        </body>
#        </html>


# You can also check this link for jinja templating: https://flask.palletsprojects.com/en/2.3.x/templating/

# You can also check this link for template designer documentation: https://jinja.palletsprojects.com/en/3.1.x/templates/

# You can also check this link for jinja documentation: https://jinja.palletsprojects.com/en/3.1.x/