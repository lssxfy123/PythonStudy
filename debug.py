#错误调试
#断言
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

#foo('0')

#日志logging
import logging
logging.basicConfig(level = logging.INFO) #设置日志的记录级别

def foo(s):
    n = int(s)
    logging.info('n = %d'% n)
    return 10 / n

foo('0')
