# -*- coding: utf-8 -*- 
from flask.ext.wtf import Form
from wtforms import StringField,BooleanField
from wtforms.validators import DataRequired

# Form这个参数一开始不知道为什么 是自动生成吗？ 
# LoginForm(object)传递的参数变成了这个
class LoginForm(Form):
	openid = StringField('openid',validators=[DataRequired()])
	remember_me = BooleanField('remember_me',default=False)    