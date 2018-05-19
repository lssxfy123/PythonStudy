# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.19
# 骰子
from random import randint


class Die:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)
