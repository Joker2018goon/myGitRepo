#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# main.py
# author: joker

import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core.background import BackgroundPage




def main():
    '''程序入口'''
    try:
        bk=BackgroundPage()
        bk.jump_background()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()