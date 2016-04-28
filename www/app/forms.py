# -*- coding: utf-8 -*- 
from flask.ext.wtf import Form
from wtforms import StringField,BooleanField,TextAreaField
#DataRequired 验证器只是简单地检查相应域提交的数据是否是空。
from wtforms.validators import DataRequired,Length

# Form这个参数一开始不知道为什么 是自动生成吗？ 
# LoginForm(object)传递的参数变成了这个
class LoginForm(Form):
	openid = StringField('openid',validators=[DataRequired()])
	remember_me = BooleanField('remember_me',default=False)    

class EditForm(Form):
	nickname = StringField('nickname',validators=[DataRequired()])
	about_me = TextAreaField('about_me',validators=[Length(min=0,max=140)])

	def __init__(self, original_nickname, *arg, **kwargs):
		Form.__init__(self,*arg,**kwargs)
		self.original_nickname = original_nickname

    # 检查是否新定义的名字是否重名
	def validate(self):
		if not Form.validate(self):
			return False
		if self.nickname.data == self.original_nickname:
			return True
		user = User.query.filter_by(nickname=self.nickname.data).first()
		if  user != None:
			self.nickname.errors.append('This nickname is already in use. Please choose another one')
			return False
		return True