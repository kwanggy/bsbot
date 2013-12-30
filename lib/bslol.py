from lolapi import LolApi
from lib_config import RIOT_API_KEY
import json

class BsLol():
    def __init__(self):
        self.API_KEY = RIOT_API_KEY
        self.REGION = 'na'
        self.lol = LolApi(self.API_KEY,self.REGION)

    def getSummonerId(self,name):
        summonerProfile = self.lol.request('summoner/by-name', str(name))
        if summonerProfile == None:
            return None
        summonerId = summonerProfile['id']
            

        #print 'name:', name, 'id:', summonerId
        return summonerId

    def getGameDate(self,summonerId):
        gameData = self.lol.request('game',str(summonerId))
        gameDate = 0

        # error handling
        if gameData == None:
            return None

        #print 'processing ' + str(len(gameData['games'])) + ' games...'
        for a in range(len(gameData['games'])):
            gameDate += gameData['games'][a]['createDate']
        return gameDate
        
    def getRecentGameStats(self,summonerId):
        recentStats = None
        recentGameStats = self.lol.request('game',str(summonerId))['games']
        
        # error checks..    
        if recentGameStats == None:
            return None
        
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
    print l.getSummonerId('soulwingzw')
