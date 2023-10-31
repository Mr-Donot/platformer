from enum import Enum

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRAVITY = 0.25
FRICTION = 0.05




class Color(Enum):
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)