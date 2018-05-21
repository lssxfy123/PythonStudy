# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.19
# 掷骰子-条形图
from die import Die
import pygal

die = Die()
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

frequencies = []

for value in range(1, die.num_sides):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
