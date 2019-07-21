from flask import Flask, request, render_template
import os
import cgi
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
def submit():
    username = request.form["username"]
    password = request.form["password"]
    passconfirm = request.form["pass_confirm"]
    email = request.form["email"]

    if valid_username(username) == False:
        errors["username"] = "Please enter a valid username, between 3 and 20 characters, with no spaces."
    if valid_password(password) == False:
        errors["password"] = "Don't forget your password!"
    if passwords_match(password, passconfirm) == False:
        errors["pass_confirm"] = "Make sure your passwords match."
    if valid_email(email) == False:
        errors["email"] = "Remember to enter your email correctly. Or not at all!"
    
    return render_template("index.html", username_error = errors["username"], password_error = errors["password"], passconfirm_error = errors["pass_confirm"], email_error = errors["email"])

@app.route("/welcome", methods=["POST"])
def welcome():
    return render_template("welcome.html")


app.run()