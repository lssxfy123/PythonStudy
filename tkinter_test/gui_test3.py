# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.6.8
# gui外观
from tkinter import *

root = Tk()
widget = Label(root, text='Hello config world')
widget.config(bg='black', fg='yellow')
label_font = ('times', 20, 'bold')
widget.config(font=label_font)
widget.config(height=3, width=20)
widget.pack(expand=YES, fill=BOTH)
root.mainloop()
