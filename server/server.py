# -w- coding: utf-8 -w-

from flask import Flask
from flask import request, render_template,logging
from utils.specialNum import fib
import logging
import xlwt
app = Flask(__name__)
# todo:生产模式时取消debugger

@app.route('/', methods=['GET', 'POST', 'DOC'])
def index():
    return render_template('index.html');


@app.route('/sys')
def sysHandler():
    with open('C:\Windows\system.ini', 'r', encoding='gbk') as f:
        b = f.read();
        print(f)
    return '<div>%s</div>' % b

@app.route('/excel',methods=['GET','POST'])
def excel():
    methods = []
    print(str(request.query_string)[1:])
    newFile = xlwt.Workbook()
    sheet = newFile.add_sheet('test',cell_overwrite_ok=True);
    sheet.write(0,0,'name')
    sheet.write(0,1,'company')
    sheet.write(0,2,'id')
    newFile.save('demo.xls')
    return '<h3>请求方式： %s</h3>' % methods;

@app.route('/calculate',methods=["POST"])
def calculate():
    response = []
    for i in request.values:
        print(i)
        response.append(i)
    return response

if __name__ == '__main__':
  app.run(port=8080, host='localhost');
