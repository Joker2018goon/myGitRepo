# -*- coding:utf-8 -*-
# author:joker

import os
import sys
dir_path=os.path.dirname(os.path.abspath(__file__))
sys.path.append(dir_path)
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from utils.path_manage import PathManage


class SeSpider:
    def __init__(self, url, limit=3):
        """新建driver，打开url"""
        chrome_path=os.path.join(dir_path,'chromedriver.exe')
        self.driver = webdriver.Chrome(chrome_path)
        self.driver.get(url)
        self.limit = limit

        # 等几秒，给页面渲染时间
        self.driver.implicitly_wait(5)

    def search(self, key_words='cat'):
        """搜索关键词"""
        el = self.driver.find_element_by_class_name('search__input')
        if el.is_displayed:
            el.click()
            print('开始搜索...')
            el.send_keys(key_words)
            el.send_keys(Keys.RETURN)

        # 等几秒，给页面渲染时间
        print('得到搜索结果')
        self.driver.implicitly_wait(10)

    # 页面往下滚一滚，多加点图片
    def get_more(self):
        print('页面滚动')
        self.driver.execute_script('window.scrollBy(0,8000)')
        print('页面滚动结束')

    # 查找图片 '.photo-item img'
    def find_image(self, css_filter):
        image_list = self.driver.find_elements_by_css_selector(css_filter)
        print('找到图片元素：', image_list[:3])
        return image_list
        
    # 保存图片, 简单点，先存三个看看
    def save_images(self, image_list):
        for img in image_list[:self.limit]:
            print('保存：', img.get_attribute('alt'))
            filename=img.get_attribute('alt') + '.jpg'
            with open(PathManage.crawler_path(filename), 'wb') as f:
                f.write(requests.get(img.get_attribute('src')).content)

    # 关闭driver
    def close_driver(self):
        self.driver.close()

    def save_images_by_url(self, key_words, css_filter):
        """根据url， key_words, css_filter取到任意网址的图片
        """
        self.search(key_words)
        self.get_more()
        self.save_images(self.find_image(css_filter))
        self.close_driver()


