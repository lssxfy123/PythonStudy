# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.12
# 字符串方法
s = 'Spam'
print('position ', s.find('pa'))

# 字符串具有不可变性
s1 = s.replace('pa', 'XYZ')
print(s)  # Spam
print(s1)  # SXYZm

line = 'aaa,bbb,ccccc,dd'
print(line.split(','))  # 返回列表

# 格式化输出
print('%s, eggs, and %s' % ('spam', 'SPAM!'))  # spam, eggs, and SPAM!
print('{0}, eggs, and {1}'.format('spam', 'SPAM!'))  # spam, eggs, and SPAM!
print()

# 查找字符串的方法
print(dir(s))
