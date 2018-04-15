# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.15
# 字符串格式化
import sys

template = '{0}, {1} and {2}'
print(template.format('spam', 'ham', 'eggs'))  # spam, ham and eggs
template = '{motto}, {pork} and {food}'
print(template.format(pork='ham', motto='spam', food='eggs'))  # spam, ham and eggs
template = '{motto}, {0} and {food}'
print(template.format('ham', motto='spam', food='eggs'))  # spam, ham and eggs
print()
x = '{motto}, {0} and {food}'.format(42, motto=3.14, food=[1, 2])
print(x)  # 3.14, 42 and [1, 2]
print(x.split(' and '))  # ['3.14, 42', '[1, 2]']
print(x.replace('and', 'but under no'))  # 3.14, 42 but under no [1, 2]

# My laptop runs win32
print('My {config[spam]} runs {sys.platform}'.format(sys=sys, config={'spam': 'laptop'}))
print()
# {0:10}, 0代表第一个参数，10字符宽
# spam       =   123.4567
print('{0:10} = {1:10}'.format('spam', 123.4567))

# {0:>10}:第一个参数，10字符宽，右对齐
# {1:<10}：第二个参数，10字符宽，左对齐
#       spam = 123.4567
print('{0:>10} = {1:<10}'.format('spam', 123.4567))

#      win32 = laptop
print('{0.platform:>10} = {1[item]:<10}'.format(sys, {'item': 'laptop'}))
print()

# 3.141590e+00, 3.142e+00
print('{0:e}, {1:.3e}'.format(3.14159, 3.14159))
