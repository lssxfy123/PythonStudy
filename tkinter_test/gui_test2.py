# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.6.8
# 自定义按钮
from tkinter import *


# 自定义Button
class HelloButton(Button):
    def __init__(self, parent=None, **config):
        super().__init__(parent, **config)
        self.pack()
        self.config(command=self.callback)

    def callback(self):
        print('Goodbye world...')
        self.quit()


if __name__ == '__main__':
    HelloButton(text='Hello subclass world!').mainloop()

