import string
import random
import pymysql

db = pymysql.connect("xxx.xx.xx", "root", "root",
                     "fesco_adecco_prd")


def operate_db(sql_str):
    # 打开数据库连接

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute(sql_str)
    db.commit()
    # 使用 fetchone() 方法获取单条数据
    # data = cursor.fetchone() # 查询出一条
    # data= cursor.fetchall() # 查询出所有数据

def create_data():
    for i in range(0, 999):
        id=''.join([random.choice(string.ascii_letters+string.digits) for _ in range(0,32)])
        # print(id)
        sql_str = f"INSERT INTO fesco_adecco_prd.ps_account_stream (id, stream_no, ps_account_id, point, balance, point_class_code, source_class, source_param, source_desc, state, start_dt, end_dt, version, valid, deleted, create_dt, update_dt, create_by, update_by, batch_no) VALUES ('{id}', 'YCW', '4c762df92ae147eab7080c43edbecece', '1.0000', '1.0000', '0001', 'recharge', 'A203493', NULL, '0', NULL, NULL, '0', '1', '0', '2019-02-26 14:40:00', NULL, '-1', NULL, NULL)"
        operate_db(sql_str)

    # 关闭数据库连接
    db.close()

def clear_data():
    sql_str = f"DELETE FROM ps_account_stream WHERE stream_no='YCW'"
    operate_db(sql_str)

    # 关闭数据库连接
    db.close()

def main():
    # id='185cb424d7744670867c196c129a4c0'+str(0)
    # print(type(id))
    # sql_str = f"INSERT INTO fesco_adecco_prd.ps_account_stream (id, stream_no, ps_account_id, point, balance, point_class_code, source_class, source_param, source_desc, state, start_dt, end_dt, version, valid, deleted, create_dt, update_dt, create_by, update_by, batch_no) VALUES ('{id}', 'YCW', '6082b0f649f34617a1d21bebdb4ce86f', '1.0000', '1.0000', '0001', 'recharge', 'A203493', NULL, '0', NULL, NULL, '0', '1', '0', '2019-01-21 16:50:29', NULL, '-1', NULL, NULL)"
    # operate_db(sql_str)

    create_data()
    # clear_data()

if __name__ == "__main__":
    main()