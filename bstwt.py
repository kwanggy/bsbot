# coding=utf-8
import twt

def bs_twt(usrinfo):
    if(usrinfo['twtid'] == None):
        return None
    bstwt = '롤 그만하시다고 저희와 약속하셨잖아요~ by #bsbot_lol'
    ret = twt.update_twt(usrinfo['twtid'], bstwt)
    if ret == None:
        return None
    return True

if __name__ == '__main__':
    usrinfo={}
    usrinfo['twtid'] = 'dog2230'
    bs_twt(usrinfo)
