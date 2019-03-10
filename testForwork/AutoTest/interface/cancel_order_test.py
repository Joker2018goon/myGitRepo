# author:joker
# cancel_order_test.py 取消订单

import requests
from unittest import TestCase

class CancelOrderTest(TestCase):
    '''取消订单操作类'''

    def setUp(self):
        self.result=''
        self.url='https://xxx.cn/pointOrder/order/cancel_order'

    def tearDown(self):
        print(self.result)

    def test_cancel_order_all_null(self):
        '''所有参数为空,以下皆为必填,这里不针对每一个参数判必填或非必填举例'''
        data={'orderNo':'','orgNo':'','merchantAccountId':'','userToken':''}
        response=requests.post(self.url,data=data)
        self.result=response.json()
        self.assertNotEqual(self.result['return_code'],200)
        self.assertNotEqual(self.result['return_msg'],'取消订单成功')

    def test_cancel_order_orderNo_invalid(self):
        '''orderNo预下单的订单号不存在'''
        data={'orderNo':'A034190307150116260','orgNo':'ALi','merchantAccountId':'FAFULI','userToken':'0fe45ef5a8a74a8bb6da6309966606e9'}
        response=requests.post(self.url,data=data)
        self.result=response.json()
        self.assertNotEqual(self.result['return_code'],200)
        self.assertNotEqual(self.result['return_msg'],'取消订单成功')

    def test_cancel_order_orgNo_invalid(self):
        '''orgNo机构号不存在'''
        data={'orderNo':'034190307150116260','orgNo':'0001','merchantAccountId':'FAFULI','userToken':'0fe45ef5a8a74a8bb6da6309966606e9'}
        response=requests.post(self.url,data=data)
        self.result=response.json()
        self.assertNotEqual(self.result['return_code'],200)
        self.assertNotEqual(self.result['return_msg'],'取消订单成功')

    def test_cancel_order_merchantAccountId_invalid(self):
        '''merchantAccountId商户授权账户ID，不存在'''
        data={'orderNo':'034190307150116260','orgNo':'ALi','merchantAccountId':'FA','userToken':'0fe45ef5a8a74a8bb6da6309966606e9'}
        response=requests.post(self.url,data=data)
        self.result=response.json()
        self.assertNotEqual(self.result['return_code'],200)
        self.assertNotEqual(self.result['return_msg'],'取消订单成功')

    def test_cancel_order_userToken_invalid(self):
        '''userToken用户token不存在'''
        data={'orderNo':'034190307150116260','orgNo':'ALi','merchantAccountId':'FA','userToken':'0fe45ef5a8a74a8bb6da6309966606e9#@'}
        response=requests.post(self.url,data=data)
        self.result=response.json()
        self.assertNotEqual(self.result['return_code'],200)
        self.assertNotEqual(self.result['return_msg'],'取消订单成功')

    def test_cancel_order_success(self):
        '''取消订单成功'''
        data={'orderNo':'034190307150116260','orgNo':'ALi','merchantAccountId':'FA','userToken':'0fe45ef5a8a74a8bb6da6309966606e9'}
        response=requests.post(self.url,data=data)
        self.result=response.json()
        self.assertEqual(self.result['return_code'],200)
        self.assertEqual(self.result['return_msg'],'取消订单成功')
