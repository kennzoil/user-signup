from flask import Flask, request
from templates.index import *

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=["POST"])
def encrypt():
    rot = request.form["rot"]
    text = request.form["text"]
    encrypted = rotate_string(text, int(rot))
    return form.format(encrypted)

app.run()