# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import url_for
from translate import translate_ms

app = Flask(__name__)

@app.route('/translate/<lang_from>/<lang_to>/<sentence>')
def returnTrans(lang_from, lang_to, sentence):
    return translate_ms(sentence, lang_from, lang_to) #return json

@app.route('/translate', methods=['POST'])
def returnTrans():
    if request.method == 'POST':
        from_lang = request.form['from_lang']
        to_lang = request.form['to_lang']
        string = request.form['string']

    return translate_ms(string, from_lang, to_lang)

if __name__ == '__main__':
    app.run(debug=True)
