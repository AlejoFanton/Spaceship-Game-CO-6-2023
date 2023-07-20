import pygame
import random
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT

class PowerUp:
    SPEED=10
    WIDTH=30
    HEIGHT=30
    POS_Y = 0
    DURATION = 5000

    def __init__(self, image):
        self.image = image
        self.image = pygame.transform.scale(self.image,(self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(120, SCREEN_WIDTH - 120)
        self.rect.y = self.POS_Y
        self.is_visible = True
        self.is_used = False
        self.time_up = 0

    def update(self, player):
        self.rect.y += self.SPEED
        if self.rect.colliderect(player.rect):
            self.is_visible = False
            self.is_used = True
            self.time_up = pygame.time.get_ticks() + self.DURATION

        
    def draw(self, screen):
        screen.blit(self.image, self.rect)