import random
import time

from game.components.enemies.ship import Ship
from game.components.enemies.ship_ovni import ShipOvni
from game.components.enemies.ship_galactic import ShipGalactic
from game.components.enemies.ship_droid import ShipDroid
from game.components.enemies.ship_stellar import ShipStellar
from game.components.enemies.enemy import Enemy


class EnemyHandler:
    def __init__(self):
        self.enemies = []
        self.timer = 0
        self.delay = 200
        self.min_enemies = 3
        self.max_enemies = 5
        self.available_ships = [Ship]
        self.current_level = 1
        self.is_countdown_active = False
        self.countdown_timer = 0
        self.countdown_duration = 3000
        self.last_enemy_time = time.time()


    def update(self, bullet_handler):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(bullet_handler)
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
            self.enemies.append(ShipGalactic())
        if len(self.enemies) < 5:
            self.enemies.append(ShipDroid())
        if len(self.enemies) < 5:
            self.enemies.append(ShipStellar())
       
        
        ship_type = random.choice(self.available_ships)
        enemy = ship_type()
        if len(self.enemies) < self.min_enemies:
            self.enemies.append(enemy)
        
    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)
    
    def increase_level(self):
        self.current_level += 1
        if self.current_level == 2:
            self.available_ships = [Ship, ShipOvni]
        elif self.current_level == 3:
            self.available_ships = [Ship, ShipOvni, ShipGalactic]
        elif self.current_level == 4:
            self.available_ships = [Ship, ShipOvni, ShipGalactic, ShipDroid]
        elif self.current_level == 5:
            self.available_ships = [Ship, ShipOvni, ShipGalactic, ShipDroid, ShipStellar]
        elif self.current_level == 6:
            self.available_ships = [Ship, ShipOvni, ShipGalactic, ShipDroid, ShipStellar]
        else:
            if self.current_level > 6:
                self.available_ships = [Ship, ShipOvni, ShipGalactic, ShipDroid, ShipStellar]