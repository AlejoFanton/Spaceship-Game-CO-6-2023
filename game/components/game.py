import pygame
import random

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE
from game.utils.constants import WP_1, WP_2, WP_3, WP_4, WHITE
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_handler import EnemyHandler
from game.components.Bullets.bullet_handler import BulletHandler
from game.components.levels.levels_handler import LevelHandler
from game.utils import text_utils
from game.components.power.power_handler import PowerHandled
from game.components.help.lifes import Life

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_handler = EnemyHandler()
        self.bullet_handler = BulletHandler()
        self.score = 0
        self.number_death = 0
        self.max_score = 0
        self.power_type = DEFAULT_TYPE
        self.power_time = 0
        self.power_handled = PowerHandled()
        self.level_handler = LevelHandler()
        self.time_next_level = 0
        self.enemies_nex_level = 3
        self.lives = Life()
        self.wp_positions = [
            (600, 300),  # wp1_pos_x, wp1_pos_y
            (200, 500),  # wp2_pos_x, wp2_pos_y
            (550, 300),  # wp3_pos_x, wp3_pos_y
            (200, 75)    # wp4_pos_x, wp4_pos_y
        ]
        self.wp_speed = self.game_speed
        self.max_level_reached = 0

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
                self.playing = False
            elif event.type == pygame.KEYDOWN:
                if not self.playing:
                    if event.key == pygame.K_RETURN:
                        self.playing = True
                        self.reset()
                        self.playing = True
                        self.number_death += 1

    def update(self):
        if self.playing:
            user_input = pygame.key.get_pressed()
            self.player.update(self.game_speed, user_input, self.bullet_handler)
            self.enemy_handler.update(self.bullet_handler)
            self.bullet_handler.update(self.player, self.enemy_handler.enemies)
            self.score = self.enemy_handler.number_enemy_destroyed
            self.power_handled.update(self.player)
            
            if self.level_handler.is_level_completed():  # Cambiar aquí (corregir nombre del método)
                self.is_countdown_active = True
                self.countdown_timer = self.countdown_duration
                self.update_max_level_reached()

            if not self.player.is_alive:
                self.lives.reduce_life()
                self.player.is_alive = True
            self.score_player()
            if self.lives.is_game_over():
                pygame.time.delay(300)
                self.playing = False
                self.number_death += 1

                # Actualizar el máximo nivel alcanzado si el nivel actual es mayor que el máximo alcanzado
                if self.level_handler.current_level_index > self.max_level_reached:
                    self.max_level_reached = self.level_handler.current_level_index

        for i in range(len(self.wp_positions)):
                self.wp_positions[i] = (self.wp_positions[i][0], self.wp_positions[i][1] + self.wp_speed)
                if self.wp_positions[i][1] >= SCREEN_HEIGHT:
                    self.wp_positions[i] = (self.wp_positions[i][0], -50)

    def draw(self):
        self.draw_background()
        if self.playing:
            self.clock.tick(FPS)    
            self.lives.draw(self.screen)   
            self.player.draw(self.screen)
            self.enemy_handler.draw(self.screen)
            self.bullet_handler.draw(self.screen)
            self.power_handled.draw(self.screen)
            self.draw_score()
            self.draw_level()
            self.draw_power_time()
            
        else:
            self.draw_menu()
            self.update_max_level_reached()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
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
            text, text_rect = text_utils.get_message('Press the enter key to start', 30, WHITE)
            self.screen.blit(text, text_rect)
        else:
            text, text_rect = text_utils.get_message('Press the enter key to restart', 30, WHITE)
            score, score_rect = text_utils.get_message(f'Your score is: {self.score}', 30, WHITE, height=SCREEN_HEIGHT//2 + 50)
            max_score, max_score_rect = text_utils.get_message(f'Your maximum score is: {self.max_score}', 30, WHITE, height=SCREEN_HEIGHT//2 + 90)
            level_handler, level_rect = text_utils.get_message(f'Maximum level reached: {self.enemy_handler.current_level}', 30, WHITE, height=SCREEN_HEIGHT//2 + 130)
            self.screen.blit(text, text_rect)
            self.screen.blit(score, score_rect)
            self.screen.blit(max_score, max_score_rect)
            self.screen.blit(level_handler, level_rect)

        
    def score_player(self):
        self.score = self.enemy_handler.number_enemy_destroyed
        if self.score > self.max_score:
            self.max_score = self.score
    
    def draw_score(self):
        score, score_rect = text_utils.get_message(f'score: {self.score}', 15, WHITE, 1000, 40)
        max_score, max_score_rect = text_utils.get_message(f'Max score: {self.max_score}', 15, WHITE, 1000, 55)
        self.screen.blit(score, score_rect)
        self.screen.blit(max_score, max_score_rect)
    
    def draw_power_time(self):
        if self.player.has_power:
            power_time = round((self.player.power_time - pygame.time.get_ticks()) /100,2)

            if power_time >= 0:
                text_power, text_power_rect = text_utils.get_message(f'{self.player.power_type.capitalize()} is enable for {power_time}', 15, WHITE, 100, 40)
                self.screen.blit(text_power, text_power_rect)
            else:
                self.player.has_power = False
                self.player.power_type = DEFAULT_TYPE
                self.player.set_default_image()
    
    def draw_level(self):
        level, level_rect = text_utils.get_message(f'Level: {self.enemy_handler.current_level}', 15, WHITE, 1000, 70)
        self.screen.blit(level, level_rect)

    def update_max_level_reached(self):
        if self.level_handler.current_level_index > self.max_level_reached:
            self.max_level_reached = self.level_handler.current_level_index

        
    def reset(self):
        self.player.reset()
        self.enemy_handler.reset()
        self.bullet_handler.reset()
        self.power_handled.reset()
        self.lives.reset()
        self.score = 0
        self.level_handler.reset()
        self.level_handler.current_level_index = self.max_level_reached




