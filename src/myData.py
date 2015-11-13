#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ricveal
# @Date:   2015-11-13 13:34:24
# @Last Modified by:   ricveal
# @Last Modified time: 2015-11-13 13:34:33

class MyData(object):
    def __init__(self, arg):
        super(MyData, self).__init__()
        self.fecha = str(arg[0])
        self.temp_int = float(arg[1])
        self.temp_ext = float(arg[2])