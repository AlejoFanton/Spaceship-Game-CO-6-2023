import pygame
import random

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE
from game.utils.constants import WP_1, WP_2, WP_3, WP_4, WHITE
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_handler import EnemyHandler
from game.components.Bullets.bullet_handler import BulletHandler
from game.utils import text_utils

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
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
        self.score = 0
        self.max_score = 0
        self.number_death = 0
        self.number_attempts = 0

    def run(self):
        # Game loop: events - update - draw
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.display.quit()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN and not self.playing:
                self.reset()
                self.playing = True
                self.number_death += 1
                self.number_attempts += 1

    def update(self):
        if self.playing:
            user_input = pygame.key.get_pressed()
            self.player.update(self.game_speed, user_input, self.bullet_handler)
            self.enemy_handler.update(self.bullet_handler)
            self.bullet_handler.update(self.player, self.enemy_handler.enemies)
            self.score = self.enemy_handler.enemies_destroyed
            if self.score > self.max_score:
                self.max_score = self.score
            if not self.player.is_alive:
                pygame.time.delay(300)
                self.playing = False
                self.score = self.enemy_handler.enemies_destroyed

            
        for i in range(len(self.wp_positions)):
                self.wp_positions[i] = (self.wp_positions[i][0], self.wp_positions[i][1] + self.wp_speed)
                if self.wp_positions[i][1] >= SCREEN_HEIGHT:
                    self.wp_positions[i] = (self.wp_positions[i][0], -50)

    def draw(self):
        self.draw_background()
        if self.playing:
            self.clock.tick(FPS)
            self.player.draw(self.screen)
            self.enemy_handler.draw(self.screen)
            self.bullet_handler.draw(self.screen)
            self.draw_score()
        else:
            self.draw_menu()
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

    def draw_menu(self):
        if self.number_death == 0:
            text, text_rect = text_utils.get_message('Press any Key to Start', 30, WHITE)
            self.screen.blit(text, text_rect)
        else:
            text, text_rect = text_utils.get_message('Press any key to Restart', 30, WHITE)
            score, score_rect = text_utils.get_message(f'Your score is: {self.score}', 30, WHITE, height=SCREEN_HEIGHT // 2 + 50)
            max_score, max_score_rect = text_utils.get_message(f'Max score: {self.max_score}', 30, WHITE, height=SCREEN_HEIGHT // 2 + 80)
            attempts, attempts_rect = text_utils.get_message(f'Attempts: {self.number_attempts}', 30, WHITE, height=SCREEN_HEIGHT // 2 + 110)
            self.screen.blit(text, text_rect)
            self.screen.blit(score, score_rect)
            self.screen.blit(max_score, max_score_rect)
            self.screen.blit(attempts, attempts_rect)

    def draw_score(self):
        score, score_rect = text_utils.get_message(f'Your score is: {self.score}', 20, WHITE, 1000, 40)
        self.screen.blit(score, score_rect)

    def reset(self):
        self.player.reset()
        self.enemy_handler.reset()
        self.bullet_handler.reset()
        self.score = 0
        self.number_death = 0
        self.number_enemy_destroyed = 0




