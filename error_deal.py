#错误处理
#try...except...finally
try:
    print('try...')
    result = 10 / 0
    print('result:', result)
except ZeroDivisionError as e:
    print('except', e)
finally:
    print('finally...')

print('END')

try:
    print('try...')
    result1 = 10 / int('2')
    print('resutl1', result1)

    result2 = 10 / int('a')
    print('resutl2', result2)

except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError', e)
finally:
    print('finally...')

print('END')


import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 3

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
    finally:
        print('finally...')

main()
print('END')


def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s'% s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()

