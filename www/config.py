# -*- coding: utf-8 -*-

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir,'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True

#Flaks-WTF 扩展只需要两个配置。 
#CSRF_ENABLED 配置是为了激活 跨站点请求伪造 保护。
#在大多数情况下，你需要激活该配置使得你的应用程序更安全些。
CSRF_ENABLED = True
#SECRET_KEY 配置仅仅当 CSRF 激活的时候才需要，
#它是用来建立一个加密的令牌，用于验证一个表单。
#当你编写自己的应用程序的时候，请务必设置很难被猜测到密钥。
SECRET_KEY   = 'unable-to-decode-pwd'
#定义一个 OpenID 提供者的列表。
OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]


# mail server settings
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None

# administrator list
ADMINS = ['chenyxup@163.com']