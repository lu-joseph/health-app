from audioop import cross
from datetime import datetime
from app import app, db
from app.activity import Activity
from app.sleep import Sleep
from app.water import Water
from app.mood import Mood
from app.journal import Journal
from app.userData import UserData
from app.dashboard import Dashboard
from flask import request
from flask_cors import cross_origin
import json


@app.route("/")
def hello():
    return "hello world"

##
# User data
##


@cross_origin
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
        return 'User entry was added', 200

    except Exception as e:
        return str(e), 500


@cross_origin
@app.route("/api/userdata/<userid>", methods=["GET"])
def getUserData(userid):
    user = UserData.getUser(userid)
    if (user is None):
        print("couldn't find user")
        return 'No user found', 204
    return user, 200

##
# Activity
##


@cross_origin()
@app.route("/api/activity/getEntries/<userid>", methods=["GET"])
def getActivityEntries(userid):
    entries = Activity.query.filter(Activity.userid == userid).all()
    return json.dumps([e.serialize() for e in entries])


@cross_origin()
@app.route("/api/activity/getEntry/<userid>", methods=["GET"])
def getActivityEntry(userid):
    date = datetime.today().strftime('%Y-%m-%d')
    entry = Activity.query.filter(
        Activity.userid == userid, Activity.date == date).first()
    if entry is None:
        return None, 200
    return entry.serialize(), 200


@cross_origin()
@app.route("/api/activity/addEntry", methods=["POST"])
def addActivityEntry():
    hours = request.form.get("hours")
    date = request.form.get("date")  # format must be yyyy-mm-dd
    userid = request.form.get("userid")
    try:
        (Activity.add_entry(userid, hours, date))
        return 'Activity entry was added', 200

    except Exception as e:
        return str(e), 500


@cross_origin()
@app.route("/api/activity/feedback/<userid>", methods=["GET"])
def getDailyActivityFeedback(userid):
    try:
        feedback = Activity.dailyActivityFeedback(userid)
        return feedback, 200

    except Exception as e:
        return str(e), 500

##
# Sleep
##


@cross_origin()
@app.route("/api/sleep/getEntries/<userid>", methods=["GET"])
def getSleepEntries(userid):
    entries = Sleep.query.filter(Sleep.userid == userid).all()
    return json.dumps([e.serialize() for e in entries])


@cross_origin()
@app.route("/api/sleep/getEntry/<userid>", methods=["GET"])
def getSleepEntry(userid):
    date = datetime.today().strftime('%Y-%m-%d')
    entry = Sleep.query.filter(
        Sleep.userid == userid, Sleep.date == date).first()
    return entry.serialize()


@cross_origin()
@app.route("/api/sleep/getRecommended/<userid>", methods=["GET"])
def getRecommendedHours(userid):
    return Sleep.getRecommendedHours(userid), 200


@cross_origin()
@app.route("/api/sleep/addEntry", methods=["POST"])
def addSleepEntry():
    hours = request.form.get("hours")
    date = request.form.get("date")  # format must be yyyy-mm-dd
    quality = request.form.get("quality")  # must be POOR, SOSO, or GOOD
    feel = request.form.get("feel")  # must be AWAKE, TIRED, or SLEEPY
    userid = request.form.get("userid")
    try:
        (Sleep.add_entry(userid, hours, quality, feel, date))
        return 'Sleep entry was added', 200

    except Exception as e:
        print("hours:", hours, "date:", date, "quality",
              quality, "feel", feel, "userid", userid)
        return str(e), 500


@cross_origin
@app.route("/api/sleep/feedback/<userid>", methods=["GET"])
def getDailySleepFeedback(userid):
    try:
        feedback = Sleep.dailySleepFeedback(
            userid, datetime.today().strftime('%Y-%m-%d'))
        return feedback, 200

    except Exception as e:
        return str(e), 500


@cross_origin
@app.route("/api/sleep/weeklyView/<userid>", methods=["GET"])
def getWeeklyFeedback(userid):
    try:
        return Sleep.getWeeklyView(userid), 200
    except Exception as e:
        return str(e), 500

##
# Water
##


@cross_origin
@app.route("/api/water/getEntries", methods=["GET"])
def getWaterEntries():
    userid = request.form.get("userid")
    entries = Water.query.filter(Water.userid == userid).all()
    return json.dumps([e.serialize() for e in entries])


@cross_origin
@app.route("/api/water/getEntry", methods=["GET"])
def getWaterEntry():
    date = request.form.get("date")
    userid = request.form.get("userid")
    entry = Water.query.filter(
        Water.userid == userid, Water.date == date).first()
    return entry


@cross_origin
@app.route("/api/water/addEntry", methods=["POST"])
def addWaterEntry():
    cups = request.form.get("cups")
    date = request.form.get("date")  # format must be yyyy-mm-dd
    userid = request.form.get("userid")
    try:
        (Water.add_entry(userid, cups, date))
        return 'Water entry was added', 200

    except Exception as e:
        return str(e), 500


@cross_origin
@app.route("/api/water/feedback/<userid>", methods=["GET"])
def getDailyWaterFeedback(userid):
    try:
        feedback = Water.dailyWaterFeedback(userid)
        return feedback, 200

    except Exception as e:
        return str(e), 500

##
# Mood
##


@cross_origin
@app.route("/api/mood/getEntries", methods=["GET"])
def getMoodEntries():
    userid = request.form.get("userid")
    entries = Mood.query.filter(Mood.userid == userid).all()
    return json.dumps([e.serialize() for e in entries])


@cross_origin
@app.route("/api/mood/getEntry", methods=["GET"])
def getMoodEntry():
    date = request.form.get("date")
    userid = request.form.get("userid")
    entry = Mood.query.filter(
        Mood.userid == userid, Mood.date == date).first()
    return entry


@cross_origin
@app.route("/api/mood/addEntry", methods=["POST"])
def addMoodEntry():
    score = request.form.get("score")  # must be between 1 and 5
    date = request.form.get("date")  # format must be yyyy-mm-dd
    stress = request.form.get("stress")
    notes = request.form.get("notes")
    userid = request.form.get("userid")
    try:
        (Mood.add_entry(userid, score, stress, notes, date))
        return 'Mood entry was added', 200

    except Exception as e:
        return str(e), 500


# returns a json with the mood scores for each day in the month specified.
#   a day will have -1 if there is no mood entered.
@cross_origin
@app.route("/api/mood/getCalendar", methods=["GET"])
def getMoodCalendar():
    year = request.form.get("year")
    month = request.form.get("month")
    userid = request.form.get("userid")
    try:
        calendar = Mood.getCalendar(userid, month, year)
        return calendar, 200

    except Exception as e:
        return str(e), 500

##
# Journal
##


@cross_origin
@app.route("/api/journal/getEntry", methods=["GET"])
def getJournalEntry():
    userid = request.form.get("userid")
    date = request.form.get("date")
    entry = Journal.query.filter(
        Journal.userid == userid, Journal.date == date).all().first()
    return entry


@cross_origin
@app.route("/api/journal/addEntry", methods=["POST"])
def addJournalEntry():
    date = request.form.get("date")  # format must be yyyy-mm-dd
    positive = request.form.get("positive")
    grateful = request.form.get("grateful")
    notes = request.form.get("notes")
    userid = request.form.get("userid")
    try:
        (Journal.add_entry(userid, positive, grateful, notes, date))
        return 'Journal entry was added', 200

    except Exception as e:
        return str(e), 500

##
# Dashboard
##


@cross_origin
@app.route("/api/dashboard/getScore/<userid>", methods=["GET"])
def getScore(userid):
    try:
        return Dashboard.calcScore(userid), 200
    except Exception as e:
        return str(e), 500


@cross_origin
@app.route("/api/dashboard/monthScores/<userid>", methods=["GET"])
def getMonthScores(userid):
    try:
        return Dashboard.calcLastMonth(userid), 200
    except Exception as e:
        return str(e), 500


if __name__ == '__main__':
    app.run()
