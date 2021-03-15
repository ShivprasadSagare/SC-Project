import os
import datetime
import hashlib
from flask import Flask, session, url_for, redirect, render_template, request, abort, flash
from werkzeug.utils import secure_filename
import json
import requests

app = Flask(__name__)
app.config.from_object('config')

@app.errorhandler(401)
def FUN_401(error):
    return render_template("page_401.html"), 401

@app.errorhandler(403)
def FUN_403(error):
    return render_template("page_403.html"), 403

@app.errorhandler(404)
def FUN_404(error):
    return render_template("page_404.html"), 404

@app.errorhandler(405)
def FUN_405(error):
    return render_template("page_405.html"), 405

@app.errorhandler(413)
def FUN_413(error):
    return render_template("page_413.html"), 413


@app.route("/")
def FUN_root():
    return render_template("index.html")

with open('./p.json', 'r') as myfile:
    politiciansDataFile = json.load(myfile)

politiciansKeys = []
for key in politiciansDataFile.keys() :
    politiciansKeys.append(key)

# global iterator
politiciansIterator = 10
@app.route("/politicians", methods=['GET', 'POST'])
def FUN_politicians():
    if(request.method == 'POST'):
        politiciansOutputFile = open('testP.json', 'a')
        sentence = request.form.get('sentence')
        req = request.form.getlist('triples')
        print(req)
        print(sentence)
        global politiciansIterator
        politiciansIterator += 1
        flag = False

        # Write into output
        text = '{\n"entity_id" : "' + politiciansKeys[politiciansIterator] + '",\n"triples": [\n'
        for triple in req:
            subject = politiciansDataFile[politiciansKeys[politiciansIterator]]['personLabel']
            predicate = triple.split(', ')[0]
            obj = triple.split(', ')[1]
            if predicate != '' and obj != '':
                text += '{\n\t"subject": "' + subject + '",\n\t"predicate": "' + predicate + '",\n\t"object": "' + obj + '"\n},'
                flag = True
        text = text[:-1]
        text += '\n],\n"sentence": "' + sentence + '"\n},\n' 
        if flag :
            politiciansOutputFile.write(text)    
        


    return render_template("politicians.html", title="politicians", jsonfile=politiciansDataFile, length = len(politiciansDataFile.keys()), key = politiciansKeys[politiciansIterator], iterator = politiciansIterator)

with open('./c.json', 'r') as myfile:
    cricketersDataFile = json.load(myfile)

cricketersKeys = []
for key in cricketersDataFile.keys() :
    cricketersKeys.append(key)
cricketersIterator = 0

@app.route("/cricketers", methods=['GET', 'POST'])
def FUN_cricketers():
    if(request.method == 'POST'):
        cricketersOutputFile = open('testC.json', 'a')
        sentence = request.form.get('sentence')
        req = request.form.getlist('triples')
        print(req)
        print(sentence)
        global cricketersIterator
        cricketersIterator += 1
        flag = False

        # Write into output
        text = '{\n"entity_id" : "' + cricketersKeys[cricketersIterator] + '",\n"triples": [\n'
        for triple in req:
            subject = cricketersDataFile[cricketersKeys[cricketersIterator]]['personLabel']
            predicate = triple.split(', ')[0]
            obj = triple.split(', ')[1]
            if predicate != '' and obj != '':
                text += '{\n\t"subject": "' + subject + '",\n\t"predicate": "' + predicate + '",\n\t"object": "' + obj + '"\n},\n'
                flag = True
        text += '],\n"sentence": "' + sentence + '"\n},\n' 
        if flag:
            cricketersOutputFile.write(text)

    return render_template("cricketers.html", title="cricketers", jsonfile=cricketersDataFile, length = len(cricketersDataFile.keys()), key = cricketersKeys[cricketersIterator], iterator = cricketersIterator)

with open('./a.json', 'r') as myfile:
    actorsDataFile = json.load(myfile)

actorsKeys = []
for key in actorsDataFile.keys() :
    actorsKeys.append(key)
actorsIterator = 0

@app.route("/actors", methods = ['GET', 'POST'])
def FUN_actors():
    if(request.method == 'POST'):
        actorsOutputFile = open('testA.json', 'a')
        sentence = request.form.get('sentence')
        req = request.form.getlist('triples')
        global actorsIterator
        actorsIterator += 1
        flag = False

        # Write into output
        text = '{\n"entity_id" : "' + actorsKeys[actorsIterator] + '",\n"triples": [\n'
        for triple in req:
            subject = actorsDataFile[actorsKeys[actorsIterator]]['personLabel']
            predicate = triple.split(', ')[0]
            obj = triple.split(', ')[1]
            text += '{\n\t"subject": "' + subject + '",\n\t"predicate": "' + predicate + '",\n\t"object": "' + obj + '"\n},\n'
            flag = True
        text += '],\n"sentence": "' + sentence + '"\n},\n' 
        if flag :
            actorsOutputFile.write(text)

    return render_template("actors.html", title="actors", jsonfile=actorsDataFile, length = len(actorsDataFile.keys()), key=actorsKeys[actorsIterator], iterator = actorsIterator)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")