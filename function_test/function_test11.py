# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.8
# 导入模块中指定的函数
from pizza import make_pizza
from pizza import make_pizza as mp  # 导入的函数指定别名
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers')

# 通过别名调用函数
mp(15, 'green peppers')
