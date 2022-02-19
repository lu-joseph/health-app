from app import app, db
from app.activity import Activity
from app.sleep import Sleep
from app.water import Water
from app.mood import Mood
from app.userData import UserData
from flask import request
import json


@app.route("/")
def hello():
    return "hello world"

##
# User data
##


@app.route("/api/userdata/addEntry", methods=["POST"])
def addUser():
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    username = request.form.get("username")
    password = request.form.get("password")
    sex = request.form.get("sex")
    weight = request.form.get("weight")
    height = request.form.get("height")
    age = request.form.get("age")
    try:
        (UserData.addUser(firstname, lastname, username,
         password, sex, weight, height, age))
        return 'Entry was added', 200

    except Exception as e:
        return str(e), 500


@app.route("/api/userdata/<id>", methods=["GET", "PUT"])
def getUserData(id):
    user = UserData.getUser(id)
    if (user is None):
        return 'No user found', 204

    if (request.method == 'GET'):
        return user, 200
    elif (request.method == 'PUT'):
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        username = request.form.get("username")
        password = request.form.get("password")
        sex = request.form.get("sex")
        weight = request.form.get("weight")
        height = request.form.get("height")
        age = request.form.get("age")
        try:
            return UserData.updateUser(id, firstname, lastname, username, password, sex, weight, height, age)
        except Exception as e:
            return str(e), 500
    else:
        return Exception('method not recognized')

##
# Activity
##


@app.route("/api/activity/getEntries", methods=["GET"])
def getActivityEntries():
    entries = Activity.query.all()
    return json.dumps([e.serialize() for e in entries])


@app.route("/api/activity/addEntry", methods=["POST"])
def addActivityEntry():
    hours = request.form.get("hours")
    date = request.form.get("date")  # format must be yyyy-mm-dd
    try:
        (Activity.add_entry(hours, date))
        return 'Entry was added', 200

    except Exception as e:
        return str(e), 500

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


@app.route("/api/water/feedback/<id>", methods=["GET"])
def getDailyWaterFeedback(id):
    try:
        feedback = Water.dailyWaterFeedback(id)
        return feedback, 200

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
