#-w- coding: utf-8 -w-

from flask import Flask
from flask import request,render_template
from utils.specialNum import fib
import logging

app = Flask(__name__)
# todo:生产模式时取消debugger
app.debug = True
a = fib(10)
@app.route('/',methods = ['GET','POST','DOC'])
def index():
    return render_template('index.html');


@app.route('/fib')
def fibHandler():
    for i in a:
        if i > 30:
            b = i
            break;
    return '<h3>number is %s</h3>' % b

app.run(port = 8080,host = 'localhost');
