#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ricveal
# @Date:   2015-11-13 14:39:22
# @Last Modified by:   ricveal
# @Last Modified time: 2015-11-14 13:22:27

from flask import Flask, jsonify, Response
from setproctitle import setproctitle
from utilities import getCurrentTime
import dbConnector as db
from conditions import Conditions
from logger import setupLogger
import json
import os

from datetime import datetime, timedelta
import threading
import time

APP_NAME = "temperatureApp"

setproctitle(APP_NAME)

app = Flask(__name__)
LOG_LEVEL = "DEBUG"
log = setupLogger(LOG_LEVEL, APP_NAME)


def OpenJSON(file):
    with open(file) as data_file:
        return json.load(data_file)


@app.route('/api')
def show_data():
    data = db.get_last_values()
    d = []
    for i in data:
        d.append(
            {'fecha': i.fecha, 'temps': {'int': i.temp_int, 'ext': i.temp_ext}})
    info = json.dumps(dict(data=d))
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
        current_conditions = {"fecha": getCurrentTime(), "temperatura_int": conditions.arduino[
            'temp'], "temperatura_ext": conditions.yahoo['temp']}
        log.debug(current_conditions)
        db.insert_value(current_conditions['fecha'], current_conditions[
                        'temperatura_int'], current_conditions['temperatura_ext'])
        time.sleep(2 * 60)


def main():
    check_db()
    w = threading.Thread(target=saveData, name='SaveData Daemon')
    w.setDaemon(True)
    w.start()
    app.run()

if __name__ == '__main__':
    main()
