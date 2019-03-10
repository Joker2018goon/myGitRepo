# -*- coding:utf-8 -*-
from django.test import TestCase
from sign.models import Guest, Event
from django.contrib.auth.models import User


# Create your tests here.
class ModelTest(TestCase):
    def setUp(self):
        Event.objects.create(id=1, name='lufei', status=True, limit=2000, address='shanghai', start_time='2018-01-24')
        Guest.objects.create(id=1, event_id=1, realname='Jack', phone='13711010011', email='jack@mail.com', sign=False)

    def test_event_models(self):
        result = Event.objects.get(name='lufei')
        self.assertEqual(result.address, 'beijin')
        self.assertTrue(result.status)

    def test_guest_models(self):
        result = Guest.objects.get()
        self.assertEqual(result.realname, 'jack')
        self.assertFalse(result.sign)


class IndexTest(TestCase):
    # 测试index登录首页

    def test_index_page_renders_index_template(self):
        response = self.client.get('/index/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class LoginActionTest(TestCase):
    # 测试登录动作

    def setUp(self):
        User.objects.create_user('test', 'test@mail.com', 'test123qwer')

    def test_add_admin(self):
        # 测试添加用户
        user = User.objects.get(username='test')
        self.assertEqual(user.username, 'test', 'username error!')
        self.assertEqual(user.email, 'test@mail.com', 'email error!')

    def test_login_action_username_password_null(self):
        # '测试用户名密码为空
        test_data = {'username': '', 'password': ''}
        response = self.client.post('/login_action/', test_data)
        self.assertEqual(response.status_code, 200, 'username empty!')
        self.assertIn('username or password null!', response.content)

    def test_login_action_username_password_error(self):
        # 测试用户名和密码错误
        test_data = {'username': 'abc', 'password': 'abc123'}
        response = self.client.post('/login_action/', test_data)
        self.assertEqual(response.status_code, 200, 'username or password error!')
        self.assertIn('username or password error!', response.content)

    def test_login_action_success(self):
        # 测试登录成功
        test_data = {'username': 'test', 'password': 'test123qwer'}
        response = self.client.post('/login_action/', test_data)
        self.assertEqual(response.status_code, 302, 'login fail!')


class EventManageTest(TestCase):
    # 发布会管理
    def setUp(self):
        User.objects.create_user('test','test@mail.com','test123qwer')
        Event.objects.create(name='xiaomi5',limit=2000,address='beijing',status=1,start_time='2018-01-24 12:30:00')
        self.login_user={'username':'test','password':'test123qwer'}

    def test_event_manage_success(self):
        # 测试发布会：xiaomi5
        response=self.client.post('/login_action/',self.login_user)
        response=self.client.post('/event_manage/')
        self.assertEqual(response.status_code,200)
        self.assertIn('beijing',response.content)
        self.assertIn('xiaomi5',response.content)

    def test_event_manage_sreach_success(self):
        test_data={'name':'x'}
        response=self.client.post('/login_action/',self.login_user)
        response=self.client.post('/search_name/',test_data)
        self.assertEqual(response.status_code,200)
        self.assertIn('xiaomi5',response.content)
        self.assertIn('beijing',response.content)