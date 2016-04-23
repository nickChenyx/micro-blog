# -*- coding: utf-8 -*-
from app import app
from flask import render_template,flash,redirect
from .forms import LoginForm
'''
# Demo1 测试路由拦截
@app.route('/')
@app.route('/index')
def index():
	return 'hello world'
'''


# Demo2 可以看到不使用模板template 输出是非常不整洁的
#@app.route('/')
#@app.route('/index')
#def index():
#    user = { 'nickname': 'Miguel' } # fake user
#    return '''
#<html>
#  <head>
#    <title>Home Page</title>
#  </head>
#  <body>
#    <h1>Hello, ''' + user['nickname'] + '''</h1>
#  </body>
#</html>
#'''

# Demo3 初识模板template
@app.route('/')
@app.route('/index')
def index():
	user = { 'nickname' : 'Chan'} #fake user
	#使用模板，title和user是要传入的数据 和html中的参数对应
	#在内部，render_template 调用了 Jinja2 模板引擎，
	#Jinja2 模板引擎是 Flask 框架的一部分。
	#Jinja2 会把模板参数提供的相应的值替换了 {{...}} 块。
	return render_template("index.html",title='Home',user=user)


# Demo4 模版中应用 if 控制语句
@app.route('/indexif')
def indexif():
	user = { 'nickname':'Chan' }
	#不传入title 后台会使用默认的title
	return render_template("indexif.html",user=user)

# Demo5 模板中应用 for 循环语句
@app.route('/indexfor')
def indexfor():
	user = { 'nickname': 'Miguel' } # fake user
	posts = [ # fake array of posts
	      	{
	            'author': { 'nickname': 'John' },
	            'body': 'Beautiful day in Portland!'
	        },
	        {
	            'author': { 'nickname': 'Susan' },
	            'body': 'The Avengers movie was so cool!'
	        }
	    ]
	return render_template("indexfor.html",
	        title = 'Home',
	        user = user,
	        posts = posts)

# Demo6 模板的继承 使用block定义模版中可插入的细节
@app.route('/indexbase')
def indexbase():
	user = { 'nickname': 'Miguel' } # fake user
	posts = [ # fake array of posts
	      	{
	            'author': { 'nickname': 'John' },
	            'body': 'this is extends from base.html !'
	        },
	        {
	            'author': { 'nickname': 'Susan' },
	            'body': 'what we say writes in block !'
	        }
	    ]
	return render_template("indexbase.html",
	        title = 'Home',
	        user = user,
	        posts = posts)

# Demo7 表单的使用
@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()

    '''
    validate_on_submit 方法做了所有表单处理工作。
    当表单正在展示给用户的时候调用它，它会返回 False.
	如果 validate_on_submit 在表单提交请求中被调用，
	它将会收集所有的数据，对字段进行验证，
	如果所有的事情都通过的话，它将会返回 True，
	表示数据都是合法的。这就是说明数据是安全的，并且被应用程序给接受了。
	如果至少一个字段验证失败的话，它将会返回 False，
	接着表单会重新呈现给用户，这也将给用户一次机会去修改错误。
	我们将会看到当验证失败后如何显示错误信息。
    '''
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data 
        	+ '", remember_me=' + str(form.remember_me.data))
        return redirect('/indexbase')
    return render_template('login.html',
        title = 'Sign In',
        form = form,
        providers = app.config['OPENID_PROVIDERS'])