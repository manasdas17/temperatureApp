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

	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	fh.setFormatter(formatter)
	ch.setFormatter(formatter)

	log.addHandler(fh)
	log.addHandler(ch)

	return log