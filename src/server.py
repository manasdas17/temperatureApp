#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ricveal
# @Date:   2015-11-13 14:39:22
# @Last Modified by:   ricveal
# @Last Modified time: 2015-11-13 15:13:26

from flask import Flask, jsonify, Response
from utilities import getCurrentTime
import dbConnector as db
from conditions import Conditions
import json, os

from datetime import datetime, timedelta
import threading


app = Flask(__name__)

def OpenJSON(file):
    with open(file) as data_file:    
        return json.load(data_file)

@app.route('/api')
def show_data():
    data = db.get_last_values()
    info = "{'data':"
    for i in data:
        this_info = "{'fecha':'"+i.fecha+"', 'temp_int':'"+str(i.temp_int)+"', 'temp_ext':'"+str(i.temp_ext)+"'},"
        info = info + this_info
    info = info.rstrip(",") + "}"
    resp = Response(info, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://ricveal.com'
    return resp

@app.errorhandler(500)
def internal_error(error):
    print error
    return "Internal Error"

@app.errorhandler(404)
def pageNotFound(error):
    return "Page Not Found"

def saveData():
    conditions = Conditions()
    current_conditions = { "fecha" : getCurrentTime(), "temperatura_int" : conditions.arduino['temp'], "temperatura_ext" : conditions.yahoo['temp'] }
    print current_conditions

    db.insert_value(current_conditions['fecha'], current_conditions['temperatura_int'], current_conditions['temperatura_ext'])

    now = datetime.now()
    run_at = now + timedelta(minutes=2)
    delay = (run_at - now).total_seconds()
    threading.Timer(delay, saveData).start()

def main():
    app.run()
    saveData()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        os._exit()
      