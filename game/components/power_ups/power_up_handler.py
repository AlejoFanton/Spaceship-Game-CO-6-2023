import pygame
import random
from game.components.power_ups.shield import Shield
from game.utils.constants import SPACESHIP_SHIELD, SCREEN_HEIGHT, POWER_SOUND

class PowerUpHandler:
    INTERVAL_TIME = 100

    def __init__(self, game):
        self.power_ups = []
        self.interval_time = 0
        self.game = game

    def update(self, player):
        self.interval_time += 1
        if self.interval_time % self.INTERVAL_TIME == 0:
            self.add_power_up()
        for power_up in self.power_ups:
            power_up.update(player)
            if not power_up.is_visible:
                self.remove_power_up(power_up)
            if power_up.is_used:
                player.activate_power_up(power_up)

                # Reproducir el sonido de los power-ups cuando son usados
                self.game.power_sound.play()

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
    
    def add_power_up(self):
        self.power_ups.append(Shield())

    def remove_power_up(self, power_up):
        self.power_ups.remove(power_up)
    
    def reset(self):
        self.power_ups = []
        self.interval_time = 0