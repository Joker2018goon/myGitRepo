# -*- coding:utf-8 -*-
# author: joker
# login_page.py 登录页面

# 绘制用户登录界面
# 用户输入用户名和密码
# 从user.json 里拿数据校验，授权登录权限（后台数据处理）
# 登录失败可能 1.密码或用户名输入错误，即忘记密码，后续可以实现通过用户名找回密码 2.未注册，模拟跳转到注册页面

import os
import sys
dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir_path)
import re
import json
import pickle
import msvcrt
from functools import wraps
from utils.path_manage import PathManage
from core.register_page import Register
from utils import color_me
from utils.log_util import Logger
from utils.image_util import DirUtil

mylog=Logger(__name__).getlog()
# 关闭日志功能
# mylog.disable(logging.DEBUG)

class Login:
    '''登录等一系列操作'''

    def __init__(self):
        '''初始化'''
        self.dirob=DirUtil()
        data={
            'username': 'admin',
            'password': 'admin',
            'type': "admin",
            'operation': ['权限管理','crawler', 'office', 'image']
        }
        with open(PathManage.db_path('admin.json'),'w',encoding='utf-8') as f:
            json.dump(data,f,ensure_ascii=False,indent=4)
        

    def __call__(self,func):
        '''对象调用'''
        @wraps(func)
        def wrapper(*args,**kw):
            print('欢迎来到51备忘录登录页面'.center(100, '*'))
            username = input('用户名:')
            password = self.input_pw('密码:')
            # password=input('密码:')
            try:
                users=self.get_users()
                if username in users:
                    with open(PathManage.db_path(f'{username}.json'),'r',encoding='utf-8') as f:
                        data=f.read()
                        data=json.loads(data)
                    if data['password']==password:
                        user_session=[]
                        user=data['username']
                        user_session.append(user)
                        if data['type']=='user':
                            if data['enabled']==1:
                                # 当做session用了
                                self.set_user_session(user_session,'session.pkl')
                                func(*args,**kw)
                            else:
                                print('你已被拉黑，请联系管理员！')
                        else:
                            # 当做session用了
                            self.set_user_session(user_session,'session.pkl')
                            func(*args,**kw)
                    else:
                        print('密码错误')
                        exit()
                else:
                    print('用户不存在，请注册！')
                    reg = Register()
                    reg.register_user()
            except Exception as e:
                mylog.error(e)
        return wrapper

    def set_user_session(self,data,db_file_name):
        '''用于保存当前的user值传到下一个页面'''
        with open(PathManage.db_path(db_file_name), 'wb') as f:
            pickle.dump(data, f, 0)

    def get_users(self):
        '''通过文件名获取所有用户名'''
        try:
            da_path=os.path.join(dir_path,'db')
            self.dirob.get_allfiles(da_path)
            allfiles=self.dirob.file_list
            users=[]
            for file in allfiles:
                if file.endswith('.json'):
                    filename=re.findall(r'[^\\]+$', file)
                    filename=''.join(filename)
                    username=filename.split('.')[0]
                    users.append(username)
            return users
        except Exception as e:
            mylog.error(e)
    

    def input_pw(self, markedWords):
        '''实现控制台密码星号输入,借鉴网上代码'''
        print(markedWords, end='', flush=True)
        li = []
        while 1:
            ch = msvcrt.getch()
            # 回车
            if ch == b'\r':
                msvcrt.putch(b'\n')
                # print('输入的密码是：%s' % b''.join(li).decode())
                return b''.join(li).decode()
            # 退格
            elif ch == b'\x08':
                if li:
                    li.pop()
                    msvcrt.putch(b'\b')
                    msvcrt.putch(b' ')
                    msvcrt.putch(b'\b')
            # Esc
            elif ch == b'\x1b':
                break
            else:
                li.append(ch)
                msvcrt.putch(b'*')

        return ''.join(li).strip()


    def findback_password(self,user):
        '''通过已有用户名，找回密码'''
        try:
            with open(PathManage(f'{user}.json'),'r',encoding='utf-8') as f:
                data=f.read()
                data=json.loads(data)
            return data['password']
        except Exception as e:
            mylog.error(e)

