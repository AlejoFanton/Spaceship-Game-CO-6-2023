import pygame
from game.components.Bullets.bullet import Bullet
from game.utils.constants import BULLET_ENEMY, BULLET_ENEMY_TYPE, SCREEN_HEIGHT

class BulletEnemy(Bullet):
    WIDTH = 9
    HEIGHT = 32
    SPEED = 20

    def __init__(self, center):
        # Cargar y escalar la imagen del proyectil del enemigo
        self.image = BULLET_ENEMY
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))

        # Establecer el tipo de proyectil del enemigo
        self.type = BULLET_ENEMY_TYPE

        # Inicializar la clase base (Bullet) con la imagen y el tipo
        super().__init__(self.image, self.type, center)

    def update(self, player):
        # Mover el proyectil hacia abajo (enemigo)
        self.rect.y += self.SPEED

        # Si el proyectil alcanza la parte inferior de la pantalla, se marca como inactivo
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_alive = False

        # Si el jugador no tiene escudo, se llama al método de actualización de la clase base (Bullet)
        if not player.has_shield:
            super().update(player)
