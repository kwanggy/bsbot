from lib.bstwt import BsTwt
from lib.bslol import BsLol
from models.user import UserModel

bsTwt = BsTwt()
bsLol = BsLol()

print 'hello world'
print 'worker has started....'


print 'reading from database...'
userModel = UserModel()
users = userModel.getActiveUsers()
print 'reading users complete!'

for user in users:
    print 'processing user ' + user.lolname + '...'

    cur_gameDate = bsLol.getGameDate(user.lolid)
    if cur_gameDate == None:
        print 'error retrieving gameDate for ' + user.loid
        continue

    last_gameDate = userModel.getLastGame(user.lolid)

    print '\tapi call: ' + str(cur_gameDate)
    print '\tdb call: ' + str(last_gameDate)

    print '\toffense:' + str(user.offense)
    if cur_gameDate != last_gameDate:
        # HOLY CRAP.. THIS GUY IS BS
        print '\t' + user.lolname + " is BS!"
        print '\t' + str(user.offense+1) + " offesne!"

        # get recent game stat
        recentGameStat = bsLol.getRecentGameStats(user.lolid)

        if recentGameStat == None:
            print 'error retreiving recent game stat'
            print 'will NOT update database or tweet'
            continue

        # construct userinfo dict
        userInfo = { "twtid": user.twtid, "gamestat": recentGameStat, "offense": user.offense }
        success = bsTwt.updateTwt(userInfo)

        if not success:
            print 'twitter post failed...'
            print 'will NOT update database...'
        else:
            print '\t\tupdating database...'
            userModel.setLastGame( user.lolid, cur_gameDate )
            userModel.updateOffense( user.lolid )

        print '\t\tdone!'

print 'worker is exiting...'

