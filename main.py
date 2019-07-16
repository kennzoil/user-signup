from flask import Flask, request, render_template
from functions import *

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def tryagain():
    username = request.form["username"]
    password = request.form["password"]
    passconfirm = request.form["pass_confirm"]
    email = request.form["email"]

    return

@app.route("/welcome", methods=["POST"])
def welcome():
    return render_template("welcome.html")


app.run()