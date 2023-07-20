from game.utils.constants import BULLET_ENEMY_TYPE, LASER_SOUND
from game.components.Bullets.bullet_enemy import BulletEnemy
from game.components.Bullets.bullet_spaceship import BulletSpaceship
from game.components.help.lifes import Life
from game.utils.constants import SCREEN_HEIGHT


class BulletHandler:
    def __init__(self):
        self.bullets = []
        self.lives = Life()
        self.laser_sound = LASER_SOUND

    def update(self, player, enemies):
        for bullet in self.bullets[:]:  # Copia de la lista para evitar problemas al eliminar elementos
            if not bullet.is_alive:
                self.bullets.remove(bullet)
            else:
                if bullet.type == BULLET_ENEMY_TYPE:
                    bullet.update(player)
                    if bullet.rect.bottom >= SCREEN_HEIGHT:
                        bullet.is_alive = False  # Marcar la bala enemiga como inactiva si llega a la parte inferior
                else:
                    for enemy in enemies:
                        bullet.update(enemy)

    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet_type, center):
        if bullet_type == BULLET_ENEMY_TYPE:
            self.bullets.append(BulletEnemy(center))
            self.laser_sound.play()
        else:
            self.bullets.append(BulletSpaceship(center))

    def reset(self):
        self.bullets = []