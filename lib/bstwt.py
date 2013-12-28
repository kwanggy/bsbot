# coding=utf-8
import tweepy
import urllib
import datetime
from lib_config import TWT_CONSUMER_KEY, TWT_CONSUMER_SECRET, TWT_ACCESS_TOKEN, TWT_ACCESS_TOKEN_SECRET


class BsTwt:
    def __init__(self):
        self.consumer_key = TWT_CONSUMER_KEY
        self.consumer_secret = TWT_CONSUMER_SECRET
        self.access_token = TWT_ACCESS_TOKEN
        self.access_token_secret = TWT_ACCESS_TOKEN_SECRET

    def updateTwt(self, userInfo):
        if 'twtid' not in userInfo:
            return None
        if 'gamestat' not in userInfo:
            return None

        # generate custom message
        custom_msg = self.getStatMessage( userInfo['gamestat'], userInfo['offense'] )
        realmsg = '@' + str(userInfo['twtid']) + " " + str(userInfo['offense']+1) +  ' ' + custom_msg 

        # post to twitter
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth)
        api.update_status(realmsg)

        return True

    def getStatMessage(self, stats, offense):
        return '롤 그만하자...'
        
        

if __name__ == '__main__':
    bstwt = BsTwt()
    user = { "twtid": "dog2230", "gamestat": "" }
    bstwt.updateTwt(user)
