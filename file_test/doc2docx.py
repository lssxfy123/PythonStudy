# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.10.22
# 所有doc文件转换docx
import os
import win32com.client as win32

all_file_list = []


def traverse(folder_path):
    fs = os.listdir(folder_path)

    try:
        for f in fs:
            tmp_path = os.path.join(folder_path, f)
            if not os.path.isdir(tmp_path):
                file_split_part = os.path.splitext(tmp_path)
                if len(file_split_part) == 2 and file_split_part[1] == '.doc' \
                        and not os.path.exists(file_split_part[0] + '.docx') \
                        and not file_split_part[0].startswith('~$'):
                    all_file_list.append(tmp_path)
            else:
                traverse(tmp_path)
    except:
        pass


def doc2docx():
    if len(all_file_list) == 0:
        return
    
    try:
        word = win32.gencache.EnsureDispatch('Word.Application')
        for file in all_file_list:
            print(file)
            file_split_part = os.path.splitext(file)
            docx_name = file_split_part[0] + '.docx'
            doc = word.Documents.Open(file)
            doc.SaveAs(docx_name, 16)
            doc.Close()
        word.Application.Quit()
    except:
        print('Exception')


if __name__ == '__main__':
    folder_path = os.getcwd()  # r'C:\Users\Zhao.LJ\Desktop\中国农业出版社'
    print('开始将doc转换为docx')
    traverse(folder_path)
    doc2docx()
    print('转换完成')
