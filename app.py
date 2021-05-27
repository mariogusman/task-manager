import os
from flask import Flask  # imports flask

if os.path.exists("env.py"):  # imports creds
    import env


app = Flask(__name__)  # create instance of flask


@app.route("/")  # check if flask is working "/" = main page/folder
def hello():
    return "Hello World"


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")), debug=True)
