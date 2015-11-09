#-*- coding: utf-8 -*-

from mstranslator import Translator
from dateTime import getCurrentDate
from dateTime import getCurrentTime

import sys
import goslate
import json
import MySQLdb
reload(sys)
sys.setdefaultencoding('utf-8')

CLIENT_ID = "translatelate"
CLIENT_SECRET = "GK7MyfCoz1NUrNuehRZBlLWLNpHMgDaAZoT8MkQOMlI="
translator_ms = Translator(CLIENT_ID, CLIENT_SECRET)

languages = ["af", "sq", "ar","be", "bg", "ca", "zh-CN", "zh-TW", "hr",
             "cs", "da", "nl", "en", "et", "tl", "fi", "fr", "gl", "de",
             "el", "iw", "hi", "hu", "is", "id", "ga", "it", "ja", "ko",
             "lv", "lt", "mk", "ms", "mt", "no", "fa", "pl", "pt", "ro",
             "ru", "sr", "sk", "sl", "es", "sw", "sv", "th", "tr", "uk",
             "vi", "cy", "yi"]

def validateLanguage(lang):
    if lang in languages:
        return True
    return False

def saveData(host, user, passwd, db, result, original, file_name, file_name_sha1, tableName):
    dBase = MySQLdb.connect(host, user, passwd, db, charset='utf8', use_unicode=True)
    cursor = dBase.cursor()

    string_1 = 'insert into %s(result, original, date, time, file_name, file_name_sha1) ' % (tableName)
    string_2 = 'values("%s", "%s", "%s", "%s", "%s", "%s")' % (result, original, getCurrentDate(), getCurrentTime(),
    file_name, file_name_sha1)

    cursor.execute("use " + db)
    cursor.execute(string_1 + string_2)
    dBase.commit()

    cursor.close()
    dBase.close()

def translate_ms(mstr, lang_from, lang_to, file_name, file_name_sha1):
    result = translator_ms.translate(mstr, lang_from, lang_to)
    result_str = str(result)
    forReturn = {"result":result_str,
                 "original":mstr}

    saveData('localhost', 'root', '0000', 'python_test', result_str, mstr, file_name, file_name_sha1, 'test')
    
    return json.dumps(forReturn, ensure_ascii=False)

def getList(host = 'localhost', user = 'root', passwd = '0000', db = 'python_test'):
    dBase = MySQLdb.connect(host, user, passwd, db, charset='utf8', use_unicode=True)
    cursor = dBase.cursor()
    
    query = "SELECT * FROM test"
    cursor.execute(query)

    _list = cursor.fetchall()

    cursor.close()
    dBase.close()

    return _list
