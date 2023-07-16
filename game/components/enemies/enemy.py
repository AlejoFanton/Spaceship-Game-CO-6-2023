import random
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, LEFT, RIGTH

class Enemy():
    X_POS_LIST = [i for i in range(10,SCREEN_WIDTH,50)]
    Y_POS = 0
    SPEED_Y = 2
    SPEED_X = 5
    MOVEMENTS = [LEFT, RIGTH]
    INTERVAL = 100

    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS
        self.mov_x = random.choice(self.MOVEMENTS)
        self.index =0
        self.is_visible = True

    def update(self):
        self.move()
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_visible = False
        self.index += 1

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        self.rect.y += self.SPEED_Y
        if self.mov_x == LEFT:
            self.rect.x -= self.SPEED_X
            if self.index > self.INTERVAL or self.rect.x <= 0:
                self.mov_x = RIGTH
                self.index = 0
        elif self.mov_x == self.MOVEMENTS:            
            self.rect.y += self.SPEED_Y
            if self.index > self.INTERVAL or self.rect.x <= 0:
                self.rect.y -= self.SPEED_Y
                self.index = 0                
        elif self.mov_x == self.MOVEMENTS:
            if self.rect.y <= 0 or self.rect.y >= SCREEN_HEIGHT - self.rect.height:
                self.SPEED_Y = -self.SPEED_Y
        else:
            self.rect.x += self.SPEED_X
            if  self.index > self.INTERVAL or self.rect.x >= SCREEN_WIDTH - self.rect.width:
                self.mov_x = LEFT
                self.index = 0