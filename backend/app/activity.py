from app import db
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

    def serialize(self):
        return {
            'id': self.id,
            'date': self.date.strftime('%Y-%m-%d'),
            'hours': self.hours,
            'userid': self.userid
        }
