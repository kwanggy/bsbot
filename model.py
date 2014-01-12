from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

import app_config as config

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = config.MOCK_DB_URI

app.config.update(
    DEBUG = True,
    )

db = SQLAlchemy(app)


twtidPerLolid = db.Table('twitidPerLolid', 
        db.Column('twtid', db.String(25), db.ForeignKey('user.twtid')),
        db.Column('lolid', db.Integer, db.ForeignKey('lol.id'))
    )

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    twtid = db.Column(db.String(25), unique=True) #getting username for mention
    lang = db.Column(db.String(2))
    regcode = db.Column(db.String, unique=True)

    lols = db.relationship("Lol", secondary=twtidPerLolid, backref=db.backref('users', lazy='dynamic'))

    def __init__(self, twtid, regcode, lang):
        self.twtid = twtid
        self.lang = 'en'
        self.regcode = regcode
        self.lang = lang
        self.active = False

class Lol(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lolname = db.Column(db.String(25), unique=True)
    lastgame = db.Column(db.Integer)

    def __init__(self, lolid, lolname, lastgame):
        self.id = lolid
        self.lolname = lolname
        self.lastgame = lastgame

