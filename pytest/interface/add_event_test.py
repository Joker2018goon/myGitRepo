# -*- coding:utf-8 -*-
import unittest
import requests
import time
import os, sys


# D:\pyWorkspace\pytest\interface
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
import HTMLTestRunner
from db_fixture.test_data import InitData

class AddEventTest(unittest.TestCase):

    def setUp(self):
        self.result = ''
        self.base_url = 'http://127.0.0.1:9999/api/add_event/'

    def tearDown(self):
        print(self.result)

    def test_add_event_all_null(self):
        u'''所有参数全为空'''
        # 创建数据
        data = {'eid': '', 'name': '', 'limit': '', 'address': '', 'start_time': ''}
        response = requests.post(self.base_url, data=data)
        self.result = response.json()
        self.assertEqual(self.result['status'], 10021)
        self.assertEqual(self.result['message'], 'parametet error')

    def test_add_event_eid_exist(self):
        # id已经存在
        '''id已经存在'''
        data = {'eid': 15, 'name': '一加4发布会', 'limit': 2000, 'address': "深圳宝体", 'start_time': '2017'}
        response = requests.post(self.base_url, data=data)
        self.result = response.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], 'event id already exists')

    def test_add_event_name_exist(self):
        # 名字已经存在
        '''名字已经存在'''
        data = {'eid': 8, 'name': '红米Pro发布会', 'limit': 2000, 'address': "深圳宝体", 'start_time': '2018-02-22 14:00:00'}
        r = requests.post(self.base_url, data=data)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10023)
        self.assertEqual(self.result['message'], 'event name already exists')

    def test_add_event_date_type_error(self):
        # 日期格式错误
        '''日期格式错误'''
        data = {'eid': 6, 'name': '一加4手机发布会', 'limit': 2000, 'address': "深圳宝体", 'start_time': '2017'}
        r = requests.post(self.base_url, data=data)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10024)
        self.assertEqual(self.result['message'], 'start_time format error.It must be in YYYY-MM-DD HH:MM:SS format')

    def test_add_event_success(self):
        # 添加成功
        '''添加成功'''
        # data = {'eid': 6, 'name': '腾讯新闻发布会', 'limit': 2000, 'address': "深圳宝体", 'start_time': '2018-02-01 14:00:00'}
        data = {'eid': 6, 'name': '腾讯新闻发布会', 'limit': 2000, 'address': '深圳宝体', 'start_time': '2018-05-01 14:20:10'}
        r = requests.post(self.base_url, data=data)
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'add event success')


if __name__ == '__main__':
    # 初始化接口测试数据
    init=InitData()
    init.init_data()
    # unittest.main()
    # 构造测试集
    suite=unittest.TestSuite()
    suite.addTest(AddEventTest('test_add_event_all_null'))
    suite.addTest(AddEventTest('test_add_event_eid_exist'))
    suite.addTest(AddEventTest('test_add_event_name_exist'))
    suite.addTest(AddEventTest('test_add_event_date_type_error'))
    suite.addTest(AddEventTest('test_add_event_success'))
    # 执行用例
    # runner=unittest.TextTestRunner()
    # runner.run(suite)
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = './interface/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='guestDemo System Interface Test Report',
                                           description='Implementation Example with: ')
    runner.run(suite)
    fp.close()

