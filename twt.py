# coding=utf-8
import tweepy
import urllib

#OAuth settings - Access level(READ and WRITE)
CONSUMER_KEY = 'yJJf9whRaBt7frTIww5jgg'
CONSUMER_SECRET = '2njNNigvmq1R1IShZn07ujRynib1Hh4T3VSENz8'

#Access token of bsbot_lol
ACCESS_TOKEN = '2264861497-beSs65r3ij9JxaB0M7dkv4g7OFPM8h2vKNdW7yD'
ACCESS_TOKEN_SECRET = 'jSD2kQpitZ94LZMYmtlDfnarM33Do01HkdnLwWlZyyJMe'

def update_twt(twtid=None, msg='stop playing lol'):
    if(twtid == None):
        return None
    realmsg = '@' + str(twtid) + ' ' + msg
    
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    api.update_status(realmsg)
    return True

if __name__ == '__main__':
    update_twt('dog2230', '롤 그만해 #bsbot_lol')
