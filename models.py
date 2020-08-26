from main import db


class AlarmClockModel(db.Model):
    __tablename__ = "alarm_clock"

    id = db.Column(db.Integer, primary_key=True)
    ring_time = db.Column(db.DateTime, nullable=False)
    worked = db.Column(db.Boolean, default=False, nullable=False)
    description = db.Column(db.Text)

    def __repr__(self):
        return "<Alarm Clock id: {}, ringing time: {}>".format(self.id, self.ring_time)
