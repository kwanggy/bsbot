from lolapi.lol import LolApi
import json

class BsLol():
    def __init__(self):
        self.API_KEY = 'dbf1810e-f182-48f3-a8bd-b48be450dcb2'
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
        recentGameStats = self.lol.request('game',str(summonerId))
        return recentGameStats

if __name__ == '__main__':
    l = BsLol()
    l.getGameDate(l.getSummonerId('soulwingz'))
