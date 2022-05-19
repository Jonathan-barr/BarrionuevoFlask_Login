from flask import Flask
from tutoria import app
from users.models import User

@app.route('/user/signup',methods=['POST'])
def signup():
    return User().signup()