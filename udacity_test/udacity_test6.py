# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.12.7
# python练习测试6：异常捕获


def create_groups(items, num_groups):
    try:
        groups = []
        size = len(items) // num_groups
        for i in range(0, len(items), size):
            groups.append(items[i:i + size])
    except ZeroDivisionError:
        print('WARNING: Returning empty list. Please use a nonzero number.')
    finally:
        print('{} groups returned.'.format(num_groups))
        return groups


print("Creating 6 groups...")
for group in create_groups(range(32), 6):
    print(list(group))

print("\nCreating 0 groups...")
for group in create_groups(range(32), 0):
    print(list(group))


def func():
    print("udacity test 6")
