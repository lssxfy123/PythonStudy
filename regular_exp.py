#正则表达式
import re
test = '010-1234567'

if re.match(r'\d{3}-\d{3,8}', test):
    print('ok')
else:
    print('failed')
