from model import *

db.drop_all()
db.create_all()
"""
user1 = User




class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lolid = db.Column(db.Integer, unique=True)
    lolname = db.Column(db.String(100), unique=True)
    twtid = db.Column(db.String(100)) #getting username for mention
    lastgame = db.Column(db.Integer)

    def __init__(self, lolid, lolname, twtid, lastgame):
        self.lolid = lolid
        self.lolname = lolname
        self.twtid = twtid
        self.lastgame = lastgame

"""
