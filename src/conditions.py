#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ricveal
# @Date:   2015-11-13 14:15:20
# @Last Modified by:   ricveal
# @Last Modified time: 2015-11-14 13:23:40

from bs4 import BeautifulSoup
import requests

from infoTiempo import InfoTiempo
from arduinoData import ArduinoData
from utilities import getCurrentTime

import json


class Conditions(object):

    """docstring for Conditions"""

    def __init__(self):
        super(Conditions, self).__init__()
        self.config = self.importConf()
        self.yahoo = self.getYahooConditions()
        self.arduino = self.getArduinoConditions()

    def obtain_yahoo_url(self, code):
        yahoo_url = "http://query.yahooapis.com/v1/public/yql?q=select%20item%20from%20weather.forecast%20where%20location%3D%22" + \
            code + "%22&format=json"
        return yahoo_url

    def getArduinoConditions(self):

        url = self.config['url_arduino']
        req = requests.get(url)

        statusCode = req.status_code
        if statusCode == 200:

            weather_json = req.json()

            arduino_data = ArduinoData(weather_json)

            condiciones_actuales = {"fecha": getCurrentTime(
            ), "temp": arduino_data.temperatura, "hum": arduino_data.humedad}

            return condiciones_actuales

        else:
            print "Status Code %d" % statusCode

    def getYahooCode(self):

        config = self.config

        url = config['url_yahoo']
        term = config['term']

        req = requests.get(url + term)

        statusCode = req.status_code
        if statusCode == 200:

            html = BeautifulSoup(req.text, 'html5lib')

            dd = html.find_all('dd')
            dt = html.find_all('dt')

            codes = {}
            new_codes = {}

            for i in range(len(dt)):
                codes[dd[i].getText()] = dt[i].getText()

            for k in codes:
                if ', ' + config['country'] in k:
                    new_codes[k] = codes[k]

            codes = new_codes

            code = codes.itervalues().next()

            config['code'] = code

            self.saveConf(config)

            return code

        else:
            print "Status Code %d" % statusCode

    def getYahooConditions(self):
        code = self.config['code'] if len(
            self.config['code']) > 0 else self.getYahooCode()
        yahoo_url = self.obtain_yahoo_url(code)
        req = requests.get(yahoo_url)

        statusCode = req.status_code
        if statusCode == 200:

            weather_json = req.json()

            tiempo = InfoTiempo(weather_json)

            condiciones_actuales = {
                "fecha": getCurrentTime(), "temp": tiempo.condiciones_actuales.temp}

            return condiciones_actuales

        else:
            print "Status Code %d" % statusCode

    def importConf(self):
        with open('../config.json') as json_data_file:
            data = json.load(json_data_file)
        return data['config']

    def saveConf(self, conf):
        data = {}
        data['config'] = conf
        with open('../config.json', 'w') as outfile:
            json.dump(data, outfile)
