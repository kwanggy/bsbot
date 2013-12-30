from model import db, User
import time

import app_config as config

class UserModel(object):
    def __init__(self):
        pass

    def getUsers(self):
        return User.query.filter_by().all()

    def getActiveUsers(self):
        return User.query.filter_by(active=True).all()

    def getUserById(self, id):
        return User.query.filter_by(id=id).first()

    def getUserByLolid(self, lolid):
        return User.query.filter_by(lolid=lolid).first()
    
    def getUserByLolname(self, lolname):
        return User.query.filter_by(lolname=lolname).first()

    def getUserByTwtid(self, twtid):
        return User.query.filter_by(twtid=twtid).first()

    def getUserByRegCode(self, regCode):
        return User.query.filter_by(regCode=regCode).first()



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

    def addNewUser(self, lolname, twtid, regCode):
        userExist = self.getUserByLolname(lolname)
        if userExist != None:
            return False
        newuser = User(lolname, twtid, regCode)
        db.session.add(newuser)
        db.session.commit()
        return True

    def activateUser(self, lolname,  lolid, lastgame):
        update_data = { 'lolid': lolid, 
                        'lastgame': lastgame,
                        'offense': 0,
                        'active': True,
                        'regCode': '-1YOUWILLNEVERGUESSTHISUKNOW',
                        'active_since': int(time.time()*1000)
                      }
        User.query.filter_by(lolname=lolname).update(update_data)
        db.session.commit()

    def pre_activateUser(self, regCode):
        user = self.getUserByRegCode(regCode)
        if user == None:
            return None

        return user.lolname

if __name__ == '__main__':
    userModel = UserModel()
    print userModel.getActiveUsers()
