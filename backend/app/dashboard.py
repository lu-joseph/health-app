from datetime import datetime
from app.activity import Activity
from app.sleep import Sleep
from app.mood import Mood
from app.water import Water


class Dashboard():
    def calcScore(userid):
        score = 0
        total = 100
        activityWeight = 15
        waterWeight = 10
        sleepWeight = 35
        moodWeight = 15
        stressWeight = 25
        activityData = Activity.dailyActivityFeedback(userid)
        if activityData["noEntry"]:
            total -= activityWeight
            print("total now", total)
        else:
            activityHours = activityData["hours"]
            activityRecommendation = activityData["recommended_hours"]
            print("activityRecommendation:", activityRecommendation)
            activityScore = activityHours / activityRecommendation
            print("activity score is " +
                  str(int(round(100 * activityScore))) + "%")
            score += int(round(activityScore * activityWeight))

        waterData = Water.dailyWaterFeedback(userid)
        if waterData["noEntry"]:
            total -= waterWeight
            print("total now", total)
        else:
            waterIntake = waterData["cups"]
            waterRecommendation = waterData["recommended_intake"]
            print("waterRecommendation:", waterRecommendation)
            waterScore = waterIntake / waterRecommendation
            print("water score is " +
                  str(int(round(100 * waterScore))) + "%")
            score += int(round(waterScore * waterWeight))

        sleepData = Sleep.dailySleepFeedback(
            userid, datetime.today().strftime('%Y-%m-%d'))
        if sleepData["noEntry"]:
            total -= sleepWeight
            print("total now", total)
        else:
            sleepHours = sleepData["hours"]
            sleepRecommendation = sleepData["recommended_hours"]
            print("sleepRecommendation:", sleepRecommendation)
            sleepScore = sleepHours / sleepRecommendation
            print("sleep score is " +
                  str(int(round(100 * sleepScore))) + "%")
            score += int(round(sleepScore * sleepWeight))

        moodData = Mood.dailyMoodFeedback(userid)
        if moodData["noEntry"]:
            total -= moodWeight
            print("total now", total)
            total -= stressWeight
            print("total now", total)
        else:
            moodResult = moodData["mood"]  # 1 to 5
            moodScore = moodResult / 5
            print("mood score is " +
                  str(int(round(100 * moodScore))) + "%")
            score += int(round(moodScore * moodWeight))

            stressLevel = moodData["stress"]  # 1 to 10, higher stress bad
            stressScore = stressLevel / 10
            print("stress score is " +
                  str(int(round(100 * stressScore))) + "%")
            score += int(round(stressScore * stressWeight))

        if total == 0:
            print("calculated score: 0")
        else:
            print("calculated score:", int(round(100 * score / total)))
