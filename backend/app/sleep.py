from app import db
from sqlalchemy import delete


class Sleep(db.Model):
    __tablename__ = 'sleep'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    hours = db.Column(db.REAL)
