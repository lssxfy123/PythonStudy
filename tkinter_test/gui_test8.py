# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.6.8
# 菜单
from tkinter import *
from tkinter.messagebox import *


def not_done():
    showerror('Not', 'Not yet available')


def make_menu(win):
    top = Menu(win)
    win.config(menu=top)
    file = Menu(top)
    file.add_command(label='New...', command=not_done, underline=0)
    file.add_command(label='Open...', command=not_done, underline=0)
    file.add_command(label='Quit', command=win.quit, underline=0)
    top.add_cascade(label='File', menu=file, underline=0)

    edit = Menu(top, tearoff=False)
    edit.add_command(label='Cut', command=not_done, underline=0)
    edit.add_command(label='Paste', command=not_done, underline=0)
    edit.add_separator()
    top.add_cascade(label='Edit', menu=edit, underline=0)

    sub_menu = Menu(edit, tearoff=True)
    sub_menu.add_command(label='Spam', command=win.quit, underline=0)
    sub_menu.add_command(label='Eggs', command=not_done, underline=0)
    edit.add_cascade(label='Stuff', menu=sub_menu, underline=0)


if __name__ == '__main__':
    root = Tk()
    root.title('menu window')
    make_menu(root)
    message = Label(root, text='Window menu basic')
    message.pack(expand=YES, fill=BOTH)
    message.config(relief=SUNKEN, width=40, height=7, bg='beige')
    root.mainloop()
