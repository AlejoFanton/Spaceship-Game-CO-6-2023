import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_5

class ShipStellar(Enemy):
    WIDHT = 40
    HEIGHT = 60

    def __init__(self):
        self.image = ENEMY_5
        self.image = pygame.transform.scale(self.image,(self.WIDHT,self.HEIGHT))
        super().__init__(self.image)