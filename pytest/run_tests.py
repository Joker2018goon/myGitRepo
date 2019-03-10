# -*- coding:utf-8 -*-
import time, sys

sys.path.append('./interface')
sys.path.append('./db_fixture')
import HTMLTestRunner
import unittest
from db_fixture.test_data import InitData

# 指定测试用例为当前文件下的interface目录
test_dir = './interface'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')

if __name__ == '__main__':
    # 初始化接口测试数据
    init=InitData()
    init.init_data()
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = './report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='guestDemo System Interface Test Report',
                                           description='Implementation Example with: ')
    runner.run(discover)
    fp.close()
