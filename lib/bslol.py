from lolapi import LolApi
from lib_config import RIOT_API_KEY
import json

class BsLol():
    def __init__(self):
        self.API_KEY = RIOT_API_KEY
        self.REGION = 'na'
        self.lol = LolApi(self.API_KEY,self.REGION)

    def getSummonerId(self,name):
        summonerId = self.lol.request('summoner/by-name',str(name))['id']
        #print 'name:', name, 'id:', summonerId
        return summonerId

    def getGameDate(self,summonerId):
        #print 'start @@@@@@@@@@@@@@@@@@@@@'
        gameData = self.lol.request('game',str(summonerId))
        #print 'haha@@@@@@@@@@@@@@@@@@@@@@'
        gameDate = 0
        for a in range(10):
            gameDate += gameData['games'][a]['createDate']
        #print 'gameDate in milliseconds:',  gameDate
        return gameDate
        
    def getRecentGameStats(self,summonerId):
        recentStats = None
        recentGameStats = self.lol.request('game',str(summonerId))['games']

        # get most recent game
        for gameStats in recentGameStats:
            if recentStats == None:
                recentStats = gameStats
                continue
            if recentStats['createDate'] < gameStats['createDate']:
                recentStats = gameStats
            
        return recentStats

if __name__ == '__main__':
    l = BsLol()
    #print l.getGameDate(l.getSummonerId('soulwingz'))
    print l.getRecentGameStats(l.getSummonerId('soulwingz'))
