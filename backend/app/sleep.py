from app import db
from app.userData import UserData
from datetime import datetime


class Sleep(db.Model):
    __tablename__ = 'sleep'

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

        entry = Sleep(userid=userid, date=date, hours=hours)
        db.session.add(entry)
        db.session.commit()
        return 'success'

    def dailySleepFeedback(id):
        user = UserData.getUser(id)
        if (user is None):
            print("user not found")
        recommendedSleep = 0
        age = user["age"]
        if 0 < age <= 2:
            recommendedSleep = 11
        elif 2 < age <= 5:
            recommendedSleep = 10
        elif 5 < age <= 12:
            recommendedSleep = 9
        elif 12 < age <= 18:
            recommendedSleep = 8
        else:
            recommendedSleep = 7
        entryToday = Sleep.query.filter(Sleep.userid == id,
                                        Sleep.date == datetime.today().strftime('%Y-%m-%d')).first()
        if (entryToday is None):
            message = "You have not inputted sleep hours today."
            result = -recommendedSleep
        else:
            sleepToday = entryToday.hours
            print("intake today: " + str(sleepToday))
            result = sleepToday - recommendedSleep
            if result < 0:
                message = "Today you slept " + str(abs(result)) + \
                    " less hours than the recommended amount. Try to do better tomorrow!"
            elif result == 0:
                message = "Good job! You slept the exact recommended number of hours today!"
            else:
                message = "Good job! You slept " + \
                    str(result) + " more hours than the recommended amount."
        return {
            'result': result,
            'message': message,
            'recommendation': "According to The Center for Disease Control and Prevention, your age group should try to sleep " +
            str(recommendedSleep) + " hours a night."
        }

    def serialize(self):
        return {
            'id': self.id,
            'date': self.date.strftime('%Y-%m-%d'),
            'hours': self.hours,
            'userid': self.userid
        }
