# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.6.7
# smtp邮件发送附件
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import email_test1
from email_test1 import format_address
from email_test1 import send_email

if __name__ == '__main__':
    message = MIMEMultipart()
    message['From'] = format_address('Python爱好者<{0}>'.format(email_test1.from_address))
    message['To'] = format_address('管理员<{0}>'.format(email_test1.to_address))
    message['Subject'] = Header('来自SMTP的问题', 'utf-8').encode()

    # 正文
    message.attach(MIMEText('Hello, send by Python...', 'plain', 'utf-8'))

    # 附件添加一个图片
    with open('..\\file_test\\画板.png', 'rb') as file:
        mime = MIMEBase('image', 'png', filename='test.png')
        mime.add_header('Content-Disposition', 'attachment', filename='test.png')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        mime.set_payload(file.read())
        encoders.encode_base64(mime)
        message.attach(mime)

    send_email(message)
    print('send email success')
