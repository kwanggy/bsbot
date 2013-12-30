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
        realmsg = '@' + str(userInfo['twtid']) + "몰래 롤하다걸림! 걸린 횟수:" + str(userInfo['offense']+1) +  ' ' + custom_msg 

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
        rnd = random.randint(0,2)
        print rnd

        base = 'stat'
        if rnd%2:
            # BASE ON OFFENSE   
            if offense != 3 and offense != 2:
                base = 'off'

        if base == 'off':
            # create msg base on offesne
            if offense+1 == 1:
                message = "퍼블! 븅신이 생성되고 있습니다 (처음 걸림)"
            elif offense+1 == 4:
                message = "병신이 미쳐 날뛰고 있습니다 (네번 걸림)"
            elif offense+1 == 5:   
                message = "병신짓을 도저히 막을 수 없습니다 (다섯번 걸림)"
            elif offense+1 == 6:
                message = "병신의 지배자 (여섯번 걸림)"
            elif offense+1 == 7:
                message = "병신의 화신 (일곱번 걸림)"
            elif offense+1 == 8:
                message = "전설의 병신 (여덞번 걸림)"

        elif base == 'stat':
            # get kills and deaths
            kills = None
            deaths = None
            for stat in stats['statistics']:
                print 'examining stat....'
                print stat
                if stat['name'] == 'NUM_DEATHS':
                    deaths = stat['value']
                elif stat['name'] == 'CHAMPIONS_KILLED':
                    kills = stat['value']

            if kills == None:
                print "kills: something went wrong"
                return message
            if deaths == None:
                print "deaths: something went wrong"
                return message

            kd = kills - deaths
            if kd < 0:
                # ByungShin
                # check by champ id
                if stats['championId'] == 64:       # LEESIN
                    message = "오버댓하는 눈 리신. 롤 좀 그만하자"

                elif stats['championId'] == 36:       # MUNDO
                    message = "오버댓하는 뇌 문도. 롤 좀 그만하자"

                elif stats['championId'] == 24:       # JAX
                    message = "오버댓하는 손 잭스. 롤 좀 그만하자"

                elif stats['championId'] == 44:
                    message = "뒤를 조심하시오...  롤 좀 그만하자"

            else:
                message = "게임은 잘했는데.. 그러다 인생은 패망.  좀 그만하자"
            

        print message
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
    user = { "twtid": "dog2230", "gamestat": "" }
    #bstwt.updateTwt(user)
    bstwt.sendDM('dog2230')
