#POP3邮件服务
#收取邮件
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

import poplib

#邮件地址，口令和POP3服务器地址
email_addr = input('Email: ')
password = input('Password: ')
pop3_server = input('POP3 server: ')

server = poplib.POP3(pop3_server)
server.set_debuglevel(1)

#身份认证
server.user(email_addr)
server.pass_(password)

#返回邮件数量和占用空间
print('Messages: %s. Size: %s' % server.stat())

#list()返回所有邮件的编号
resp, mails, octets = server.list()

index = len(mails)
resp, lines, octets = server.retr(index)

#获得整个邮件的原始文本
msg_content = b'\n'.join(lines).decode('utf-8')

#解析邮件
msg = Parser().parsestr(msg_content)
#print('msg: ', msg)
server.quit()

def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        print('content-type', content_type)
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset

def print_info(msg, indent = 0):
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % (' ' * indent, header, value))

    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % (' ' * indent, n))
            print('%s---------------' % (' ' * indent))
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            content = msg.get_payload(decode = True)
            charset = guess_charset(msg)
            print('content: ', content)
            print('charset: ', charset)
            if charset:
                content = content.decode(charset)
                print('%sText: %s' % (' ' * indent, content + '...'))
        else:
            print('%sAttachment: %s' % (' ' * indent, content_type))




print('print receive email------------------------')
print_info(msg)


