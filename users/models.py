#from login import mongo

from flask import Flask,jsonify, request, session, redirect
import uuid
from passlib.hash import pbkdf2_sha256
import tutoria 
class User:

    def start_session(self,user):
        del user['passwrd']
        del user['passwrd2']
        session['logged_in']=True
        session['user']=user
        return jsonify(user), 200


    def signup(self):
        #crear usuario
        user={
            "_id":uuid.uuid4().hex,
            "cedula":  request.form.get('cedula'),
            "nombres":request.form.get('nombre'),
            "apellidos":request.form.get('apellido'),
            "usuario":request.form.get('usuario'),
            "email":request.form.get('email'),
            "passwrd":request.form.get('passwrd'),
            "passwrd2":request.form.get('passwrd2'),
            "fecha_nacimiento":request.form.get('date'),
            "telefono":request.form.get('telefono'),
            "celular":request.form.get('celular'),
            "pais":request.form.get('pais'),
            "ciudad":request.form.get('ciudad'),
            "codigo_postal":request.form.get('codigo_postal'),
            "tipo_sangre":request.form.get('sangre'),
            "genero":request.form.get('genero')

       
        }
     
        #validad si el correo ya esta registrado
        if tutoria.db.user.find_one({ "email": user['email'] }):
            return jsonify({ "error": "El correo ya existe" }), 400
                 # Encrypt the password
        user['passwrd'] = pbkdf2_sha256.encrypt(user['passwrd'])
        user['passwrd2'] = pbkdf2_sha256.encrypt(user['passwrd2'])
        #usuario
        if tutoria.db.user.insert_one(user):
          return self.start_session(user)

        return jsonify({"error":"Registro Fallido"}),400
     
    def signout(self):
        session.clear()
        return redirect('/')
        
    def login(self):
        user = tutoria.db.user.find_one({
            "email": request.form.get('email')
        })
        if user and pbkdf2_sha256.verify(request.form.get('passwrd'), user['passwrd']):
            return self.start_session(user)
    
        return jsonify({ "error": "Error no existe el usuario o Credenciales erroneas" }), 400