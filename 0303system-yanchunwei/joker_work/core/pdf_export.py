# -*- coding:utf-8 -*-
# author: joker
# pdf_export.py pdf导出

import time
import os
import sys
dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir_path)
from core.base.pdf_base import Pdf
from utils.path_manage import PathManage

class PdfManage:
    '''PDf操作类'''


    def __init__(self,data,user):
        '''初始化'''
        self.data_list=data
        self.user=user


    def export(self,filename):
        '''导出功能'''
        data_list = self.data_list
        Pdf.create_input_pdf(self.user, data_list)