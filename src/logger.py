#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ricveal
# @Date:   2015-11-14 11:48:03
# @Last Modified by:   ricveal
# @Last Modified time: 2015-11-14 13:24:16

import logging


def setupLogger(level, name):
    log = logging.Logger(name)
    log.setLevel(level)

    # fileHandler
    fh = logging.FileHandler('debug.log')
    fh.setLevel(logging.DEBUG)

    # consoleHandler
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    log.addHandler(fh)
    log.addHandler(ch)

    return log
