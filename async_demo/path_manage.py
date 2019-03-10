# -*- encoding:utf-8 -*-

import os
# base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
base_path = os.path.dirname(os.path.abspath(__file__))



class PathManage:
    '''自定义工具类，用于处理图片和文档的路径问题'''

    @staticmethod
    def pic_path(pic_file_name):
        '''处理图片路径，图片保存在pic文件夹下'''
        # pic_path = os.path.join(base_path, 'pic', pic_name)
        # return pic_path
        pic_path = os.path.join(base_path, 'pic')
        if not os.path.exists(pic_path):
            os.mkdir(pic_path)
        pic_file_path = os.path.join(pic_path, pic_file_name)
        return pic_file_path

    @staticmethod
    def doc_path(doc_file_name):
        '''生成的文档路径在office文件夹下'''
        office_path = os.path.join(base_path, 'office')
        if not os.path.exists(office_path):
            os.mkdir(office_path)
        doc_file_path = os.path.join(office_path, doc_file_name)
        return doc_file_path

    @staticmethod
    def db_path(db_file_name):
        '''已存文档（需要用到的数据）路径在db文件夹下'''
        db_path = os.path.join(base_path, 'db')
        if not os.path.exists(db_path):
            os.mkdir(db_path)
        db_file_path = os.path.join(db_path, db_file_name)
        return db_file_path

    @staticmethod
    def log_path(log_file_name):
        '''已存文档（需要用到的数据）路径在log文件夹下'''
        log_path = os.path.join(base_path, 'log')
        if not os.path.exists(log_path):
            os.mkdir(log_path)
        log_file_path = os.path.join(log_path, log_file_name)
        return log_file_path

    @staticmethod
    def config_path(config_file_name):
        '''包装配置文件路径'''
        conf_path = os.path.join(base_path, 'conf')
        if not os.path.exists(conf_path):
            os.mkdir(conf_path)
        conf_file_path = os.path.join(conf_path, config_file_name)
        return conf_file_path
    
    @staticmethod
    def download_path(dow_file_name):
        '''包装下载的文件路径'''
        download_path = os.path.join(base_path, 'download')
        if not os.path.exists(download_path):
            os.mkdir(download_path)
        dow_file_path = os.path.join(download_path, dow_file_name)
        return dow_file_path

    @staticmethod
    def crawler_path(filename):
        '''网上爬取的数据保存在crawler文件夹'''
        crawler_path=os.path.join(base_path,'crawler')
        if not os.path.exists(crawler_path):
            os.mkdir(crawler_path)
        crawler_file_path=os.path.join(crawler_path,filename)
        return crawler_file_path
