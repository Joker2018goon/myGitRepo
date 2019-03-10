# !/usr/bin/env Python
# -*- coding:utf-8 -*-
# 网上找的打印心形图案

import os
import sys
dir_test_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir_test_path)
import time
from utils import color_me

# sentence = color_me.ColorMe("love").red()
sentence = "love"
for char in sentence.split():
   allChar = []
   for y in range(12, -12, -1):
       lst = []
       lst_con = ''
       for x in range(-30, 30):
            formula = ((x*0.04)**2+(y*0.2)**2-1)**3-(x*0.04)**2*(y*0.2)**3
            if formula <= 0:
                lst_con += char[(x) % len(char)]
            else:
                lst_con += ' '
       lst.append(lst_con)
       allChar += lst
   print('\n'.join(allChar))
   time.sleep(1)