#SMTP邮件服务
#发送附件
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

#输入Email地址和口令
from_addr = input('From: ')
password = input('Password: ')

#输入收件人地址
to_addr = input('To: ')

#输入SMTP服务器地址
smtp_server = input('SMTP server: ')

msg = MIMEMultipart()
msg['From'] = _format_addr('Python爱好者<%s>' % from_addr)
msg['To'] = _format_addr('管理员<%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候...', 'utf-8').encode()

#邮件正文
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

with open('test.jpg', 'rb') as f:
    #设置附件的MIME和文件名
    mime = MIMEBase('image', 'jpeg', filename = 'test.jpg')
    mime.add_header('Content-Disposition', 'attachment', filename = 'test.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(f.read())

    #base64编码
    encoders.encode_base64(mime)
    msg.attach(mime)

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()


