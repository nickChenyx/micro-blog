# -*- coding:utf-8 -*-
import os
import unittest

from config import basedir
from app import app, db
from app.models import User


'''
TestCase 类中含有我们的测试。setUp 和 tearDown 方法是特别的，它们分别在测试之前以及测试之后运行。

在上面代码中 setUp 和 tearDown 方法十分普通。在 setUp 中做了一些配置，在 tearDown 中重置数据库内容。

测试实现成了方法。一个测试支持运行应用程序的多个函数，并且有已知的结果以及应该断言结果是否不同于预期的。

目前为止在测试框架中有两个测试。第一个就是验证 Gravatar 的头像 URL生成是否正确。注意测试中期待的结果是硬编码，验证 User 类的返回的头像 URL。

第二个就是我们前面编写的 make_unique_nickname 方法，同样是在 User 类中。
'''
class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_avatar(self):
        u = User(nickname='john', email='john@example.com')
        avatar = u.avatar(128)
        expected = 'http://www.gravatar.com/avatar/d4c74594d841139328695756648b6bd6'
        assert avatar[0:len(expected)] == expected

    def test_make_unique_nickname(self):
        u = User(nickname='john', email='john@example.com')
        db.session.add(u)
        db.session.commit()
        nickname = User.make_unique_nickname('john')
        assert nickname != 'john'
        u = User(nickname=nickname, email='susan@example.com')
        db.session.add(u)
        db.session.commit()
        nickname2 = User.make_unique_nickname('john')
        assert nickname2 != 'john'
        assert nickname2 != nickname

if __name__ == '__main__':
    unittest.main()