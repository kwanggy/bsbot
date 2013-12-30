from flask.ext.wtf import Form
from wtforms import TextField, validators
from bslol import BsLol
from bstwt import BsTwt

class RegistrationForm(Form):
    summonername = TextField('summonername', validators=[validators.Length(min=4, max=25), validators.Required()])
    twtid = TextField('twtid', validators=[validators.Required()])

    def __init__(self):
        Form.__init__(self)
        self.bslol = BsLol()
        self.bstwt = BsTwt()

    def validate(self, regCode):
        rv = Form.validate(self)
        if not rv:
           return False

        # check if user has given valid lol id
        summonerid = self.bslol.getSummonerId(self.summonername.data)
        if summonerid == None:
            self.summonername.errors.append("You've entered and invalid summoner id")
            return False

        # check if user has givne a valid twitter id

        # FIX: we must send reg_code to the dm
        twtRetCode = self.bstwt.sendDM(self.twtid.data, regCode)
        if twtRetCode != 0:
            if twtRetCode == 34: # error code 34: twitter user does not exist
                self.twtid.errors.append("You've entered an invalid Twitter ID!")
                return False
            elif twtRetCode == 150: # error code 150: not following us
                self.twtid.errors.append('To verify your Twitter account, we need to send you a direct message. Follow @bsbot_lol now!')
                return False
            else:
                self.twtid.errors.append('Error connecting to Twitter :(')
                return False

        return True
