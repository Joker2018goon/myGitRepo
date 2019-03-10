# -*- coding:utf-8 -*-
# author:joker
# crawler_page.py 数据爬取操作页面

import os
import sys
dir_path=os.path.dirname(os.path.abspath(__file__))
sys.path.append(dir_path)
from down import ItemSpider,Recorder
from selenium_pic import SeSpider

class CrawlerManage:
    '''数据爬取操作类'''

    def __init__(self):
        '''初始化'''
        pass

    def crawler_page(self):
        '''爬取数据页面'''
        print('欢迎来到爬虫页面'.center(100,'*'))
        # TODO 两个相关的功能
        menu=['爬取京东功能','selenium图片抓取功能']

        for i in range(len(menu)):
            print(i+1,menu[i])

        id=input('请选择功能序号')
        if id.isdigit():
            id=int(id)
            if id==1:
                url = 'https://search.jd.com/Search?keyword=iPhone%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&bs=1&wq=iPhone%E6%89%8B%E6%9C%BA&ev=exbrand_Apple%5E&page={}&s=58&click=0'
                headers = {
                    'User-agent':
                    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
                    "referer":
                    "https://passport.jd.com"
                }
                item_spider = ItemSpider(headers=headers)
                item_spider.fetch_data(url, 'iphoneAll.csv', 1, 5, 2, Recorder())
            elif id==2:
                url = 'https://www.pexels.com/'
                se = SeSpider(url, 5)
                se.save_images_by_url('dog', '.photo-item img')
            else:
                print('输入有误！')

