# -*- coding:utf-8 -*-
# using Python 3.6+
# author: joker

import time
import os
import sys
import random
import string
import asyncio
import logging

import requests
import aiohttp
from log_util import Logger
from timeit import DecoTime


# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(levelname)-10s: %(message)s',
# )

BASE_DIR = r'D:\Documents and Settings\yanchunwei\桌面\第四模块第四章作业\async_demo'
download_dir = os.path.join(BASE_DIR, "download")


class AsynCrawler:
    '''异步爬虫类'''
    def __init__(self,urls):
        '''初始化'''
        self.TEST_URLS=urls
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)

    def fetch_url(self):
        '''获取urls'''
        return self.TEST_URLS


    def make_temp_name(self,count=5, f='.jpg'):
        '''拼接图片名'''
        return ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(count)]) + f


    def download_image(self,url):
        '''下载并且保存图片'''
        try:
            r = requests.get(url).content
            logging.debug(f'get image with {url}')
            if r:
                self.save_file(os.path.join(download_dir, self.make_temp_name()), r) 
        except Exception as e:
            print(e)


    def save_file(self,filename, data):
        '''保存图片'''
        logging.debug(f'saving file {filename}')
        with open(filename, 'wb') as f:
            f.write(data)

    async def adownload_image(self,url, loop):
        '''协程下载'''
        async with aiohttp.ClientSession(loop=loop) as session:
            async with session.get(url) as resp:
                filename = os.path.join(download_dir, self.make_temp_name(f='-a.jpg'))
                with open(filename, 'wb') as f:
                    while True:
                        block = await resp.content.read(1024)
                        if not block:
                            break
                        f.write(block)


    async def acrawler(self,loop):
        '''协程爬取网站'''
        logging.debug('starting async crawler...')
        urls = self.fetch_url()
        tasks = [self.adownload_image(url, loop) for url in urls]
        await asyncio.gather(*tasks)


    @DecoTime()
    def run_async_crawler(self):
        '''协程异步'''
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.acrawler(loop))


    @DecoTime()
    def crawler(self):
        '''普通爬取'''
        logging.debug('starting crawler...')
        urls = self.fetch_url()
        for url in urls:
            logging.debug(f'start downling: {url}')
            self.download_image(url)
        logging.debug('finish crawler.')

    

def main():
    
    # TEST_URLS = [
    #     'https://source.unsplash.com/random',
    #     'https://source.unsplash.com/user/erondu/1600x900',
    #     'http://via.placeholder.com/350x150',
    #     'http://via.placeholder.com/350x150/1c2b3c/999'
    # ]
    # async_object=AsynCrawler(TEST_URLS)
    # async_object.crawler()
    # async_object.run_async_crawler()

    try:
        if len(sys.argv)==1:
            print('''
                -> 请在程序结尾，空格+您要爬取的网址
                -> 爬取多个网址，网址之间请用空格隔开
            ''')

        if len(sys.argv)>1:
            urls=[]
            for i in range(1,len(sys.argv)):
                urls.append(sys.argv[i])
            async_object=AsynCrawler(urls)
            async_object.crawler()
            async_object.run_async_crawler()
    except Exception as e:
        print(e)
     


if __name__ == '__main__':
    main()