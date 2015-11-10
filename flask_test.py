# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os
import io
import uuid
import hashlib
from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import url_for
from flask import send_file
from flask import send_from_directory
from werkzeug import secure_filename
from translate import translate_ms
from translate import getList

UPLOAD_FOLDER = './static/image'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/translate/<lang_from>/<lang_to>/<sentence>')
def returnTrans(lang_from, lang_to, sentence):
    return translate_ms(sentence, lang_from, lang_to) #return json

@app.route('/translate', methods=['POST'])
def returnTrans():
    if request.method == 'POST':
        from_lang = request.form['from_lang']
        to_lang = request.form['to_lang']
        string = request.form['string']
        
        img = request.files['img']
        imgName = secure_filename(img.filename)
        imgDBname = hashlib.sha1(str(uuid.uuid4())).hexdigest()
        img.save(os.path.join(app.config['UPLOAD_FOLDER'], imgDBname))

    return translate_ms(string, from_lang, to_lang, imgName, imgDBname)

@app.route('/show')
def showData():
    for data in getList():
        print data[0]
        
    return render_template('template.html', data_list = getList())

@app.route('/img/<filename>/<original>/<result>')
def showImg(filename, original, result):
    return render_template('img.html', name = filename, original = original, result = result)

if __name__ == '__main__':
    app.run(debug=True)
