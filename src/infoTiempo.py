#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ricveal
# @Date:   2015-11-13 14:13:01
# @Last Modified by:   ricveal
# @Last Modified time: 2015-11-14 13:23:45

from tiempo import Tiempo


class InfoTiempo(object):

    """Clase prevision for prevision"""

    def __init__(self, weather_json):
        super(InfoTiempo, self).__init__()
        prevision_json = weather_json['query']['results']['channel']['item']
        self.condiciones_actuales = Tiempo(prevision_json['condition'])
        condiciones_futuras = []
        for prevision in prevision_json['forecast']:
            estado_tiempo = Tiempo(prevision)
            condiciones_futuras.append(estado_tiempo)
        self.condiones_futuras = condiciones_futuras
