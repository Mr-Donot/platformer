from constants import *
from block import *


def generate_map(id):
    if id == 0:
        return map0()

def map0():
    blocks = []

    blocks.append(Block(0, SCREEN_HEIGHT-SCREEN_HEIGHT/30, SCREEN_WIDTH, SCREEN_HEIGHT/30, Color.GREEN.value)) #ground


    blocks.append(Block(SCREEN_WIDTH*3/16, SCREEN_HEIGHT*13/16, SCREEN_WIDTH/8, SCREEN_HEIGHT/30, Color.BLUE.value))
    blocks.append(Block(SCREEN_WIDTH/2 - SCREEN_WIDTH/8, SCREEN_HEIGHT*11/16, SCREEN_WIDTH/8, SCREEN_HEIGHT/30, Color.BLUE.value))
    blocks.append(Block(SCREEN_WIDTH*3/4 - SCREEN_WIDTH/8, SCREEN_HEIGHT*9/16, SCREEN_WIDTH/8, SCREEN_HEIGHT/30, Color.BLUE.value))
    blocks.append(Block(SCREEN_WIDTH*11/32, SCREEN_HEIGHT*15/32, SCREEN_WIDTH/8, SCREEN_HEIGHT/30, Color.BLUE.value))
    
    blocks.append(Block(SCREEN_WIDTH*4/64, SCREEN_HEIGHT*12/32, SCREEN_WIDTH/8, SCREEN_HEIGHT/30, Color.BLUE.value))
    blocks.append(Block(SCREEN_WIDTH*7/32, SCREEN_HEIGHT*8/32, SCREEN_WIDTH/8, SCREEN_HEIGHT/30, Color.BLUE.value))

    blocks.append(Block(SCREEN_WIDTH*7/16, SCREEN_HEIGHT*3/16, SCREEN_WIDTH/8, SCREEN_HEIGHT/30, Color.BLUE.value))
    blocks.append(Block(SCREEN_WIDTH*43/64, SCREEN_HEIGHT*9/32, SCREEN_WIDTH/8, SCREEN_HEIGHT/30, Color.BLUE.value))




    blocks.append(Block(SCREEN_WIDTH*7/8, SCREEN_HEIGHT*3/16, SCREEN_WIDTH*3/80, SCREEN_HEIGHT/30, Color.YELLOW.value, type="win"))

    return blocks