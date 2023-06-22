# -*- coding: utf8 -*-
# @LastAuthor: TakanashiKoucha
# @Date: 2021-07-04 14:04:41
from flask import Flask, render_template
from flask_compress import Compress
from whitenoise import WhiteNoise

import kanaasobi as asobi

app = Flask(__name__)
app.wsgi_app = WhiteNoise(app.wsgi_app, root='static/')
Compress(app)

returnStr = ''


@app.route("/")
def hello():
    return render_template("hello.html", text="在网址后跟上参数即可，例如：/hira/10/5    意味着生成随机10个平假名，范围是五十音前5个<br />" + '''
    可使用参数：<br />
    /hira/X/X    生成平假名，首个X为生成个数，第二个X为生成范围，下同不做解释<br />
    /kata/X/X    生成片假名<br />
    /rooma/X/X    生成罗马字<br />
    /mix/X/X    生成平假名片假名混合<br />
    ''')


@app.route("/hira/<int:num1>/<int:num2>/")
def hira(num1, num2):
    returnStr = ''
    for i in asobi.hira(num1, num2):
        if str(i) == '○':
            pass
        else:
            returnStr = returnStr+"    "+str(i)
    return render_template("show.html", text=returnStr)


@app.route("/kata/<int:num1>/<int:num2>/")
def kata(num1, num2):
    returnStr = ''
    for i in asobi.kata(num1, num2):
        if str(i) == '○':
            pass
        else:
            returnStr = returnStr+"    "+str(i)
    return render_template("show.html", text=returnStr)


@app.route("/rooma/<int:num1>/<int:num2>/")
def rooma(num1, num2):
    returnStr = ''
    for i in asobi.rooma(num1, num2):
        if str(i) == '○':
            pass
        else:
            returnStr = returnStr+"    "+str(i)
    return render_template("show.html", text=returnStr)


@app.route("/mix/<int:num1>/<int:num2>/")
def mix(num1, num2):
    returnStr = ''
    for i in asobi.mix(num1, num2):
        if str(i) == '○':
            pass
        else:
            returnStr = returnStr+"    "+str(i)
    return render_template("show.html", text=returnStr)


if __name__ == "__main__":
    app.run()
