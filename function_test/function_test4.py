# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.4
# 函数中修改参数


def modify(para):
    if isinstance(para, int):
        print("para is int.")
        para = 5
    elif isinstance(para, str):
        print("para is string.")
        para = 'Jam'
    elif isinstance(para, list):
        print("para is list.")
        # para = ['hamster']
        para.append('cat')
    print("In modify() para is modified: " + str(para))


parameter = 1
print("before modify(): " + str(parameter))
modify(parameter)
print("after modify(): " + str(parameter))
print()

parameter = 'Tom'
print("before modify(): " + str(parameter))
modify(parameter)
print("after modify(): " + str(parameter))
print()

parameter = ['dog']
print("before modify(): " + str(parameter))
modify(parameter)
print("after modify(): " + str(parameter))
