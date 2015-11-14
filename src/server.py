#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ricveal
# @Date:   2015-11-13 14:39:22
# @Last Modified by:   ricveal
# @Last Modified time: 2015-11-14 11:59:20

from flask import Flask, jsonify, Response
from utilities import getCurrentTime
import dbConnector as db
from conditions import Conditions
from logger import setupLogger
import json, os

from datetime import datetime, timedelta
import threading, time


app = Flask(__name__)
LOG_LEVEL = "DEBUG"
log = setupLogger(LOG_LEVEL, "temperatureApp")

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
    log.error(error)
    return "Internal Error"

@app.errorhandler(404)
def pageNotFound(error):
    return "Page Not Found"

def check_db():
    if not os.path.isfile(db.FILE):
        log.debug("DB doesn't exist. Creating...")
        db.create_table()

def saveData():
    while(True):
        conditions = Conditions()
        current_conditions = { "fecha" : getCurrentTime(), "temperatura_int" : conditions.arduino['temp'], "temperatura_ext" : conditions.yahoo['temp'] }
        log.debug(current_conditions)
        db.insert_value(current_conditions['fecha'], current_conditions['temperatura_int'], current_conditions['temperatura_ext'])
        time.sleep(10)


def main():
    check_db()
    w = threading.Thread(target=saveData, name='SaveData Daemon')
    w.setDaemon(True)
    w.start()
    app.run()  

if __name__ == '__main__':
    main()