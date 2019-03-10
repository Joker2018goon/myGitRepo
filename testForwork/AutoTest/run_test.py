# author:joker
# run_test.py 统一启动所有的测试类

import os, sys
import time

sys.path.append('./interface')
sys.path.append('./db_fixture')

from unittest import defaultTestLoader
import HTMLTestRunner

test_dir = './interface'
discover = defaultTestLoader.discover(test_dir, pattern='*_test.py')

if __name__ == "__main__":
    report_time = time.strftime('%Y-%m-%d %H_%M_%S')
    file_name = './report/' + report_time + '_result.html'
    f = open(file_name, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=f,
        title='order test report',
        description='Implementation Example with: ')
    runner.run(discover)
    f.close()