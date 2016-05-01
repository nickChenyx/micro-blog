# -*- coding:utf-8 -*-
from app import db
from hashlib import md5

#创建用户关注表

followers = db.Table('followers',
	db.Column('follower_id',db.Integer,db.ForeignKey('user.id')),
	db.Column('followed_id',db.Integer,db.ForeignKey('user.id'))
)

class User(db.Model):
	id = db.Column(db.Integer,primary_key = True)
	nickname = db.Column(db.String(64),index = True,unique = True)
	email = db.Column(db.String(120),index = True,unique = True)
	posts = db.relationship('Post',backref='author',lazy='dynamic')
	about_me = db.Column(db.String(140))
	last_seen = db.Column(db.DateTime)
	followed = db.relationship('User',
		secondary = followers,
		primaryjoin = (followers.c.follower_id == id),
		secondaryjoin = (followers.c.followed_id == id),
		backref = db.backref('followers',lazy = 'dynamic'),
		lazy = 'dynamic')
	'''
	posts :
	值得注意的是我们已经在 User 类中添加一个新的字段称为 posts，
	它是被构建成一个 db.relationship 字段。这并不是一个实际的数据库字段，因此是不会出现在上面的图中。
	对于一个一对多的关系，db.relationship 字段通常是定义在“一”这一边。
	在这种关系下，我们得到一个 user.posts 成员，它给出一个用户所有的 blog。
	不用担心很多细节不知道什么意思，以后我们会不断地看到例子。

	followed :
	‘User’ 是这种关系中的右边的表(实体)(左边的表/实体是父类)。因为定义一个自我指向的关系，我们在两边使用同样的类。
	secondary 指明了用于这种关系的辅助表。
	primaryjoin 表示辅助表中连接左边实体(发起关注的用户)的条件。注意因为 followers 表不是一个模式，获得字段名的语法有些怪异。
	secondaryjoin 表示辅助表中连接右边实体(被关注的用户)的条件。
	backref 定义这种关系将如何从右边实体进行访问。当我们做出一个名为 followed 的查询的时候，将会返回所有跟左边实体联系的右边的用户。当我们做出一个名为 followers 的查询的时候，将会返回一个所有跟右边联系的左边的用户。lazy 指明了查询的模式。dynamic 模式表示直到有特定的请求才会运行查询，这是对性能有很好的考虑。
	lazy 是与 backref 中的同样名称的参数作用是类似的，但是这个是应用于常规查询。


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


	# 关注和取消关注
	def follow(self,user):
		if not self.is_following(user):
			self.followed.append(user)
			return self

	def unfollow(self,user):
		if self.is_following(user):
			self.followed.remove(user)
			return self

	def is_following(self,user):
		return self.followed.filter(followers.c.followed_id == user.id).count()>0


	def followed_posts(self):
		return Post.query.join(followers,(followers.c.followed_id == Post.user_id)).filter(
			followers.c.follower_id == self.id).order_by(Post.timestamp.desc())

	@staticmethod
	def make_unique_nickname(nickname):
		if User.query.filter_by(nickname=nickname).first() == None:
			return nickname
		version = 2
		while True:
			new_nickname = nickname + str(version)
			if User.query.filter_by(nickname = new_nickname).first() == None:
				break
			version += 1
		return new_nickname

class Post(db.Model):
	id = db.Column(db.Integer,primary_key = True)
	body = db.Column(db.String(140))
	timestamp = db.Column(db.DateTime)
	user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

	def __repr__():
		return '<Post %r>' % (self.body)

