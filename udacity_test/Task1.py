"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."
"""
total_telephone_numbers = []


def get_total_telephone_numbers(telephone_list):
    for item in telephone_list:
        if item[0] not in total_telephone_numbers:
            total_telephone_numbers.append(item[0])

        if item[1] not in total_telephone_numbers:
            total_telephone_numbers.append(item[1])


get_total_telephone_numbers(texts)
get_total_telephone_numbers(calls)

print(len(total_telephone_numbers))
