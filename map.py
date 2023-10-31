from constants import *
from block import *


def generate_map():
    blocks = []

    blocks.append(Block(0, SCREEN_HEIGHT-20, SCREEN_WIDTH, 20, Color.GREEN.value)) #ground


    blocks.append(Block(SCREEN_WIDTH*3/16, SCREEN_HEIGHT*13/16, SCREEN_WIDTH/8, 20, Color.BLUE.value))
    blocks.append(Block(SCREEN_WIDTH/2 - SCREEN_WIDTH/8, SCREEN_HEIGHT*11/16, SCREEN_WIDTH/8, 20, Color.BLUE.value))
    blocks.append(Block(SCREEN_WIDTH*3/4 - SCREEN_WIDTH/8, SCREEN_HEIGHT*9/16, SCREEN_WIDTH/8, 20, Color.BLUE.value))
    
    blocks.append(Block(SCREEN_WIDTH*11/32, SCREEN_HEIGHT*15/32, SCREEN_WIDTH/8, 20, Color.BLUE.value))
    
    blocks.append(Block(SCREEN_WIDTH*7/32, SCREEN_HEIGHT*5/16, SCREEN_WIDTH/8, 20, Color.BLUE.value))
    blocks.append(Block(SCREEN_WIDTH*7/16, SCREEN_HEIGHT*3/16, SCREEN_WIDTH/8, 20, Color.BLUE.value))
    blocks.append(Block(SCREEN_WIDTH*21/32, SCREEN_HEIGHT*9/32, SCREEN_WIDTH/8, 20, Color.BLUE.value))




    blocks.append(Block(SCREEN_WIDTH*13/16, SCREEN_HEIGHT*3/16, 30, 20, Color.YELLOW.value, type="win"))

    return blocks