# -*- coding:utf-8 -*-
# author:joker
# image_page.py 图片处理操作

import os
import sys
dir_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(dir_path)
from utils.image_util import ImageUtils
from utils.path_manage import PathManage


class ImageManage:
    '''图片操作类'''

    def __init__(self):
        '''初始化'''
        source_dir=os.path.join(os.path.dirname(dir_path),'image')
        target_dir=os.path.join(os.path.dirname(dir_path),'image_target')
        self.imageutil = ImageUtils(source_dir, target_dir)
        

    def image_page(self):
        '''图片处理页面'''
        print('欢迎来到图片处理页面'.center(100, '*'))
        # TODO 完成两个相关方法
        menu=['文件夹下所有图片缩略功能','获取件夹下所有图片大小数据并且保存到excel']

        for i in range(len(menu)):
            print(i+1,menu[i])

        id=input('请选择功能序号')
        if id.isdigit():
            id=int(id)
            if id==1:
                self.imageutil.thumbnail_all()
            elif id==2:
                self.imageutil.save_to_excel(PathManage('pc_size.xls'))
            else:
                print('输入有误！')
