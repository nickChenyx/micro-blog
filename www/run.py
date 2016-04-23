# -*- coding: utf-8 -*-
#!flask/bin/python
from app import app #从app文件夹中得到实例化的app
from sys import argv
#通过命令行传值
#f,h,p = argv
#print h,p
#app.run(host=h,port=int(p),debug=True)
app.run(debug = True)
#app.run(host='127.0.0.1' port=5000 debug=True)