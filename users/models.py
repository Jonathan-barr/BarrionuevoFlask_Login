#from login import mongo
import imp
from flask import Flask,jsonify, request
import uuid
from passlib.hash import pbkdf2_sha256
from tutoria import db
class User:
    def signup(self):
        #crear usuario
        user={
            "_id":uuid.uuid4().hex,
            "cedula":  request.form.get('cedula'),
            "nombres":request.form.get('nombre'),
            "apellidos":request.form.get('apellido'),
            "usuario":request.form.get('usuario'),
            "correo":request.form.get('correo'),
            "passwrd":request.form.get('passwrd'),
            "passwrd2":request.form.get('passwrd2'),
            "fecha_nacimiento":request.form.get('date'),
            "etnia":request.form.get('etnia'),
            "telefono":request.form.get('telefono'),
            "celular":request.form.get('celular'),
            "pais":request.form.get('pais'),
            "ciudad":request.form.get('ciudad'),
            "codigo_postal":request.form.get('codigo_postal'),
            "tipo_sangre":request.form.get('sangre'),
            "genero":request.form.get('genero')

       
        }
        
       # Encrypt the password
        user['passwrd'] = pbkdf2_sha256.encrypt(user['passwrd'])
        user['passwrd2'] = pbkdf2_sha256.encrypt(user['passwrd2'])
        db.user.insert_one(user)
        print(request.form);
 #       mongo.users.insert(user)
        return jsonify(user),200
        