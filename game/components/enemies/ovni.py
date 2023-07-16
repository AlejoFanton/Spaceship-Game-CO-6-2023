import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_2

class ShipOvni(Enemy):
    WIDHT = 40
    HEIGHT = 60

    def __init__(self):
        self.image = ENEMY_2
        self.image = pygame.transform.scale(self.image,(self.WIDHT,self.HEIGHT))
        super().__init__(self.image)
