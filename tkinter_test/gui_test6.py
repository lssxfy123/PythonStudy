# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.6.8
# 对话框
from tkinter import *
from tkinter.messagebox import *


def callback():
    if askyesno('Verify', 'Do you really want to quit?'):
        showwarning('Yes', 'Quit not yet implemented')  # 提示
    else:
        showinfo('No', 'Quit has been cancelled')  # 信息


if __name__ == '__main__':
    error = 'Sorry, no Spam allowed'
    Button(text='Quit', command=callback).pack(fill=X)
    Button(text='Spam', command=(lambda: showerror('Spam', error))).pack(fill=X)
    mainloop()
