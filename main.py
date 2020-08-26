from flask import Flask
from flask_socketio import SocketIO
from flask_restful import Resource, Api
from flask_migrate import Migrate
from flask_migrate import MigrateCommand
from flask_script import Manager

from config import Configuration
from resources.alarm_clock import AlarmClock
from resources.alarm_clock import AlarmClockList 

from db import db



app = Flask(__name__)
app.config.from_object(Configuration)
api = Api(app)
db.init_app(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
socketio = SocketIO(app)

api.add_resource(AlarmClock, "/alarm_clock")
api.add_resource(AlarmClockList, "/list_alarm_clock")




if __name__ == "__main__":
    socketio.run(app)