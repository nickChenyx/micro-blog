#Micro-Blog 

###基于Python的Flask框架的个人博客系统，实现自Miguel Grinberg的[The Flask Mega-Tutorial](http://www.pythondoc.com/flask-mega-tutorial/index.html)

----


**还未完成，简单写一写现有的入口：**
- 部署于腾讯云服务器，URL—— `http://119.29.176.190:5000/`
- `/index`是默认跳转的页面
- `/login`是登录页，利用的是`OpenID`，现有的接口里面似乎只有`YaHoo`的接口能用，`Google`似乎已经停止对`OpenID`的支持。所以可以用`YaHoo`的账号来登陆。
- `/indexbase`是登陆之后的展示页
- `/user/<username>`是用户的信息展示页
- .....

*Easy-Way:*  
- [http://119.29.176.190:5000/](http://119.29.176.190:5000/)
- [http://119.29.176.190:5000/index](http://119.29.176.190:5000/index)
- [http://119.29.176.190:5000/login](http://119.29.176.190:5000/login)
- [http://119.29.176.190:5000/user/nickChen](http://119.29.176.190:5000/nickChen)