# coding=utf-8
import tweepy
from djk.djk import djkReader
from lib_config import TWT_CONSUMER_KEY, TWT_CONSUMER_SECRET, TWT_ACCESS_TOKEN, TWT_ACCESS_TOKEN_SECRET


class BsTwt:
    def __init__(self):
        self.consumer_key = TWT_CONSUMER_KEY
        self.consumer_secret = TWT_CONSUMER_SECRET
        self.access_token = TWT_ACCESS_TOKEN
        self.access_token_secret = TWT_ACCESS_TOKEN_SECRET
        self.strings = djkReader('lib/djk/en_v1.djk', 'lib/djk/kr_v1.djk').djkString

    def updateTwt(self, userInfo):
        if 'twtid' not in userInfo:
            return None
        if 'gamestat' not in userInfo:
            return None

        # generate custom message
        # we need to clean up userinfo for our custom mssg..
        # get needed info from statistsics..
        recentStats = userInfo['gamestat']['statistics']
        death = kills =assists = 'none'
        for item in recentStats:
            if item['name'] == 'NUM_DEATHS':
                deaths = item['value']
            elif item['name'] == 'CHAMPIONS_KILLED':
                kills = item['value']
            elif item['name'] == 'ASSISTS':
                assists = item['value']


        mapid = userInfo['gamestat']['mapId']
        championid = userInfo['gamestat']['championId']
        custom_msg = self.getMessage( {'twtid': userInfo['twtid'], 'lolname':userInfo['lolname'], 'lang': userInfo['lang'], 'kills': kills, 'deaths':deaths, 'assists':assists, 'mapid': mapid, 'championid': championid}   )

        # post to twitter
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth)

        try:
            api.update_status(custom_msg)
        except tweepy.TweepError as e:
            print e
            print 'status update failed'
            return False

        return True

    def getMessage(self, userInfo):
        lang = userInfo['lang']
        twtFormat = self.strings[lang]['twt_format'][0]

        # update userInfo to include champion name based on lang
        userInfo['championname'] = self.strings[lang]['champions'][userInfo['championid']]
        userInfo['mapname'] = self.strings[lang]['maps'][userInfo['mapid']]

        msg = self.reformatMsg(twtFormat, userInfo)
        
        return msg

    def reformatMsg(self, twtFormat, userInfo ):
        while twtFormat.find('<')!= -1:
            one = twtFormat.find('<') + 1 
            two = one + twtFormat[one:].find('>')
            keyword = twtFormat[one:two] # keyword to replace is here

            # find replacement string, nothing if it does not exist
            replaceKeyword = userInfo.get(keyword, "")

            # replace keyword
            twtFormat = twtFormat.replace( '<' + keyword + '>', str(replaceKeyword) )

        return twtFormat
                           
                            
        
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
    user = { "twtid": "dog2230", "lolname": 'devty' , "gamestat": "", 'lang': 'kr'}
    print bstwt.getMessage(user)
    #bstwt.sendDM('dog2230')
