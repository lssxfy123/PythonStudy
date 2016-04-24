#list列表生成式
#生成[1x1, 2x2, ..., 10x10]
L = [x * x for x in range(1, 11)]
print('[1x1, 2x2, ..., 10x10]', L)

L1 = [x * x for x in range(1, 11) if x % 2 == 0]
print('[2x2, 4x4, ..., 10x10]', L1)

#两次for循环生成全排列
L2 = [m + n for m in 'ABC' for n in 'XYZ']
print('ABC和XYZ的全排列', L2)

#当前目录下的所有文件和目录名
import os
L3 = [dir for dir in os.listdir('.')]
print('当前目录下的所有文件和目录名', L3)

d = {'x' : 'A', 'y' : 'B', 'z' : 'C'}
L4 = [key + '=' + value for key, value in d.items()]
print(L4)

#将list中的字符串变成小写
L5 = ['Hello', 'World', 'IBM', 'Apple']
L6 = [s.lower() for s in L5]
print('[\'Hello\', \'World\', \'IBM\', \'Apple\']大写转小写', L6)

#将list中的合法字符串变成小写
L7 = ['APPLE', 'IBM', 17, 'WINDOWS', None]
L8 = [s.lower() for s in L7 if isinstance(s, str)]
print('[\'APPLE\', \'IBM\', 17, \'WINDOWS\', None]大写转小写', L8)