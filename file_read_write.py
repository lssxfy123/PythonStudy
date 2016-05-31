#文件读写
#与C兼容

#写文件
with open('test.txt', 'w', encoding = 'gbk') as f:
    f.write('测试\n')
    f.write('学习\n')

with open('test1.txt', 'w', encoding = 'gbk') as f:
    L = ['测试\n', '学习\n']
    f.writelines(L)

with open('test2.txt', 'a+', encoding = 'gbk') as f:
    f.write('重复添加\n')

#读文件
with open('test.txt', 'r', encoding = 'gbk') as f:
    print(f.read())

with open('test2.txt', 'r', encoding = 'gbk') as f:
    for line in f.readlines():
        print(line.strip())
