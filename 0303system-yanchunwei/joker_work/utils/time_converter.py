# -*- coding:utf-8 -*-
# 时间转换器 time_converter.py
# 工具类

# 给定随意的几种时间形式，自动转成统一格式
# 举例：
# '2018/1/8 14:28', 4.7, '2018年2月8日 14:28' 都能自动转成 2018-01-08 14:28:00, 没有时间的自动添加当前时间 注
# 意返回值，区分datetime类型和str类型

# '2018/1/8 14:28'
# 中文的年月日的处理 ， 如'2018年2月8日 14:28'
# 只有日期，自动追加时间，如  1.7 或者 1月7日


from datetime import datetime, date
from dateutil import parser

now = datetime.now()
class TimeCoverter:
    '''时间转化器，工具类，用于用户输入的不规范时间格式转换'''


    # def __init__(self):
    #     '''初始化'''
    #     self.now=datetime.now()

    @staticmethod
    def change_datetime(dt):
        '''2018/1/8 14:28 转换日期时间格式到yyyy-mm-dd hh:mm:ss'''
        date1 = parser.parse(dt)
        dt = date1.strftime('%Y-%m-%d %X')
        # print(type(date_str))
        # print(date_str.count('00:00:00'))
        # print('00:00:00' in date_str)
        if '00:00:00' in dt:
            dt=dt.replace('00:00:00','').strip()
            if dt.count('-',0)==2:
                year, month, day = dt.split('-')
                memo_date = now.replace(year=int(year), day=int(day), month=int(month))
            elif dt.count('-',0)==1:
                month, day = dt.split('-')
                print(year, month, day)
                memo_date = now.replace(day=int(day), month=int(month))
            return memo_date.strftime('%Y-%m-%d %X')
        else:
            return dt

    @staticmethod
    def change_datetime_cn(dt):
        '''转换中文年月日的时间'''
        date1 = dt.replace('年', '/').replace('月', '/').replace('日', '')
        return TimeCoverter.change_datetime(date1)

    @staticmethod
    def change_datetime_num(dt):
        '''转换'1.5'这种月日格式的日期，并添加时间'''
        if dt.count('.',0)==2:
            year, month, day = dt.split('.')
            memo_date = now.replace(year=int(year), day=int(day), month=int(month))
        elif dt.count('.',0)==1:
            month, day = dt.split('.')
            memo_date = now.replace(day=int(day), month=int(month))
        return memo_date.strftime('%Y-%m-%d %X')


def main():
    # d = TimeCoverter.change_datetime_num('2019.01.14')
    # print(d)
    d = TimeCoverter.change_datetime_cn('2020年2月8日')
    print(d)
    # d=TimeCoverter.change_datetime('2018-1-8')
    # print(d)


if __name__ == '__main__':
    main()