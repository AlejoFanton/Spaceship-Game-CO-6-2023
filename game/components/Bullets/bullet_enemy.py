import pygame

from game.utils.constants import BULLET_ENEMY
from game.components.Bullets.bullet import Bullet

class BulletEnemy(Bullet):
    WIDTH = 9
    HEIGHT = 12
    SPEED = 20

    def __init__(self, center):
        self.image = BULLET_ENEMY
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image, center)

    def update(self, player):
        self.rect.y += self.SPEED
        super().update(player)
