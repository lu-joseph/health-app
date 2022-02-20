from app import db
# from app.userData import UserData
from datetime import datetime


class Journal(db.Model):
    __tablename__ = 'journal'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    positive = db.Column(db.String)
    grateful = db.Column(db.String)
    notes = db.Column(db.String)
    userid = db.Column(db.Integer)

    # date must be in dd-mm-yyyy format
    def add_entry(userid, positive, grateful, notes, date=datetime.today().strftime('%Y-%m-%d')):
        if (date is None or userid is None or positive is None or grateful is None or notes is None):
            raise Exception('field cannot be null')

        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect data format, should be yyyy-mm-dd")

        entry = Journal(userid=userid, date=date,
                        positive=positive, grateful=grateful, notes=notes)
        db.session.add(entry)
        db.session.commit()
        return 'success'

    def serialize(self):
        return {
            'id': self.id,
            'date': self.date.strftime('%Y-%m-%d'),
            'positive': self.positive,
            'grateful': self.grateful,
            'notes': self.notes,
            'userid': self.userid
        }
