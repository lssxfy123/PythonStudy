# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.10.22
# 遍历文件夹下所有文件
import os


def traverse(folder_path):
    fs = os.listdir(folder_path)
    for f in fs:
        tmp_path = os.path.join(folder_path, f)
        if not os.path.isdir(tmp_path):
            print('文件:{0}'.format(tmp_path))
        else:
            traverse(tmp_path)


if __name__ == '__main__':
    folder_path = r'C:\study\Python学习'
    traverse(folder_path)
