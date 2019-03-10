import os
import sys
dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir_path)


from docx.enum.style import WD_STYLE_TYPE
from docx import *
from utils.path_manage import PathManage

document = Document()
styles = document.styles

#生成所有段落样式
for s in styles:
    if s.type == WD_STYLE_TYPE.PARAGRAPH:
        document.add_paragraph('Paragraph style is : '+ s.name, style = s)

document.save(PathManage.doc_path('para_style.docx'))