# -*- coding:utf-8 -*-
# author:joker
# admin_manage.py 管理员操作类


import os
import sys
dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir_path)
import re
import json
import pickle
from utils.image_util import DirUtil
from utils.path_manage import PathManage


class AdminManage:
    '''管理员操作类'''
    def __init__(self):
        '''初始化'''
        self.dirob=DirUtil()
        self.users=self.get_users()
        self.user_info=self.get_users_info()
        self.role_dict=self.get_role_info()


    def get_users_info(self):
        '''获取所有用户信息'''
        data_users={}
        for user in self.users:
            with open(PathManage.db_path(f'{user}.json'),'r',encoding='utf-8') as f:
                data=f.read()
                data=json.loads(data)
                data_users[f'{user}']=data
        return data_users

    def get_enabled_users(self,enabled):
        '''通过enabled获取对应用户'''
        # 1为正常，0为加入黑名单
        general_users=[]
        for user in self.users:
            user_info=self.user_info[user]
            if user_info['type']=='user' and user_info['enabled']==enabled:
                general_users.append(user)
        return general_users

    def get_type_users(self,type_str='admin'):
        '''通过type获取管理员或者普通用户'''
        target_users=[]
        for user in self.users:
            user_info=self.user_info[user]
            if user_info['type']==type_str:
                target_users.append(user)
        return target_users

    def set_user_blacklist(self):
        '''拉黑用户'''
        general_users=self.get_enabled_users(1)

        if len(general_users)>0:
            print('目前注册的普通用户如下:')
            for i in range(len(general_users)):
                print(i+1,general_users[i])
        else:
            print('目前没有可拉黑的普通用户！')

        id_str=input("请选择要拉黑的用户序号（支持拉黑多用户,序号用'+'符隔开）：")
        id_list=id_str.split('+')
        for id in id_list:
            id=id.strip()
            id=int(id)
            user=general_users[id-1]
            user_info=self.user_info[user]
            user_info['enabled']=0

        self.save_userinfo()


    def cancel_black(self):
        '''取消拉黑'''
        general_users=self.get_enabled_users(0)

        if len(general_users)>0:
            print('目前已拉黑的普通用户如下:')
            for i in range(len(general_users)):
                print(i+1,general_users[i])
        else:
            print('目前没有拉黑的普通用户！')

        id_str=input("请选择要取消拉黑的用户序号（支持拉黑多用户,序号用'+'符隔开）：")
        id_list=id_str.split('+')
        for id in id_list:
            id=id.strip()
            id=int(id)
            user=general_users[id-1]
            user_info=self.user_info[user]
            user_info['enabled']=1

        self.save_userinfo()

    def creat_role(self):
        '''创建角色,存到pkl中'''
        role_dict=self.role_dict
        menu_list=['权限管理','crawler', 'office', 'image']
        print('菜单权限'.center(100,'*'))
        for i in range(len(menu_list)):
            print(i+1,menu_list[i])
        role_list=[]
        role_name=input('请输入要创建的角色名称:')
        id_str=input("请输入你要展示的菜单序号（支持多选，'+'隔开）:")
        id_list=id_str.split('+')
        for id in id_list:
            id=id.strip()
            id=int(id)
            role_list.append(menu_list[id-1])
        role_dict[role_name]=role_list
        self.save_role_info(role_dict)

    def save_role_info(self,role_dict):
        '''保存角色信息'''
        with open(PathManage.db_path('role.pkl'), 'wb') as f:
            pickle.dump(role_dict, f, 0)

    def get_role_info(self):
        '''获取所有角色的信息'''
        with open(PathManage.db_path('role.pkl'), 'rb') as f:
            data=pickle.load(f)
        return data

    def show_role_info(self):
        '''展示所有角色信息以及菜单权限'''
        role_dict=self.role_dict
        print('角色名称'.ljust(20,' '),'菜单权限')
        for name , value in role_dict.items():
            role='、'.join(value)
            print(name.ljust(20,' '),role)

    def delete_role(self):
        '''删除角色'''
        role_dict=self.role_dict
        role_menu=role_dict.keys()
        print('角色列表'.center(100,'*'))
        self.show_role_info()
        role_del=input('请输入你要删除的角色名称:')
        if role_del in role_menu:
            del role_dict[role_del]
        else:
            print('输入有误！')
        self.save_role_info(role_dict)

    def empower_user(self):
        '''赋权给用户'''
        print('赋权给用户'.center(100,'*'))
        self.show_role_info()
        print('分割线'.center(50,'-'))
        users=self.get_type_users('user')
        self.show_user_name(users)
        role_user=input('请分别输入角色和用户名称（角色名称+用户名称）')
        role_name=role_user.split('+')[0]
        user_name=role_user.split('+')[1]
        if role_name in self.role_dict.keys() and user_name in self.users:
            menu=self.role_dict[role_name]
            user_info=self.user_info[user_name]
            user_info['operation']=menu
            if '权限管理' in menu:
                user_info['type']='admin'
            self.save_userinfo()
        else:
            print('输入有误')


    def cancel_power(self):
        '''撤去用户权限'''
        print('撤去用户权限'.center(100,'*'))
        users=self.get_type_users('user')
        self.show_user_name(users)
        cancel_name=input('请正确输入需要撤权的用户名:')
        if cancel_name in users:
            user_info=self.user_info[cancel_name]
            user_info['operation']=[]
            self.save_userinfo()
        else:
            print('输入有误！')

    def show_user_name(self,users):
        '''展示当前普通用户'''
        print('当前可操作用户:')
        for user in users:
            print(user)
        print('(注：同级别不可权限操作，admin权限大于user)')

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

    def save_userinfo(self):
        '''保存处理过的用户信息'''
        for user in self.users:
            data=self.user_info[user]
            with open(PathManage.db_path(f'{user}.json'),'w',encoding='utf-8') as f:
                json.dump(data,f,ensure_ascii=False,indent=4)

def main():
    ad=AdminManage()
    # ad.creat_role()
    # ad.empower_user()
    ad.cancel_power()

if __name__ == '__main__':
    main()