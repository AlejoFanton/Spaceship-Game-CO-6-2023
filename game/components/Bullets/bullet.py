import pygame

class Bullet:
    def __init__(self, image, bullet_type, center):
        self.image = image
        self.bullet_type = bullet_type
        self.rect = self.image.get_rect(center=center)
        self.is_alive = True

    def update(self, target):
        if self.rect.colliderect(target.rect):
            target.is_alive = False
            self.is_alive = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    