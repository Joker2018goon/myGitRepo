# -*- coding:utf-8 -*-
import requests
import unittest
import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_fixture.test_data import InitData

class getGuestListTest(unittest.TestCase):
    def setUp(self):
        self.result=''
        self.url='http://127.0.0.1:9999/api/get_guest_list/'

    def tearDown(self):
        print(self.result)

    def test_get_guest_list_eid_empty(self):
        # eid 为空
        data={'eid':''}
        response=requests.get(self.url,params=data)
        self.result=response.json()
        self.assertEqual(self.result['status'],10021)
        self.assertEqual(self.result['message'],'eid cannot be empty')

    def test_get_guest_list_result_empty(self):
        # 查询结果为空
        data={'eid':5,'phone':1311001100}
        response=requests.get(self.url,params=data)
        self.result=response.json()
        self.assertEqual(self.result['status'],10022)
        self.assertEqual(self.result['message'],'query result is empty')

    def test_get_guest_list_success(self):
        # 查询成功
        data={'eid':1,'phone':13511001101}
        response=requests.get(self.url,params=data)
        self.result=response.json()
        self.assertEqual(self.result['status'],200)
        self.assertEqual(self.result['message'],'success')
        self.assertEqual(self.result['data']['realname'],'has sign')
        self.assertEqual(self.result['data']['phone'],'13511001101')

if __name__ == '__main__':
    # 数据初始化
    init=InitData()
    init.init_data()
    unittest.main()