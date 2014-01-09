
from lolapi import LolApi
from lib_config import RIOT_API_KEY
import requests


""" EN
if __name__ == '__main__':
    lol = LolApi(RIOT_API_KEY, 'na')
    champions = lol.request('champion', "")
    for champion in champions['champions']:
        print str(champion['id']) + ";" + champion['name']
"""
if __name__ == '__main__':
    lol = LolApi(RIOT_API_KEY, 'na')
    champions = lol.request('champion', "")
    for champion in champions['champions']:
        r = requests.get('http://gameinfo.leagueoflegends.co.kr/ko/game-info/champions/' + champion['name'].lower())
        if r.status_code == 200:
            first = r.text.find('title')
            second = r.text.find('title', first+1)
            print str(champion['id']) + ';' + r.text[first:second].split('>')[1].split('|')[0].rstrip()
        else:
            print 'ERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRROR'
            break
            



