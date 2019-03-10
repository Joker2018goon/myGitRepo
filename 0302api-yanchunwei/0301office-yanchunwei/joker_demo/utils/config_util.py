# -*- conding:utf-8 -*-
# config_util.py 用作设置配置文件的模块
# author:Joker

import os
import sys
dir_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(dir_path)
import configparser
from path_manage import PathManage


class ConfigAdmin:
    '''一系列配置文件操作'''

    def __init__(self):
        '''初始化'''
        self.config = configparser.ConfigParser()

    def read_config(self, config_path):
        '''读取配置文件'''
        self.config.read(config_path)

    def get_section_option(self, section):
        '''返回某个项目中的所有键的序列'''
        return self.config.options(section)

    def get_section_option_value(self, section, option):
        '''返回section中的option的键值'''
        return self.config.get(section, option)

    def add_config_section(self, section_name):
        '''添加一个配置文件的section节点'''
        try:
            if self.config.has_section(section_name):
                print(f'该域名{section_name}已存在')
            else:
                self.config.add_section(section_name)
                # self.write_config()
        except Exception as e:
            print(e)

    def add_config_option(self, section, option, val):
        '''设置某个section中键名为option的值'''
        self.config.set(section, option, val)

    def get_config_sections(self):
        '''返回配置文件中所有的section'''
        return self.config.sections()

    def write_config(self, config_path, data={}):
        '''写入配置文件'''
        for k, v in data.items():
            self.config[k] = v
        # config_path = os.path.join(base_dir, 'demo.ini')
        with open(config_path, 'w') as f:
            self.config.write(f)

    def check_section(self,section_name):
        flag=False
        if self.config.has_section(section_name):
            flag=True
        return flag


def main():
    data = {
        'DEFAULT': {
            'base_dir':
            'D:/Documents and Settings/yanchunwei/桌面/0301office-yanchunwei/joker_demo/db',
            'db_type':
            'db'
        }
    }

    configAdmin = ConfigAdmin()
    # configAdmin.write_config(PathManage.config_path('mome.ini'))
    # configAdmin.read_config(PathManage.config_path('mome.ini'))
    # configAdmin.write_config(PathManage.config_path('mome.ini'),data)

    # configAdmin.add_config_section('DEFAULT')
    # configAdmin.add_config_option('DEFAULT','db_type','db')
    # configAdmin.write_config(PathManage.config_path('mome.ini'))
    configAdmin.add_config_section('joker3')
    configAdmin.add_config_option('joker3','db_type','db')
    configAdmin.write_config(PathManage.config_path('mome.ini'))
    print(data)


if __name__ == '__main__':
    main()