# author:joker
# test_pre_order.py 预下单

import requests
from unittest import TestCase,TestSuite,TextTestRunner


# 预下单
# 涉及到保密性，相关域名以及返回的code，用于拟造

class PreOrderTest(TestCase):
    '''测试预下单的接口测试类'''
    def setUp(self):
        self.result=''
        self.url='https://xxx.cn/pointOrder/order/pre_order' # 拟造假域名，涉及保密性

    def tearDown(self):
        print(self.result)

    def test_pre_order_requiredFields_null(self):
        '''所有必填参数都为空,以下皆为必填,这里不针对每一个参数判必填或非必填举例'''
        data={'orgNo':'','merchantAccountId':'','sign':''}
        response=requests.post(self.url,data=data)
        self.result=response.json()
        self.assertNotEqual(self.result['return_code'],200)
        self.assertNotEqual(self.result['return_msg'],'预下单成功')

    def test_pre_order_orgNo_wrong(self):
        '''机构号orgNo不存在'''
        data={'orgNo':'FA001','merchantAccountId':'FAFULI','sign':'0'}
        response=requests.post(self.url,data=data)
        self.result=response.json()
        self.assertNotEqual(self.result['return_code'],200)
        self.assertNotEqual(self.result['return_msg'],'预下单成功')

    def test_pre_order_accountId_wrong(self):
        '''商户授权账户ID，merchantAccountId不存在'''
        data={'orgNo':'ALi','merchantAccountId':'FA','sign':'0'}
        response=requests.post(self.url,data=data)
        self.result=response.json()
        self.assertNotEqual(self.result['return_code'],200)
        self.assertNotEqual(self.result['return_msg'],'预下单成功')

    def test_pre_order_sign_wrong(self):
        '''签名sign不存在'''
        data={'orgNo':'ALi','merchantAccountId':'FAFULI','sign':'1'}
        response=requests.post(self.url,data=data)
        self.result=response.json()
        self.assertNotEqual(self.result['return_code'],200)
        self.assertNotEqual(self.result['return_msg'],'预下单成功')

    def test_pre_order_success(self):
        '''预下单成功'''
        data={'orgNo':'ALi','merchantAccountId':'FAFULI','sign':'0'}
        response=requests.post(self.url,data=data)
        self.result=response.json()
        self.assertEqual(self.result['return_code'],200)
        self.assertEqual(self.result['return_msg'],'预下单成功')
    
if __name__ == "__main__":
    suit=TestSuite()
    suit.addTest(PreOrderTest('test_pre_order_requiredFields_null'))
    suit.addTest(PreOrderTest('test_pre_order_orgNo_wrong'))
    suit.addTest(PreOrderTest('test_pre_order_accountId_wrong'))
    suit.addTest(PreOrderTest('test_pre_order_sign_wrong'))
    suit.addTest(PreOrderTest('test_pre_order_success'))
    runner=TextTestRunner()
    runner.run(suit)