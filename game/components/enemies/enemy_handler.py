from game.components.enemies.ship import Ship
from game.components.enemies.ovni import ShipOvni
from game.components.enemies.hunter import ShipHunter
from game.components.enemies.enemy_3 import ShipEnemy3
from game.components.enemies.enemy_5 import ShipEnemy5

class EnemyHandler:
    def __init__(self):
        self.enemies = []

    def update(self):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update()
            if not enemy.is_visible:
                self.remove_enemy(enemy)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < 3:
            self.enemies.append(Ship())
        if len(self.enemies) < 3:
            self.enemies.append(ShipOvni())
        if len(self.enemies) < 3:
            self.enemies.append(ShipHunter())
        if len(self.enemies) < 5:
            self.enemies.append(ShipEnemy3())
        if len(self.enemies) < 5:
            self.enemies.append(ShipEnemy5())

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)