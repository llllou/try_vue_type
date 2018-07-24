# -w- coding: utf-8 -w-

from flask import Flask
from flask import request, render_template
from utils.specialNum import fib
from io import StringIO
import time
import logging
app = Flask(__name__)
# todo:生产模式时取消debugger
app.debug = True
a = fib(10)


@app.route('/', methods=['GET', 'POST', 'DOC'])
def index():
    return render_template('index.html');


@app.route('/fib')
def fibHandler():
    for i in a:
        if i > 30:
            b = i
            break;
    return '<h3>time:%a \n number is %s</h3>' % (time.asctime(time.time()), b)

@app.route('/sys')
def sysHandler():
    with open('C:\Windows\system.ini', 'r', encoding='gbk') as f:
        b = f.read();
        print(b)
    return '<div>%a</div>' % b

if __name__ == '__main__':
  app.run(port=8080, host='localhost');
