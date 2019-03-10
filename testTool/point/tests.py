from django.test import TestCase

# Create your tests here.
import time
import random
import threading
import requests
import json
import pymysql

url = 'https://xxx.com/pointPlatformOrder/sync'
headers = {'Content-Type': 'application/json'}


def craet_order_status():
    '''随机获取一个合法的订单状态'''
    orderStatus_list=['待支付','待发货','已发货','已完成','已取消','已关闭','已退款']
    index_random=random.randint(0,6)
    orderStatus=orderStatus_list[index_random]
    return orderStatus

def creat_main_order(n,order_count=100):
    '''拟造主-子订单数据'''
    main_orders_type={'HC0201901211100':'O2O订单','HC0201901211101':'主订单','HC0201901211102':'兑换订单','HC0201901211103':'实物','HC0201901211104':'常规订单','HC0201901211105':'流量','HC0201901211106':'生活缴费','HC0201901211107':'电影票','HC0201901211108':'视频卡','HC0201901211109':'话费'}
    # n=random.randint(0,9)
    orderType=list(main_orders_type.items())[n][1]
    orderNo=list(main_orders_type.items())[n][0]
    orderStatus=craet_order_status()
    print(f'生成的主订单号:{orderNo}')
    json_main_order={
            "orderType": orderType,
            "orderNo": orderNo,
            "parentOrderNo": "",
            "orderCreateDt": "2019-01-02 14:58:00",
            "orderTitle": "京东超市",
            "productNum": 1,
            "productMarketPrice": 12,
            "productSalePrice": 15,
            "orderProductPrice": 15,
            "orderSettlePrice": 15,
            "orderFreight": 3,
            "orderAmount": 18,
            "orderSettleTotalPrice": 18,
            "accountNo": "8763562t",
            "accountToken": "65f165a41511472a8b9eb6e0112e6189",
            "orderStatus": orderStatus,
            "receiverName": "胡",
            "receiverMobile": "18056082679",
            "receiverAddress": "上海浦西",
            "expressName": "韵达",
            "expressNo": "1234565",
            "supplier": "秒核"
        }
    jsond,order_list=craet_order_data(order_count)
    for json_item in jsond:
        json_item['parentOrderNo']=orderNo
    jsond.insert(0,json_main_order)
    return jsond,order_list


def craet_order_data(order_count=100):
    '''拟造子订单数据'''
    jsond=[]
    order_list=[]
    for _ in range(0,order_count):
        int_list=[]
        for _ in range(0,14):
            n=random.randint(0,9)
            int_list.append(str(n))
        orderNo='2019'+''.join(int_list)
        order_list.append(orderNo)
        orderStatus=craet_order_status()
        json_item={
            "orderType": "子订单",
            "orderNo": orderNo,
            "parentOrderNo": "",
            "orderCreateDt": "2019-01-02 14:58:00",
            "orderTitle": "京东超市",
            "productNum": 1,
            "productMarketPrice": 12,
            "productSalePrice": 15,
            "orderProductPrice": 15,
            "orderSettlePrice": 15,
            "orderFreight": 3,
            "orderAmount": 18,
            "orderSettleTotalPrice": 18,
            "accountNo": "8763562t",
            "accountToken": "65f165a41511472a8b9eb6e0112e6189",
            "orderStatus": orderStatus,
            "receiverName": "胡",
            "receiverMobile": "18056082679",
            "receiverAddress": "上海浦西",
            "expressName": "韵达",
            "expressNo": "1234565",
            "supplier": "秒核"
        }
        jsond.append(json_item)
    return jsond,order_list

def test_api(m,jsond):
    print(f'批次号:{m}')
    channelCode=['51point','mall']
    index_random=random.randint(0,1)
    data = {
        "batchNo": m,
        "channelCode": channelCode[index_random],
        "access_token": "6488215a-4e37-4480-88db-18d744aca198"
    }
    # jsond=craet_order_data(order_count)
    jsond = json.dumps(jsond)
    r = requests.request(
        "POST", url, headers=headers, params=data, data=jsond.encode('utf-8'))

    print(r.text)

def thread_test_diffent_orders(m,order_count=100,thread_count=50):
    '''每个线程（批次号）订单号没有一个相同的'''
    threads = []
    batchNo_list=[]
    order_all_list=[]
    for i in range(0, thread_count):
        jsond,order_list=creat_main_order(i,order_count)
        t = threading.Thread(target=test_api(m,jsond))
        print(f'批次号{m}生成的订单:{order_list}')
        threads.append(t)
        batchNo_list.append(str(m))
        order_all_list.append(order_list)
        m+=1
        

    for i in range(0, thread_count):
        threads[i].start()
        print(f'线程{i}启动时间:{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}')
        
    for i in range(0, thread_count):
        threads[i].join()

    return order_all_list

def thread_test_same_orders(m,jsond,thread_count=50):
    '''每个线程（批次号）拉同一批订单'''
    threads = []
    batchNo_list=[]
    for i in range(0, thread_count):
        t = threading.Thread(target=test_api(m,jsond))
        threads.append(t)
        batchNo_list.append(str(m))
        m+=1

    for i in range(0, thread_count):
        threads[i].start()
        print(f'线程{i}启动时间:{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}')
        
    for i in range(0, thread_count):
        threads[i].join()

    # print(f'生成的批次号:{batchNo_list}')


def get_data_fromdb(sql_str):
    # 打开数据库连接
    db = pymysql.connect("xxx.xx.xx","root","root","fesco_adecco_prd" )
    
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    
    # 使用 execute()  方法执行 SQL 查询 
    cursor.execute(sql_str)
    
    # 使用 fetchone() 方法获取单条数据.
    # data = cursor.fetchone() # 查询出一条
    data= cursor.fetchall() # 查询出所有数据
    
    # print (f"Database return : 一共查询到{len(data)}条数据,具体:{data}" )
    
    # 关闭数据库连接
    db.close()
    return data

def main():
    ticks = time.time()
    m=int(ticks)
    # order_main=[{
    #         "orderType": "实物",
    #         "orderNo": "HC0201901211103",
    #         "parentOrderNo": "",
    #         "orderCreateDt": "2019-01-02 14:58:00",
    #         "orderTitle": "京东超市",
    #         "productNum": 1,
    #         "productMarketPrice": 12,
    #         "productSalePrice": 15,
    #         "orderProductPrice": 15,
    #         "orderSettlePrice": 15,
    #         "orderFreight": 3,
    #         "orderAmount": 18,
    #         "orderSettleTotalPrice": 18,
    #         "accountNo": "8763562t",
    #         "accountToken": "65f165a41511472a8b9eb6e0112e6189",
    #         "orderStatus": "已发货",
    #         "receiverName": "胡",
    #         "receiverMobile": "18056082679",
    #         "receiverAddress": "上海浦西",
    #         "expressName": "韵达",
    #         "expressNo": "1234565",
    #         "supplier": "秒核-1"
    #     },{
    #         "orderType": "子订单",
    #         "orderNo": "211946468385844700",
    #         "parentOrderNo": "HC0201901181449",
    #         "orderCreateDt": "2019-01-02 14:58:00",
    #         "orderTitle": "京东超市",
    #         "productNum": 1,
    #         "productMarketPrice": 12,
    #         "productSalePrice": 15,
    #         "orderProductPrice": 15,
    #         "orderSettlePrice": 15,
    #         "orderFreight": 3,
    #         "orderAmount": 18,
    #         "orderSettleTotalPrice": 18,
    #         "accountNo": "8763562t",
    #         "accountToken": "65f165a41511472a8b9eb6e0112e6189",
    #         "orderStatus": "已退款",
    #         "receiverName": "胡",
    #         "receiverMobile": "18056082679",
    #         "receiverAddress": "上海浦西",
    #         "expressName": "韵达",
    #         "expressNo": "1234565",
    #         "supplier": "秒核"
    #     }]

    # 测试单条数据验证功能或者查看字段
    # test_api(m,order_main)
    # db_data=get_data_fromdb(f'select * from ps_merchant_order_sync WHERE batch_no="{m}"')
    # db_data_log=get_data_fromdb(f'select * from ps_merchant_order_sync_log WHERE batch_no="{m}"')
    # print(f'从ps_merchant_order_sync表一共查询到{len(db_data)}条数据,具体如下'.center(100,'*'))
    # print(f'从ps_merchant_order_sync表查询到的数据:{db_data}')
    # print(f'从ps_merchant_order_sync_log表一共查询到{len(db_data_log)}条数据,具体如下'.center(100,'*'))
    # print(f'从ps_merchant_order_sync_log表查询到的数据:{db_data_log}')


    
    # # 用于压测
    exist_orders=[]
    miss_orders=[]

    # # 每个线程（批次号）拉同一批订单
    # # jsond,order_list=craet_order_data(10)
    # # print(f'批次号{m}生成的订单:{order_list}')
    # # thread_test_same_orders(m,jsond,50)
    # # for order_no in order_list:
    # #     db_data1=get_data_fromdb(f"select * from ps_merchant_order_sync WHERE order_no='{order_no}'")
    # #     db_data2=get_data_fromdb(f"select * from ps_merchant_order_sync WHERE order_no='{order_no}'")
    # #     if db_data1:
    # #         exist_orders.append(order_no)
    # #     elif db_data2:
    # #         exist_orders.append(order_no)
    # #     else:
    # #         miss_orders.append(order_no)




    
    # 每个线程（批次号）订单号没有一个相同的
    order_all_list=thread_test_diffent_orders(m,100,10)
    time.sleep(15)

    for orderlist in order_all_list:
        for order_no in orderlist:
            # print(f'order_no的数据类型：{type(order_no)},值：{order_no}')
            db_data=get_data_fromdb(f"select * from ps_merchant_order_sync WHERE order_no='{order_no}'")
            # time.sleep(5)
            if db_data:
                exist_orders.append(order_no)
            else:
                miss_orders.append(order_no)


    # 数据处理,将入库和丢失的order栓选出来
    print(f'一共有{len(exist_orders)}条记录存入库,具体如下'.center(100,'-'))
    print(f'存入库的orders:{exist_orders}')
    print(f'一共有{len(miss_orders)}条记录丢失,具体如下'.center(100,'-'))
    print(f'丢失的orders:{miss_orders}')



if __name__ == "__main__":
    main()