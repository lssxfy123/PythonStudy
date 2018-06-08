# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.6.8
# gui按钮与鼠标
from tkinter import *

widget = Button(text='Spam', padx=10, pady=10)
widget.pack(padx=20, pady=20)
widget.config(cursor='gumby')
widget.config(bd=8, relief=RAISED)
widget.config(bg='dark green', fg='white')
widget.config(font=('helvetica', 20, 'underline italic'))
mainloop()
