import pygame
import random

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE
from game.utils.constants import WP_1, WP_2, WP_3, WP_4
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_handler import EnemyHandler
from game.components.Bullets.bullet_handler import BulletHandler

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.player = Spaceship()
        self.enemy_handler = EnemyHandler()
        self.bullet_handler = BulletHandler()
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.wp_positions = [
            (600, 300),  # wp1_pos_x, wp1_pos_y
            (200, 500),  # wp2_pos_x, wp2_pos_y
            (550, 300),  # wp3_pos_x, wp3_pos_y
            (200, 75)    # wp4_pos_x, wp4_pos_y
        ]
        self.wp_speed = self.game_speed

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.display.quit()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(self.game_speed, user_input)
        self.enemy_handler.update(self.bullet_handler)
        self.bullet_handler.update(self.player)
        if not self.player.is_alive:
            pygame.time.delay(300)
            self.playing = False

        
        for i in range(len(self.wp_positions)):
            self.wp_positions[i] = (self.wp_positions[i][0], self.wp_positions[i][1] + self.wp_speed)
            if self.wp_positions[i][1] >= SCREEN_HEIGHT:
                self.wp_positions[i] = (self.wp_positions[i][0], -50)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_handler.draw(self.screen)
        self.bullet_handler.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        self.screen.fill((255, 255, 255))  # Limpia la pantalla con un color blanco

        # Dibuja el fondo principal
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image.get_height()))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image.get_height()))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

        # Dibuja WP sobre el fondo principal
        wp_images = [WP_1, WP_2, WP_3, WP_4]
        wp_sizes = [(400, 100), (300, 100), (100, 100), (150, 150)]

        for i in range(len(self.wp_positions)):
            wp_scaled = pygame.transform.scale(wp_images[i], wp_sizes[i])
            self.screen.blit(wp_scaled, self.wp_positions[i])
