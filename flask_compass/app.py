from flask import (Flask,g,redirect,render_template,request,session,url_for)

app = Flask(__name__)
app.secret_key = 'somesecretkeythatonlyishouldknow'
        
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    return render_template('profile.html')