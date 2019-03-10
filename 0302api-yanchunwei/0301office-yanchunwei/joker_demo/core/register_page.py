# -*- coding:utf-8 -*-
# login_page.py 注册页面
# author: joker

# 绘制用户注册界面
# 用户输入注册信息：用户名和密码（使用一下正则表达式，复习）
# 密码由6-10字母和数字组成,不能是纯数字或纯英文 ^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,10}$  非空
# 用户名表达式：必须以字母开头，长度在10位以内 [a-zA-z]\\w{0,9}  非空
# 存在pickle里 users.pkl-------后台校验users.pkl是否已经存在该用户（字典的健不可重复）
# 添加配置文件，为备忘录数据指定路径类型和文件名    如：zhangsna。则文件可以为zhangsan或者zhangsna.db

import os
import sys
dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir_path)
import pickle
import msvcrt
import re
from utils.path_manage import PathManage
from utils.config_util import ConfigAdmin
from utils.email_util import MailMaster

class Register:
    '''注册操作'''

    def __init__(self):
        '''初始化'''
        self.register_dict = self.get_users_data()
        dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # dir_path = dir_path.replace('\\', '/')
        self.base_dir = os.path.join(dir_path, 'db').replace('\\', '/')
        self.data= {'DEFAULT': {'base_dir': self.base_dir, 'db_type': 'db','da_name':r'${base_dir}/memo.db','max_items':1000,'auto_save':True}}

    def get_users_data(self):
        '''获取users.pkl数据'''
        try:
            with open(PathManage.db_path('users.pkl'), 'rb') as f:
                users_dict = pickle.load(f)
        except Exception:
            data = {}
            self.save_users_data(data)
            with open(PathManage.db_path('users.pkl'), 'rb') as f:
                users_dict = pickle.load(f)
        return users_dict

    def save_users_data(self, data):
        '''保存用户注册信息'''
        with open(PathManage.db_path('users.pkl'), 'wb') as f:
            pickle.dump(data, f, 0)

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
                if user in self.register_dict.keys():
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

    def create_config(self, user,config_file='memo.ini'):
        '''添加配置文件'''
        configAdmin = ConfigAdmin()
        # configAdmin.add_config_section(user)
        # configAdmin.add_config_option(user,'db_name',r'${DEFAULT:base_dir}'+f'/{user}.pkl')
        # configAdmin.add_config_option(user,'db_type','pkl')
        dict_val={}
        dict_val['db_name']=self.base_dir+f'/{user}.db'
        dict_val['db_type']='db'
        self.data[user]=dict_val
        configAdmin.write_config(PathManage.config_path(config_file),self.data)
        configAdmin.read_config(PathManage.config_path(config_file))
        


    def ini_register_page(self):
        '''初始化注册页面'''
        print('欢迎注册'.center(100, '*'))
        # 需要校验是否用户已经存在
        user = input('请输入用户名:')
        # 密码密文，但是输入密码时，不会将任何内容打印到标准输出.想用* 显示
        # pwd=getpass.getpass('请输入密码:')
        # email=input('邮箱:')
        if self.check_user(user):
            pwd = self.creat_pw('请输入密码:')
            pwd_again = self.creat_pw('请确认输入的密码:')
            if self.check_pwd(pwd):
                if self.check_pwd(pwd_again):
                    if pwd == pwd_again:
                        self.register_dict[user] = pwd
                        # self.register_dict['email'] = email
                        # mail_master=MailMaster()
                        # mail_master.add_email_to_list(email)
                        # mail_master.notice(user,'欢迎来到51备忘录！')
                        self.save_users_data(self.register_dict)
                        for user in self.register_dict.keys():
                            self.create_config(user,'user_memo.ini')
                    else:
                        print('两次输入的密码不相同！')
        return user
