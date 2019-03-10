# -*- coding:utf-8 -*-
# author:joker
# role_manage.py  角色管理

from admin_manage import AdminManage

class RoleManage:
    '''角色管理操作'''

    def __init__(self):
        '''初始化'''
        self.admin_manage=AdminManage()
        

    def role_page(self):
        '''角色管理页面'''
        print('欢迎来到角色管理页面'.center(100,'*'))
        menu_list=['添加角色','删除角色','角色配置给用户','撤去用户权限']
        print('功能展示:')
        for i in range(len(menu_list)):
            print(i+1,menu_list[i])
        id_str=input('请选择功能(选择对应序号)')
        id=int(id_str)
        if menu_list[id-1]=='添加角色':
            self.admin_manage.creat_role()
        elif menu_list[id-1]=='删除角色':
            self.admin_manage.delete_role()
        elif menu_list[id-1]=='角色配置给用户':
            self.admin_manage.empower_user()
        elif menu_list[id-1]=='撤去用户权限':
            self.admin_manage.cancel_power()
        else:
            print('请输入正确的序号')