import os
import sys
dir_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir_path)
import datetime
import pickle
# import subprocess
import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
print(pdfmetrics.getRegisteredFontNames()) # 'Symbol', 'ZapfDingbats'
from reportlab.pdfbase.ttfonts import TTFont 
from utils.path_manage import PathManage


# 参考 https://blog.csdn.net/syshzbtt/article/details/73394580 


def create_pdf(user):
    '''字典生成pdf文件'''
    with open(PathManage.db_path(f'{user}.db'), 'rb') as f:
        data_list = pickle.load(f)

    c = canvas.Canvas(PathManage.download_path(f'{user}.pdf'))
    pdfmetrics.registerFont(TTFont('msyh', PathManage.db_path('msyh.ttf')))
    # c.drawString(100, 300, u'雅黑雅黑')
    c.setFont('msyh', 12)
    textobject = c.beginText()
    textobject.setTextOrigin(inch, 11 * inch)
    now = datetime.datetime.today()
    # 设定日期格式
    date = now.strftime('%Y-%m-%d %H:%M:%S')
    for i in range(0, len(data_list)):
        data_dict = data_list[i]
        text_memo = f'{i+1}' + '. '
        num = 1
        for k, v in data_dict.items():
            if num == len(data_dict):
                text_memo += f'{k}: {v} 。'
                num += 1
            else:
                text_memo += f'{k}: {v} ,'
                num += 1
        # print(text_memo)
        textobject.textLines(text_memo)
    # 设置下载时间
    textobject.textLines(f'下载时间:{date}'.center(80, '-'))
    c.drawText(textobject)
    c.showPage()
    c.save()

create_pdf('joker')