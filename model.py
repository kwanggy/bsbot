from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

import app_config as config

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = config.MOCK_DB_URI

app.config.update(
    DEBUG = True,
    )

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lolid = db.Column(db.Integer, unique=True)
    lolname = db.Column(db.String(100), unique=True)
    twtid = db.Column(db.String(100)) #getting username for mention
    lastgame = db.Column(db.Integer)
    offense = db.Column(db.Integer)

    def __init__(self, lolid, lolname, twtid, lastgame):
        self.lolid = lolid
        self.lolname = lolname
        self.twtid = twtid
        self.lastgame = lastgame
        self.offense = 0
