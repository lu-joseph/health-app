from app import db
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

    def serialize(self):
        return {
            'id': self.id,
            'date': self.date.strftime('%Y-%m-%d'),
            'cups': self.cups
        }
