#-*- coding: utf-8 -*-

import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def getCurrentDate():
    now = time.localtime()
    date = "%04d.%02d.%02d" % (now.tm_year, now.tm_mon, now.tm_mday)
    return date

def getCurrentTime():
    now = time.localtime()
    t = "%02d:%02d:%02d" % (now.tm_hour, now.tm_min, now.tm_sec)
    return t
