from game.utils.constants import BULLET_ENEMY_TYPE, BULLET_PLAYER_TYPE
from game.components.Bullets.bullet_enemy import BulletEnemy
from game.components.Bullets.bullet_spaceship import BulletSpaceship


class BulletHandler:
    def __init__(self):
        self.bullets = []

    def update(self, player, enemies):
        for bullet in self.bullets:
            if not bullet.is_alive:
                self.remove_bullet(bullet)
            else:
                if bullet.type == BULLET_ENEMY_TYPE:
                        bullet.update(player)
                else:
                    for enemy in enemies:
                        bullet.update(enemy)

    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)

    def add_bullet(self, type, center):
        if type == BULLET_ENEMY_TYPE:
            self.bullets.append(BulletEnemy(center))
        else:
            self.bullets.append(BulletSpaceship(center))
    
    def remove_bullet(self, bullet):
        self.bullets.remove(bullet)
    
    def reset(self):
        self.bullets = []