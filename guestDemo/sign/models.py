# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.
# 发布会表
class Event(models.Model):
    # 发布会标题
    name = models.CharField(max_length=100)
    # 参加人数
    limit = models.IntegerField()
    # 状态
    status = models.BooleanField()
    # 地址
    address = models.CharField(max_length=200)
    # 发布会时间
    start_time = models.DateTimeField()
    # 创建时间（自动获取当前时间）
    create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# 嘉宾表
class Guest(models.Model):
    # 关联发布会id
    event = models.ForeignKey(Event,on_delete=models.PROTECT)
    # 姓名
    realname = models.CharField(max_length=64)
    # 手机号
    phone = models.CharField(max_length=16)
    # 邮箱
    email = models.EmailField()
    # 签到状态
    sign = models.BooleanField()
    # 创建时间
    create_time = models.DateTimeField(auto_now=True)


    class Meta:
        unique_together = ('event', 'phone')


    def __str__(self):
        return self.realname
