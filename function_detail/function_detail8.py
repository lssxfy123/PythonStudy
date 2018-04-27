# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.24
# 函数对象


# 间接函数调用
def echo(message):
    print(message)


def indirect(func, arg):
    func(arg)


indirect(echo, "Argument Call")  # Argument Call
print()

# 函数本身是对象，可以存储在序列中
schedule = [(echo, 'Spam!'), (echo, 'Ham!')]
for (func, arg) in schedule:
    func(arg)
    # func.count += 1  # Error，echo没有属性count
print()

# 函数属性，类似类对象的属性
echo.count = 0
schedule1 = [(echo, 'Spam1!'), (echo, 'Ham1!')]
for (func, arg) in schedule1:
    func(arg)
    func.count += 1  # OK, echo有count属性
