# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.1
# 变量、对象与类型

# 共享引用
print("不可变对象的共享引用")
a = 3
b = a
print('a = ' + str(a))
print('b = ' + str(b))

a = 'spam'
print('a = ' + a)
print('b = ' + str(b))

c = 3
d = c
c = c + 2
print('c = ' + str(c))
print('d = ' + str(d))

print()
print("可变对象的共享引用")
L1 = [1, 2, 3]
L2 = L1

L1 = 24
print("L1:" + str(L1))
print("L2:" + str(L2))
print()

L1 = [4, 5, 6]
print("L1:" + str(L1))
print("L2:" + str(L2))
print()

L3 = [1, 2, 3]
L4 = L3
L3[0] = 99
print("L3:" + str(L3))
print("L4:" + str(L4))
print(id(L3))
print(id(L4))
print()

L5 = [1, 2, 3]

# 通过拷贝后，
# L5和L6引用的对象不同
L6 = L5[:]
L5[0] = 99
print("L5:" + str(L5))
print("L6:" + str(L6))
print(id(L5))
print(id(L6))
