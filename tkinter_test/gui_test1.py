# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.6.8
# gui初探
import sys
from tkinter import *


def greeting():
    print('Hello python world!...')


# 点击退出回调函数
def button_quit():
    print('Hello, I must be going...')
    sys.exit()


if __name__ == '__main__':
    widget = Frame()
    widget.pack()
    Button(widget, text='Hello', command=greeting).pack(side=LEFT, fill=Y)
    Label(widget, text='Hello container world').pack(side=TOP)
    Button(widget, text='Quit', command=button_quit).pack(side=RIGHT, expand=YES, fill=X)

    widget.mainloop()
