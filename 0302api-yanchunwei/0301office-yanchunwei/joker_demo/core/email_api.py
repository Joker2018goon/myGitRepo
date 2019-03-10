# -*- coding:utf-8 -*-
# email_api.py 邮件接口
# author：joker


# 根据输入内容选择发送整月或整年的数据
# 直接将数据以正文形式发送？
# 数据以附件形式发送？

import re
import pickle
import os
import sys
dir_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir_path)
from core.memo_admin import MemoAdmin
from utils.path_manage import PathManage
from utils.email_util import MailMaster
from utils.log_util import Logger

mylog=Logger(__name__).getlog()
# 关闭日志
# mylog.disable(logging.DEBUG)

class EmailApi:
    '''邮件interface'''
    def __init__(self):
        pass

    def send_email(self,to_addr,user,year,month=None):
        '''邮件接口，筛选某用户整年或整月备忘录数据邮件给对应用户,month不填是整年'''
        ret={'staus':0,'message':'success','data':{}}
        flag=True

        if not re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$',to_addr):
            ret['staus']=1
            ret['message']=f'{to_addr} email format wrong'
            flag=False
            mylog.error(ret['message'])

        with open(PathManage.db_path('users.pkl'), 'rb') as f:
            users_dict = pickle.load(f)
            users_list=users_dict.keys()

        if not user in users_list:
            ret['staus']=2
            ret['message']='user not exists'
            flag=False
            mylog.error(ret['message'])

        if not re.match(r'\d{4}',year):
            ret['staus']=2
            ret['message']=f'{year} wrong,please input Four-digit year!'
            flag=False
            mylog.error(ret['message'])

        if month:
            if re.match(r'\d{1,2}',month):
                if int(month) not in range(1,13):
                    ret['staus']=4
                    ret['message']=f'{month} wrong,month must in [1,12]!'
                    flag=False
                    mylog.error(ret['message'])
            else:
                ret['staus']=3
                ret['message']=f'{month} wrong,please input two-digit month!'
                flag=False
                mylog.error(ret['message'])


        if flag:
            memoAdmin=MemoAdmin(user)
            memo_list=memoAdmin.memo_list
            target_list=[]
            subject=''
            for memo in memo_list:
                # print(memo)
                if memo['date']:
                    memo_date_year=memo['date'].split('-')[0]
                    memo_date_year=int(memo_date_year)
                    memo_date_month=memo['date'].split('-')[1]
                    memo_date_month=int(memo_date_month)
                    # print(memo_date_moth)
                    if month:
                        if memo_date_month==int(month) and memo_date_year==int(year):
                            target_list.append(memo)
                            # print(target_list)
                            subject=f'{year}年{month}月份备忘录数据'
                    else:
                        if memo_date_year==int(year):
                            target_list.append(memo)
                            subject=f'{year}年备忘录数据'
                            # print(target_list)
            print(target_list)
            ret['data']=target_list
            data=','.join('%s' %data for data in target_list)
            mail_master=MailMaster()
            mail_master.add_email_to_list(to_addr)
            mail_master.notice(user,data,subject)
            mylog.info('email success.result:%d'%(ret['data']))

        return ret

