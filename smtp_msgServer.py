#SMTP服务
#发送日志文件到指定的邮箱
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr

import smtplib

from datetime import datetime
import os

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = 'liushenshen123@163.com'
password = '19880124'
to_addr = 'liushenshenxfy@126.com'
smtp_server = 'smtp.163.com'

msg = MIMEMultipart()
msg['From'] = _format_addr('消息服务器日志<%s>' % from_addr)
msg['To'] = _format_addr('管理员<%s>' % to_addr)
msg['Subject'] = Header('SMTP邮件服务...', 'utf-8').encode()


msg.attach(MIMEText('消息服务器日志', 'plain', 'utf-8'))
log_path = '/usr/log'

for root, dirs, files in os.walk(log_path):
    for name in files:
        if name.endswith('.log'):
            file_name = os.path.join(root, name)
            with open(file_name, 'rb') as f:
                mime = MIMEBase('application', 'octet-stream')
                mime.add_header('Content-Disposition', 'attachment', filename = name)
                mime.set_payload(f.read())
                encoders.encode_base64(mime)
                msg.attach(mime)


try:
    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
    for root, dirs, files in os.walk(log_path):
        for name in files:
            os.remove(os.path.join(root, name))
except Exception as e:
    print('except', e)



