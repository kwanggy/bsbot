from model import db, User

import app_config as config

class UserModel(object):
    def __init__(self):
        pass

    def getUserById(self, id):
        return User.query.filter_by(id=id).first()

    def getUserByLolid(self, lolid):
        return User.query.filter_by(lolid=lolid).first()
    
    def getUserByLolname(self, lolname):
        return User.query.filter_by(lolname=lolname).first()

    def getUserByTwtid(self, twtid):
        return User.query.filter_by(twtid=twtid).first()

    def retLastgame(self, lolid):
        userExist = self.getUserByLolid(lolid)
        if userExist == None:
            return None
        return userExist.lastgame

    def addNewUser(self, lolid, lolname, twtid, lastgame):
        userExist = self.getUserByLolname(lolname)
        if userExist != None:
            return False
        newuser = User(lolid, lolname, twtid, lastgame)
        db.session.add(newuser)
        db.session.commit()
        return True
