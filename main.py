from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask_migrate import Migrate
from flask_migrate import MigrateCommand
from flask_script import Manager

from config import Configuration



app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
api = Api(app)



if __name__ == "__main__":
    app.run(debug=True)