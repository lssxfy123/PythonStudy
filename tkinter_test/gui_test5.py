# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.6.8
# 多个独立窗口
import tkinter
from tkinter import Tk, Button
tkinter.NoDefaultRoot()

# 两个独立的根窗口
win1 = Tk()
win2 = Tk()

Button(win1, text='Spam', command=win1.destroy).pack()
Button(win2, text='SPAM', command=win2.destroy).pack()
win1.mainloop()
