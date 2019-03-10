# author:joker
# pay_order_test.py 正式下单

import requests
from unittest import TestCase

class PayOrderTest(TestCase):
    '''支付订单'''
    def setUp(self):
        self.result=''
        self.url='https://xxx.cn/pointOrder/order/pay_order' # 拟造假域名，涉及保密性

    def tearDown(self):
        print(self.result)

    def test_pay_order_requiredFields_null(self):
        '''所有必填参数都为空,这里不针对每一个参数判必填或非必填举例'''
        data={'orderScene':'','payMethod':'','orderNo':'','orderPoint':'','orderCash':''}
        response=requests.post(self.url,data=data)
        self.result=response.json()
        self.assertNotEqual(self.result['return_code'],200)
        self.assertNotEqual(self.result['return_msg'],'支付订单成功')

    def test_pay_order_orderScene_invalid(self):
        '''orderScene下单场景，PC;WECHAT,不符合枚举值'''
        data={'orderScene':'11','payMethod':'全积分支付','orderNo':'034190307150116260','orderPoint':'219','orderCash':'81'}
        response=requests.post(self.url)
        self.result=response.json()
        self.assertNotEqual(self.result['return_code'],200)
        self.assertEqual(self.result['return_msg'],'支付订单成功')

    def test_pay_order_payMethod_invalid(self):
        '''payMethod支付方式,全积分支付；全支付宝支付；全微信支付；积分+支付宝；积分+微信'''
        data={'orderScene':'PC','payMethod':'000','orderNo':'034190307150116260','orderPoint':'219','orderCash':'81'}
        response=requests.post(self.url,data=data)
        self.result=response.json()
        self.assertNotEqual(self.result['return_code'],200)
        self.assertNotEqual(self.result['return_msg'],'支付订单成功')

    def test_pay_order_orderNo_notExist(self):
        '''orderNo不存在'''
        data={'orderScene':'PC','payMethod':'全积分支付','orderNo':'9001','orderPoint':'219','orderCash':'81'}
        response=requests.post(self.url,data=data)
        self.result=response.json()
        self.assertNotEqual(self.result['return_code'],200)
        self.assertNotEqual(self.result['return_msg'],'支付订单成功')
    
    def test_pay_order_orderPoint_invalid(self):
        '''orderPoint支付积分非数字类型'''
        data={'orderScene':'PC','payMethod':'全积分支付','orderNo':'034190307150116260','orderPoint':'219','orderCash':'81'}
        response=requests.post(self.url,data=data)
        self.result=response.json()
        self.assertNotEqual(self.result['return_code'],200)
        self.assertNotEqual(self.result['return_msg'],'支付订单成功')

    def test_pay_order_orderCash_invalid(self):
        '''orderCash支付现金非数字类型'''
        data={'orderScene':'PC','payMethod':'全积分支付','orderNo':'034190307150116260','orderPoint':'219','orderCash':'81'}
        response=requests.post(self.url,data=data)
        self.result=response.json()
        self.assertNotEqual(self.result['return_code'],200)
        self.assertNotEqual(self.result['return_msg'],'支付订单成功')

    def test_pay_order_success(self):
        '''支付订单成功'''
        data={'orderScene':'PC','payMethod':'全积分支付','orderNo':'034190307150116260','orderPoint':'219','orderCash':'81'}
        response=requests.post(self.url,data=data)
        self.result=response.json()
        self.assertEqual(self.result['return_code'],200)
        self.assertEqual(self.result['return_msg'],'支付订单成功')

