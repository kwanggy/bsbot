# coding=utf-8
import tweepy
import urllib
import random
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
        realmsg = '@' + str(userInfo['twtid']) + "몰래 롤하다걸림! 걸린 횟수:" + str(userInfo['offense']+1) +  ' ' + custom_msg  + '\xea\xb0\x80\xeb\xa0\x8c'

        # post to twitter
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth)

        try:
            api.update_status(realmsg)
        except tweepy.TweepError as e:
            print e
            print 'status update failed'
            return False

        return True

    def getStatMessage(self, stats, offense):
        message = '롤하지말라고...'
        return message
        
    def sendDM(self, twtid, message):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth)

        try:
            api.send_direct_message(text=message, user=twtid)
        except tweepy.TweepError as e:
            print e[0][0]['code']
            return e[0][0]['code']

        return 0


if __name__ == '__main__':
    bstwt = BsTwt()
    user = { "twtid": "dog2230", "gamestat": "", 'offense': 1}
    bstwt.updateTwt(user)
    #bstwt.sendDM('dog2230')
