# -*- coding:utf-8 -*-
from app import db
from hashlib import md5

class User(db.Model):
	id = db.Column(db.Integer,primary_key = True)
	nickname = db.Column(db.String(64),index = True,unique = True)
	email = db.Column(db.String(120),index = True,unique = True)
	posts = db.relationship('Post',backref='author',lazy='dynamic')
	about_me = db.Column(db.String(140))
	last_seen = db.Column(db.DateTime)
	'''
	值得注意的是我们已经在 User 类中添加一个新的字段称为 posts，
	它是被构建成一个 db.relationship 字段。这并不是一个实际的数据库字段，因此是不会出现在上面的图中。
	对于一个一对多的关系，db.relationship 字段通常是定义在“一”这一边。
	在这种关系下，我们得到一个 user.posts 成员，它给出一个用户所有的 blog。
	不用担心很多细节不知道什么意思，以后我们会不断地看到例子。
	'''

	def __repr__(self):
		return '<User %r>'%(self.nickname)

	#is_authenticated 方法有一个具有迷惑性的名称。
	#一般而言，这个方法应该只返回 True，
	#除非表示用户的对象因为某些原因不允许被认证。
	def is_authenticated(self):
		return True

	#is_active 方法应该返回 True，除非是用户是无效的，比如因为他们的账号是被禁止。
	def is_active(self):
		return True

	#is_anonymous 方法应该返回 True，除非是伪造的用户不允许登录系统。
	def is_anonymous(self):
		return False

	def get_id(self):
		try:
			return unicode(self.id) #python 2
		except NameError:
			return str(self.id) #python 3

	def avatar(self,size):
		return 'http://www.gravatar.com/avatar/'+md5(self.email).hexdigest()+'?d=mm&s='+str(size)

class Post(db.Model):
	id = db.Column(db.Integer,primary_key = True)
	body = db.Column(db.String(140))
	timestamp = db.Column(db.DateTime)
	user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

	def __repr__():
		return '<Post %r>' % (self.body)