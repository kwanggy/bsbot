from model import db, User

class UserModel(object):
    def __init__(self):
        pass

    def getUsers(self):
        return User.query.filter_by().all()

    def getActiveUsers(self):
        return User.query.filter_by(active=True).all()

    def getUserById(self, id):
        return User.query.filter_by(id=id).first()

    def getUserByTwtid(self, twtid):
        return User.query.filter_by(twtid=twtid).first()

    def getUserByRegcode(self, regcode):
        return User.query.filter_by(regcode=regcode).first()
    
    def getUserLolsByTwtid(self, twtid):
        user = self.getUserByTwtid(twtid)
        if user == None:
            print 'User not found: ' + twtid
            return None

        return user.lols

    def updateUserAtActivation(self, twtid, regcode, lang):
        user = self.getUserByTwtid(twtid)
        if user == None:
            return False
        user.regcode = regcode
        user.lang = lang
        db.session.commit()
        return True

    def addNewUser(self, twtid, regcode, lang):
        print 'addNewUser called'
        newuser = User(twtid, regcode, lang)
        db.session.add(newuser)
        db.session.commit()
        return User.query.filter_by(twtid=twtid).first()

    def addLolToTwtid(self, twtid, regcode, lol):
        user = self.getUserByTwtid(twtid)
        
        # user data yet to exist
        if user == None:
            # something has gone wrong..
            print 'user yet to exist'
            return False

        # regcode does not match
        if user.regcode != regcode:
            print 'reg code does not match!'
            return False


        # somehow addNewUSer could fail.. not likely though
        if user == None:
           return None

        # we will do this at activation now
        # append lol record for this twt user
        user.lols.append(lol)

        db.session.commit()

        return True
        
    def activateUserByRegcode(self, regcode):
        user = self.getUserByRegcode(regcode)

        # user could not be found..
        if not user:
            return False

        # activate user
        user.active = True

        # commit result 
        db.session.commit()

        return True
        
    
    """
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
    """

if __name__ == '__main__':
    userModel = UserModel()
    print userModel.addLol("ltae9110", "devty", "lol")
