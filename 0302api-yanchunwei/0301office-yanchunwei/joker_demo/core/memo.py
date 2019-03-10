# /usr/bin/env/python
# -*- coding:utf-8 -*-
# memo.py 备忘录类
# author:joker

import time
import pickle


class Memo:
    '''备忘录类'''

    def __init__(self, date, event, time):
        '''初始化'''
        self._id = 0
        self.date = date
        self.event = event
        self.time = time
        self.data = {'date': self.date, 'event': self.event, 'time': self.time}

    @property
    def id(self):
        '''获得id属性'''
        return self._id
