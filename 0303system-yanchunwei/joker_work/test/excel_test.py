import os
import sys
dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir_path)
import re
from core.base.excel_base import Excel
from utils.path_manage import PathManage


def main():
    def A():
        '''测试所用'''
        wb_new = Excel()
        wb2 = Excel(PathManage.db_path('btc.xlsx'))
        sh1 = wb2.get_sheet_method('btc')
        wb_new.add_sheet_method('test', 0)
        sh_new = wb_new.get_sheet_method('test')

        for row in range(1, sh1.max_row + 1):
            date = sh1.cell(row=row, column=1).value
            sh_new.cell(row=row, column=1).value = date
        wb_new.excel_save(PathManage.db_path('btc_new.xlsx'))

    def B():
        '''测试所用'''
        wb = Excel(PathManage.db_path('btc.xlsx'))
        sheet_btc = wb.get_sheet_method('btc')
        wb.add_sheet_method('2016', 1)
        sheet_new = wb.get_sheet_method('2016')
        sheet_new.cell(
            row=1, column=1).value = sheet_btc.cell(
                row=1, column=1).value
        sheet_new.cell(
            row=1, column=2).value = sheet_btc.cell(
                row=1, column=2).value
        print(sheet_new.max_row)
        list_row=[]
        for row in range(2, sheet_btc.max_row + 1):
            date = sheet_btc.cell(row=row, column=1).value
            regex = re.compile('^(2016)')
            match = regex.match(date)
            
            if match:
                # print(row)
                list_row.append(row)
                print(list_row[0])
                a=list_row[0]-2
                for column in range(1, sheet_btc.max_column + 1):
                    sheet_new.cell(row=row-a, column=column).value = sheet_btc.cell(row=row, column=column).value
        print(sheet_new.max_row)

        wb.excel_save(PathManage.db_path('btc.xlsx'))

    def del_data(sheet_name):
        '''测试删除工作表所用'''
        excel=Excel(PathManage.db_path('btc.xlsx'))
        excel.delete_sheet_method(sheet_name)
        excel.excel_save(PathManage.db_path('btc.xlsx'))

    for i in range(3,9):
        '''调用删除方法'''
        del_data(f'201{i}')


if __name__ == '__main__':
    main()