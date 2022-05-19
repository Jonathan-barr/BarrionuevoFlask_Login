from functools import wraps
from flask import Flask, redirect, render_template, session
import pymongo 



app = Flask(__name__)
app.secret_key=b'\xc04\x90\x17s\x08\xd1W\xae\xf7R\xd7\x1e$\x16{'
#ROuter
from users import routes

#Databes
client = pymongo.MongoClient("mongodb+srv://Login:GQl9ccoFKKG11fDd@cluster0.qd2uc.mongodb.net/?retryWrites=true&w=majority")
db = client.Login
#conexion valida
#decoration
def login_requiere(f):
    @wraps(f)
    def wrap(*args, **kwarg):
        if 'logged_in' in session:
            return f(*args, **kwarg)
        else:
            return redirect('/')
    return wrap

@app.route("/")
def lo():
    return render_template('login.html')
@app.route("/dashboart")
@login_requiere
def home():
    return render_template('dashboart.html')

@app.route("/signup/")
def sigup():
    return render_template('signup.html')