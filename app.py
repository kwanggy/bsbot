from flask import Flask, render_template, request, session, redirect, url_for, flash, send_from_directory
from models import user
import app_config as config
from lib.bslol  import BsLol

app = Flask(__name__)
app.config.from_object('app_config')

user = user.UserModel()
bslol = BsLol()

@app.route('/',methods=['GET','POST'])
def index():
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

    return render_template('signup.html')

'''
@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        
    return render_template('signup.html')
'''

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

if __name__ == "__main__":
    app.run(debug=True)
