from constants import *


class Player():

    def __init__(self, x, y, width, height, speed_x=0.1, jumping_height=(SCREEN_HEIGHT/6), jumping_time=0.1, color=Color.RED.value, keys=['up', 'down', 'left', 'right'], name='player_1'):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.width = width
        self.height = height
        self.speed_x = speed_x
        self.jumping_height = jumping_height
        print(self.jumping_height)
        self.jumping_time = jumping_time
        self.color = color
        self.keys = keys
        self.name = name
        self.can_jump = False
        self.jumping = False
        self.nb_jumping_frame = 0

    def __str__(self):
        return f"{self.name} : \n x,y : [{self.x},{self.y}]\n dx,dy : [{self.dx},{self.dy}]"