from models.user import UserModel

userModel = UserModel()
users = userModel.getUsers()

for user in users:
    print user.lolname
    print '\tlolid: ' + str(user.lolid)
    print '\ttwtid: ' + str(user.twtid)
    print '\tlastgame: ' + str(user.lastgame)
    print '\toffense: ' + str(user.offense)
    print '\tactive: ' + str(user.active)
    print '\tactive_since: ' + str(user.active_since)
    print '\tlive_since: ' + str(user.live_since)
    print '\tregCode: ' + user.regCode
