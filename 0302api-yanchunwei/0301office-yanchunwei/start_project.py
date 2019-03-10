#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# start_project.py
# 初始化工程目录
# # author: joker
# 借鉴de8ug老师的代码

import os
import sys

__author__ = 'joker'
path = os.path.dirname(os.path.abspath(__file__))


def start_project():
    '''从命令行参数取工程名， 默认为joker_demo'''
    project_name = 'joker_demo'
    if len(sys.argv) > 1:
        project_name = sys.argv[1]
    '''创建目录, readme, __init__文件'''
    folders = ['bin', 'conf', 'core', 'test', 'db', 'log', 'utils']
    for folder in folders:
        folder_path = os.path.join(path, project_name, folder)
        print(folder_path)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        '''创建readme文件，编码问题用，, encoding="utf-8" '''
        with open(
                os.path.join(path, project_name, 'readme.md'),
                'w',
                encoding='utf-8') as f:
            f.write('# ' + project_name + '\n\n')
            f.write('> Author:' + __author__ + '\n')
            f.write('> bin: 放入口函数' + '\n')
            f.write('> conf: 配置文件' + '\n')
            f.write('> core: 放一些py文件（模块1）' + '\n')
            f.write('> test: 测试类或者API(后期可能会有)' + '\n')
            f.write('> db: 数据文件' + '\n')
            f.write('> utils: 提供公共方法' + '\n')
            f.write('> log: 日志文件' + '\n')
        '''add init file,使得文件夹变为代码包，被调用'''
        with open(
                os.path.join(path, project_name, folder, '__init__.py'), 'w'):
            pass


def main():
    start_project()


if __name__ == '__main__':
    main()