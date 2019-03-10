# -*- coding:utf-8 -*-
# author:joker
# office_page.py 文件操作

import os
import sys
dir_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(dir_path)
from pdf_export import PdfManage
from utils.path_manage import PathManage

class OfficeManage:
    '''文件操作类'''

    def __init__(self,user):
        '''初始化'''
        self.user=user

    def office_page(self):
        '''文件操作页面'''
        print('欢迎来到文件操作页面'.center(100,'*'))
        # TODO 实现连个相关的方法
        menu=['输入文字导出PDF功能']

        for i in range(len(menu)):
            print(i+1,menu[i])

        input_str=input('请输入你要写入的文字')
        data=[]
        data.append(input_str)
        pdf_ob=PdfManage(data,self.user)
        pdf_ob.export('data_export.pdf')