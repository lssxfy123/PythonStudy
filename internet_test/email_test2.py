# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.6.7
# smtp邮件发送html
from email.header import Header
from email.mime.text import MIMEText
import email_test1
from email_test1 import format_address
from email_test1 import send_email

if __name__ == '__main__':
    # 发送html
    # 网易的html无法包含超链接
    message = MIMEText('<html><body><h1>Hello</h1>' + '<p>send by ...</p>' + '</body></html>', 'html', 'utf-8')
    message['From'] = format_address('Python爱好者<{0}>'.format(email_test1.from_address))
    message['To'] = format_address('管理员<{0}>'.format(email_test1.to_address))
    message['Subject'] = Header('来自SMTP的问题', 'utf-8').encode()
    send_email(message)
    print('send email success')

