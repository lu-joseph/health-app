from app import db
from app.userData import UserData
from datetime import datetime


class Water(db.Model):
    __tablename__ = 'water'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    cups = db.Column(db.Integer)
    userid = db.Column(db.Integer)

    # date must be in dd-mm-yyyy format

    def add_entry(userid, cups, date=datetime.today().strftime('%Y-%m-%d')):
        if (cups is None or userid is None):
            raise Exception('field cannot be null')
        elif (int(cups) < 0):
            raise Exception('field cannot be negative')

        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect data format, should be yyyy-mm-dd")

        entry = Water(userid=userid, date=date, cups=cups)
        db.session.add(entry)
        db.session.commit()
        return 'success'

    def dailyWaterFeedback(id):
        user = UserData.getUser(id)
        recommendedIntake = 0
        if user is None:
            raise Exception("user not found")
        else:
            recommendedIntake = 15.5 if user["sex"] == 'M' else 11.5
        # result = 0
        intakeToday = 0

        entryToday = Water.query.filter(Water.userid == id,
                                        Water.date == datetime.today().strftime('%Y-%m-%d')).first()

        entryFound = entryToday is not None
        # if (entryToday is None):
        #     message = "You have not inputted water intake today."
        # else:
        if entryFound:
            intakeToday = entryToday.cups
            # result = intakeToday - recommendedIntake
            # if result < 0:
            #     message = "Today you drank " + str(abs(result)) + \
            #         " less cups of water than the recommended amount. Try to do better tomorrow!"
            # elif result == 0:
            #     message = "Good job! You drank the exact recommended amount of water today!"
            # else:
            #     message = "Good job! You drank " + \
            #         str(result) + " more cups of water than the recommended amount."

        return {
            # 'result': result,
            'entryFound': entryFound,
            # 'message': message,
            'recommended_intake': recommendedIntake,
            'cups': intakeToday,
            # 'recommendation': "According to The U.S. National Academies of Sciences, Engineering, and Medicine, you should try to drink " +
            # str(recommendedIntake) + " cups of water each day."
        }

    def serialize(self):
        return {
            'id': self.id,
            'date': self.date.strftime('%Y-%m-%d'),
            'cups': self.cups,
            'userid': self.userid
        }
