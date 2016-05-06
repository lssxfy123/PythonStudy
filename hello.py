#模块测试
#一个.py文件就是一个模块
__author__ = 'liu shen shen'

import sys #导入sys模块

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello world!')
    elif len(args) == 2:
        print('Hello, %s!'% args[1])
    else:
        print('Too many arguments!')

#执行python3 hello.py时，python解释器把一个特殊变量__name__置为__main__，
#如果在其它地方导入该hello模块，if判断将失败
if __name__ == '__main__':
    test()
