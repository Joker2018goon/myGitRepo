# -*- coding: utf-8 -*-
import unittest
import requests
import os,sys

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_fixture.test_data import InitData

class GetEventListTest(unittest.TestCase):
    # 发布会查询接口
    def setUp(self):
        self.result = ''
        self.url = 'http://127.0.0.1:9999/api/get_event_list/'

    def tearDown(self):
        print(self.result)

    def test_get_event_list_parameter_error(self):
        data = {'eid': '', 'name': ''}
        response = requests.get(self.url, params=data)
        self.result = response.json()
        self.assertEqual(self.result['status'], 10021)
        self.assertEqual(self.result['message'], 'parameter error')

    def test_get_event_list_result_empty(self):
        data = {'eid': 901, 'name': '米'}
        response = requests.get(self.url, params=data)
        self.result = response.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], 'query result is empty')

    def test_get_event_list_success(self):
        data = {'eid': 1, 'name': '米'}
        response = requests.get(self.url, params=data)
        self.result = response.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['data']['name'], '红米Pro发布会')


if __name__ == '__main__':
    # 初始化接口测试数据
    init=InitData()
    init.init_data()
    unittest.main()
