from model import db, User

import app_config as config

class UserModel(object):
    def __init__(self):
        pass

    def getUsers(self):
        return User.query.filter_by().all()

    def getUserById(self, id):
        return User.query.filter_by(id=id).first()

    def getUserByLolid(self, lolid):
        return User.query.filter_by(lolid=lolid).first()
    
    def getUserByLolname(self, lolname):
        return User.query.filter_by(lolname=lolname).first()

    def getUserByTwtid(self, twtid):
        return User.query.filter_by(twtid=twtid).first()

    def getLastGame(self, lolid):
        userExist = self.getUserByLolid(lolid)
        if userExist == None:
            return None
        return userExist.lastgame

    def setLastGame(self, lolid, lastgame):
        User.query.filter_by(lolid=lolid).update({'lastgame': lastgame})
        db.session.commit()

    def updateOffense(self, lolid):
        user = self.getUserByLolid(lolid)
        User.query.filter_by(lolid=lolid).update({'offense': user.offense + 1})
        db.session.commit()

    def addNewUser(self, lolid, lolname, twtid, lastgame):
        userExist = self.getUserByLolname(lolname)
        if userExist != None:
            return False
        newuser = User(lolid, lolname, twtid, lastgame)
        db.session.add(newuser)
        db.session.commit()
        return True

if __name__ == '__main__':
    userModel = UserModel()
    print userModel.getUsers()
