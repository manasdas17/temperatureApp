#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ricveal
# @Date:   2015-11-13 14:39:22
# @Last Modified by:   ricveal
# @Last Modified time: 2015-11-14 17:47:15

from flask import Flask, jsonify, Response, make_response, request, current_app, render_template
from functools import update_wrapper
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


def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/api')
@crossdomain(origin='*')
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
