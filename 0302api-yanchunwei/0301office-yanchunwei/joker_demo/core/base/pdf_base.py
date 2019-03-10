import os
import sys
dir_path = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(dir_path)
import datetime
import pickle
import datetime
import PyPDF2
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
from reportlab.pdfbase import pdfmetrics
# print(pdfmetrics.getRegisteredFontNames()) # 'Symbol', 'ZapfDingbats'
from reportlab.pdfbase.ttfonts import TTFont
from utils.path_manage import PathManage

# 参考 https://blog.csdn.net/syshzbtt/article/details/73394580

# 从pdf中读取文本
# 写pdf  nnnn
# 加密解密pdf
# 合并pdf，加水印


class Pdf:
    '''pdf文档类'''

    def __init__(self, pdf_file):
        '''初始化'''
        self.pdf_file_read = open(pdf_file, 'rb')
        self.pdf_read = PyPDF2.PdfFileReader(self.pdf_file_read)
        self.pdf_writer = PyPDF2.PdfFileWriter()

    def get_pdf_Pages(self):
        '''获取pdf文件总页数'''
        return self.pdf_read.numPages

    def get_pdf_page(self, num):
        '''获取pdf文件某一页'''
        try:
            # pdf文件页码从0开始
            return self.pdf_read.getPage(num)
        except Exception as e:
            print(e)

    def get_page_text(self, num):
        '''获取某页文本内容'''
        page = self.get_pdf_page(num)
        return page.extractText()

    def write_pdf(self, num, new_pdf_file):
        '''从pdf文件中读取某页，写入新的pdf文件'''
        page = self.get_pdf_page(num)
        self.pdf_writer.addPage(page)
        with open(new_pdf_file, 'wb') as f:
            self.pdf_writer.write(f)

    def close_read_pdf(self):
        '''释放资源'''
        self.pdf_file_read.close()

    @staticmethod
    def add_pwd_forPdf(pwd_before_pdf, pwd, pwd_after_pdf):
        '''加密pdf文件'''
        with open(pwd_before_pdf, 'rb') as f_in:
            pdf = PyPDF2.PdfFileReader(f_in)
            pdf_writer = PyPDF2.PdfFileWriter()
            for page_num in range(pdf.numPages):
                pdf_writer.addPage(pdf.getPage(page_num))
            pdf_writer.encrypt(pwd)
            with open(pwd_after_pdf, 'wb') as f_out:
                pdf_writer.write(f_out)

    @staticmethod
    def del_pwd_forPdf(pwd_after_pdf, pwd):
        '''解密pdf文件'''
        with open(pwd_after_pdf, 'rb') as f_in:
            pdf = PyPDF2.PdfFileReader(f_in)
            print(pdf.isEncrypted)
            pdf.decrypt(pwd)

    @staticmethod
    def add_watemark(before_watemark_pdf,
                     after_watemark_pdf,
                     watemark_pdf='watemark.pdf'):
        '''添加水印'''
        with open(before_watemark_pdf, 'rb') as f_in:
            with open(watemark_pdf, 'rb') as f_w:
                pdf = PyPDF2.PdfFileReader(f_in)
                pdf_w = PyPDF2.PdfFileReader(f_w)

                pdf_writer = PyPDF2.PdfFileWriter()
                for page_num in range(pdf.numPages):
                    page = pdf.getPage(page_num)
                    page.mergePage(pdf_w.getPage(0))
                    pdf_writer.addPage(page)
                with open(after_watemark_pdf, 'wb') as f_out:
                    pdf_writer.write(f_out)

    @staticmethod
    def create_watermark(content='made by joker',
                         watemark_pdf='watemark.pdf'):
        '''制作简单的文本pdf水印文件'''
        #默认大小为21cm*29.7cm
        c = canvas.Canvas(watemark_pdf)
        #移动坐标原点(坐标系左下为(0,0))
        c.translate(13 * cm, 2 * cm)
        #设置字体
        c.setFont("Helvetica", 80)
        #旋转45度，坐标系被旋转
        c.rotate(60)
        #指定填充颜色
        c.setFillColorRGB(0.6, 0, 0)
        #设置透明度，1为不透明
        c.setFillAlpha(0.1)
        #画几个文本，注意坐标系旋转的影响
        c.drawString(3 * cm, 9 * cm, content)
        # c.setFillAlpha(0.6)
        # c.drawString(3*cm, 9*cm, content)
        #关闭并保存pdf文件
        c.save()

    @staticmethod
    def create_pdf(user,data_list):
        '''字典生成pdf文件'''
        c = canvas.Canvas(PathManage.download_path(f'{user}.pdf'))
        pdfmetrics.registerFont(TTFont('msyh', PathManage.db_path('msyh.ttf')))
        c.setFont('msyh', 12)
        textobject = c.beginText()
        textobject.setTextOrigin(inch, 11 * inch)
        now = datetime.datetime.today()
        # 设定日期格式
        date = now.strftime('%Y-%m-%d %H:%M:%S')
        # 设置下载时间
        textobject.textLines(f'下载时间:{date}'.center(80, '-'))
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
            textobject.textLines(text_memo)
        c.drawText(textobject)
        c.showPage()
        c.save()
