# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.30
# 描述符类方法参数测试


class Descriptor:
    def __get__(self, instance, owner):
        print(self, instance, owner, sep='\n')


class Sub:
    attr = Descriptor()


if __name__ == '__main__':
    x = Sub()
    x.attr  # 实例访问
    print()
    Sub.attr  # 类访问
