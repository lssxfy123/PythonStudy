# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.11
# 作用域
languages = ['English', 'Chinese']
for language in languages:
    study = language

print(study)  # OK
print(language)  # OK

if len(languages) > 0:
    money = '1000'
else:
    money = '0'
print(money)  # OK

while len(languages) > 0:
    name = 'Tom'
    break
print(name)  # OK

try:
    result = 10 / 5
except ZeroDivisionError:
    result = 'Error'
print(result)  # OK
