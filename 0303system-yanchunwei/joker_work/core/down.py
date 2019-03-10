# -*- coding:utf-8 -*-
# 获取信息+保存到csv

import os
import sys
dir_path=os.path.dirname(os.path.abspath(__file__))
sys.path.append(dir_path)
import json
import re
import csv
import time
import requests
from urllib.parse import urlparse
from datetime import datetime, timedelta
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
from utils.path_manage import PathManage

class Throttle:
    '''阀门类,相同域名的访问添加延迟时间，避免访问过快'''

    def __init__(self, delay):
        '''初始化'''
        # 延迟时间，避免访问过快
        self.delay = delay
        # 用字典保存访问某域名的时间
        self.domains = {}

    def wait(self, url):
        '''设置访问间隙,延迟时间'''
        domain = urlparse(url).netloc
        print(domain)
        last_accessed = self.domains.get(domain)
        if self.delay > 0 and last_accessed is not None:
            sleep_secs = self.delay - (datetime.now() - last_accessed).seconds
            if sleep_secs > 0:
                time.sleep(sleep_secs)
        self.domains[domain] = datetime.now()


class Downder:
    '''下载类'''

    def __init__(self,
                 heads=None,
                 retries=3,
                 proxies=None,
                 delay=3,
                 timeout=30):
        '''初始化'''
        self.throttle = Throttle(delay)
        self.retries = retries
        self.heads = heads
        self.proxies = proxies
        self.delay = delay
        self.timeout = timeout

    def download(self, url, is_json=False):
        '''通过URL，获取页面'''
        print('下载的页面:', url)
        try:
            self.throttle.wait(url)
            response = requests.get(
                url,
                headers=self.heads,
                proxies=self.proxies,
                timeout=self.timeout)
            if response.status_code == 200:
                if is_json:
                    return response.json()
                else:
                    return response.content
            return None
        except RequestException as e:
            print(e.response)
            html = ''
            if hasattr(e.response, 'status_code'):
                code = e.response.status_code
                print('error code', code)
                if self.retries > 0 and 500 <= code < 600:
                    html = self.download(url)
                    self.retries -= 1
            else:
                code = None
        return html

    def write_csv(self, filename, all_list):
        '''保存到CSV'''
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            fields = ('商品详情', '商品id', '商品价格', '好评率', '评价数')
            writer.writerow(fields)
            for row in all_list:
                writer.writerow(row)


class Recorder:
    '''根据不同保存类型使用相应方法，通过类对象使用回掉函数凡是直接调用'''

    def __init__(self, save_type='csv'):
        '''初始化'''
        self.save_type = save_type

    def __call__(self, filename, fields, row_list):
        '''对象直接调用此方法，调用方式和类实例化对象一样，暂时这么理解'''
        if hasattr(self, self.save_type):
            function = getattr(self, self.save_type)
            return function(filename, fields, row_list)
        else:
            return {'status': 1, 'statusText': 'no record function'}

    def csv(self, filename, fields, row_list):
        '''保存到CSV'''
        try:
            with open(PathManage.crawler_path(filename), 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(fields)
                for row in row_list:
                    writer.writerow(row)
            return {'status': 0, 'statusText': 'csv saved'}
        except Exception:
            return {'status': 1, 'statusText': 'csv error'}


class ItemSpider:
    '''爬虫类'''

    def __init__(self,
                 headers=None,
                 retries=3,
                 proxies=None,
                 delay=3,
                 timeout=30):
        '''初始化'''
        self.headers = headers
        self.retries = retries
        self.proxies = proxies
        self.downder = Downder(headers, retries, proxies, delay, timeout)
        self.timeout = timeout

    def find_all(self, url):
        '''通过一个网址，爬取信息'''
        # url='https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=%E6%89%8B%E6%9C%BA&pvid=f8fd8008e6d64e839566fda3691c9cfd'
        page = self.downder.download(url)
        soup_all = BeautifulSoup(page, 'lxml')
        gl_item_list = soup_all.find_all('li', attrs={'class': 'gl-item'})

        row_list = []
        for soup in gl_item_list:
            name = soup.find(
                'div', attrs={
                    'class': 'p-name p-name-type-2'
                }).find('em').text
            print('商品详情:', name)

            product_id = soup.get('data-sku')
            print('商品id:', product_id)

            # item = soup.find('div', attrs={'class': 'p-name p-name-type-2'}).find('a')
            # print('item:', item['href'])

            product_price = soup.find(
                'div', attrs={
                    'class': 'p-price'
                }).find('i').text
            print('商品价格:', product_price)

            comment_url = f'https://sclub.jd.com/comment/productPageComments.action?productId={product_id}&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
            data = self.downder.download(comment_url, True)
            good_rate = data['productCommentSummary']['goodRate']
            comment_count = data['productCommentSummary']['commentCount']
            print('好评率:', good_rate)
            print('评价数:', comment_count)
            print('分割线'.center(100, '*'))

            row = []
            row.append(name)
            row.append(product_id)
            row.append(product_price)
            row.append(good_rate)
            row.append(comment_count)
            row_list.append(row)

        return row_list

    def fetch_data(self,
                   url,
                   filename,
                   page_start,
                   page_end,
                   page_offset,
                   callback=None):
        '''根据页数搜索所有信息'''
        row_all_list = []
        for page in range(page_start, page_end, page_offset):
            row_list = self.find_all(url.format(page))
            row_all_list = row_list + row_all_list
            print(f'完成第{page}页')

        # self.downder.write_csv(filename, row_all_list)
        if callback:
            callback(filename, ('商品详情', '商品id', '商品价格', '好评率', '评价数'),
                     row_all_list)
