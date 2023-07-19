import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))


SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))
WP_1 = pygame.image.load(os.path.join(IMG_DIR, 'Wallpaper/galaxy.png'))
WP_2 = pygame.image.load(os.path.join(IMG_DIR, 'Wallpaper/galaxy_2.png'))
WP_3 = pygame.image.load(os.path.join(IMG_DIR, 'Wallpaper/planet.png'))
WP_4 = pygame.image.load(os.path.join(IMG_DIR, 'Wallpaper/planet_2.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/hunter.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/ovni.png"))
ENEMY_3 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/galactic.png"))
ENEMY_4 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/droid.png"))
ENEMY_5 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/stellar.png"))

WHITE = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)

FONT_STYLE = 'freesansbold.ttf'

LEFT = 'left'
RIGTH = 'rigth'
DIAGONAL = "diagonal"
BOUNCE = "bounce"

BULLET_ENEMY_TYPE = 'enemy'
BULLET_PLAYER_TYPE = 'ship'