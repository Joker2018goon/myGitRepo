# -*- coding:utf-8 -*-
import unittest
import requests
import os, sys


# E:\pyWorkspace\pytest\interface\add_guest_test.py
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_fixture.test_data import InitData

class AddGuestTest(unittest.TestCase):
    def setUp(self):
        self.result=''
        self.url = 'http://127.0.0.1:9999/api/add_guest/'

    def tearDown(self):
        print(self.result)

    def test_add_guest_null(self):
        # 参数为空
        data = {'eid': '', 'realname': '', 'phone': '', 'email': ''}
        response = requests.post(self.url, data=data)
        self.result = response.json()
        self.assertEqual(self.result['status'], 10021)
        self.assertEqual(self.result['message'], 'parameter error')

    def test_add_guest_eid_null(self):
        # 发布会id不存在
        data = {'eid': 901, 'realname': 'post', 'phone': 12132323, 'email': 'post@mail.com'}
        response = requests.post(self.url, data=data)
        self.result = response.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], 'event id null')

    def test_add_guest_event_status_not_available(self):
        # 发布会当前状态为0--关闭
        data = {'eid': 3, 'realname': 'krea', 'phone': 121323333, 'email': 'post@mail.com'}
        response = requests.post(self.url, data=data)
        self.result = response.json()
        self.assertEqual(self.result['status'], 10023)
        self.assertEqual(self.result['message'], 'event status is not available')

    def test_add_guest_event_number_full(self):
        # 发布会限制人数已满
        data = {'eid': 2, 'realname': 'krea', 'phone': 121323333, 'email': 'post@mail.com'}
        response = requests.post(self.url, data=data)
        self.result = response.json()
        self.assertEqual(self.result['status'], 10024)
        self.assertEqual(self.result['message'], 'event number is full')

    def test_add_guest_event_started(self):
        # 发布会已经开始
        data = {'eid': 4, 'realname': 'krea', 'phone': 121323333, 'email': 'post@mail.com'}
        response = requests.post(self.url, data=data)
        self.result = response.json()
        self.assertEqual(self.result['status'], 10025)
        self.assertEqual(self.result['message'], 'event has started')

    def test_add_guest_phone_repeat(self):
        # 电话号码重复
        data ={'eid':5,'realname':'kk','phone':13511001100}
        response = requests.post(self.url, data=data)
        self.result = response.json()
        self.assertEqual(self.result['status'], 10026)
        self.assertEqual(self.result['message'], 'the event guest phone number repeat')

    def test_add_guest_success(self):
        # 添加成功
        data = {'eid': 5,'realname': 'krea', 'phone': 13511001103, 'email': 'krea@mail.com'}
        r = requests.post(self.url, data=data)
        '''
        print(r)
        print(r.url)
        print( r.raise_for_status())
        print(r.status_code)
        '''
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'add guest success')


if __name__ == '__main__':
    # 初始化接口测试数据
    init=InitData()
    init.init_data()
    unittest.main()