from flask import Flask, request
from templates.index import *

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def index():
    return form.format("")

# @app.route("/", methods=["POST"])
#     def signup():
#         #do code here
#         return pass

app.run()