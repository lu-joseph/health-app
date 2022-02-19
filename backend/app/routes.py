from app import app, db
from app.sleep import Sleep
from app.water import Water
from app.mood import Mood
from flask import request
import json


@app.route("/")
def hello():
    return "hello world"

##
# Sleep
##


@app.route("/api/sleep/getEntries", methods=["GET"])
def getSleepEntries():
    entries = Sleep.query.all()
    return json.dumps([e.serialize() for e in entries])


@app.route("/api/sleep/addEntry", methods=["POST"])
def addSleepEntry():
    hours = request.form.get("hours")
    date = request.form.get("date")  # format must be yyyy-mm-dd
    try:
        (Sleep.add_entry(hours, date))
        return 'Entry was added', 200

    except Exception as e:
        return str(e), 500

##
# Water
##


@app.route("/api/water/getEntries", methods=["GET"])
def getWaterEntries():
    entries = Water.query.all()
    return json.dumps([e.serialize() for e in entries])


@app.route("/api/water/addEntry", methods=["POST"])
def addWaterEntry():
    cups = request.form.get("cups")
    date = request.form.get("date")  # format must be yyyy-mm-dd
    try:
        (Water.add_entry(cups, date))
        return 'Entry was added', 200

    except Exception as e:
        return str(e), 500

##
# Mood
##


@app.route("/api/mood/getEntries", methods=["GET"])
def getMoodEntries():
    entries = Mood.query.all()
    return json.dumps([e.serialize() for e in entries])


@app.route("/api/mood/addEntry", methods=["POST"])
def addMoodEntry():
    score = request.form.get("score")  # must be between 1 and 5
    date = request.form.get("date")  # format must be yyyy-mm-dd
    try:
        (Mood.add_entry(score, date))
        return 'Entry was added', 200

    except Exception as e:
        return str(e), 500


if __name__ == '__main__':
    app.run()
