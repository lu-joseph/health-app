from app import db
from app.userData import UserData
from datetime import datetime


class Activity(db.Model):
    __tablename__ = 'activity'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    hours = db.Column(db.REAL)
    userid = db.Column(db.Integer)

    # date must be in dd-mm-yyyy format
    def add_entry(userid, hours, date=datetime.today().strftime('%Y-%m-%d')):
        if (hours is None or userid is None):
            raise Exception('field cannot be null')
        elif (float(hours) < 0):
            raise Exception('field cannot be negative')

        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect data format, should be yyyy-mm-dd")

        entry = Activity(userid=userid, date=date, hours=hours)
        db.session.add(entry)
        db.session.commit()
        return 'success'

    def dailyActivityFeedback(id):
        user = UserData.getUser(id)
        if (user is None):
            return Exception("user not found")
        age = user["age"]
        if 0 < age <= 4:
            recommendedActivity = 3
        elif 4 < age <= 17:
            recommendedActivity = 1
        else:
            recommendedActivity = 2.5
        entryToday = Activity.query.filter(Activity.userid == id,
                                           Activity.date == datetime.today().strftime('%Y-%m-%d')).first()
        entryFound = entryToday is not None
        activityToday = 0
        # if (noEntry):
        #     message = "You have not inputted active hours today."
        # else:
        if entryFound:
            print("b1")
            activityToday = entryToday.hours

            # result = activityToday - recommendedActivity
            # if result < 0:
            #     message = "Today you were active for " + str(abs(result)) + \
            #         " less hours than the recommended amount. Try to do better tomorrow!"
            # elif result == 0:
            #     message = "Good job! You reached the exact recommended number of active hours today!"
            # else:
            #     message = "Good job! You were active for " + \
            #         str(result) + " more hours than the recommended amount."
        return {
            # 'result': result,
            'entryFound': entryFound,
            # 'message': message,
            'hours': activityToday,
            'recommended_hours': recommendedActivity,
            # 'recommendation': "According to The WHO, your age group should try to reach " +
            # str(recommendedActivity) + " active hours a day."
        }

    def getRecommendedHours(id):
        user = UserData.getUser(id)
        if (user is None):
            return Exception("user not found")
        age = user["age"]
        if 0 < age <= 4:
            recommendedActivity = 3
        elif 4 < age <= 17:
            recommendedActivity = 1
        else:
            recommendedActivity = 2.5
        return recommendedActivity

    def serialize(self):
        return {
            'id': self.id,
            'date': self.date.strftime('%Y-%m-%d'),
            'hours': self.hours,
            'userid': self.userid
        }
