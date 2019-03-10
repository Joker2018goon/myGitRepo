# -*- coding:utf-8 -*-
# author: joker
# authority_manage.py  权限管理页面

from role_manage import RoleManage
from user_manage import UserManage
from utils.log_util import Logger

mylog=Logger(__name__).getlog()
# 关闭日志功能
# mylog.disable(logging.DEBUG)


class AuthorityManage:
    '''权限管理类'''

    def __init__(self):
        '''初始化'''
        pass

    def authority_page(self):
        '''权限管理页面'''
        print('欢迎来到权限管理页面'.center(100,'*'))
        menu_list=['用户管理','角色管理']
        print('菜单展示:')
        for i in range(len(menu_list)):
            print(i+1,menu_list[i])
        id_str=input('请选择要进入的页面(选择对应序号)')
        id=int(id_str)
        if menu_list[id-1]=='用户管理':
            user_manage=UserManage()
            user_manage.user_manage_page()
            mylog.info(f'进入{menu_list[id-1]}页面')
        elif menu_list[id-1]=='角色管理':
            role_manage=RoleManage()
            role_manage.role_page()
            mylog.info(f'进入{menu_list[id-1]}页面')
        else:
            print('请输入正确的序号')