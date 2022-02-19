from app import app, db
from app.sleep import Sleep
from flask import request
import json


@app.route("/")
def hello():
    return "hello world"


@app.route("/api/sleep/addEntry", methods=["POST"])
def addEntry():
    hours = request.form.get("hours")
    date = request.form.get("date")
    try:
        (Sleep.add_entry(hours, date))
        return 'Entry was added', 200

    except Exception as e:
        return str(e), 500


@app.route("/api/sleep/getEntries", methods=["GET"])
def getSleepEntries():
    entries = Sleep.query.all()
    return json.dumps([e.serialize() for e in entries])


if __name__ == '__main__':
    app.run()
