# author=joker

import os, sys
import configparser
from pymysql import connect, cursors

# d:\Documents and Settings\yanchunwei\桌面\testForwork\AutoTest
current_dir = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
target_dir = current_dir + '/db_config.ini'
target_dir = target_dir.replace('\\', '/')
cf = configparser.ConfigParser()
cf.read(target_dir)

host = cf.get('mysqlconf', 'host')
port = cf.get('mysqlconf', 'port')
db = cf.get('mysqlconf', 'db_name')
user = cf.get('mysqlconf', 'user')
password = cf.get('mysqlconf', 'password')

# data使用固定格式
# data={key:value}  key- column_name, value-column_value
# 举例：
'''
{'id': 12, 'name': 'xxx', '`limit`': 0, 'status': 1, 'address': 'yyyy'}
'''


class DbOperation:
    '''数据库操作类,将数据作为变量或者将sql作为变量'''

    def __init__(self):
        '''初始化'''
        try:
            self.conn = connect(
                host=host, port=int(port), user=user, password=password, db=db)
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(e)

    def insert_data(self, table_name, data):
        '''插入数据，data使用固定格式'''
        for key in data:
            data[key] = "'" + str(data[key]) + "'"
        key = ','.join(data.keys())
        value = ','.join(data.values())
        insert_sql = "INSERT INTO " + table_name + "(" + key + ") VALUES (" + value + ")"
        self.cursor.execute(insert_sql)
        self.conn.commit()

    def clear_data(self,table_name):
        '''删除操作'''
        clear_sql="DELETE FROM "+table_name+";"
        self.cursor.execute(clear_sql)
        self.conn.commit()

    def modify_data(self,table_name,column,column_value):
        '''更新操作'''
        pass

    def query_data(self):
        '''查询数据'''
        pass

    def sql_operate(self, sql_str):
        '''直接使用sql去执行操作数据库'''
        self.cursor.execute(sql_str)
        self.conn.commit()


def main():
    data = {
        'id': 7,
        'name': '红米Pro发布会',
        '`limit`': 2000,
        'status': 1,
        'address': '北京会展中心',
        'start_time': '2019-02-01 14:00:00',
        'create_time': '2019-02-01 14:00:00'
    }
    sql="select * from sign_event;"
    db = DbOperation()
    # db.insert_data('sign_event', data)
    db.sql_operate(sql)
    query_response=db.cursor.fetchall()
    print(query_response)


if __name__ == "__main__":
    main()