# -*- coding:utf-8 -*-
# log_util.py 改编de8ug的代码
# log的工程应用
# author: joker
import os
import sys
dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir_path)

import logging
import time
from utils.path_manage import PathManage
"""
工程使用需求：
1-不同日志名称
2-打印同时在控制台，也有文件
3-灵活控制等级

# 使用logger.XX来记录错误,这里的"error"可以根据所需要的级别进行修改
try:
    open('/path/to/does/not/exist', 'rb')
except (SystemExit, KeyboardInterrupt):
    raise
except Exception, e:
    logger.error('Failed to open file', exc_info=True)


如果需要将日志不上报错误，仅记录，可以将exc_info=False，

"""


class Logger:
    '''定义log类'''

    def __init__(self, log_file='Joker', logger='Joker-Log'):
        '''指定保存日志的文件路径，日志级别，以及调用文件,日志存入到指定的文件中'''
        # logging.basicConfig(filemode='a', datefmt='%a, %d %b %Y %H:%M:%S')
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.INFO)

        # 添加时间戳
        rq = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        if log_file:
            log_file = log_file + '-' + rq + '.log'
        else:
            log_file = rq + '.log'

        # 这里进行判断，如果logger.handlers列表为空，则添加，否则，直接去写日志
        if not self.logger.handlers:
            log_file=PathManage.log_path(log_file)
            # 创建文件 handler
            fh = logging.FileHandler(filename=log_file, encoding='utf-8')
            fh.setLevel(logging.INFO)

            # 创建控制台 handler
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)

            # 创建 formatter
            formatter = logging.Formatter(
                '%(asctime)s [%(levelname)s] %(name)s {%(filename)s line:%(lineno)d}  ->>>>> %(message)s'
            )
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)

            # 把 ch， fh 添加到 logger
            self.logger.addHandler(fh)
            self.logger.addHandler(ch)
            # print(self.logger.handlers, '================')

    def getlog(self):
        '''获得日志对象'''
        return self.logger

    @staticmethod
    def closeLog(level=logging.DEBUG):
        '''关闭log'''
        # print('================')
        # print(type(logging.DEBUG))
        # print('================')
        logging.disable(level)

def main():
    # 测试
    logger = Logger('test').getlog()
    Logger.closeLog()
    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')


if __name__ == '__main__':
    main()
