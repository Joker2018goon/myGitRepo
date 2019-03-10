#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# main.py
# author: joker

import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core.login_page import Login 
from core.memo_admin import MemoAdmin
from core.register_page import Register
from core.query_api import QueryApi
from core.email_api import EmailApi
from utils.image_util import ImageUtils


args=sys.argv[:]
function_list=['-h','-add','-del','-mod','-query','-email','-rotate','-crop']

def check_user(user):
    '''校验用户'''
    flag=False
    register_object=Register()
    if user in register_object.register_dict.keys():
        flag=True
    return flag

def menu():
    '''菜单'''
    print('''
        python main.py -h                                                                              功能列表
                        -add   [user]                                                              备忘录增加功能
                        -del   [user]                                                              备忘录删除功能
                        -mod   [user]                                                              备忘录修改功能
                        -query [from_month,to_month,user]                                          备忘录查询接口 
                        -email [to_addr,user,year,month=None]                 
                                                                                                邮件发送数据功能
                        -rotate [source_dir, target_dir,filename, degrees,target_filename,isMirror=False,mirrorCode=None]           
                                                                                                    旋转图片功能
                        -crop [source_dir, target_dir,filename,left, upper, right,lower,target_filename]
                                                                                                    裁剪图片功能
    
    ''')

def arge_function():
    '''命令行调用'''

    if len(args)==1:
        loginAdmin=Login()
        loginAdmin.init_login_page()

    if len(args)==2 and args[1]=='-h':
        print('''
            python main.py -h                                                                              功能列表
                           -add   [user]                                                              备忘录增加功能
                           -del   [user]                                                              备忘录删除功能
                           -mod   [user]                                                              备忘录修改功能
                           -query [from_month,to_month,user]                                          备忘录查询接口 
                           -email [to_addr,user,year,month=None]                 
                                                                                                    邮件发送数据功能
                           -rotate [source_dir, target_dir,filename, degrees,target_filename,isMirror=False,mirrorCode=None]           
                                                                                                        旋转图片功能
                           -crop [source_dir, target_dir,filename,left, upper, right,lower,target_filename]
                                                                                                        裁剪图片功能
        
        ''')

    if args[1] in function_list:
        if args[1]=='-add':
            if len(args)==3:
                user=args[2]
                if check_user(user):
                    memo_admin=MemoAdmin(user)
                    memo_admin.add()
                else:
                    print('用户不存在')
            elif len(args)==2:
                print('Missing Parameters.suggest using the this command for help--->python main.py -h ')

        if args[1]=='-del':
            if len(args)==3:
                user=args[2]
                if check_user(user):
                    memo_admin=MemoAdmin(user)
                    memo_admin.delete()
                else:
                    print('用户不存在')
            elif len(args)<3:
                print('Missing Parameters.suggest using the this command for help--->python main.py -h ')

        if  args[1]=='-mod':
            if len(args)==3:
                user=args[2]
                if check_user(user):
                    memo_admin=MemoAdmin(user)
                    memo_admin.modify()
                else:
                    print('用户不存在')
            elif len(args)<3:
                print('Missing Parameters.suggest using the this command for help--->python main.py -h ')

        if args[1]=='-query':
            if len(args)==5:
                from_month=int(args[2])
                to_month=int(args[3])
                user=args[4]
                if check_user(user):
                    query_api=QueryApi()
                    query_api.query_memo(from_month,to_month,user)
                else:
                    print('用户不存在')
            elif len(args)<5:
                print('Missing Parameters.suggest using the this command for help--->python main.py -h ')

        if args[1]=='-email':
            if len(args==5):
                to_addr=args[2]
                user=args[3]
                year=args[4]
                if check_user(user):
                    email_api=EmailApi()
                    email_api.send_email(to_addr,user,year)
                else:
                    print('用户不存在')
            elif len(args==6):
                to_addr=args[2]
                user=args[3]
                year=args[4]
                month=args[5]
                if check_user(user):
                    email_api=EmailApi()
                    email_api.send_email(to_addr,user,year,month)
                else:
                    print('用户不存在')
            else:
                print('Missing Parameters.suggest using the this command for help--->python main.py -h ')

            


        #  -rotate [source_dir,target_dir,filename, degrees,target_filename,isMirror=False,mirrorCode=None]           旋转,isMirror为tru的时候为镜像翻转，mirrorCode=0代表水平翻转，mirrorCode=1代表上下翻转filename为绝对路径，target_filename为文件名
        if args[1]=='-rotate':
            source_dir=args[2]
            target_dir=args[3]
            filename=args[4]
            degrees=args[5]
            target_filename=args[6]
            if len(args==7):
                image=ImageUtils(source_dir,target_dir)
                image.rotate(filename, degrees,target_filename)
            elif len(args==9):
                isMirror=args[7]
                mirrorCode=args[8]
                image=ImageUtils(source_dir,target_dir)
                image.rotate(filename, degrees,target_filename,isMirror,mirrorCode)
            else:
                print('Missing Parameters.suggest using the this command for help--->python main.py -h ')
            
        # -crop [source_dir, target_dir,filename,left, upper, right,lower,target_filename] 裁剪图片,source_dir根目录, target_dir图片处理后要保存目录，filename为绝对路径，target_filename为文件名
        if len(args)==9 and args[1]=='-crop':
            if check_user(user):
                source_dir=args[2]
                target_dir=args[3]
                filename=args[4]
                left,upper=args[5]
                right=args[6]
                lower=args[7]
                target_filename=args[8]
                image=ImageUtils(source_dir,target_dir)
                image.crop(filename,left,upper,right,lower,target_filename)
            else:
                print('用户不存在')
    else:
        menu()

def main():
    '''程序入口'''
    try:
        arge_function()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()