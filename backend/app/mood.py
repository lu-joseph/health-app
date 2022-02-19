from app import db
from datetime import datetime
from calendar import monthrange


class Mood(db.Model):
    __tablename__ = 'mood'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    score = db.Column(db.Integer)
    userid = db.Column(db.Integer)

    # date must be in dd-mm-yyyy format
    def add_entry(userid, score, date=datetime.today().strftime('%Y-%m-%d')):
        if (score is None or userid is None):
            raise Exception('field cannot be null')
        elif (int(score) < 1 or int(score) > 5):
            raise Exception('field must be between 1 and 5')

        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect data format, should be yyyy-mm-dd")

        entry = Mood(userid=userid, date=date, score=score)
        db.session.add(entry)
        db.session.commit()
        return 'success'

    # requires: 1 <= month <= 12
    def getCalendar(userid, month, year):
        numDays = monthrange(int(year), int(month))[1]
        print(numDays)
        moodScores = {}
        for day in range(1, numDays + 1):
            calculatedDate = "%s-%s-%s" % (year,
                                           str(month).zfill(2), str(day).zfill(2))
            print("calculated date: " + calculatedDate)
            entry = Mood.query.filter(Mood.userid == userid,
                                      Mood.date == calculatedDate).first()
            score = -1
            if entry is not None:
                score = entry.score
            moodScores[str(day).zfill(2)] = score
        return moodScores

    def serialize(self):
        return {
            'id': self.id,
            'date': self.date.strftime('%Y-%m-%d'),
            'score': self.score,
            'userid': self.userid
        }
