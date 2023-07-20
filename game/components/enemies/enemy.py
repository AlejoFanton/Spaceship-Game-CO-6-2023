import random
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, BULLET_ENEMY_TYPE

class Enemy:
    X_POS_LIST = [i for i in range(50, SCREEN_WIDTH, 50)]
    Y_POS = 20
    LEFT = "left"
    RIGHT = "right"
    DIAGONAL = "diagonal"
    BOUNCE = "bounce"
    MOVEMENTS = [LEFT, RIGHT, DIAGONAL, BOUNCE]
    INTERVAL = 100
    SHOOTING_TIME = 30

    def __init__(self, image, speed_x, speed_y):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS
        self.mov = random.choice(self.MOVEMENTS)
        self.index = 0
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.is_alive = True
        self.is_destroyed = False
        self.shooting_time = 0

    def update(self, bullet_handler):
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_alive = False

        self.shooting_time += 1
        self.move()
        self.shoot(bullet_handler)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        self.rect.y += self.speed_y

        if self.mov == self.LEFT:
            self.move_left()
        elif self.mov == self.DIAGONAL:
            self.move_diagonal()
        elif self.mov == self.BOUNCE:
            self.move_bounce()
        else:
            self.move_right()

        self.index += 1

    def move_left(self):
        self.rect.x -= self.speed_x
        if self.index > self.INTERVAL or self.rect.x <= 0:
            self.mov = self.RIGHT
            self.index = 0

    def move_diagonal(self):
        self.rect.x -= self.speed_x
        if self.index > self.INTERVAL or self.rect.x <= 0:
            self.rect.y -= self.speed_y
            self.index = 0

    def move_bounce(self):
        if self.rect.y <= 0 or self.rect.y >= SCREEN_HEIGHT - self.rect.height:
            self.speed_y = -self.speed_y

    def move_right(self):
        self.rect.x += self.speed_x
        if self.index > self.INTERVAL or self.rect.x >= SCREEN_WIDTH - self.rect.width:
            self.mov = self.LEFT
            self.index = 0

    def shoot(self, bullet_handler):
        if self.shooting_time % self.SHOOTING_TIME == 0:
            bullet_handler.add_bullet(BULLET_ENEMY_TYPE, self.rect.center)