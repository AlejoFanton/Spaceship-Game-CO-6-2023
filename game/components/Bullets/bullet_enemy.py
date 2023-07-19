import pygame
from game.components.Bullets.bullet import Bullet
from game.utils.constants import BULLET_ENEMY, BULLET_ENEMY_TYPE, SCREEN_HEIGHT, SHIELD_TYPE
from game.components.spaceship import Spaceship

class BulletEnemy(Bullet):
    WIDTH = 9
    HEIGHT = 32
    SPEED = 20

    def __init__(self, center):
        self.image = BULLET_ENEMY
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.type = BULLET_ENEMY_TYPE
        super().__init__(self.image, self.type, center)

    def update(self, player):
        self.rect.y += self.SPEED
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_alive = False
    
        if not player.power_type == SHIELD_TYPE:
            super().update(player)
