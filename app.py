from flask import Flask, render_template

app = Flask(__name__)

# for web apps or APIs, URL - universal resource locator

@app.route("/")
def main_page():
    return "Hello from Flask!"

@app.route("/bye")
def bye_page():
    return "Goodbye from Flask!"

@app.route("/greeting")
def greeting_page():
    return "Greetings from Flask!"

@app.route("/static")
def static_page():
    return """
    <html>
    <head>
        <title>Simple static page!</title>
    </head>
    <body>
        <h1>Static page.</h1>
        <p>This is a static page!</p>
    </body>

    </html>
    """
# <> dynamic placeholder
@app.route("/name/<name>/")
def dynamic_url(name):
    return """
    <html>
    <head>
        <title>Simple - Flask routes</title>
    </head>
    <body>
        <h1>Name page</h1>
        <p>Hello {}!</p>
    </body>

    </html>
    """.format(name)

# <> dynamic placeholder "(Method: POST)"
@app.route("/age/<int:age>/")
def type_url(age):
    return """
    <html>
    <head>
        <title>Simple - Flask routes</title>
    </head>
    <body>
        <h1>Age page</h1>
        <p>You are {} years old!</p>
    </body>

    </html>
    """.format(age)

@app.route("/hello/<name>")
def template_base(name):
    return render_template('base.html', name=name, group="Everyone")

# demonstratio of additional syntax
@app.route("/loop/<name>")
def loop_demo(name):
    return render_template('favourites.html', my_list=['Yoga', 'Tennis', 'F1'], 
    name=name, group="Team")

@app.route("/popup/<name>")
def popup_demo(name):
    return render_template('popup.html', popup_list=['Warning', 'Alerts', 'Error', 'Virus Alert', 'Free Money', 'Only need 3 digits of your card', 'Car accident', 'Have you been missold PPI???', 'Free Iphone 13 Pro!'], name=name, group="Team")