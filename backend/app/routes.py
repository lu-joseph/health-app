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


@app.route("/api/userdata", methods=["GET", "PUT"])
def getUserData():
    userid = request.form.get("userid")
    user = UserData.getUser(userid)
    if (user is None):
        print("couldn't find user")
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
            return UserData.updateUser(userid, firstname, lastname, username, password, sex, weight, height, age)
        except Exception as e:
            return str(e), 500
    else:
        return Exception('method not recognized')

##
# Activity
##


@app.route("/api/activity/getEntries", methods=["GET"])
def getActivityEntries():
    userid = request.form.get("userid")
    entries = Activity.query.filter(Activity.userid == userid).all()
    return json.dumps([e.serialize() for e in entries])


@app.route("/api/activity/addEntry", methods=["POST"])
def addActivityEntry():
    hours = request.form.get("hours")
    date = request.form.get("date")  # format must be yyyy-mm-dd
    userid = request.form.get("userid")
    try:
        (Activity.add_entry(userid, hours, date))
        return 'Entry was added', 200

    except Exception as e:
        return str(e), 500

##
# Sleep
##


@app.route("/api/sleep/getEntries", methods=["GET"])
def getSleepEntries():
    userid = request.form.get("userid")
    entries = Sleep.query.filter(Sleep.userid == userid).all()
    return json.dumps([e.serialize() for e in entries])


@app.route("/api/sleep/addEntry", methods=["POST"])
def addSleepEntry():
    hours = request.form.get("hours")
    date = request.form.get("date")  # format must be yyyy-mm-dd
    userid = request.form.get("userid")
    try:
        (Sleep.add_entry(userid, hours, date))
        return 'Entry was added', 200

    except Exception as e:
        return str(e), 500


@app.route("/api/sleep/feedback", methods=["GET"])
def getDailySleepFeedback():
    userid = request.form.get("userid")
    try:
        feedback = Sleep.dailySleepFeedback(userid)
        return feedback, 200

    except Exception as e:
        return str(e), 500

##
# Water
##


@app.route("/api/water/getEntries", methods=["GET"])
def getWaterEntries():
    userid = request.form.get("userid")
    entries = Water.query.filter(Water.userid == userid).all()
    return json.dumps([e.serialize() for e in entries])


@app.route("/api/water/addEntry", methods=["POST"])
def addWaterEntry():
    cups = request.form.get("cups")
    date = request.form.get("date")  # format must be yyyy-mm-dd
    userid = request.form.get("userid")
    try:
        (Water.add_entry(userid, cups, date))
        return 'Entry was added', 200

    except Exception as e:
        return str(e), 500


@app.route("/api/water/feedback", methods=["GET"])
def getDailyWaterFeedback():
    userid = request.form.get("userid")
    try:
        feedback = Water.dailyWaterFeedback(userid)
        return feedback, 200

    except Exception as e:
        return str(e), 500

##
# Mood
##


@app.route("/api/mood/getEntries", methods=["GET"])
def getMoodEntries():
    userid = request.form.get("userid")
    entries = Mood.query.filter(Mood.userid == userid).all()
    return json.dumps([e.serialize() for e in entries])


@app.route("/api/mood/addEntry", methods=["POST"])
def addMoodEntry():
    score = request.form.get("score")  # must be between 1 and 5
    date = request.form.get("date")  # format must be yyyy-mm-dd
    userid = request.form.get("userid")
    try:
        (Mood.add_entry(userid, score, date))
        return 'Entry was added', 200

    except Exception as e:
        return str(e), 500


if __name__ == '__main__':
    app.run()
