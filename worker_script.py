from lib.bstwt import BsTwt
from lib.bslol import BsLol
from models.user import UserModel

bsTwt = BsTwt()
bsLol = BsLol()

print 'hello world'
print 'worker has started....'


print 'reading from database...'
userModel = UserModel()
users = userModel.getUsers()
print 'reading users complete!'

for user in users:
    print 'processing user ' + user.lolname + '...'
    cur_gameDate = bsLol.getGameDate(user.lolid)
    last_gameDate = userModel.getLastGame(user.lolid)

    print '\tapi call: ' + str(cur_gameDate)
    print '\tdb call: ' + str(last_gameDate)

    print '\toffense:' + str(user.offense)
    if cur_gameDate != last_gameDate:
        # HOLY CRAP.. THIS GUY IS BS
        print '\t' + user.lolname + " is BS!"
        print '\t' + str(user.offense+1) + " offesne!"
        # construct userinfo dict
        userInfo = { "twtid": user.twtid, "gamestat": "", "offense": user.offense }
        bsTwt.updateTwt(userInfo)

        # TODO: UPDATE DB
        print '\t\tupdating database...'
        userModel.setLastGame( user.lolid, cur_gameDate )
        userModel.updateOffense( user.lolid )
        print '\t\tdone!'

