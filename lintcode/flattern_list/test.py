# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.9.2
# lintcode：平面列表
import copy


def flatten(nestedList):
    result = []
    flag = False
    while True:
        for item in nestedList:
            if isinstance(item, list):
                flag = True
                for child in item:
                    result.append(child)
            else:
                result.append(item)
        if flag:
            nestedList = copy.deepcopy(result)
            result.clear()
            flag = False
        else:
            return result


def flatten1(nestedList):
    stack = [nestedList]
    flatten_list = []

    while stack:
        top = stack.pop()  # 移除最后一个元素
        if isinstance(top, list):
            for elem in reversed(top):  # 反向遍历
                stack.append(elem)
        else:
            flatten_list.append(top)

    return flatten_list


if __name__ == '__main__':
    nested_list = [1, 2, [1, 2, [1, 3]]]
    result = flatten(nested_list)
    print(result)
    result = flatten1(nested_list)
    print(result)
