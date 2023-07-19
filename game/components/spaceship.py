import pygame
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, BULLET_PLAYER_TYPE, DEFAULT_TYPE, SHIELD_TYPE

class Spaceship:
    WIDTH = 40
    HEIGHT = 60
    X_POS = (SCREEN_WIDTH // 2) - WIDTH
    Y_POS = 500

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.has_power = False
        self.is_alive = True
        self.power_type = DEFAULT_TYPE
    
    def update(self, game_speed, user_input, bullet_handler):
        if user_input[pygame.K_LEFT]:
            self.move_left(game_speed)
        elif user_input[pygame.K_RIGHT]:
            self.move_rigth(game_speed)
        elif user_input[pygame.K_UP]:
            self.move_up(game_speed)
        elif user_input[pygame.K_DOWN]:
            self.move_down(game_speed)
        elif user_input[pygame.K_SPACE]:
            self.shoot(bullet_handler)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move_left(self, game_speed):
        self.rect.x -= game_speed
        self.display_limit()

    def move_rigth(self, game_speed):
        self.rect.x += game_speed
        self.display_limit()
    
    def move_up(self, game_speed):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -= game_speed
    
    def move_down(self, game_speed):
        if self.rect.bottom < SCREEN_HEIGHT - self.HEIGHT:
            self.rect.y += game_speed

    #Primera tarea
    def display_limit(self):
        if self.rect.x < 0: # Limite izquierdo
            self.rect.x = SCREEN_WIDTH # Reaparece lado derecho
        elif self.rect.x > SCREEN_WIDTH: 
            self.rect.x = 0
    
    def shoot(self, bullet_handler):
        bullet_handler.add_bullet(BULLET_PLAYER_TYPE, self.rect.center)
    
    def reset(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.is_alive = True