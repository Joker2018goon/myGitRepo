# -*- coding -*-
# email_demo_exercise.py 邮件小案例，用于联系

# 发送邮件步骤
    # 打开邮箱
    # 登录
    # 写正文
    # 发送
    # 退出


import os
import sys
dir_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir_path)

import smtplib
from smtplib import SMTP_SSL  # 安全加密
from email.header import Header  # 邮件标题
from email.mime.text import MIMEText   # 邮件正文
from email.mime.multipart import MIMEMultipart   # 邮件附件
from email.mime.base import MIMEBase
from email import encoders
from utils.path_manage import PathManage


def get_paw():
    '''获取第三方认证密码'''
    return 'bafnfzrgryejddcf'

smtp=SMTP_SSL('smtp.qq.com')
# smtp.set_debuglevel(1)
smtp.ehlo('smtp.qq.com')
smtp.login('2773187283@qq.com',get_paw())


def send_email():
    '''发邮件'''
    msg=MIMEText('这是一封测试邮件','plain','utf-8')
    msg['Subject']=Header('这是邮件标题','utf-8')
    msg['from']='2773187283@qq.com'
    msg['to']='15618515795@163.com'
    smtp.sendmail('2773187283@qq.com','15618515795@163.com',msg.as_string())

    smtp.quit()

def send_email_attach(body,attachment):
    '''带有附件的邮件'''
    msg=MIMEMultipart()
    msg['Subject']=Header('这是带附件的邮件标题','utf-8')
    msg['from']='2773187283@qq.com'
    to_mail=['2773187283@qq.com','15618515795@163.com']
    msg['to']=','.join(to_mail)

    # plain 表示纯文本
    msg.attach(MIMEText(body,'plain','utf-8'))
     # 二进制方式模式文件  
    with open(attachment, 'rb') as f:  
        # MIMEBase表示附件的对象  
        mime = MIMEBase('text', 'txt', filename=attachment)  
        # filename是显示附件名字  
        mime.add_header('Content-Disposition', 'attachment', filename=attachment)  
        # 获取附件内容  
        mime.set_payload(f.read())  
        encoders.encode_base64(mime)  
        # 作为附件添加到邮件  
        msg.attach(mime)  
    try:  
        smtp.sendmail('2773187283@qq.com', '2773187283@qq.com', msg.as_string())
        smtp.quit()  
    except smtplib.SMTPException as e:  
        print(e)  


def main():
    # send_email()
    send_email_attach('这是测试附件的邮件',PathManage.download_path('jokerwatemark.pdf'))

if __name__ == '__main__':
    main()