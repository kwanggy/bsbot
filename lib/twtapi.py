# coding=utf-8
import tweepy
import urllib

from lib_config import TWT_CONSUMER_KEY, TWT_CONSUMER_SECRET, TWT_ACCESS_TOKEN, TWT_ACCESS_TOKEN_SECRET

def update_twt(twtid=None, msg='stop playing lol'):
    if(twtid == None):
        return None
    realmsg = '@' + str(twtid) + ' ' + msg
    
    auth = tweepy.OAuthHandler(TWT_CONSUMER_KEY, TWT_CONSUMER_SECRET)
    auth.set_access_token(TWT_ACCESS_TOKEN, TWT_ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    api.update_status(realmsg)
    return True

if __name__ == '__main__':
    update_twt('dog2230', '롤 그만해? #bsbot_lol')
