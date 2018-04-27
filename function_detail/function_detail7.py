# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.24
# 递归函数


def my_sum(L):
    if not L:
        return 0
    else:
        return L[0] + my_sum(L[1:])


def my_sum1(L):
    return 0 if not L else L[0] + my_sum1(L[1:])


print(my_sum([1, 2, 3, 4, 5]))  # 15
print(my_sum1([1, 2, 3, 4, 5]))  # 15


# 一般不提倡递归，但递归可以出来嵌套的序列
def sumtree(L):
    tot = 0
    for x in L:
        if not isinstance(x, list):
            tot += x
        else:
            tot += sumtree(x)
    return tot


L = [1, [2, [3, 4], 5], 6, [7, 8]]
print(sumtree(L))  # 36
print(sumtree([1, [2, [3, [4, [5]]]]]))  # 15
