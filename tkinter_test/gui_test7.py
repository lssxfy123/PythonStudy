# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.6.8
# 对话框演示
from tkinter.filedialog import askopenfilename
from tkinter.colorchooser import askcolor
from tkinter.messagebox import askquestion, showerror
from tkinter.simpledialog import askfloat
from tkinter import *


demos = {
    'Open': askopenfilename,
    'Color': askcolor,
    'Query': lambda: askquestion('Warning', 'You typed "rm *"\n Confirm?'),
    'Error': lambda: showerror('Error!', "He's dead, Jim"),
    'Input': lambda: askfloat('Entry', 'Enter credit card number')
}


class Demo(Frame):
    def __init__(self, parent=None, **options):
        super().__init__(parent, **options)
        self.pack()
        Label(self, text='Basic demos').pack()
        for key, value in demos.items():
            Button(self, text=key, command=value).pack(side=TOP, fill=BOTH)


if __name__ == '__main__':
    Demo().mainloop()
