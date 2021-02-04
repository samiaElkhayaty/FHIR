# -*- coding: utf-8 -*-
"""
Created on Tues Feb 2 15:45:02 2021

@author: Samia
"""
from app import app
from flask import Flask, render_template,request
#import sqlite3
import json
#
#def createdb():
#    conn = sqlite3.connect ('mydatabase.db')
#    print ("base de donnéées ouverte avec succès")
#    conn.execute ("CREATE TABLE Etudiants (nom TEXT, addr TEXT, pin TEXT)")
#    print ("Table créée avec succès")
#    conn.close()
#
#def adduser(nom,addr,pin):
#    with sqlite3.connect("mydatabase.db") as con:
#        cur = con.cursor()
#        cur.execute("INSERT INTO Etudiants(nom,addr,pin) VALUES(?,?,?)" , (nom ,addr,pin))
#        con.commit()
#    con.close()


#donnes = 'data.json'
#f = open(donnes)
#data = json.load(f)
#f.close()
#print(data)

@app.route("/")
def index1():
    return render_template ('new_bdd.html')

@app.route("/Patient", methods = ['GET'])
def index():
    title ={'title':'Patient'}
    Prenom = request.args.get("Prenom")
    Nom = request.args.get("Nom")    
    user = {'Nom': str(Nom), 'Prenom': str(Prenom)}
    return render_template ('index.html', title=title, user=user)



#
    #http://127.0.0.1:5000/Patient?Nom=ELK&Prenom=SAM
    
#@app.route("/")
#def index():
#    return render_template ('new.html')

# @app.route('/params',methods=['GET'])
# def params():
#     surname = request.args.get("surname")
#     print (surname)
#     name = request.args.get("name")
#     print (name)

# @app.route("/new",methods=['POST'])
# def new():
#     createdb(S)
#     nom = request.form.get('nom')
#     addr = request.form.get ('add')
#     pin = request.form.get('pin')
#     adduser(nom, adr, pin)
#     return "c'est bon mon gaté"

# @app.route('/')
# def index():
#     return render_template('new_bdd')

# @app.route('/new', methods=['POST'])
# def addetudiant():
#     nom = request.form.get['nom']
#     adr = request.form.get['add'] 
#     pin = request.form.get['pin']
#     import insert
#     insert(nom, adr, pin)
#     return "Insertion OK"

#@app.route('/')
#def index():
#    return render_template('base.html')
