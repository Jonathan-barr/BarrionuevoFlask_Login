from crypt import methods
from flask import Flask
from tutoria import app
from users.models import User

@app.route('/user/signup',methods=['POST'])
def signup():
    return User().signup()

@app.route('/user/signout')
def signout():
  return User().signout()

@app.route('/user/login', methods=['POST'])
def login():
  return User().login()