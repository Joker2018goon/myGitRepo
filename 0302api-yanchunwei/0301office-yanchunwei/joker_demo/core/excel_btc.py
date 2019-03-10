# !/usr/bin/env Python
# -*- coding:utf-8 -*-
# excel_btc.py 完成作业

import os
import sys
dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir_path)

import re
import logging
from core.base.excel_base import Excel
from utils.path_manage import PathManage
from utils.log_util import Logger

mylog=Logger(__name__).getlog()
# 关闭日志功能
# Logger.closeLog(logging.WARNING)

class ExcelAdmin:
    '''excel操作类，用于完成作业'''

    def __init__(self, file_name):
        '''初始化'''
        self.wb = Excel(file_name)
        self.ret = {'state': 0, 'stateMessage': 'success'}

    def split_data(self, key_data):
        '''处理字符串，获取相应的数据'''
        sheet_btc = self.wb.get_sheet_method('btc')
        self.wb.add_sheet_method(key_data, 1)
        sheet_new = self.wb.get_sheet_method(key_data)
        sheet_new.cell(
            row=1, column=1).value = sheet_btc.cell(
                row=1, column=1).value
        sheet_new.cell(
            row=1, column=2).value = sheet_btc.cell(
                row=1, column=2).value
        list_row=[]
        for row in range(2, sheet_btc.max_row + 1):
            date = sheet_btc.cell(row=row, column=1).value
            regex = re.compile(f'^({key_data})')
            match = regex.match(date)
            if match:
                list_row.append(row)
                a=list_row[0]-2
                for column in range(1, sheet_btc.max_column + 1):
                    sheet_new.cell(row=row-a, column=column).value = sheet_btc.cell(row=row, column=column).value
        # print(sheet_new.max_row)

    def add_average(self,key_data):
        '''添加平均值'''
        try:
            sheet=self.wb.get_sheet_method(key_data)
            sheet.cell(row=sheet.max_row+1,column=1).value='平均值'
            sheet.cell(row=sheet.max_row,column=2).value=f'=average(B2:B{sheet.max_row-1})'
        except Exception:
            # print(e)
            mylog.error('add_average error')
            self.ret['state'] = 1
            self.ret['stateMessage'] = 'add_average error'

    def save_method(self,fila_name):
        '''保存文件'''
        try:
            self.wb.excel_save(fila_name)
        except Exception:
            # print(e)
            mylog.error('save_method error')
            self.ret['state'] = 1
            self.ret['stateMessage'] = 'save_method error'

    def del_sheet_method(self,sheet_name):
        '''删除工作表'''
        self.wb.delete_sheet_method(sheet_name)

def main():
    exAdmin = ExcelAdmin(PathManage.db_path('btc.xlsx'))
    for i in range(3,9):
        # 作业需要没有放在项目main.py下执行，相应年份的数据放到的相应的工作表中
        exAdmin.split_data(f'201{i}')
        exAdmin.add_average(f'201{i}')

        # 数据拆分完还可删除，方便循环测试，只要打开下面注释就可
        # exAdmin.del_sheet_method(f'201{i}')
    exAdmin.save_method(PathManage.db_path('btc.xlsx'))
    

if __name__ == '__main__':
    main()