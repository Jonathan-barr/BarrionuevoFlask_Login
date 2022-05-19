from flask import Flask, render_template
import pymongo 



app = Flask(__name__)
#ROuter
from users import routes

#Databes
client = pymongo.MongoClient("mongodb+srv://Login:GQl9ccoFKKG11fDd@cluster0.qd2uc.mongodb.net/?retryWrites=true&w=majority")
db = client.Login

#client=pymongo.MongoClient('mongodb+srv://Login:Huevos/1@cluster0.qd2uc.mongodb.net/Login?retryWrites=true&w=majority')
#app.config["MONGO_URI"] = "mongodb+srv://proyectoml:8voyOIN8aam7j94e@cluster0.qd2uc.mongodb.net/ProyectoML?retryWrites=true&w=majority"
#mongo = PyMongo(app)
#client=mongo_client(MONGO_URI)


@app.route("/")
def home():
    return render_template('login.html')

@app.route("/signup/")
def dashboard():
    return render_template('signup.html')