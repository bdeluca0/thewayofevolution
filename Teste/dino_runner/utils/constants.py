import pygame
import os

# Global Constants
TITLE = "Aviator"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
X_POS_BG = 0 
Y_POS_BG = 380
GAME_SPEED = 20

X_POS = 80
Y_POS = 310

Y_POS_DUCK = 310

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Dino/AviaoQuebrado.png"))
ICON1 = pygame.image.load(os.path.join(IMG_DIR, "Dino/Logo.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Aviao.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Aviao 1.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/AviaoShield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/AviaoShield1.png")),
]

RUNNING_TIRO = [ 
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Tiro.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Tiro1.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/Aviao.png"))
JUMPING_TIRO = pygame.image.load(os.path.join(IMG_DIR, "Dino/Tiro.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/AviaoShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))


DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/AviaoDuck.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/AviaoDuck1.png")),
]

DUCKING_TIRO = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Tiro.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Tiro1.png"))
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/AviaoDuckShield1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/AviaoDuckShield.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/Mt.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/Mt3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/Mt2.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/Arvores1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/Arvores2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/Arvores3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Míssel.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))
TIRO = pygame.image.load(os.path.join(IMG_DIR, 'Other/TiroLogo.png'))
BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

JUMP_VEL = 8.5

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
TIRO_TYPE = "bullet"