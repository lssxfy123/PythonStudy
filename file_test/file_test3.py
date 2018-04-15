# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.15
# 文件解析
import pickle


with open('datafile.txt') as file_obj:
    line = file_obj.readline()
    print(line)
    parts = line.split('$')
    # eval()将字符串转换为python对象
    objects = [eval(part) for part in parts]
    print(objects)
print()

# 存储python的原生对象
data = {'a': 1, 'b': 2}
with open('pythondata.pkl', 'wb') as file_save:
    pickle.dump(data, file_save)


# 读取
with open('pythondata.pkl', 'rb') as file_read:
    e = pickle.load(file_read)
    print(e)
