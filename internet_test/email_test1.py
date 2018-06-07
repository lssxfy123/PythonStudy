# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.6.7
# smtp邮件
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


def format_address(s):
    name, address = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), address))


from_address = 'liushenshenxfy@126.com'
password = 'lss19871203'
to_address = '357455175@qq.com'
smtp_server = 'smtp.126.com'


def send_email(message):
    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_address, password)
    server.sendmail(from_address, [to_address], message.as_string())
    server.quit()


if __name__ == '__main__':
    # 发送纯文本
    message = MIMEText('Hello, send by Python...', 'plain', 'utf-8')
    message['From'] = format_address('Python爱好者<{0}>'.format(from_address))
    message['To'] = format_address('管理员<{0}>'.format(to_address))
    message['Subject'] = Header('来自SMTP的问题', 'utf-8').encode()
    send_email(message)
    print('send email success')
