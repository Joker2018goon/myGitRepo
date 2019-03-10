#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# start_project.py
# 初始化工程目录
# # author: joker
# 网上借鉴的思路


import os
import sys

__author__ = 'joker'
path = os.path.dirname(os.path.abspath(__file__))


def start_project():
    '''从命令行参数取工程名， 默认为joker_demo'''
    project_name = 'joker_work'
    if len(sys.argv) > 1:
        project_name = sys.argv[1]
    '''创建目录, readme, __init__文件'''
    # folders = ['bin', 'conf', 'core', 'test', 'db', 'log', 'utils','amage','crawler']
    folders = ['db_fixture', 'interface', 'report']
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
            f.write('> db_fixture: 封装数据库操作方法，数据初始化' + '\n')
            f.write('> interface: 测试用例' + '\n')
            f.write('> report: 生成的测试报告目录' + '\n')
            f.write('> HTMLTestRunner.py: 生成的测试报告使用的模板' + '\n')

    '''add init file,使得文件夹变为代码包，被调用'''
    folder_inits = ['db_fixture', 'interface']
    for folder in folder_inits:
        with open(
                os.path.join(path, project_name, folder, '__init__.py'), 'w'):
            pass

    files=['db_config.ini','HTMLTestRunner.py','run_test.py']
    for file in files:
        print(os.path.join(path,project_name,file))
        with open(os.path.join(path,project_name,file),'w') as f:
            pass

    with open(os.path.join(path,project_name,'db_config.ini'),'w',encoding='utf-8') as f:
        f.write('[mysqlconf]'+'\n')
        f.write('host='+'\n')  
        f.write('port='+'\n')  
        f.write('user='+'\n')  
        f.write('password='+'\n')  
        f.write('db_name='+'\n')  


def main():
    start_project()


if __name__ == '__main__':
    main()