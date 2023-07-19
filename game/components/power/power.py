import pygame
import random
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Power:
    POWER_SPEED=10
    POWER_WIDTH=30
    POWER_HEIGHT=30

    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.image = pygame.transform.scale(self.image,(self.POWER_WIDTH, self.POWER_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(120, SCREEN_WIDTH - 120)
        self.rect.y = 0
        self.is_alive = True

    def update(self):
        self.rect.y += self.POWER_SPEED
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_alive = False
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)