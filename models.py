from db import db
from datetime import datetime



class AlarmClockModel(db.Model):
    __tablename__ = "alarm_clock"

    id = db.Column(db.Integer, primary_key=True)
    ring_time = db.Column(db.DateTime, nullable=False)
    worked = db.Column(db.Boolean, default=False)
    description = db.Column(db.Text)

    def __repr__(self):
        return "<Alarm Clock id: {}, ringing time: {}>".format(self.id, self.ring_time)


    def __init__(self, ring_time, description):
        self.ring_time = ring_time
        self.description = description
        self.worked = False


    def json(self):
        return {"ring_time": str(self.ring_time), "description" : self.description}


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
