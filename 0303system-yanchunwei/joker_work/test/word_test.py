# -*- encoding:utf-8 -*-
import os
import sys
dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(dir_path)
sys.path.append(dir_path)
from core.base.word_base import Word
from utils.path_manage import PathManage


def main():
    docAdmin = Word()
    # print(docAdmin.ret)
    docAdmin.add_head_method('这是标题', 0)
    # print(docAdmin.ret)
    heart_path = PathManage.pic_path('heart.jpg')
    docAdmin.add_pic_method(heart_path)
    # print(docAdmin.ret)
    docAdmin.add_paragraph_method('这是副标题', 'Subtitle')
    p2=docAdmin.add_paragraph_method('这是普通文字，这是普通文字，这是普通文字，这是普通文字，这是普通文字')
    docAdmin.add_style_method(p2,'Title')
    print(type(p2))
    p2_words=docAdmin.add_paragraph_words_method(p2,'这是追加的文字')
    # docAdmin.add_fontSize_method(p2,33)
    print(type(p2_words))
    print(docAdmin.ret)
    doc_path = PathManage.doc_path('loveletter.docx')
    docAdmin.save_method(doc_path)


if __name__ == '__main__':
    main()