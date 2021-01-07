"""
log.py : Create log file for current session.
"""

import logging


filelogger = logging.getLogger()
filelogger.setLevel(logging.DEBUG)

switch_log_levels = {
    'debug' : filelogger.debug,
    'info' : filelogger.info,
    'warning' : filelogger.warning,
    'error' : filelogger.error,
    'critical' : filelogger.critical 
}

def logsetup(logfile):
    global filelogger

    logFormatStr = "[%(asctime)s %(threadName)s, %(levelname)s] %(message)s"
    consoleFormatStr = "[%(threadName)s, %(levelname)s] %(message)s"

    # log file handler
    logFormatter = logging.Formatter(logFormatStr)
    fileHandler = logging.FileHandler(logfile)
    fileHandler.setFormatter(logFormatter)
    filelogger.addHandler(fileHandler)

    # Stream handler for stdout, stderror
    consoleFormatter = logging.Formatter(consoleFormatStr)
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(consoleFormatter)
    filelogger.addHandler(consoleHandler)

def logevent(string, level='debug', print_screen=False, remove_newlines=False):

    if remove_newlines:
        string = string.replace('\r', '').replace('\n', ' ')

    if print_screen:
        switch_log_levels[level](string)

    switch_log_levels[level](string)
