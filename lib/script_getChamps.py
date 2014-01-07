
from lolapi import LolApi
from lib_config import RIOT_API_KEY

if __name__ == '__main__':
    lol = LolApi(RIOT_API_KEY, 'na')
    champions = lol.request('champion', "")
    for champion in champions['champions']:
        print str(champion['id']) + ";" + champion['name']
        
