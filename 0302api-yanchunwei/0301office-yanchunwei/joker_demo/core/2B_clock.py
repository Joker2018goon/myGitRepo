# -*- coding:utf-8 -*-
# 2B闹钟 2B_clock.py

# 需求：
"""
2B闹钟，添加自虐功能，为正常起床服务
- 定时功能
- 随机出一个计算题，答对才能关闭闹钟

目标：
- 练习时间模块的使用
- 复习函数操作
- 练习编程思维
- 学习控制台的驻留技术
"""

import sys
import os
dir_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print('===='+dir_path)
sys.path.append(dir_path)
import time
import random
import subprocess  # 调用子进程，与系统命令进行交互
from utils.path_manage import PathManage


def alert():
    # 第一步，设置时间
    set_time=input('请设置闹钟时间(如8:00):')
    print('现在时间是:')
    flag=True
    while flag:
        dt = time.localtime()
        fmt = '%X'
        now = time.strftime(fmt, dt)
        # print(now)
        # '\r' => 回车的意思，后面不换行，flush 刷新
        # print('现在时间是:')
        print(now+'\r',end='',flush=True)
        # sys.stdout 标准输出
        # sys.stdout.write(now+'\r')
        # sys.stdout.flush()
        time.sleep(1)
        # print('++++'+now[12:17]+'++++')
        # print(set_time.rjust(5,'0'))
        if now[:5]==set_time.rjust(5,'0'):
            str='闹钟响啦，起床啦!'
            print(str)
            subprocess.Popen(['start','起床歌.mp3'],shell=True)
            if random_math:
                mProcess =subprocess.Popen(['start','起床歌.mp3'],shell=True)
                mProcess.terminate()
            # break
            flag=not random_math()


def random_math():
    '''随机数学题，答对返回true'''
    try:
        while True:
            a=random.randint(1,10)
            b=random.randint(1,10)
            print(f'回答：{a} + {b} =')
            answer=int(input('请输入答案:'))
            if answer==a+b:
                print('ringht!')
                return True
                break
            else:
                print('wrong!')
    except Exception as e:
        print(e)

def main():
    # random_math()
    alert()

if __name__ == '__main__':
    main()