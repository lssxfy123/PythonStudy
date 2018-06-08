# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.6.8
# 绑定事件
from tkinter import *


def show_pos_event(event):
    print('Widget={0}, X={1}, Y={2}'.format(event.widget, event.x, event.y))


def show_all_event(event):
    print(event)
    for attr in dir(event):
        if not attr.startswith('__'):
            print(attr, '=>', getattr(event, attr))


# 键按下
def on_key_press(event):
    print('Got key press:', event.char)


# 向上箭头按下
def on_arrow_key(event):
    print('Got up arrow key press')


# 回车按钮
def on_return_key(event):
    print('Got return key press')


# 鼠标左键点击
def on_left_click(event):
    print('Got left mouse button click:', end=' ')
    show_pos_event(event)


# 鼠标右键
def on_right_click(event):
    print('Got right mouse button click:', end=' ')
    show_pos_event(event)


# 鼠标中间按钮
def on_middle_click(event):
    print('Got middle mouse button click:', end=' ')
    show_pos_event(event)
    show_all_event(event)


# 左键拖动
def on_left_drag(event):
    print('Got left mouse button drag:', end=' ')
    show_pos_event(event)


# 鼠标左键双击
def on_double_left_click(event):
    print('Got double left mouse click:', end=' ')
    show_pos_event(event)
    tk_root.quit()


if __name__ == '__main__':
    tk_root = Tk()
    label_font = ('courier', 20, 'bold')
    widget = Label(tk_root, text='Hello bind world')
    widget.config(bg='red', font=label_font)
    widget.config(height=5, width=20)
    widget.pack(expand=YES, fill=BOTH)

    widget.bind('<Button-1>', on_left_click)
    widget.bind('<Button-3>', on_right_click)
    widget.bind('<Button-2>', on_middle_click)

    widget.bind('<Double-1>', on_double_left_click)
    widget.bind('<B1-Motion>', on_left_drag)
    widget.bind('<KeyPress>', on_key_press)
    widget.bind('<Up>', on_arrow_key)
    widget.bind('<Return>', on_return_key)
    widget.focus()
    tk_root.title('Click Me')
    tk_root.mainloop()
