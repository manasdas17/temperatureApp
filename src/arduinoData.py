#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ricveal
# @Date:   2015-11-13 14:19:09
# @Last Modified by:   ricveal
# @Last Modified time: 2015-11-14 13:23:23


class ArduinoData(object):

    """Objeto con la informacion obtenida de Arduino"""

    def __init__(self, arg):
        super(ArduinoData, self).__init__()
        self.humedad = arg['humidity']
        self.temperatura = arg['temperature']
