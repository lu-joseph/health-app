from app import db
#from sqlalchemy import delete
from datetime import datetime


class Sleep(db.Model):
    __tablename__ = 'sleep'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    hours = db.Column(db.REAL)

    # date must be in dd-mm-yyyy format
    def add_entry(hours, date="today"):
        if (hours is None):
            raise Exception('field cannot be null')
        elif (float(hours) < 0):
            raise Exception('field cannot be negative')
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect data format, should be yyyy-mm-dd")
        if (date == "today"):
            date = datetime.today().strftime('%Y-%m-%d')
        entry = Sleep(date=date, hours=hours)
        db.session.add(entry)
        db.session.commit()
        return 'success'

    def serialize(self):
        return {
            'id': self.id,
            'date': self.date.strftime('%Y-%m-%d'),
            'hours': self.hours
        }
