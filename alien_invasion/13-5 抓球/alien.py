#!/usr/local/python365/bin/python3
# -*- coding:utf-8 -*-

import pygame
from pygame.sprite import Sprite



class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, ai_settings, screen):
        """初始化外星人并设置其起始位置"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图像，并设置其rect属性
        self.image = pygame.image.load('../../images/ball_little.png')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    def update(self):
        """向左或向右移动外星人"""
        self.x += 0
        self.rect.x = self.x
        self.y += self.ai_settings.fleet_drop_speed
        self.rect.y = self.y
