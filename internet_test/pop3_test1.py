# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.6.7
# pop3接收邮件
import poplib
from email.parser import Parser

email = 'liushenshenxfy@126.com'
password = 'lss19871203'
pop3_server = 'pop.126.com'

server = poplib.POP3(pop3_server)
server.set_debuglevel(1)

server.user(email)
server.pass_(password)
print('Messages: {0}, Size: {1}'.format(server.stat()[0], server.stat()[1]))

resp, mails, octets = server.list()

# 获取最新邮件
index = len(mails)
resp, lines, octets = server.retr(index)
message_content = b'\r\n'.join(lines).decode('utf-8')
message = Parser().parsestr(message_content)

server.quit()
