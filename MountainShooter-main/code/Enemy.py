#!/usr/bin/python
# -*- coding: utf-8 -*-


import pygame
import math
import random
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_WIDTH, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
class Enemy3(Enemy):
    def __init__(self,name: str,position: tuple ):
        super().__init__(name, position)
        self.vertical_speed = 2
        self.amplitude = 30
        self.direction = 1

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

        if self.rect.centery >= WIN_HEIGHT-40:
            self.direction = -1
            self.vertical_speed = 4
        elif self.rect.centery <= 40:
            self.direction = 1
            self.vertical_speed = 2
        self.rect.centery += self.vertical_speed * self.direction

        if self.rect.centerx < -50:
            self.rect.centerx = WIN_WIDTH + 10
            self.rect.centery = random.randint(40, WIN_HEIGHT - 40)

    def shoot(self):
        if random.randint(1, 100) <= 5:
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))