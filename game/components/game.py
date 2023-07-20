import pygame
from game.utils.constants import *
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_handler import EnemyHandler
from game.components.Bullets.bullet_handler import BulletHandler
from game.components.levels.levels_handler import LevelHandler
from game.utils import text_utils
from game.components.power_ups.power_up_handler import PowerUpHandler
from game.components.help.lifes import Life

class Game:
    def __init__(self):
        pygame.init()
        self.init_window()
        self.init_game_variables()

    def init_window(self):
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

    def init_game_variables(self):
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
        self.power_up_handler = PowerUpHandler(self)
        self.level_handler = LevelHandler()
        self.time_next_level = 0
        self.enemies_nex_level = 3
        self.lives = Life()
        self.wp_positions = [(600, 300), (200, 500), (550, 300), (200, 75)]
        self.wp_speed = self.game_speed
        self.max_level_reached = 0
        self.bg = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.bg_start = pygame.transform.scale(BGSTART, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.show_start_menu = True
        self.game_started = False
        self.game_over = False
        self.start_sound = START_SOUND
        self.sound_played = False
        self.laser_sound = LASER_SOUND
        self.power_sound = POWER_SOUND

    def run(self):
        self.running = True
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
        pygame.display.quit()
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
            elif event.type == pygame.KEYDOWN:
                if not self.playing:
                    if event.key == pygame.K_RETURN:
                        self.playing = True
                        self.game_started = True
                        self.reset()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not self.playing and event.button == 1:  # 1: Left mouse button
                    self.playing = True
                    self.game_started = True
                    self.reset()

    def update(self):
        if self.playing:
            self.update_game_components()
            self.update_score()
            self.update_power_time()

        self.update_waypoints()

    def update_game_components(self):
        user_input = pygame.key.get_pressed()
        self.player.update(self.game_speed, user_input, self.bullet_handler)
        self.enemy_handler.update(self.bullet_handler)
        self.bullet_handler.update(self.player, self.enemy_handler.enemies)
        self.power_up_handler.update(self.player)
        self.score = self.enemy_handler.number_enemy_destroyed

        if not self.sound_played:
            self.start_sound.stop()
            self.sound_played = True

        if self.level_handler.is_level_completed():
            self.is_countdown_active = True
            self.countdown_timer = self.countdown_duration
            self.update_max_level_reached()

        if not self.player.is_alive:
            self.lives.reduce_life()
            self.player.is_alive = True

        if self.lives.is_game_over():
            pygame.time.delay(300)
            self.playing = False
            self.number_death += 1

            if self.level_handler.current_level_index > self.max_level_reached:
                self.max_level_reached = self.level_handler.current_level_index

    def update_score(self):
        self.score = self.enemy_handler.number_enemy_destroyed
        if self.score > self.max_score:
            self.max_score = self.score

    def update_power_time(self):
        if self.player.has_power:
            power_time = round((self.player.power_time - pygame.time.get_ticks()) / 100, 2)

            if power_time >= 0:
                text_power, text_power_rect = text_utils.get_message(
                    f'{self.player.power_type.capitalize()} is enabled for {power_time}',
                    15,
                    WHITE,
                    100,
                    40
                )
                self.screen.blit(text_power, text_power_rect)
            else:
                self.player.has_power = False
                self.player.power_type = DEFAULT_TYPE
                self.player.set_default_image()

    def update_waypoints(self):
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
            self.power_up_handler.draw(self.screen)
            self.draw_score()
            self.draw_level()
            self.draw_power_time()
        else:
            self.draw_menu()
            self.update_max_level_reached()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        self.screen.fill(BLACK)

        if not self.game_started:
            if self.show_start_menu:
                self.screen.blit(self.bg_start, (0, 0))
            else:
                image_height = self.bg.get_height()
                self.screen.blit(self.bg, (self.x_pos_bg, self.y_pos_bg))
                self.screen.blit(self.bg, (self.x_pos_bg, self.y_pos_bg - image_height))
                if self.y_pos_bg >= SCREEN_HEIGHT:
                    self.screen.blit(self.bg, (self.x_pos_bg, self.y_pos_bg - image_height))
                    self.y_pos_bg = 0
                self.y_pos_bg += self.game_speed
        else:
            self.screen.blit(self.bg_start, (0, 0))

        wp_images = [WP_1, WP_2, WP_3, WP_4]
        wp_sizes = [(400, 100), (300, 100), (100, 100), (150, 150)]

        for i in range(len(self.wp_positions)):
            wp_scaled = pygame.transform.scale(wp_images[i], wp_sizes[i])
            self.screen.blit(wp_scaled, self.wp_positions[i])

    def draw_menu(self):
        if self.number_death == 0:
            self.show_start_menu = True
            image = pygame.transform.scale(BGSTART, (SCREEN_WIDTH, SCREEN_HEIGHT))
            self.screen.blit(image, (0, 0))
            title, title_text_rect = text_utils.get_message('Interstellar Ship', 50, (255, 255, 0), height=SCREEN_HEIGHT//2 - 200)
            subtitle, subtitle_text_rect = text_utils.get_message('Saving the Galaxy', 50, (255, 255, 0), height=SCREEN_HEIGHT//2 - 150)
            text, text_rect = text_utils.get_message('Press the enter key to start', 30, WHITE)
            self.screen.blit(title, title_text_rect)
            self.screen.blit(subtitle, subtitle_text_rect)
            self.screen.blit(text, text_rect)
            self.start_sound.play()
        else:
            self.show_start_menu = False
            text, text_rect = text_utils.get_message('Press the enter key to restart', 30, WHITE)
            score, score_rect = text_utils.get_message(f'Your score is: {self.score}', 30, WHITE, height=SCREEN_HEIGHT//2 + 50)
            max_score, max_score_rect = text_utils.get_message(f'Your maximum score is: {self.max_score}', 30, WHITE, height=SCREEN_HEIGHT//2 + 90)
            level_handler, level_rect = text_utils.get_message(f'Maximum level reached: {self.enemy_handler.current_level}', 30, WHITE, height=SCREEN_HEIGHT//2 + 130)
            self.screen.blit(text, text_rect)
            self.screen.blit(score, score_rect)
            self.screen.blit(max_score, max_score_rect)
            self.screen.blit(level_handler, level_rect)

    def draw_score(self):
        score, score_rect = text_utils.get_message(f'Score: {self.score}', 15, WHITE, 1000, 40)
        max_score, max_score_rect = text_utils.get_message(f'Max score: {self.max_score}', 15, WHITE, 1000, 55)
        self.screen.blit(score, score_rect)
        self.screen.blit(max_score, max_score_rect)

    def draw_power_time(self):
        if self.player.has_power:
            power_time = round((self.player.power_time - pygame.time.get_ticks()) / 100, 2)

            if power_time >= 0:
                text_power, text_power_rect = text_utils.get_message(
                    f'{self.player.power_type.capitalize()} is enabled for {power_time}',
                    15,
                    WHITE,
                    100,
                    40
                )
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
        self.power_up_handler.reset()
        self.lives.reset()
        self.score = 0
        self.level_handler.reset()
        self.power_up_handler.reset()
        self.level_handler.current_level_index = self.max_level_reached
        self.game_started = False
        self.show_start_menu = False




