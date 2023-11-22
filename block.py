from constants import *


class Block():

    def __init__(self, x, y, width, height, color, type="normal"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.type = type

    def apply_effect(self, game, player):
        if self.type == "win"and player.dy >= 0 and self.x - player.width < player.x < self.x + self.width and player.y < self.y:
            game.running = False
        if self.type == "jump" and not player.is_buff_jump:
            player.jumping_height /= BUFF_JUMP
            player.is_buff_jump = True
        if self.type == "lava":
            self.go_to_spawn(game, player)
            player.dx = 0
            player.dy = 0
        

    def go_to_spawn(self, game, player):
        player.x, player.y = game.spawn_block.x + (game.spawn_block.width - player.width)/2, game.spawn_block.y - player.height - 20
    def __str__(self):
        return f"{self.type} : \n x,y : [{self.x},{self.y}]\n w,h : [{self.width},{self.height}]"
