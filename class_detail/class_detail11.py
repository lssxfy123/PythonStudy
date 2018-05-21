# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.7
# __call__


class Callee:
    def __call__(self, *args, **kwargs):
        print('Called:', args, kwargs)


C = Callee()
C(1, 2, 3)  # 自动调用__call__
C(1, 2, 3, x=4, y=5)
# __call__支持所有参数传递方式
C(*[1, 2], **dict(c=3, d=4))
C(1, *(2,), c=3, **dict(d=4))
