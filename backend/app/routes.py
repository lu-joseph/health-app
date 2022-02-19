from app import app, db
from app.sleep import Sleep
from flask import Flask


@app.route("/")
def hello():
    return "hello world"


if __name__ == '__main__':
    app.run()
