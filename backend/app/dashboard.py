from app.activity import Activity
from app.sleep import Sleep
from app.mood import Mood


class Dashboard():
    def calcScore(userid):
        score = 0
        total = 100
        activityWeight = 25
        sleepWeight = 35
        moodWeight = 15
        stressWeight = 25
        activityData = Activity.dailyActivityFeedback(userid)
        if activityData["noEntry"]:
            total -= activityWeight
        else:
            activityResults = activityData["result"]
            activityScore = min(max((25 / 3) * activityResults + 25,
                                    0),
                                activityWeight)
            print("activity score is " +
                  str(int(round(100 * activityScore / activityWeight))) + "%")
            score += activityScore

        sleepData = Sleep.dailySleepFeedback(userid)
        if sleepData["noEntry"]:
            total -= sleepWeight
        else:
            sleepResults = sleepData["result"]
            sleepScore = min(max(3.5 * sleepResults + 35,
                                 0),
                             sleepWeight)
            print("sleep score is " +
                  str(int(round(100 * sleepScore / sleepWeight))) + "%")
            score += sleepScore

        moodData = Mood.dailyMoodFeedback(userid)
        if moodData["noEntry"]:
            total -= moodWeight
            total -= stressWeight
        else:
            moodResults = moodData["result"]  # 1 to 5
            moodScore = min(max(3.75 * moodResults - 3.75,
                                0),
                            moodWeight)
            print("mood score is " +
                  str(int(round(100 * moodScore / moodWeight))) + "%")
            score += moodScore

            stressLevel = moodData["stress"]  # 1 to 10, higher stress bad
            stressScore = min(max((-25 / 9) * stressLevel + (250 / 9),
                                  0),
                              stressWeight)
            print("stress score is " +
                  str(int(round(100 * stressScore / stressWeight))) + "%")
            score += stressScore
        print("calculated score:", int(round(100 * score / total)))
