# -*- coding:utf-8 -*-
# author: joker
# login_page.py 注册页面


# 绘制用户注册界面
# admin不能再注册
# 用户输入注册信息：用户名和密码（使用一下正则表达式，复习）
# 密码由6-10字母和数字组成,不能是纯数字或纯英文 ^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,10}$  非空
# 用户名表达式：必须以字母开头，长度在10位以内 [a-zA-z]\\w{0,9}  非空

import os
import sys
dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir_path)
import json
import pickle
import msvcrt
import re
from utils.path_manage import PathManage
from utils.config_util import ConfigAdmin
from utils.email_util import MailMaster
from utils.image_util import DirUtil

class Register:
    '''注册操作'''

    def __init__(self):
        '''初始化'''
        self.dirob=DirUtil()
        self.users=self.get_users()
        # dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # dir_path = dir_path.replace('\\', '/')
        # self.base_dir = os.path.join(dir_path, 'db').replace('\\', '/')
        # self.data= {'DEFAULT': {'base_dir': self.base_dir, 'db_type': 'db','da_name':r'${base_dir}/memo.db','max_items':1000,'auto_save':True}}


    def save_users_data(self, data):
        '''保存用户注册信息'''
        with open(PathManage.db_path('users.pkl'), 'wb') as f:
            pickle.dump(data, f, 0)

    def save_users_json(self,data):
        '''保存到用户.json'''
        user=data['username']
        with open(PathManage.db_path(f'{user}.json'),'w',encoding='utf-8') as f:
            json.dump(data,f,ensure_ascii=False,indent=4)

    def creat_pw(self, markedWords):
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

    def check_user(self, user):
        '''校验用户名'''
        flag = True
        # 用户名由英文字母和数字组成的4-11位字符,以字母开头
        regex = re.compile('^[a-zA-Z][a-zA-Z0-9]{3,10}')
        match = regex.match(user)
        if user!='':
            if match:
                if user in self.users:
                    flag = False
                    print('该用户已注册过')
            else:
                flag = False
                print('用户名必须英文字母和数字组成的4-11位字符,以字母开头')
        else:
            flag=False
            print('用户名不能为空')
            
        return flag

    def check_pwd(self, pwd):
        '''检验密码'''
        flag = False
        # 密码由6-10字母和数字组成,不能是纯数字或纯英文
        regex = re.compile('^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,10}$')
        match = regex.match(pwd)
        if pwd!='':
            if match:
                flag=True
            else:
                print('密码由6-10字母和数字组成,不能是纯数字或纯英文')
        else:
            print('密码不能为空')

        return flag

    def get_users(self):
        '''通过文件名获取所有用户名'''
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


    def register_user(self):
        '''注册普通用户'''
        print('欢迎注册'.center(100, '*'))
        # 需要校验是否用户已经存在
        user = input('请输入用户名:')
        if self.check_user(user):
            pwd = self.creat_pw('请输入密码:')
            pwd_again = self.creat_pw('请确认输入的密码:')
            if self.check_pwd(pwd):
                if self.check_pwd(pwd_again):
                    if pwd == pwd_again:
                        data={}
                        data['username']=user
                        data['password']=pwd
                        data['type']='user'
                        data['operation']=[]
                        data['enabled']=1
                        self.save_users_json(data)
                    else:
                        print('两次输入的密码不相同！')
