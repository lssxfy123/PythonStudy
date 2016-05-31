#操作文件和目录
import os
print(os.name)
print(os.uname())
print(os.environ)
print(os.environ.get('PATH'))

print(os.path.abspath('.'))

#获取当前目录的绝对路径
s = os.path.abspath('.')

#在当前目录下创建一个testdir文件夹
new_dir = os.path.join(s, 'testdir')
os.mkdir(new_dir)

#列出当前目录下所有后缀名为.py的文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])
