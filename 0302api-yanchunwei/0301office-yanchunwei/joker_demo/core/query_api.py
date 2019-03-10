# -*- coding:utf-8 -*-
# query_aoi.py 查询接口
# author: joker

# 作业需求点：
# 增加查询接口
# 根据月份返回json数据
# 扩充一点：user体现登录权限，实际中可能会校验user_token

import pickle
import sys
import os
dir_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir_path)
from core.memo_admin import MemoAdmin
from utils.path_manage import PathManage
from utils.log_util import Logger

mylog=Logger(__name__).getlog()
# 关闭日志功能
# mylog.disable(logging.DEBUG)

class QueryApi:
    '''interface'''
    def __init__(self):
        pass

    def query_memo(self,from_month,to_month,user='admin'):
        '''根据月份查询备忘录记录'''
        ret={'staus':0,'message':'success','data':{}}
        flag=True

        if isinstance(from_month,int):
            if not from_month in range(1,13):
                ret['staus']=2
                ret['message']='from_month not in [1,12]'
                flag=False
                mylog.error(ret['message'])
        else:
            ret['staus']=3
            ret['message']='from_month data type error'
            flag=False
            mylog.error(ret['message'])
            
        if isinstance(to_month,int):
            if not to_month in range(1,13):
                ret['staus']=2
                ret['message']='to_month not in [1,12]'
                flag=False
                mylog.error(ret['message'])
        else:
            ret['staus']=3
            ret['message']='to_month data type error'
            flag=False
            mylog.error(ret['message'])

        if from_month>to_month:
            ret['staus']=4
            ret['message']='from_month should not greater than to_month'
            flag=False
            mylog.error(ret['message'])

        with open(PathManage.db_path('users.pkl'), 'rb') as f:
            users_dict = pickle.load(f)
            users_list=users_dict.keys()

        if not user in users_list:
            ret['staus']=1
            ret['message']='user not exists'
            flag=False
            mylog.error(ret['message'])

        if flag:
            memoAdmin=MemoAdmin(user)
            memo_list=memoAdmin.memo_list
            target_list=[]
            for memo in memo_list:
                # print(memo)
                if memo['date']:
                    memo_date_month=memo['date'].split('-')[1]
                    memo_date_month=int(memo_date_month)
                    # print(memo_date_moth)
                    if memo_date_month>=from_month and memo_date_month<=to_month:
                        target_list.append(memo)
                        # print(target_list)
            ret['data']=target_list
            mylog.info('query success.result:%s'%(ret['data']))

        return ret

def main():
    query_api=QueryApi()
    query_api.query_memo(6,10,'joker')

if __name__ == '__main__':
    main()