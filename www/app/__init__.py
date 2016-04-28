# -*- coding: utf-8 -*-

'''
创建一个该类的实例，第一个参数是应用模块或者包的名称。 
如果你使用单一的模块（如本例），你应该使用 __name__ ，
因为模块的名称将会因其作为单独应用启动还是作为模块导入而有不同
（ 也即是 '__main__' 或实际的导入名）。
这是必须的，这样 Flask 才知道到哪去找模板、静态文件等等。
'''
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir,ADMINS,MAIL_SERVER,MAIL_PORT,MAIL_USERNAME,MAIL_PASSWORD
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)
lm.login_view='login'
#Flask-OpenID 扩展需要一个存储文件的临时文件夹的路径。
#对此，我们提供了一个 tmp 文件夹的路径。
oid = OpenID(app,os.path.join(basedir,'tmp'))

# 如果发生错误，向邮箱发送错误log
if not app.debug:
	import logging
	from logging.handlers import SMTPHandler
	credentials = None
	if MAIL_USERNAME or MAIL_PASSWORD:
		credentials = (MAIL_USERNAME,MAIL_PASSWORD)
	mail_handler = SMTPHandler((MAIL_SERVER,MAIL_PORT),'no-reply@' 
					+ MAIL_SERVER,ADMINS,'microblog failure',credentials)
	mail_handler.setLevel(logging.ERROR)
	app.logger.addHandler(mail_handler)

# 如果发生错误，向文件写入log
# 日志文件将会在 tmp 目录，名称为 microblog.log。
# 我们使用了 RotatingFileHandler 以至于生成的日志的大小是有限制的。
# 在这个例子中，我们的日志文件的大小限制在 1 兆，我们将保留最后 10 个日志文件作为备份。
if not app.debug:
	import logging
	from logging.handlers import RotatingFileHandler
	file_handler = RotatingFileHandler('tmp/microblog.log','a', 1 * 1024 * 1024, 10)
	file_handler.setFormatter(logging.Formatter(
		'%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
	app.logger.setLevel(logging.INFO)
	file_handler.setLevel(logging.INFO)
	app.logger.addHandler(file_handler)
	app.logger.info('microblog startup')

#app/views.py 文件中使用到了app.route 必须在app对象实例化之后导入
from app import views,models