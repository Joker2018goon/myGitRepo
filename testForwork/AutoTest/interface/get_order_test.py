# author:joker
# get_order_test.py 查询订单接口测试

import requests
from unittest import TestCase

class GetOrderTest(TestCase):
    '''查询订单接口测试类'''

    def setUp(self):
        self.result=''
        self.url='https://xxx.cn/pointOrder/order/get_order'

    def tearDown(self):
        print(self.result)

    def test_get_order_all_null(self):
        '''所有参数为空,以下皆为必填,这里不针对每一个参数判必填或非必填举例'''
        data={'orderNo':'','orgBNo':'','merchantAccountId':''}
        response=requests.post(self.url,data=data)
        self.result=response.json()
        self.assertNotEqual(self.result['return_code'],200)
        self.assertNotEqual(self.result['return_msg'],'查询订单')

    def test_get_order_orderNo_invalid(self):
        '''orderNo预下单的订单号不存在'''
        data={'orderNo':'A034190307150116260','orgBNo':'ALi','merchantAccountId':'FAFULI'}
        response=requests.post(self.url,data=data)
        self.result=response.json()
        self.assertNotEqual(self.result['return_code'],200)
        self.assertNotEqual(self.result['return_msg'],'查询订单')

    def test_get_order_orgNo_invalid(self):
        '''orgNo机构号不存在'''
        data={'orderNo':'034190307150116260','orgBNo':'001','merchantAccountId':'FAFULI'}
        response=requests.post(self.url,data=data)
        self.result=response.json()
        self.assertNotEqual(self.result['return_code'],200)
        self.assertNotEqual(self.result['return_msg'],'查询订单')

    def test_get_order_merchantAccountId_invalid(self):
        '''merchantAccountId不存在'''
        data={'orderNo':'034190307150116260','orgBNo':'ALi','merchantAccountId':'FA'}
        response=requests.post(self.url,data=data)
        self.result=response.json()
        self.assertNotEqual(self.result['return_code'],200)
        self.assertNotEqual(self.result['return_msg'],'查询订单')

    def test_get_order_success(self):
        '''查询订单成功'''
        data={'orderNo':'034190307150116260','orgBNo':'ALi','merchantAccountId':'FAFULI'}
        response=requests.post(self.result,data=data)
        self.result=response.json()
        self.assertEqual(self.result['return_code'],200)
        self.assertEqual(self.result['return_msg'],'查询订单')