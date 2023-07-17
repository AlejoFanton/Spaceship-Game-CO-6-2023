import pygame
from game.components.enemies.enemy_handler import EnemyHandler
from game.utils.constants import WHITE_COLOR

class LevelHandler:
    def __init__(self):
        self.levels = []
        self.current_level_index = 0
        self.is_countdown_active = False
        self.countdown_timer = 0
        self.countdown_duration = 3000

    def update(self):
        pass

    def draw(self):
        pass

    def add_level(self, enemy_count):
        level = {
            'enemy_count': enemy_count,
            'enemy_handler': EnemyHandler(),
        }
        self.levels.append(level)
    
    def get_current_level(self):
        if self.current_level_index < len(self.levels):
            return self.levels[self.current_level_index]
        else:
            return None