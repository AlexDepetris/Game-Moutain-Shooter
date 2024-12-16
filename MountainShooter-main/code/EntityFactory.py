#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy, Enemy3
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, level: int = 1):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):  # level1bg images number
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Level2Bg':
                list_bg = []
                for i in range(5):  # level2bg images number
                    list_bg.append(Background(f'Level2Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level2Bg{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'Level3Bg':
                list_bg = []
                for i in range(5):  # level3bg images number
                    list_bg.append(Background(f'Level3Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level3Bg{i}', (WIN_WIDTH, 0)))

                if level == 3:
                    enemies = []
                    for i in range(10):
                        enemies.append(Enemy3('Enemy3',(WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT -40))))
                    list_bg.append(enemies)
                return list_bg


            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2 - 30))
            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy3':
                return Enemy3('Enemy3', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))

    @staticmethod
    def load_enemies(level: int):
        enemies = []
        if level == 3:
            for i in range(10):
                enemies.append(Enemy3('Enemy3',(WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40))))
        elif level == 4:
            for i in range(10):
                enemies.append(Enemy('Enemy2',(WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40))))
        else:
            for i in range(10):
                enemies.append(Enemy('Enemy1',(WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40))))
        return enemies