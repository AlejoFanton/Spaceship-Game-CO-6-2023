import pygame
from game.utils.constants import HEART

class Life:
    def __init__(self, icon_size=32):
        self.max_lives = 3
        self.current_lives = self.max_lives
        self.life_image = HEART
        self.icon_size = icon_size
        self.life_image = pygame.transform.scale(HEART, (self.icon_size, self.icon_size))
        self.life_rect = self.life_image.get_rect()
        self.life_rect.x = 10  
        self.life_rect.y = 10  
    
    def update(self):
        self.reduce_life()

    def reduce_life(self):
        if self.current_lives > 0:
            self.current_lives -= 1

    def is_game_over(self):
        return self.current_lives <= 0

    def draw(self, screen):
        for i in range(self.current_lives):
            x_offset = i * (self.life_rect.width + 5)
            screen.blit(self.life_image, (self.life_rect.x + x_offset, self.life_rect.y))

    def reset(self):
        self.current_lives = self.max_lives