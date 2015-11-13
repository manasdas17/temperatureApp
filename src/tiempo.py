#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ricveal
# @Date:   2015-11-13 14:12:06
# @Last Modified by:   ricveal
# @Last Modified time: 2015-11-13 14:25:38

from utilities import f_to_c

class Tiempo(object):
    """Modelización tiempo"""
    def __init__(self, tiempo_json):
        super(Tiempo, self).__init__()
        self.text = tiempo_json['text']
        if 'temp' in tiempo_json:
            self.temp = f_to_c(tiempo_json['temp'])
            self.is_current = True
        else:
            self.temp_max = f_to_c(tiempo_json['high'])
            self.temp_min = f_to_c(tiempo_json['low'])
            self.date = tiempo_json['date']
            self.is_current = False