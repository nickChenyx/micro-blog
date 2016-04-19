# -*- coding: utf-8 -*-

'''
创建一个该类的实例，第一个参数是应用模块或者包的名称。 
如果你使用单一的模块（如本例），你应该使用 __name__ ，
因为模块的名称将会因其作为单独应用启动还是作为模块导入而有不同
（ 也即是 '__main__' 或实际的导入名）。
这是必须的，这样 Flask 才知道到哪去找模板、静态文件等等。
'''
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')
#app/views.py 文件中使用到了app.route 必须在app对象实例化之后导入
from app import views