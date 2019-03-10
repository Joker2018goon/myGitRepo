# /usr/bin/env/python
# -*- coding:utf-8 -*-
# memo_admin.py 备忘录管理类
# author:joker

# 新需求：导出文件功能，将历史数据导出为pdf格式
# 添加日志
# 关闭日志功能

import time
import os
import sys
dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir_path)
import pickle
import re
from core import memo
from core.base.pdf_base import Pdf
from utils import color_me
from utils.path_manage import PathManage
from utils.time_converter import TimeCoverter



class MemoAdmin:
    '''备忘录管理类'''

    def __init__(self, user):
        '''初始化'''
        self.user = user
        self.user_db_file_name = f'{user}' + '.db'
        try:
            self.memo_list = self.load(self.user_db_file_name)
        except Exception:
            list = []
            self.save(list, self.user_db_file_name)
            self.memo_list = self.load(self.user_db_file_name)

    def add(self):
        '''新建'''
        import time
        select = input('确认新增y或退出q')
        if select == 'y':
            dt_input = input(color_me.ColorMe('请输入日期（如：2018/1/8 14:28, 4.7,2018年2月8日 14:28），缺失部分默认当前时间').blue())
            now = time.time()
            date = self.date_manage(dt_input)
            #转换成时间数组
            timeArray = time.strptime(date,'%Y-%m-%d %X')
            #转换成时间戳
            timestamp = time.mktime(timeArray)
            if timestamp>=now:
                event = input(color_me.ColorMe('请输入事件：').blue())
                time = input(color_me.ColorMe('请输入用时(单位为分钟)：').blue())
                memObj = memo.Memo(date, event, time)
                self.memo_list = self.load(self.user_db_file_name)
                self.memo_list.append(memObj.data)
                self.save(self.memo_list, self.user_db_file_name)
            else:
                print('请输入不小于当前时间的日期,备忘未来的事！')
        else:
            print('退出新增页面')

    def date_manage(self, dt_input):
        '''根据输入的不同的日期进行处理'''
        date=''
        try:
            if '.' in dt_input:
                date=TimeCoverter.change_datetime_num(dt_input)
            elif '年' in dt_input or '月' in dt_input:
                date=TimeCoverter.change_datetime_cn(dt_input)
            else:
                date=TimeCoverter.change_datetime(dt_input)
        except Exception as e:
            print(e)
            print('请按提示的格式输入日期')
            exit()
        
        return date

    def delete(self):
        '''删除'''
        self.memo_list = self.load(self.user_db_file_name)
        self.query()
        select = input('确认删除y或退出q')
        if select == 'y':
            if len(self.memo_list) > 0:
                id = input(color_me.ColorMe('请输入需要删除的记录序号').yellow())
                if id.isdigit():
                    id = int(id)
                    if 0 < id < len(self.memo_list) + 1:
                        self.memo_list.pop(id - 1)
                        self.save(self.memo_list, self.user_db_file_name)
                    else:
                        print('请输入存在的序号！')
                else:
                    print(color_me.ColorMe('请输入数字！').red())
            else:
                print('您还没新增备忘录记录，赶快添加吧')
        else:
            print('退出删除')

    def modify(self):
        '''修改'''
        self.memo_list = self.load(self.user_db_file_name)
        self.query()
        select = input('确认修改y或退出q')
        if select == 'y':
            if len(self.memo_list) > 0:
                id = input(color_me.ColorMe('请输入需要修改的记录序号').yellow())
                if id.isdigit():
                    id = int(id)
                    if 0 < id < len(self.memo_list) + 1:
                        # date = input(color_me.ColorMe('请输入日期：').blue())
                        dt_input = input(color_me.ColorMe('请输入日期（如：2018/1/8 14:28, 4.7,2018年2月8日 14:28），缺失部分默认当前时间').blue())
                        date = self.date_manage(dt_input)
                        event = input(color_me.ColorMe('请输入事件：').blue())
                        time = input(color_me.ColorMe('请输入用时：').blue())
                        self.memo_list[id - 1]['date'] = date
                        self.memo_list[id - 1]['event'] = event
                        self.memo_list[id - 1]['time'] = time
                        self.save(self.memo_list, self.user_db_file_name)
                    else:
                        print('请输入存在的序号！')
                else:
                    print(color_me.ColorMe('请输入数字！').red())
            else:
                print('您还没新增备忘录记录，赶快添加吧')
        else:
            print('退出修改页面')

    def query(self):
        '''查询'''
        self.memo_list = self.load(self.user_db_file_name)
        all_time = 0
        for i in range(0, len(self.memo_list)):
            all_time += int(re.sub(r'\D', '', self.memo_list[i]['time']))
            data_dict = self.memo_list[i]
            text_memo = f'{i+1}' + '. '
            num = 1
            for k, v in data_dict.items():
                if num == len(data_dict):
                    text_memo += f'{k}: {v} 。'
                    num += 1
                else:
                    text_memo += f'{k}: {v} ,'
                    num += 1
            print(text_memo)
        print(f'共{len(self.memo_list)}条待办事项, 总时长：{all_time}分钟。')

    def export(self):
        '''导出功能'''
        self.memo_list = self.load(self.user_db_file_name)
        Pdf.create_pdf(self.user, self.memo_list)
        Pdf.create_watermark(watemark_pdf=PathManage.db_path('watemark.pdf'))
        Pdf.add_watemark(
            PathManage.download_path(f'{self.user}'+'.pdf'),
            PathManage.download_path(f'{self.user}'+'-watemark.pdf'),
            PathManage.db_path('watemark.pdf'))

    def save(self, data, db_file_name='memo.pkl'):
        '''写入数据文件'''
        with open(PathManage.db_path(db_file_name), 'wb') as f:
            pickle.dump(data, f, 0)

    def load(self, db_file_name='memo.pkl'):
        '''读取数据文件'''
        with open(PathManage.db_path(db_file_name), 'rb') as f:
            data = pickle.load(f)
            return data
