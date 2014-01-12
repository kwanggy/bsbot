from lib.bstwt import BsTwt
from lib.bslol import BsLol
from models.user import UserModel
from models.lol import LolModel

bsTwt = BsTwt()
bsLol = BsLol()

print 'hello world'
print 'worker has started....'


print 'reading lols from database...'
lolModel = LolModel()
lols = lolModel.getLols()
print 'reading lolss complete!'

for lol in lols:
    print 'processing user ' + lol.lolname + '...'

    curLastgame = bsLol.getLastgame(lol.id)
    if curLastgame == None:
        print 'error retrieving gameDate for ' + str(user.lolid)
        continue

    lastgame = lol.lastgame

    print '\tapi call: ' + str(curLastgame)
    print '\tdb call: ' + str(lastgame)

    print '\tusers:'
    for user in lol.users:
        print '\t\t' + user.twtid

    if curLastgame != lastgame:
        # user has played a game!
        print '\t' + lol.lolname + " has played a game!"

        # get recent game stat
        recentGameStat = bsLol.getRecentGameStats(lol.id)

        if recentGameStat == None:
            print 'error retreiving recent game stat'
            print 'will NOT update database or tweet'
            continue

        # update twt for each user associated with this lolid
        success = []
        for user in lol.users:
            # construct userinfo dict
            userInfo = { "twtid": user.twtid, 'lolname': lol.lolname,  "gamestat": recentGameStat, 'lang': user.lang }
            success.append(bsTwt.updateTwt(userInfo))

        if False in success:
            print '\t\ttwitter post failed for at least one follower'
            print '\t\tupdating database for ' + lol.lolname
            lolModel.setLastGame( lol.lolname, curLastgame )
        else:
            print '\t\tupdating database for ' + lol.lolname
            lolModel.setLastGame( lol.lolname, curLastgame )

        print '\t\tdone!'

print 'worker is exiting...'

