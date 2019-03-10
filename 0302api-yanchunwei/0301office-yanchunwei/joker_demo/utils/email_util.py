# -*- coding:utf-8 -*-
# email_util.py 发邮件的方法模块


import smtplib
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText  
from email.mime.multipart import MIMEMultipart   
from email.mime.base import MIMEBase
from email import encoders

class NoMailListError(Exception):
    """没有添加邮件列表"""
    pass

class MailMaster:
    """邮箱大师"""
    def __init__(self, password='bafnfzrgryejddcf', smtp_server='smtp.qq.com', email_addr='2773187283@qq.com'):
        self.smtp = SMTP_SSL(smtp_server)
        # smtp.set_debuglevel(1)
        self.smtp.ehlo(smtp_server)
        self.smtp.login(email_addr, password)
        self.email_from = email_addr
        self.email_to = []

    def add_email_to_list(self, addr):
        self.email_to.append(addr)

    def notice(self, username, text, subject='通知信息'):
        self.send_email_all(subject, f'{username}\n' + text)

    def send_email_all(self, subject, body, mailtype='plain', attachment=None):  
        """  发送邮件通用接口
        subject: 邮件标题
        body: 邮件内容
        mailtype： 邮件类型，默认是文本，发html时候指定为html
        attachment： 附件
        """
        msg = MIMEMultipart()  # 构造一个MIMEMultipart对象代表邮件本身

        msg["Subject"] = Header(subject, "utf-8")
        msg["from"] = self.email_from

        try:  
            if len(self.email_to) > 0:
                to_mail = self.email_to  
                msg['To'] = ','.join(to_mail)
            else:
                raise NoMailListError('还没添加发送人呢，使用add_email_to_list进行填加')

            # mailtype代表邮件类型，纯文本或html等
            msg.attach(MIMEText(body, mailtype, 'utf-8'))  

            # 有附件内容，才添加到邮件
            if attachment:
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
            self.smtp.sendmail(self.email_from, msg['To'], msg.as_string())
            self.smtp.quit()  
        except smtplib.SMTPException as e:  
            print(e)  


def main():
    mm=MailMaster()
    mm.add_email_to_list('15618515795@163.com')
    mm.notice('joker','默认登录')


if __name__ == '__main__':
    main()