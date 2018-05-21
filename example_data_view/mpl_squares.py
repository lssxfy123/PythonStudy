# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.19
# 数据可视化-折线图
import matplotlib.pyplot as plt

input_vales = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_vales, squares, linewidth=5)
plt.title("Square Numbers", fontsize=14)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.show()
