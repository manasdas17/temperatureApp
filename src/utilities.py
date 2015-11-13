#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ricveal
# @Date:   2015-11-13 14:25:06
# @Last Modified by:   ricveal
# @Last Modified time: 2015-11-13 14:36:55

from datetime import datetime

def f_to_c (f):
    c = (int(f)-32)/1.8
    return "{0:.2f}".format(round(c,2))

def getCurrentTime():
    currentMinute = datetime.now().minute
    currentHour = datetime.now().hour
    return str(currentHour) + ':' + str(currentMinute)