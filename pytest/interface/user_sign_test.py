# -*- coding:utf-8 -*-
import requests
import unittest
import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_fixture.test_data import InitData

class userSignTest(unittest.TestCase):
    def setUp(self):
        self.result = ''
        self.url = 'http://127.0.0.1:9999/api/user_sign/'

    def tearDown(self):
        print(self.result)

    def test_user_sign_params_error(self):
        # 参数为空
        data = {'eid': '', 'phone': ''}
        r = requests.post(self.url, data=data)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10021)
        self.assertEqual(self.result['message'], 'parameter error')

    def test_user_sign_eid_empty(self):
        # 发布会id为空
        data = {'eid': 901, 'phone': 13511001100}
        r = requests.post(self.url, data=data)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], 'event id null')

    def test_user_sign_status_available(self):
        # 发布会状态非法
        data = {'eid': 3, 'phone': 13511001100}
        r = requests.post(self.url, data=data)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10023)
        self.assertEqual(self.result['message'], 'event status is not available')

    def test_user_sign_event_started(self):
        # 发布会已结束（开完了）
        data={'eid':4,'phone':13511001100}
        response=requests.post(self.url,data=data)
        self.result=response.json()
        self.assertEqual(self.result['status'],10024)
        self.assertEqual(self.result['message'],'event has started')

    def test_user_sign_phone_null(self):
        # phone=10100001111 手机号不存在
        data = {'eid': 5, 'phone': 10100001111}
        response = requests.post(self.url, data=data)
        self.result = response.json()
        self.assertEqual(self.result['status'], 10025)
        self.assertEqual(self.result['message'], 'user phone null')

    def test_user_sign_phone_not_participate(self):
        # eid=1, phone=13511001102 手机号与发布会不匹配
        data = {'eid': 1, 'phone': 13511001102}
        r = requests.post(self.url, data=data)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10026)
        self.assertEqual(self.result['message'], 'user did not participate in the conference')

    def test_user_sign_aleary_sign(self):
        # 已签到
        data = {'eid': 1, 'phone': 13511001101}
        r = requests.post(self.url, data=data)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10027)
        self.assertEqual(self.result['message'], 'user has sign in')

    def test_user_sign_success(self):
        # 签到成功
        data = {'eid': 5, 'phone': 13511001100}
        r = requests.post(self.url, data=data)
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'sign success')


if __name__ == '__main__':
    init=InitData()
    init.init_data()
    unittest.main()