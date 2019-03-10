from django.shortcuts import render

# Create your views here.
import redis

class RedisAdmin():
    '''redis操作类'''
    def __init__(self):
        self.client=redis.StrictRedis(host='10.11.71.176',port=6379)

    def set_name(self,name,value):
        pass

    def hit_page(self,page):
        '''访问页面自动累加次数'''
        self.client.incr(page)

    def get_hit_count(self,page):
        '''获取点击量'''
        return self.client.get(page).decode('utf-8')


