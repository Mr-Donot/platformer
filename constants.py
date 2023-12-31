from enum import Enum
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRAVITY = 0.25
FRICTION = 0.05
BUFF_JUMP = 3/2

PLAYER_WIDTH = SCREEN_WIDTH/40
PLAYER_HEIGHT = SCREEN_HEIGHT/20

FPS = 60


class Color(Enum):
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BURGUNDY = (144, 12, 63)
    LIGHT_GREEN = (218, 247, 166)
    LIGHT_GREY = (191, 191, 191)
    DARK_GREY = (63, 63, 63)


KEYS = {
    "up": pygame.K_UP,
    "down": pygame.K_DOWN,
    "left": pygame.K_LEFT,
    "right": pygame.K_RIGHT,
    "z": pygame.K_z,
    "q": pygame.K_q,
    "s": pygame.K_s,
    "d": pygame.K_d
}