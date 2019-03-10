# -*- coding:utf-8 -*-
import sys
import time

now = time.strftime('%Y-%m-%d %H_%M_%S')
sys.path.append('../db_fixture')
try:
    from mysql_db import DB
except ImportError:
    from .mysql_db import DB

# create data
datas = {
    'sign_event': [
        {'id': 11, 'name': '红米Pro发布会', '`limit`': 2000, 'status': 1, 'address': '北京会展中心',
         'start_time': '2019-02-01 14:00:00','create_time':now},
        {'id': 12, 'name': '可参加人数为0', '`limit`': 0, 'status': 1, 'address': '北京会展中心',
         'start_time': '2019-08-20 14:00:00','create_time':now},
        {'id': 13, 'name': '当前状态为0关闭', '`limit`': 2000, 'status': 0, 'address': '北京会展中心',
         'start_time': '2019-08-20 14:00:00','create_time':now},
        {'id': 14, 'name': '发布会已结束', '`limit`': 2000, 'status': 1, 'address': '北京会展中心',
         'start_time': '2018-08-20 14:00:00','create_time':now},
        {'id': 15, 'name': '小米5发布会', '`limit`': 2000, 'status': 1, 'address': '北京国家会议中心',
         'start_time': '2019-02-01 14:00:00','create_time':now},
    ],
    'sign_guest': [
        {'id': 11, 'realname': 'alen', 'phone': 13511001100, 'email': 'alen@mail.com', 'sign': 0, 'create_time':now,'event_id': 12},
        {'id': 12, 'realname': 'has sign', 'phone': 13511001101, 'email': 'sign@mail.com', 'sign': 1, 'create_time':now,'event_id': 13},
        {'id': 13, 'realname': 'tom', 'phone': 13511001102, 'email': 'tom@mail.com', 'sign': 0, 'create_time':now,'event_id': 14},
    ],
}


# Inster table datas
class InitData:
    def __init__(self):
        self.db=DB()

    def init_data(self):
        for table, data in datas.items():
            self.db.clear(table)
            # print(data)
            for d in data:
                self.db.insert(table, d)
        self.db.close()


