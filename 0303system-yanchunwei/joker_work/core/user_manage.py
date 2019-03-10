# -*- coding:utf-8 -*-
# author:joker
# user_manage.py 用户管理

from admin_manage import AdminManage

class UserManage:
    '''用户管理操作类'''

    def __init__(self):
        '''初始化'''
        self.admin_manage=AdminManage()

    def user_manage_page(self):
        '''用户管理页面'''
        print('欢迎来到用户管理页面'.center(100,'*'))
        menu_list=['拉黑用户','取消拉黑']
        print('功能展示:')
        for i in range(len(menu_list)):
            print(i+1,menu_list[i])
        id_str=input('请选择功能(选择对应序号)')
        id=int(id_str)
        if menu_list[id-1]=='拉黑用户':
            self.admin_manage.set_user_blacklist()
        elif menu_list[id-1]=='取消拉黑':
            self.admin_manage.cancel_black()
        else:
            print('请输入正确的序号')