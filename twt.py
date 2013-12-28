import tweepy

#OAuth settings - Access level(READ and WRITE)
CONSUMER_KEY = 'yJJf9whRaBt7frTIww5jgg'
consuMER_SECRET = '2njNNigvmq1R1IShZn07ujRynib1Hh4T3VSENz8'

#Access token of bsbot_lol
ACCESS_TOKEN = '2264861497-beSs65r3ij9JxaB0M7dkv4g7OFPM8h2vKNdW7yD'
ACCESS_TOKEN_SECRET = 'jSD2kQpitZ94LZMYmtlDfnarM33Do01HkdnLwWlZyyJMe'

#user information from database
twtid = 'dog2230' 

#UPDATE TWT as post request for twitter server
POST_URL = 'https://api.twitter.com/1.1/statuses/update.json'
POST_CONTEXT = '?status=%40'+ twtid + '%20stop%20playing%20league%20%23bsbot_lol&display_coordinates=false'

def update_twt(msg='@dog2230 stop playing lol'):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    api.update_status(msg)

if __name__ == '__main__':
    update_twt()
