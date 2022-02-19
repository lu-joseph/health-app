from app import db
from app.userData import UserData
from datetime import datetime


class Water(db.Model):
    __tablename__ = 'water'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    cups = db.Column(db.Integer)

    # date must be in dd-mm-yyyy format
    def add_entry(cups, date=datetime.today().strftime('%Y-%m-%d')):
        if (cups is None):
            raise Exception('field cannot be null')
        elif (int(cups) < 0):
            raise Exception('field cannot be negative')

        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect data format, should be yyyy-mm-dd")

        entry = Water(date=date, cups=cups)
        db.session.add(entry)
        db.session.commit()
        return 'success'

    def dailyWaterFeedback(id):
        user = UserData.getUser(id)
        recommendedIntake = 15.5 if user["sex"] == 'M' else 11.5
        entryToday = Water.query.filter(
            Water.date == datetime.today().strftime('%Y-%m-%d')).first()
        if (entryToday is None):
            message = "You have not inputted water intake today."
            result = -recommendedIntake
        else:
            intakeToday = entryToday.cups
            print("intake today: " + str(intakeToday))
            result = intakeToday - recommendedIntake
            if result < 0:
                message = "Today you drank " + str(abs(result)) + \
                    " less cups of water than the recommended amount. Try to do better tomorrow!"
            elif result == 0:
                message = "Good job! You drank the exact recommended amount of water today!"
            else:
                message = "Good job! You drank " + \
                    str(result) + " more cups of water tahn the recommended amount."
        return {
            'result': result,
            'message': message,
            'recommendation': "According to The U.S. National Academies of Sciences, Engineering, and Medicine, you should try to drink " +
            str(recommendedIntake) + " cups of water each day."
        }

    def serialize(self):
        return {
            'id': self.id,
            'date': self.date.strftime('%Y-%m-%d'),
            'cups': self.cups
        }
