import pygame
from game.components.enemies.enemy_handler import EnemyHandler
from game.utils import text_utils
from game.utils.constants import WHITE

class LevelHandler:
    def __init__(self):
        self.levels = []
        self.current_level_index = 0
        self.is_countdown_active = False
        self.countdown_timer = 0
        self.countdown_duration = 3000

    def add_level(self, enemy_count, enemy_handler=None):
        if enemy_handler is None:
            enemy_handler = EnemyHandler()
        level = {
            'enemy_count': enemy_count,
            'enemy_handler': enemy_handler,
        }
        self.levels.append(level)

    def get_current_level(self):
        if self.current_level_index < len(self.levels):
            return self.levels[self.current_level_index]
        else:
            return None

    def update(self, bullet_handler):
        current_level = self.get_current_level()
        if self.is_countdown_active:
            self.countdown_timer -= pygame.time.get_ticks()
            if self.countdown_timer <= 0:
                self.is_countdown_active = False
                self.advance_to_next_level()
        else:
            if current_level:
                current_level['enemy_handler'].update(bullet_handler)
                if self.is_level_completed():
                    self.is_countdown_active = True
                    self.countdown_timer = self.countdown_duration

    def draw(self, screen):
        current_level = self.get_current_level()
        if self.is_countdown_active:
            countdown_seconds = int(self.countdown_timer / 1000) + 1
            countdown_text = f"The next level will start in: {countdown_seconds} seconds"
            text, text_rect = text_utils.get_message(countdown_text, 40, WHITE)
            screen.blit(text,text_rect)
        elif current_level:
            current_level['enemy_handler'].draw(screen)
        

    def is_level_completed(self):
        current_level = self.get_current_level()
        if current_level:
            return current_level['enemy_handler'].number_enemy_destroyed >= current_level['enemy_count']
        else:
            return False

    def advance_to_next_level(self):
        self.current_level_index += 1
        if self.current_level_index >= len(self.levels):
            self.current_level_index = len(self.levels) - 1

    def reset(self):
        self.current_level_index = 0
        for level in self.levels:
            level['enemy_handler'].reset()