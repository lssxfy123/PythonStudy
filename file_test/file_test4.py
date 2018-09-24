# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.9.9
# 图片删除
import os


def file_name(file_dir):
    ret = []
    for root, dirs, files in os.walk(file_dir):
        for file_path in files:
            tmp = os.path.join(root, file_path)
            size = os.path.getsize(tmp)
            if size < 1024:
                ret.append(tmp)
    return ret


def remove_file(file_list):
    for file in file_list:
        os.remove(file)


if __name__ == '__main__':
    root_dir = r"D:\tool"
    print(file_name(root_dir))

