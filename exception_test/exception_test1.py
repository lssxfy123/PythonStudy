# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.10
# 异常处理
try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")
print()

try:
    print("try...")
    result = 10 / int(input('division number: '))
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:  # 没有异常发生会自动执行else块
    print('no error!')
    print('result ', result)
finally:  # 无论如何都会执行的块
    print("divide finally")
print()

# 处理文件异常
file_name = 'alice.txt'
try:
    with open(file_name) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + file_name + " doesn't exist"
    print(msg)
else:
    print("The file " + file_name + " has about " + str(len(contents)) + " words")