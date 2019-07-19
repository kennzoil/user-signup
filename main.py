from flask import Flask, request, render_template
from functions import *

errors = {
    "username": "",
    "password": "",
    "pass_confirm": "",
    "email": ""
}

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

    if valid_username(username) == False:
        username_error = "Please enter a valid username, between 3 and 20 characters, with no spaces."
    elif valid_password(password) == False:
        password_error = "Don't forget your password!"
    elif passwords_match(password, passconfirm) == False:
        passconfirm_error = "Make sure your passwords match."
    elif valid_email(email) == False:
        email_error = "Remember to enter your email correctly. Or not at all!"

    return

@app.route("/welcome", methods=["POST"])
def welcome():
    return render_template("welcome.html")


app.run()