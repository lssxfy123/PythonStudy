# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.20
# while循环详解
x = 'spam'
while x:
    print(x, end=' ')  # spam pam am m
    x = x[1:]
print()

# while与else的结合
m = 7
n = m // 2  # floor除法

# while循环如果发生break，就不会执行else
# 如果while循环的条件不再满足，就会执行else语句块
# 这种用法可以省去其他语言类似功能需要的标志位
while n > 1:
    if m % n == 0:
        print(m, 'has factor', n)
        break
    n -= 1
else:
    print(m, 'is prime')
