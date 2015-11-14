#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ricveal
# @Date:   2015-09-19 13:26:02
# @Last Modified by:   ricveal
# @Last Modified time: 2015-11-14 13:23:33

import sqlite3
import os
from myData import MyData

FILE = 'temperature.db'


def run_query(query=''):

    conn = sqlite3.connect(FILE)  # Conectar a la base de datos
    with conn:
        cursor = conn.cursor()         # Crear un cursor
        cursor.execute(query)          # Ejecutar una consulta

    if query.upper().startswith('SELECT'):
        data = cursor.fetchall()   # Traer los resultados de un select
    else:
        conn.commit()              # Hacer efectiva la escritura de datos
        data = None

    cursor.close()                 # Cerrar el cursor
    conn.close()                   # Cerrar la conexion

    return data


def create_table():
    query = "CREATE TABLE temperature (date text, temp_int integer, temp_ext integer)"
    run_query(query)


def insert_value(date, temp_int, temp_ext):
    query = '''INSERT INTO temperature (date, temp_int, temp_ext) VALUES ("%s", "%d", "%d")''' % (
        date, float(temp_int), float(temp_ext))
    run_query(query)


def get_last_values():
    query = "SELECT * FROM temperature"
    data = run_query(query)

    limit_data = 0 if (len(data) - 30 * 24) < 0 else (len(data) - 30 * 24)

    allData = []

    for x in xrange(limit_data, len(data)):
        d = data[x]
        my_data = MyData(d)
        allData.append(my_data)
    return allData
