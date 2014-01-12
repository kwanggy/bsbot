from flask import Flask, render_template, request, session, redirect, url_for, flash, send_from_directory
from models import user, lol
import app_config as config
from lib.bslol  import BsLol
from lib.RegistrationForm import RegistrationForm
import hashlib

app = Flask(__name__)
app.config.from_object('app_config')

user = user.UserModel()
lol = lol.LolModel()
bslol = BsLol()

@app.route('/dev/users')
def users():
    users = user.getUsers()

    return render_template('users.html', users=users)

@app.route('/register/<twtid>/<lolname>/<key>')
def activateUser(twtid, lolname, key):
    # step 1: retrive lolname
    loluser = lol.getLolByLolname(lolname)

    if not loluser:
        return render_template('info.html', info='activation failed :( could not find lolname')

    # step 2: append loluser if regcode is matched. if user record does not exist, we automatically create it
    ret = user.addLolToTwtid(twtid=twtid, regcode=key, lol=loluser)
 
    if not ret:
        return render_template('info.html', info='activation failed :(')
    return render_template('info.html', info='activation complete! good luck!')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/',methods=['GET','POST'])
def index():
    form = RegistrationForm()
    if request.method == 'GET':
        return render_template('index.html', form=form)
    elif request.method == 'POST':
        # generate registration code
        regcode = hashlib.sha224( form.summonername.data + form.twtid.data ).hexdigest()

        if form.validate(regcode):
            # twitter user was found!

            # step 1: get loluser. If user is not found, returns None
            loluser = lol.getLolByLolname(form.summonername.data)
            
            if not loluser:
                # if loluser does not exsit...
                # 1. get user data from riot api
                lolid = bslol.getSummonerId(form.summonername.data)
                lastgame = bslol.getLastgame(lolid)

                # 2. create new lol data
                loluser = lol.addNewLol(lolid=lolid, lastgame=lastgame, lolname=form.summonername.data )

            # step 2: check if user exists
            myUser = user.getUserByTwtid( form.twtid.data )

            # if uesr does not exist, create one
            if myUser == None:
                ret = user.addNewUser( form.twtid.data, regcode, form.lang.data )
            # if user exists, we need to update regcode and lang
            else:
               ret = user.updateUserAtActivation( form.twtid.data, regcode, form.lang.data)

            if ret:
                flash( "Success! Check your twitter's direct message to complete registration", 'success' )
            else:
                flash( "Registration failed! " + ret, "error")

        else:
            # VALIDATION HAS FAILED.. BUT WHAT ERROR?
            if len(form.summonername.errors):
                flash( form.summonername.errors[0], 'error' )
            elif len(form.twtid.errors):    
                flash( form.twtid.errors[0], 'error')

        return render_template('index.html', form=form)

if __name__ == "__main__":
    """
    lol = lol.addNewLol('1234', 'devty', '5678')
    print user.addLoltoTwtid("ltae9110", "devty", lol)
    print user.addLoltoTwtid("dob2230", "starvinglol", lol)
    print len(user.getUserLolsByTwtid('ltae9110'))
    print user.getUserLolsByTwtid('ltae9110')[0].id
    
    print user.getUserLolsByTwtid('ltae9110')[0]
    """
    app.run(debug=True)
