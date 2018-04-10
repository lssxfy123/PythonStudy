# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.8
# 导入函数模块
import pizza
import pizza as pa  # 给导入的模块指定别名

# 调用模块的函数
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers')

pa.make_pizza(15, 'green peppers')
