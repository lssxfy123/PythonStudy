#操作文件和目录
import os


#列出当前目录下所有子目录
pwd = os.path.abspath('.')

print(os.path.join(pwd, 'test1'))

L = os.listdir(os.path.join(pwd, 'test1'))

if os.path.isdir(os.path.join(pwd, 'test1', L[0])):
    print('dir')
else:
    print('not dir')

#print([x for x in os.listdir(os.path.join(pwd, 'test1/')) if os.path.isdir(x)])

#遍历指定目录及其子目录，并查找包含文件名包含1-4的文件
def sub_dir(dir_path):
    L = os.listdir(dir_path)
    for num in range(len(L)):
        name = L[num]
        
        if os.path.isdir(os.path.join(dir_path, L[num])):
            print(os.path.join(dir_path, L[num]))
            sub_dir(os.path.join(dir_path, L[num]))
        else:
            if L[num].find('1-4') >= 0:
                print(os.path.join(dir_path, L[num]))

sub_dir(pwd)

