# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.12.6
# python练习测试5：input测试
names = input("Enter names separated by commas: ")
assignments = input("Enter assignment counts separated by commas: ")
grades = input("Enter grades separated by commas: ")

names = names.split(',')
assignments = assignments.split(',')
grades = grades.split(',')

for name, assignment, grade in zip(names, assignments, grades):
    message = "Hi {},\n\nThis is a reminder that you have {} assignments left to submit before you can graduate. Your" \
              " current grade is {} and can increase to {} if you submit all assignments before " \
              "the due date\n".format(name, assignment, grade, int(grade) + 2 * int(assignment))
    print(message)
