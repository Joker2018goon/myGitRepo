# -*- coding:utf-8 -*-
# image_util.py 图片处理
# author：joker

# 获得图片文件名
# 获得图片文件大小
# 对图片进行旋转
# 对图片进行裁剪

import os
import sys
dir_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir_path)
import re
from PIL import Image
from core.base.excel_base import Excel
from utils.path_manage import PathManage
from utils.log_util import Logger

mylog=Logger(__name__).getlog()
# 关闭日志
# mylog.disable(logging.DEBUG)

class DirUtil:
    '''遍历目录获取所有文件'''
    def __init__(self):
        self.file_list=[]

    def get_allfiles(self,dirname):
        '''获取文件夹下所有文件'''
        files=os.listdir(dirname)
        for fi in files:
            fi_path=os.path.join(dirname,fi)
            if os.path.isfile(fi_path):
                self.file_list.append(fi_path)
            elif os.path.isdir(fi_path):
                self.get_allfiles(fi_path)

    
    @staticmethod
    def get_file_size(filename):
        '''获取文件大小'''
        return os.path.getsize(filename)



class ImageUtils:
    '''图片处理工具类'''

    def __init__(self, source_dir, target_dir):
        '''初始化'''
        dir_util=DirUtil()
        dir_util.get_allfiles(source_dir)
        self.files=dir_util.file_list
        self.source_dir = source_dir
        self.target_dir = target_dir


    def thumbnail(self, filename, target_filename,percent=0.5):
        '''缩略一张，filename为绝对路径，target_filename为文件名'''
        thumbnail_filename=os.path.join(self.target_dir,target_filename)
        im = Image.open(filename)
        print(im.format, im.size, im.mode)
        # 获得图像尺寸:
        w, h = im.size
        print('尺寸: %sx%s' % (w, h))
        # 缩放到50%:
        im.thumbnail((int(w * percent), int(h * percent)))
        print('缩略图尺寸为: %sx%s' % (int(w * percent), int(h * percent)))
        # 把缩放后的图像用jpeg格式保存:
        im.save(thumbnail_filename, 'jpeg')
        
    def thumbnail_all(self, percent=0.5):
        '''缩略文件夹下所有图片文件'''

        for file in self.files:
            if re.match('(.*jpg&)|(.*png)|(.*bmp)',file):
                self.thumbnail(file,percent)
            else:
                # print('没有符合的文件')
                mylog.error('没有符合的文件')

    def save_to_excel(self,excel_filename):
        excel=Excel()
        excel.add_sheet_method('pic data',0)
        sheet=excel.get_sheet_method('pic data')
        sheet.cell(row=1, column=1).value = '文件名'
        sheet.cell(row=1, column=2).value = '文件大小'
        file_name=[]
        file_size=[]
        for file in self.files:
            print(file)
            if re.match('(.*png)|(.*bmp)|(.*jpg)$',file):
                name=file.split('\\')[-1]
                file_name.append(name)
                size=DirUtil.get_file_size(file)
                file_size.append(size)

        if len(file_name):
            if len(file_name)>2:
                for row in range(2,len(file_name)+2):
                    sheet.cell(row=row, column=1).value = file_name[row-2]
                    sheet.cell(row=row, column=2).value = file_size[row-2]
            else:
                sheet.cell(row=2, column=1).value = file_name[0]
                sheet.cell(row=2, column=2).value = file_size[0]
        excel.excel_save(PathManage.doc_path(excel_filename))

    def crop(self,filename,left, upper, right,lower,target_filename):
        '''裁剪图片,filename为绝对路径，target_filename为文件名'''
        im=Image.open(filename)
        box = (left, upper, right,lower)
        region = im.crop(box)
        region_filename=os.path.join(self.target_dir,target_filename)
        print(region_filename)
        region.save(region_filename)

    def rotate(self,filename, degrees,target_filename,isMirror=False,mirrorCode=None):
        '''旋转,isMirror为tru的时候为镜像翻转，mirrorCode=0代表水平翻转，mirrorCode=1代表上下翻转filename为绝对路径，target_filename为文件名'''
        rotate_filename=os.path.join(self.target_dir,target_filename)
        im=Image.open(filename)
        if not isMirror:
            im.rotate(degrees).save(rotate_filename)
        else:
            if mirrorCode==0:
                im.transpose(Image.FLIP_LEFT_RIGHT).save(rotate_filename)
            elif mirrorCode==1:
                im.transpose(Image.FLIP_TOP_BOTTOM).save(rotate_filename)
            else:
                # print('mirrorCode error or None')
                mylog.error('mirrorCode error or None')

    def add_logo(self):
        '''添加logo'''
        pass

    def new_image(self, words, position, font, color):
        '''新建图片'''
        pass

    def resize(self,h_ratio,w_ratio):
        '''调整大小'''
        pass

def main():
    imageutil=ImageUtils(r'C:\Users\yanchunwei\Desktop\作业',r'C:\Users\yanchunwei\Desktop\test')
    # imageutil.save_to_excel('图片数据.xlsx')
    # imageutil.crop(r'C:\Users\yanchunwei\Desktop\作业\timg.jpg',10,10,20,20,'tt.png')
    imageutil.rotate(r'C:\Users\yanchunwei\Desktop\作业\草帽海贼团.bmp',60,'xz.png')
    imageutil.rotate(r'C:\Users\yanchunwei\Desktop\作业\草帽海贼团.bmp',30,'xz2.png',0,True)



if __name__ == '__main__':
    main()