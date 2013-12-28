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
        realmsg = '@' + str(userInfo['twtid']) + " " + str(userInfo['offense']+1) +  ' ' + custom_msg 

        # post to twitter
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth)
        api.update_status(realmsg)

        return True

    def getStatMessage(self, stats, offense):
        message = '롤하지말라고... ㅂㅅ'
        rnd = random.randint(0,2)
        print rnd

        base = 'stat'
        if rnd%2:
            # BASE ON OFFENSE   
            if offense != 3 or offense != 2:
                base = 'off'

        if base == 'off':
            # create msg base on offesne
            if offense+1 == 1:
                message = "퍼블! 병신이 생성되고 있습니다 (처음 걸림)"
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
            for stat in stats['statistics']:
                if stat['name'] == 'NUM_DEATHS':
                    deaths = stat['value']
                elif stat['name'] == 'CHAMPIONS_KILLED':
                    kills = stat['value']

            kd = kills - deaths
            if kd < 0:
                # ByungShin
                # check by champ id
                if stat['championId'] == 64:       # LEESIN
                    message = "오버댓하는 눈 리신. 접어라"

                elif stat['championId'] == 36:       # MUNDO
                    message = "오버댓하는 뇌 문도. 접어라"

                elif stat['championId'] == 24:       # JAX
                    message = "오버댓하는 손 잭스. 접어라"

                elif stat['championId'] == 44:
                    message = "뒤를 조심하시오 ㅂㅅ이여. 그리고 접어라"

            else:
                message = "게임은 잘하는데 인생은 패망이네. 접어라"
            

        return message
        
        
        

if __name__ == '__main__':
    bstwt = BsTwt()
    user = { "twtid": "dog2230", "gamestat": "" }
    bstwt.updateTwt(user)
