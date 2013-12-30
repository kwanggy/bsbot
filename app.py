from flask import Flask, render_template, request, session, redirect, url_for, flash, send_from_directory
from models import user
import app_config as config
from lib.bslol  import BsLol
from lib.RegistrationForm import RegistrationForm
import hashlib

app = Flask(__name__)
app.config.from_object('app_config')

user = user.UserModel()
bslol = BsLol()

@app.route('/register/<key>')
def activateUser(key):
    lolname = user.pre_activateUser(key)
    print lolname
    if lolname == None:
        return render_template('info.html', info='activation failed!')
    else:
        lolid = bslol.getSummonerId(lolname)
        lastgame = bslol.getGameDate(lolid)
        user.activateUser(lolname, lolid, lastgame)
        return render_template('info.html', info='activation complete! good luck!')

@app.route('/test',methods=['GET','POST'])
def test():
    form = RegistrationForm()
    if request.method == 'GET':
        return render_template('index.html', form=form)
    elif request.method == 'POST':
        regCode = hashlib.sha224( form.summonername.data + form.twtid.data ).hexdigest()
        if form.validate(regCode):
            # generate registration code
            ret = user.addNewUser(lolname=form.summonername.data,twtid=form.twtid.data, regCode=regCode)
            if ret:
              flash( "Success! Check your twitter's direct message to complete registration", 'success' )
            else:
              flash( "Registration failed: You are already registered!", "error")
        else:
            # VALIDATION HAS FAILED.. BUT WHAT ERROR?
            if len(form.summonername.errors):
                flash( form.summonername.errors[0], 'error' )
            elif len(form.twtid.errors):    
                flash( form.twtid.errors[0], 'error')

        return render_template('index.html', form=form)





@app.route('/',methods=['GET','POST'])
def index():
    form = RegistrationForm()

    if request.method == 'POST':
        lolname = request.form['summonerid']
        twtid = request.form['twtid']
        lolid = bslol.getSummonerId(lolname)
        lastgame = bslol.getGameDate(lolid)
        ret = user.addNewUser(lolid,lolname,twtid,lastgame)
        if ret != False:
            print 'welcome to bs world'
        else:
            print 'user already exist'
            return redirect(url_for('index'))
        return redirect(url_for('welcome'))

    return render_template('signup.html', form=form)

@app.route('/signup', methods=['GET','POST'])
def signup():
    #if request.method == 'POST':
        
    return render_template('signup.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

if __name__ == "__main__":
    app.run(debug=True)
