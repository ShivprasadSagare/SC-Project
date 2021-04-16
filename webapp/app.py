import os
import datetime
import hashlib
from typing import Tuple
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
politiciansIterator = 0
@app.route("/politicians", methods=['GET', 'POST'])
def FUN_politicians():
    if(request.method == 'POST'):
        politiciansOutputFile = open('testP.json', 'a')
        sentence = request.form.get('sentence')
        req = request.form.getlist('triples')
        print(req)
        print(sentence)
        global politiciansIterator
        flag = False

        # Write into output
        jsonobject = {politiciansKeys[politiciansIterator]:{"entity_id":politiciansKeys[politiciansIterator], "triples":[], "sentence":sentence}}
        subject = politiciansDataFile[politiciansKeys[politiciansIterator]]['personLabel']
        for triple in req:
            predicate = triple.split(', ')[0]
            obj = triple.split(', ')[1]
            temp_dict = {'subject':'', 'predicate':'', 'object':''}
            if predicate != '' and obj != '':
                temp_dict['subject'] = subject
                temp_dict['predicate'] = predicate
                temp_dict['object'] = obj
                flag = True
            jsonobject[politiciansKeys[politiciansIterator]]['triples'].append(temp_dict)
        if flag:
            politiciansOutputFile.write('"'+ politiciansKeys[politiciansIterator] + '":')
            json.dump(jsonobject[politiciansKeys[politiciansIterator]], politiciansOutputFile)
            politiciansOutputFile.write(',\n')
        politiciansIterator += 1
        


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
        flag = False
        # Write into output
        jsonobject = {cricketersKeys[cricketersIterator]:{"entity_id":cricketersKeys[cricketersIterator], "triples":[], "sentence":sentence}}
        subject = cricketersDataFile[cricketersKeys[cricketersIterator]]['personLabel']
        for triple in req:
            predicate = triple.split(', ')[0]
            obj = triple.split(', ')[1]
            temp_dict = {'subject':'', 'predicate':'', 'object':''}
            if predicate != '' and obj != '':
                temp_dict['subject'] = subject
                temp_dict['predicate'] = predicate
                temp_dict['object'] = obj
                flag = True
            jsonobject[cricketersKeys[cricketersIterator]]['triples'].append(temp_dict)
        if flag:
            cricketersOutputFile.write('"'+ cricketersKeys[cricketersIterator] + '":')
            json.dump(jsonobject[cricketersKeys[cricketersIterator]], cricketersOutputFile)
            cricketersOutputFile.write(',\n')
        cricketersIterator += 1

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
        flag = False

        # Write into output
        jsonobject = {actorsKeys[actorsIterator]:{"entity_id":actorsKeys[actorsIterator], "triples":[], "sentence":sentence}}
        subject = actorsDataFile[actorsKeys[actorsIterator]]['personLabel']
        for triple in req:
            predicate = triple.split(', ')[0]
            obj = triple.split(', ')[1]
            temp_dict = {'subject':'', 'predicate':'', 'object':''}
            if predicate != '' and obj != '':
                temp_dict['subject'] = subject
                temp_dict['predicate'] = predicate
                temp_dict['object'] = obj
                flag = True
            jsonobject[actorsKeys[actorsIterator]]['triples'].append(temp_dict)
        if flag:
            actorsOutputFile.write('"'+ actorsKeys[actorsIterator] + '":')
            json.dump(jsonobject[actorsKeys[actorsIterator]], actorsOutputFile)
            actorsOutputFile.write(',\n')
        actorsIterator += 1

    return render_template("actors.html", title="actors", jsonfile=actorsDataFile, length = len(actorsDataFile.keys()), key=actorsKeys[actorsIterator], iterator = actorsIterator)


# TEST RESULTS

politiciansTestFile = open('Transformer Output/politicians_test.json', 'r')
politiciansResultsFile = open('Transformer Output/politicians_matches.json', 'r')
with open('Transformer Output/politicians_test.json', 'r') as politiciansTestFile:
    politiciansTestData = json.load(politiciansTestFile)
with open('Transformer Output/politicians_matches.json', 'r') as politiciansResultsFile:
    politiciansResultsData = json.load(politiciansResultsFile)

politiciansTestKeys = []
politiciansResultsKeys = []

for key in politiciansTestData.keys():
    politiciansTestKeys.append(key)

for key in politiciansResultsData.keys():
    politiciansResultsKeys.append(key)

politiciansResultsIterator = 0
@app.route("/politicians_results", methods=['GET', 'POST'])
def politiciansResults():
    if(request.method == 'POST'):
        global politiciansResultsIterator
        politiciansResultsIterator += 1
    return render_template("results.html", title = "politicians", testData = politiciansTestData, resultsData = politiciansResultsData, iterator = politiciansResultsIterator, testKey = politiciansTestKeys[politiciansResultsIterator])

cricketersTestFile = open('Transformer Output/cricketers_test.json', 'r')
cricketersResultsFile = open('Transformer Output/cricketers_matches.json', 'r')
with open('Transformer Output/cricketers_test.json', 'r') as cricketersTestFile:
    cricketersTestData = json.load(cricketersTestFile)
with open('Transformer Output/cricketers_matches.json', 'r') as cricketersResultsFile:
    cricketersResultsData = json.load(cricketersResultsFile)

cricketersTestKeys = []
cricketersResultsKeys = []

for key in cricketersTestData.keys():
    cricketersTestKeys.append(key)

for key in cricketersResultsData.keys():
    cricketersResultsKeys.append(key)

cricketersResultsIterator = 0
@app.route("/cricketers_results", methods=['GET', 'POST'])
def cricketersResults():
    if(request.method == 'POST'):
        global cricketersResultsIterator
        cricketersResultsIterator += 1
    return render_template("results.html", title = "cricketers", testData = cricketersTestData, resultsData = cricketersResultsData, iterator = cricketersResultsIterator, testKey = cricketersTestKeys[cricketersResultsIterator])

actorsTestFile = open('Transformer Output/actors_test.json', 'r')
actorsResultsFile = open('Transformer Output/actors_matches.json', 'r')
with open('Transformer Output/actors_test.json', 'r') as actorsTestFile:
    actorsTestData = json.load(actorsTestFile)
with open('Transformer Output/actors_matches.json', 'r') as actorsResultsFile:
    actorsResultsData = json.load(actorsResultsFile)

actorsTestKeys = []
actorsResultsKeys = []

for key in actorsTestData.keys():
    actorsTestKeys.append(key)

for key in actorsResultsData.keys():
    actorsResultsKeys.append(key)

actorsResultsIterator = 0
@app.route("/actors_results", methods=['GET', 'POST'])
def actorsResults():
    if(request.method == 'POST'):
        global actorsResultsIterator
        actorsResultsIterator += 1
    return render_template("results.html", title = "actors", testData = actorsTestData, resultsData = actorsResultsData, iterator = actorsResultsIterator, testKey = actorsTestKeys[actorsResultsIterator])

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")