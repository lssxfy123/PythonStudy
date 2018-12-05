# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.2
# 相等的判断
a = 3
b = 3

print("a == b:" + str(a == b))
print("a is b:" + str(a is b))
print()

tuple_a = 1, 2  # 元组可以省略()
tuple_b = (1, 2)

print("tuple_a == tuple_b:" + str(tuple_a == tuple_b))  # True
print("tuple_a is tuple_b " + str(tuple_a is tuple_b))  # False
print()

L = [1, 2, 3]
M = [1, 2, 3]
print("L == M:" + str(L == M))
print("L is M:" + str(L is M))
print()

L1 = [1, 2, 3]
M1 = L1
print("L1 == M1:" + str(L1 == M1))
print("L1 is M1:" + str(L1 is M1))
