# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.12
# unicode
import sys

B = b'spam'
S = 'spam'
print(type(B))  # <class 'bytes'>
print(type(S))  # <class 'str'>
print(B[0], S[0])  # 115 s
print(sys.getdefaultencoding())  # utf-8

# 编码与解码
S = '\u00c4\u00e8'
print(S)  # Äè
print(len(S))  # 2
print(S.encode('utf-8'))  # b'\xc3\x84\xc3\xa8'
print(len(S.encode('utf-8')))  # 4
print()

B = b'\xc3\x84\xc3\xa8'
print(B)  # b'\xc3\x84\xc3\xa8'
print(len(B))  # 4
print(B.decode('utf-8'))  # Äè
print(len(B.decode('utf-8')))  # 2
