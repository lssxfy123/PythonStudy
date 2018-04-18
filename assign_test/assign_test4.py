# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.18
# 增强赋值
# Python中的增强赋值种类
# += &= -= |= *= ^= /= >>= %= <<= **= //=

# 增强赋值后 L的id不变，列表支持原处修改
L = [1, 2, 3]
print("L id: ", id(L))  # 830456954632
L += [4, 5]  # 增强赋值，在原处修改
print("after increase L id: ", id(L))  # 830456954632
print()

# 合并会产生新的对象，合并后的L1的id与之前的不同
L1 = [1, 2, 3]
print("L1 id: ", id(L1))  # 830456954568
L1 = L1 + [4, 5]  # 合并，产生新的对象
print("after merge L1 id: ", id(L1))  # 830456030472
print()

# 不变对象不支持原处修改，增强赋值
# 会产生新的对象
a = 1
print("a id: ", id(a))
a += 2
print("after increase a id: ", id(a))

X = Y = [1, 2, 3]
print("X = ", X, " Y = ", Y)  # X =  [1, 2, 3]  Y =  [1, 2, 3]
X += [4, 5]
print("X = ", X, " Y = ", Y)  # X =  [1, 2, 3, 4, 5]  Y =  [1, 2, 3, 4, 5]
