import os
import sys
dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir_path)

from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from utils.path_manage import PathManage

def create_watermark(content='made by joker',file='watemark.pdf'):
    #默认大小为21cm*29.7cm
    c = canvas.Canvas(file)
    #移动坐标原点(坐标系左下为(0,0))
    c.translate(13*cm, 2*cm)
                                                                                                                                
    #设置字体
    c.setFont("Helvetica", 80)
    #指定描边的颜色
    # c.setStrokeColorRGB(0, 1, 0)
    #指定填充颜色
    # c.setFillColorRGB(0, 1, 0)
    #画一个矩形
    # c.rect(cm, cm, 7*cm, 17*cm, fill=1)
                                                                                                                                
    #旋转45度，坐标系被旋转
    c.rotate(60)
    #指定填充颜色
    c.setFillColorRGB(0.6, 0, 0)
    #设置透明度，1为不透明
    c.setFillAlpha(0.1)
    #画几个文本，注意坐标系旋转的影响
    c.drawString(3*cm, 9*cm, content)
    # c.setFillAlpha(0.6)
    # c.drawString(3*cm, 9*cm, content)
                                                                                                                                
    #关闭并保存pdf文件
    c.save()
create_watermark(PathManage.db_path('watemark.pdf'))