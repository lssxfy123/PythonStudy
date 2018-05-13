# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.13
# 外星人入侵主程序
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.title)

    ship = Ship(ai_settings, screen)  # 创建飞船
    bullets = Group()  # 创建子弹编组

    # 创建外星人组
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


if __name__ == '__main__':
    run_game()
