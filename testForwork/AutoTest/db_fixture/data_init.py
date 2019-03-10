# author:joker
# 用作测试数据初始化

import sys
sys.path.append('../db_fixture')
try:
    from db_operation import DbOperation
except ImportError:
    from .db_operation import DbOperation


class DataInit:
    ''''数据初始化操作类'''
    def __init__(self):
        pass