# -*- coding:utf-8 -*-
# author: joker
# background 后台操作界面

# 根据role来跳页面 

import os
import sys
dir_path=os.path.dirname(os.path.abspath(__file__))
sys.path.append(dir_path)
import json
import pickle
from login_page import Login
from utils.path_manage import PathManage
from authority_management import AuthorityManage
from crawler_page import CrawlerManage
from office_page import OfficeManage
from image_page import ImageManage
from utils.log_util import Logger

mylog=Logger(__name__).getlog()
# 关闭日志功能
# mylog.disable(logging.DEBUG)

class BackgroundPage:
    '''后台页面'''
    def __init__(self):
        '''初始化'''
        self.remove_user_session()
        

    def get_user_session(self):
        '''读取session文件'''
        with open(PathManage.db_path('session.pkl'), 'rb') as f:
            data = pickle.load(f)
            return data[0]

    def remove_user_session(self):
        '''删除session文件'''
        if os.path.exists(PathManage.db_path('session.pkl')):
            os.remove(PathManage.db_path('session.pkl'))



    @Login()
    def jump_background(self):
        '''方法注释：进入应用界面'''
        print('欢迎来到应用界面'.center(100, '*'))
        try:
            user=self.get_user_session()
            with open(PathManage.db_path(f'{user}.json'),'r',encoding='utf-8') as f:
                data=f.read()
                data=json.loads(data)
            # print(data['operation'])
            # print(user)
            menu_list=data['operation']
            print('菜单展示:')
            if len(menu_list)>0:
                for i in range(len(menu_list)):
                    print(i+1,menu_list[i])
            else:
                print('您还没开通权限，请联系管理员！')
                exit()
            id_str=input('请选择要进入的页面(选择对应序号)')
            id=int(id_str)
            if menu_list[id-1]=='权限管理':
                authority=AuthorityManage()
                authority.authority_page()
                mylog.info(f'进入{menu_list[id-1]}页面')
            elif menu_list[id-1]=='crawler':
                crawler_manage=CrawlerManage()
                crawler_manage.crawler_page()
                mylog.info(f'进入{menu_list[id-1]}页面')
            elif menu_list[id-1]=='office':
                office_manage=OfficeManage(user)
                office_manage.office_page()
                mylog.info(f'进入{menu_list[id-1]}页面')
            elif menu_list[id-1]=='image':
                image_manage=ImageManage()
                image_manage.image_page()
                mylog.info(f'进入{menu_list[id-1]}页面')
            else:
                print('请输入正确的序号')
        except Exception as e:
            mylog.error(e)
            
        


def main():
    bp=BackgroundPage()
    bp.jump_background()
    # jump_background()

if __name__ == '__main__':
    main()