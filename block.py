from constants import *


class Block():

    def __init__(self, x, y, width, height, color, type="normal"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.type = type

    def apply_effect(self, game):
        if self.type == "win"and game.player.dy >= 0 and self.x - game.player.width < game.player.x < self.x + self.width and game.player.y < self.y:
            game.running = False
        if self.type == "jump" and not game.player.is_buff_jump:
            game.player.jumping_height /= BUFF_JUMP
            game.player.is_buff_jump = True
        if self.type == "lava":
            self.go_to_spawn(game)
            game.player.dx = 0
            game.player.dy = 0
        

    def go_to_spawn(self, game):
        game.player.x, game.player.y = game.spawn_block.x + (game.spawn_block.width - game.player.width)/2, game.spawn_block.y - game.player.height - 20
    def __str__(self):
        return f"{self.type} : \n x,y : [{self.x},{self.y}]\n w,h : [{self.width},{self.height}]"
