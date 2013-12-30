import json
import requests

class LolApi:
    protocol = 'https'
    baseUrl = '://prod.api.pvp.net'
    ddragon = None

    apiKey = None
    region = None

    def __init__(self, apiKey, region):
        self.apiKey = apiKey
        self.region = region

        url = 'http://ddragon.leagueoflegends.com/realms/na.json'
        self.ddragon = json.loads(requests.get(url).content)

    def profileIcon(self, iconId):
        cdn = self.ddragon['cdn']
        ver = str(self.ddragon['n']['profileicon'])
        url = cdn + '/' + ver + '/img/profileicon/' + str(iconId) + '.png'
        return url 

    def request(self, api, param):
        subapi = None
        if '/' in api:
            api, subapi = api.split('/')
        url = self.protocol + self.baseUrl
        url += '/api/lol/' + self.region
        if api == 'champion':
            url += '/v1.1/champion'
        elif api == 'game':
            url += '/v1.2/game/by-summoner/' + param + '/recent'
        elif api == 'league':
            url += '/v2.2/league/by-summoner/' + param
        elif api == 'stats':
            if subapi == 'summary':
                url += '/v1.2/stats/by-summoner/' + param + '/summary'
            elif subapi == 'ranked':
                url += '/v1.2/stats/by-summoner/' + param + '/ranked'
        elif api == 'summoner':
            if subapi == 'masteries':
                url += '/v1.2/summoner/' + param + '/masteries'
            elif subapi == 'runes':
                url += '/v1.2/summoner/' + param + '/runes'
            elif subapi == 'by-name':
                url += '/v1.2/summoner/by-name/' + param
            elif subapi == 'summonerId':
                url += '/v1.2/summoner/' + param
            elif subapi == 'summonerIds':
                url += '/v1.2/summoner/' + ','.join(param) + '/name'
        elif api == 'team':
            url += '/v2.2/team/by-summoner/' + param
        url += '?api_key=' + self.apiKey

        r = requests.get(url)
        if r.status_code == 404:
            return None
        res = json.loads(r.content)
        #if api == 'summoner':
        #    res['profileIcon'] = self.profileIcon(res['profileIconId'])
        return res


if __name__ == '__main__':
    import sys
    print sys.argv
    if len(sys.argv) > 1:
        key = sys.argv[1]
    else:
        key = raw_input('Your api key: ')
    print key
    lol = LolApi(key, 'na')
    resp = lol.request('summoner/by-name', 'RiotSchmick')
    print resp
    print 'id:', resp['id']
    print 'name:', resp['name']
    print 'profile icon:', lol.profileIcon(resp['profileIconId'])

