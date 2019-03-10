# -*- coding:utf-8 -*-
# login_page.py 登录页面
# author: joker

# 绘制用户登录界面
# 用户输入用户名和密码
# 从users.pkl 里拿数据校验，授权登录权限（后台数据处理）
# 登录失败可能 1.密码或用户名输入错误，即忘记密码，后续可以实现通过用户名找回密码 2.未注册，模拟跳转到注册页面

import os
import sys
dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir_path)
import pickle
import msvcrt
from utils.path_manage import PathManage
from core.register_page import Register
from core.memo_admin import MemoAdmin
from core.memo import Memo
from utils import color_me
from utils.log_util import Logger

mylog=Logger(__name__).getlog()
# 关闭日志功能
# mylog.disable(logging.DEBUG)

class Login:
    '''登录等一系列操作'''

    def __init__(self):
        '''初始化'''
        self.users = self.get_users_data()

    def get_users_data(self):
        '''获取user.pkl数据'''
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

    def check_login(self, user, pwd):
        '''授权是否可以登录'''
        # 0-可以登录 1-没有该用户 2-密码错误
        flag = 0
        if user in self.users.keys():
            if pwd != self.users[user]:
                flag = 2
        else:
            flag = 1
        return flag

    def init_login_page(self,user=''):
        '''登录页面'''
        print(f'{user} 欢迎来到51备忘录登录页面'.center(100, '*'))
        user = input('用户名:')
        # pwd = self.input_pw('密码:')
        pwd=input('密码:')
        flag=self.check_login(user, pwd)
        if flag==0:
            # 跳转到操作页面
            # print('跳转到操作页面')
            mylog.info('登录成功，跳转到操作页面')
            self.manage_memoAdmin(user)
        elif flag==1:
            # 这个print 作为提示
            # print('您输入的用户名不存在')
            mylog.warn('您输入的用户名不存在')
            select=input('请选择注册-按r或者退出注册页面-按q:')
            if select=='r':
                mylog.info('注册新用户')
                reg = Register()
                user=reg.ini_register_page()
                # 重新加载一下数据
                self.users=self.get_users_data()
                mylog.info('重新跳转到登录页面')
                self.init_login_page(user)
            elif select=='q':
                print()
                self.init_login_page()
        else:
            # print('密码错误，找回密码(功能就简单些)')
            mylog.error('密码错误，找回密码(功能就简单些)')
            user_for_pwd=input('您的用户名:')
            back_pwd=self.findback_password(user_for_pwd)
            # 这个print 是作为提示
            print(f'您的密码为{back_pwd},请妥善保管')
            mylog.info('密码找回成功')
            self.init_login_page()


    def findback_password(self,user):
        '''通过已有用户名，找回密码'''
        return self.users[user]

    def manage_memoAdmin(self,user):
        '''备忘录操作界面'''
        print(f'{user} 欢迎来到51备忘录'.center(100, '*'))
        flag = True
        while (flag):
            one = {'1': 'add', '2': 'query', '3': 'delete', '4': 'modify','5':'export'}
            for k, v in one.items():
                print(f'{k}:{v}')
            action_id = input(color_me.ColorMe('选择以上功能的序号:').blue())
            memoAdmin = MemoAdmin(user)
            if action_id.isdigit():
                if 0 < int(action_id) < len(one)+1:
                    attr = one[action_id]
                    try:
                        if hasattr(memoAdmin, attr):
                            if attr == 'add':
                                mylog.info('正在新增备忘事件')
                                memoAdmin.add()
                            elif attr == 'query':
                                mylog.info('查询备忘事件')
                                memoAdmin.query()
                            elif attr == 'delete':
                                mylog.warn('删除备忘事件')
                                memoAdmin.delete()
                            elif attr == 'modify':
                                mylog.warn('修改备忘事件')
                                memoAdmin.modify()
                            else:
                                memoAdmin.export()
                    except Exception as e:
                        # print(color_me.ColorMe('出现异常(最好先add哦！===)：').red(), e)
                        mylog.error(e)
                else:
                    print(color_me.ColorMe('请输入存在的序号！').red())
            else:
                print(color_me.ColorMe('请输入数字！').red())
            flag = input(color_me.ColorMe('y返回主页，q退出：').blue()) == 'y'
            mylog.info('退出系统')
