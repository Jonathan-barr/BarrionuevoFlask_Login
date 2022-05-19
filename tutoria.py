from functools import wraps
from flask import Flask, redirect, render_template, session
import pymongo 
import cv2
import base64
import random
import numpy as np



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

@app.route('/validacion')
def index():
    data = crearFigura()
    imgdata = 'data:image/jpg;base64,' + base64.b64encode(data[0]).decode('ascii')
    revi = valores()
    return render_template('index.html', image = imgdata, texto="Holaaa", coordenadas=data[1], revisar = revi)

def valores():
    alt1 = random.randrange(0, 2, 1)
    alt2 = random.randrange(0, 2, 1)
    alt3 = random.randrange(0, 2, 1)
    alt4 = random.randrange(0, 2, 1)
    alt5 = random.randrange(0, 2, 1)
    total = ''
    if alt1 == 0:
        total += "Rectangulo "
    else:
        total += "Circulo "
    if alt2 == 0:
        total += "Rectangulo "
    else:
        total += "Circulo "
    if alt3 == 0:
        total += "Rectangulo "
    else:
        total += "Circulo "
    if alt4 == 0:
        total += "Rectangulo "
    else:
        total += "Circulo "
    if alt5 == 0:
        total += "Rectangulo "
    else:
        total += "Circulo "
    return total

def crearFigura():
    ubicaciones = []
    imagen = cv2.imread('./static/gato.jpg')

    alt1=0
    alt2=2
    alt3=1
    alt4=3
    
    #while alt1 == alt2 or alt3 == alt4:
    #    alt1 = random.randrange(1, 4, 1)
    #    alt2 = random.randrange(1, 4, 1)
    #    alt3 = random.randrange(1, 4, 1)
    #    alt4 = random.randrange(1, 4, 1)


    for i in range(2):
        for j in range(4):
            espacio = random.randrange(10, 40, 1)
            x = ((round(imagen.shape[1]/4)-1)*j)+espacio
            y = ((round(imagen.shape[0]/2)-1)*i)+espacio
                
            w = random.randrange(50, round(imagen.shape[1]/4)-1-espacio, 1)
            h = random.randrange(50, round(imagen.shape[0]/2)-1-espacio, 1)
            
            if i == 0:
                if j == alt1:
                    ubicaciones.append(["Rectangulo",x,y,w+x,h+y])
                    cv2.rectangle(imagen, (x, y), (x + w, y + h), (0, 255, 255), 2)
                elif j == alt2:
                    ubicaciones.append(["Circulo",x+50,y+50,w-round(w/2)])
                    cv2.circle(imagen, (x+50, y+50), w-round(w/2), (0, 0, 255), 2)
                    #ubicaciones.append(['Tria',x,y,w,h])
                    #pts = np.array([[x-w+80,y+90],[x+50,y],[x+w,y+90]], np.int32)
                    #pts = pts.reshape((-1,1,2))
                    #cv2.polylines(imagen,[pts],True,(0,0,255), 2)
            elif i == 1:
                if j == alt3:
                    ubicaciones.append(["Rectangulo",x,y,w+x,h+y])
                    cv2.rectangle(imagen, (x, y), (x + w, y + h), (0, 255, 255), 2)
                elif j == alt4:
                    ubicaciones.append(["Circulo",x+50,y+50,w-round(w/2)])
                    cv2.circle(imagen, (x+50, y+50), w-round(w/2), (0, 0, 255), 2)
            
    imagen = cv2.imencode('.jpg', imagen)[1]
    return [imagen,ubicaciones]
