import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from flask_migrate import Migrate
from flask_socketio import SocketIO




app = Flask(__name__)
app.secret_key=os.environ.get('SECRET')
socketio = SocketIO(app, manage_session=False)


# Often people will also separate these into a separate config.py file

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)