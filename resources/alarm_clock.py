from flask_restful import Resource, reqparse, inputs
from flask import request
from models import AlarmClockModel
from datetime import datetime
import json



class AlarmClock(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument("ring_time",
                        type=lambda x: datetime.strptime(x,'%Y-%m-%d %H:%M:%S'),
                        required=True,
                        help="bad date_srt")
    
    parser.add_argument("worked",
                        required=False,
                        type=bool)

    parser.add_argument("description",
                        type=str)
 
    def post(self):
        data = AlarmClock.parser.parse_args()
        alarm_clock = AlarmClockModel(data["ring_time"], data["description"])

        try:
            alarm_clock.save_to_db()
        except Exception as e:
            return {"message": "error info {}".format(e)}, 500 #internal server error

        return alarm_clock.json(), 201



class AlarmClockList(Resource):
    
    def get(self):
        return {"alarm_clock": [alarm_clock.json() for alarm_clock in AlarmClockModel.query.filter_by(worked=False) ]}
