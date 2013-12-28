from flask import Flask, render_template, request, session, redirect, url_for, flash, send_from_directory
from models import user
import app_config as config

app = Flask(__name__)
app.config.from_object('app_config')

user = user.UserModel()


@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        pass
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
