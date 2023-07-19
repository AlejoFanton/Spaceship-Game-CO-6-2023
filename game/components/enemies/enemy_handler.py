import random
import pygame

from game.components.enemies.ship import Ship
from game.components.enemies.ship_ovni import ShipOvni
from game.components.enemies.ship_galactic import ShipGalactic
from game.components.enemies.ship_droid import ShipDroid
from game.components.enemies.ship_stellar import ShipStellar
from game.utils.constants import WHITE
from game.utils import text_utils


class EnemyHandler:
    
    def __init__(self):
        self.enemies = []
        self.number_enemy_destroyed = 0
        self.timer = 0
        self.delay = 200
        self.min_enemies = 3
        self.max_enemies = 3
        self.available_ships = [Ship]
        self.current_level = 1
        self.is_countdown_active = False
        self.countdown_timer = 0
        self.countdown_duration = 3000

    def update(self, bullet_handler):
        self.timer += 1
        self.add_enemy()
        if self.timer >= self.delay and self.min_enemies <= self.max_enemies:
            self.min_enemies += 1
            self.timer = 0
        for enemy in self.enemies:
            enemy.update(bullet_handler)
            if not enemy.is_alive:
                self.number_enemy_destroyed += 1
                self.remove_enemy(enemy)
        if self.is_countdown_active:
            pygame.time.wait(self.countdown_duration)
            self.countdown_timer -= pygame.time.get_ticks() + 3000
            if self.countdown_timer <= 0:
                self.is_countdown_active = False   
                self.countdown_timer = 0         
        if self.number_enemy_destroyed == self.max_enemies:
            self.increase_level() 
            self.is_countdown_active = True
            self.max_enemies += 4

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
        if self.is_countdown_active:
            countdown_seconds = int(self.countdown_duration / 1000)
            text, text_rect = text_utils.get_message(f"Next level in {countdown_seconds} seconds", 40, WHITE)
            screen.blit(text,text_rect)
                

    def add_enemy(self):
        ship_type = random.choice(self.available_ships)
        enemy = ship_type()
        if len(self.enemies) < self.min_enemies:
            self.enemies.append(enemy)

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)
    
    def reset(self):
        self.enemies = []
        self.number_enemy_destroyed = 0
        self.min_enemies = 3
        self.max_enemies = 3
        self.available_ships = [Ship]
        self.current_level = 1
        self.countdown_timer = 0
    
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
    
    
