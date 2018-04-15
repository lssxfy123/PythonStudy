# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.15
# 字符串扩展
print('spam', repr('spam'))  # spam 'spam'

s = 'xxxxSPAMxxxxSPAMxxxx'
where = s.find('SPAM')
print(where)  # 4
s1 = s[:where] + 'EGGS' + s[(where+4):]
print(s1)  # xxxxEGGSxxxxSPAMxxxx
print()
s2 = s.replace('SPAM', 'EGGS')
print(s2)  # xxxxEGGSxxxxEGGSxxxx
print()
s3 = s.replace('SPAM', 'EGGS', 1)
print(s3)  # xxxxEGGSxxxxSPAMxxxx
