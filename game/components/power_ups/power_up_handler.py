import pygame
import random
from game.components.power_ups.shield import Shield
from game.utils.constants import SPACESHIP_SHIELD, SCREEN_HEIGHT, POWER_SOUND

class PowerUpHandler:
    INTERVAL_TIME = 300

    # Diccionario para mantener un registro de power-ups disponibles y sus clases
    POWER_UPS_AVAILABLE = {
        "shield": Shield
        # Agregar más power-ups aquí si es necesario en el futuro
    }

    def __init__(self, game):
        self.power_ups = []
        self.interval_time = 0
        self.game = game

    def update(self, player):
        # Controlar el tiempo de generación de power-ups
        self.interval_time += 1
        if self.interval_time >= self.INTERVAL_TIME:
            self.interval_time = 0
            self.add_power_up()

        for power_up in self.power_ups:
            power_up.update(player)

            # Remover el power-up si ya no es visible
            if not power_up.is_visible:
                self.remove_power_up(power_up)

            # Activar el power-up si el jugador lo toma
            if power_up.is_used:
                player.activate_power_up(power_up)

                # Reproducir el sonido de los power-ups cuando son usados
                self.game.power_sound.play()

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
    
    def add_power_up(self):
        # Seleccionar aleatoriamente un power-up del diccionario y agregarlo a la lista
        power_up_type = random.choice(list(self.POWER_UPS_AVAILABLE.keys()))
        power_up_class = self.POWER_UPS_AVAILABLE[power_up_type]
        self.power_ups.append(power_up_class())

    def remove_power_up(self, power_up):
        self.power_ups.remove(power_up)
    
    def reset(self):
        self.power_ups = []
        self.interval_time = 0