# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.13
# 设置


class Settings:

    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.title = "Alien Invasion"
        self.ship_speed_factor = 1.5  # 飞船速度因子

        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (60, 60, 60)

        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10

        # 1向右移，-1向左移
        self.fleet_direction = 1
