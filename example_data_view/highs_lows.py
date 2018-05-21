# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.19
# csv文件
import csv
from matplotlib import pyplot as plt
from datetime import datetime

file_name = "sitka_weather_07-2014.csv"
with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)  # 文件第1行

    highs = []  # 最高气温
    dates = []  # 日期
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)

    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red')
    plt.title("Daily high temperatures,July 2014", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
