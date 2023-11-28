from constants import *
from block import *


def generate_map(id):
    if id == 0:
        return map0()
    elif id == 1:
        return map1()
    elif id == 2:
        return map2()
    elif id == 3:
        return map3()
    elif id == 4:
        return map4()
    else:
        return no_map()

def no_map():
    blocks = []
    blocks.append(Block(0, SCREEN_HEIGHT-SCREEN_HEIGHT/30, SCREEN_WIDTH, SCREEN_HEIGHT/30, Color.YELLOW.value, type="win")) #ground
    blocks.append(Block(SCREEN_WIDTH/16 - SCREEN_WIDTH/80, SCREEN_HEIGHT-SCREEN_HEIGHT/30, SCREEN_WIDTH/20, SCREEN_HEIGHT/60, Color.LIGHT_GREY.value, type="spawn")) #spawn point
    return blocks

def map0():
    blocks = []

    blocks.append(Block(0, SCREEN_HEIGHT-SCREEN_HEIGHT/30, SCREEN_WIDTH, SCREEN_HEIGHT/30, Color.GREEN.value)) #ground
    blocks.append(Block(SCREEN_WIDTH/16 - SCREEN_WIDTH/80, SCREEN_HEIGHT-SCREEN_HEIGHT/30, SCREEN_WIDTH/20, SCREEN_HEIGHT/60, Color.LIGHT_GREY.value, type="spawn")) #spawn point

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

def map1():
    blocks = []
    blocks.append(Block(0, SCREEN_HEIGHT-SCREEN_HEIGHT/30, SCREEN_WIDTH, SCREEN_HEIGHT/30, Color.GREEN.value)) #ground
    blocks.append(Block(SCREEN_WIDTH/16 - SCREEN_WIDTH/80, SCREEN_HEIGHT-SCREEN_HEIGHT/30, SCREEN_WIDTH/20, SCREEN_HEIGHT/60, Color.LIGHT_GREY.value, type="spawn")) #spawn point
    #Mains horizontals platforms
    blocks.append(Block(0, SCREEN_HEIGHT*3/4 - SCREEN_HEIGHT/30, SCREEN_WIDTH*13/16, SCREEN_HEIGHT/30, Color.BLUE.value))
    blocks.append(Block(SCREEN_WIDTH*3/16, SCREEN_HEIGHT/2 - SCREEN_HEIGHT/30, SCREEN_WIDTH*13/16, SCREEN_HEIGHT/30, Color.BLUE.value))
    blocks.append(Block(0, SCREEN_HEIGHT/4 - SCREEN_HEIGHT/30, SCREEN_WIDTH*13/16, SCREEN_HEIGHT/30, Color.BLUE.value))
    
    blocks.append(Block(SCREEN_WIDTH*15/16, SCREEN_HEIGHT*3/4 + SCREEN_HEIGHT/15, SCREEN_WIDTH/16, SCREEN_HEIGHT/30, Color.BLUE.value))

    blocks.append(Block(0, SCREEN_HEIGHT*5/8 - SCREEN_HEIGHT/16, SCREEN_WIDTH*3/64, SCREEN_HEIGHT/30, Color.BLUE.value))
    blocks.append(Block(0, SCREEN_HEIGHT/2 - SCREEN_HEIGHT/16, SCREEN_WIDTH/32, SCREEN_HEIGHT/30, Color.BLUE.value))

    blocks.append(Block(SCREEN_WIDTH*3/16 - SCREEN_WIDTH/40, SCREEN_HEIGHT/2 - SCREEN_HEIGHT/8, SCREEN_WIDTH/40, SCREEN_HEIGHT/4, Color.BLUE.value))

    blocks.append(Block(SCREEN_WIDTH/3, SCREEN_HEIGHT*9/16, SCREEN_WIDTH/40, SCREEN_HEIGHT*3/16 - SCREEN_HEIGHT/30, Color.BLUE.value))
    blocks.append(Block(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH/40, SCREEN_HEIGHT*3/16 - SCREEN_HEIGHT/30 + SCREEN_HEIGHT/40, Color.BLUE.value))
    blocks.append(Block(SCREEN_WIDTH*2/3, SCREEN_HEIGHT*9/16, SCREEN_WIDTH/40, SCREEN_HEIGHT*3/16 - SCREEN_HEIGHT/30, Color.BLUE.value))

    blocks.append(Block(SCREEN_WIDTH*7/8,SCREEN_HEIGHT*3/8 - SCREEN_HEIGHT/30, SCREEN_WIDTH/16,SCREEN_HEIGHT/30,Color.BLUE.value))
    blocks.append(Block(SCREEN_WIDTH/32, SCREEN_HEIGHT/8 - SCREEN_HEIGHT/30, SCREEN_WIDTH*3/80, SCREEN_HEIGHT/30, Color.YELLOW.value, type="win"))

    return blocks


def map2():
    blocks = []

    blocks.append(Block(0, SCREEN_HEIGHT-SCREEN_HEIGHT/30, SCREEN_WIDTH, SCREEN_HEIGHT/30, Color.GREEN.value)) #ground
    blocks.append(Block(SCREEN_WIDTH/16 - SCREEN_WIDTH/80, SCREEN_HEIGHT-SCREEN_HEIGHT/30, SCREEN_WIDTH/20, SCREEN_HEIGHT/60, Color.LIGHT_GREY.value, type="spawn")) #spawn point
    blocks.append(Block(SCREEN_WIDTH*3/16, SCREEN_HEIGHT*13/16, SCREEN_WIDTH/8, SCREEN_HEIGHT/30, Color.BURGUNDY.value, type="jump"))
    blocks.append(Block(SCREEN_WIDTH*3/4 - SCREEN_WIDTH/8, SCREEN_HEIGHT*9/16, SCREEN_WIDTH/8, SCREEN_HEIGHT/30, Color.BURGUNDY.value, type="jump"))
    blocks.append(Block(SCREEN_WIDTH*3/32, SCREEN_HEIGHT*12/32, SCREEN_WIDTH/8, SCREEN_HEIGHT/30, Color.BURGUNDY.value, type="jump"))
    blocks.append(Block(SCREEN_WIDTH*3/4 - SCREEN_WIDTH/8, SCREEN_HEIGHT*3/16, SCREEN_WIDTH/8, SCREEN_HEIGHT/30, Color.BURGUNDY.value, type="jump"))
    blocks.append(Block(SCREEN_WIDTH*28/32, SCREEN_HEIGHT/8 - SCREEN_HEIGHT/30, SCREEN_WIDTH*3/80, SCREEN_HEIGHT/30, Color.YELLOW.value, type="win"))

    return blocks


def map3():
    blocks = []


    blocks.append(Block(SCREEN_WIDTH/16 - SCREEN_WIDTH/80, SCREEN_HEIGHT/10, SCREEN_WIDTH/20, SCREEN_HEIGHT/30, Color.LIGHT_GREY.value, type="spawn")) #spawn point
    blocks.append(Block(0, SCREEN_HEIGHT-SCREEN_HEIGHT/30, SCREEN_WIDTH, SCREEN_HEIGHT/30, Color.RED.value, type="lava")) #ground

    blocks.append(Block((SCREEN_WIDTH - SCREEN_WIDTH/40)/2, 0, SCREEN_WIDTH/40, SCREEN_HEIGHT/2,Color.BLUE.value))

    blocks.append(Block((SCREEN_WIDTH - SCREEN_WIDTH/40)/2, SCREEN_HEIGHT/2 + PLAYER_HEIGHT*3/2, SCREEN_WIDTH/40, SCREEN_HEIGHT/4,Color.BLUE.value))


    blocks.append(Block(SCREEN_WIDTH*3/4,SCREEN_HEIGHT*3/4,SCREEN_WIDTH/8, SCREEN_HEIGHT/30, Color.BURGUNDY.value, type="jump"))
    blocks.append(Block((SCREEN_WIDTH - SCREEN_WIDTH/40)/2 + SCREEN_WIDTH/40, SCREEN_HEIGHT/2 - SCREEN_HEIGHT/30, SCREEN_WIDTH/8, SCREEN_HEIGHT/30, Color.BURGUNDY.value, type="jump"))
    blocks.append(Block((SCREEN_WIDTH - SCREEN_WIDTH/40)/2 + SCREEN_WIDTH/40, SCREEN_HEIGHT/10 + SCREEN_HEIGHT/30, SCREEN_WIDTH/8, SCREEN_HEIGHT/30, Color.BURGUNDY.value, type="jump"))
    
    blocks.append(Block(SCREEN_WIDTH - (SCREEN_WIDTH/16 - SCREEN_WIDTH/80) - SCREEN_WIDTH/20, SCREEN_HEIGHT/10, SCREEN_WIDTH/20, SCREEN_HEIGHT/30, Color.YELLOW.value, type="win"))
    

    return blocks


def map4():
    blocks=[]

    blocks.append(Block(SCREEN_WIDTH/16 - SCREEN_WIDTH/80, SCREEN_HEIGHT-SCREEN_HEIGHT/15, SCREEN_WIDTH/20, SCREEN_HEIGHT/30, Color.LIGHT_GREY.value, type="spawn")) #spawn point
    blocks.append(Block(0, SCREEN_HEIGHT-SCREEN_HEIGHT/30, SCREEN_WIDTH, SCREEN_HEIGHT/30, Color.RED.value, type="lava")) #ground
    blocks.append(Block(SCREEN_WIDTH - SCREEN_WIDTH/10, SCREEN_HEIGHT*2/15, SCREEN_WIDTH/10, SCREEN_HEIGHT*13/15,Color.RED.value, type="lava"))

    #verticals
    blocks.append(Block(SCREEN_WIDTH/4, SCREEN_HEIGHT/8, SCREEN_WIDTH/40, SCREEN_HEIGHT*7/8 - SCREEN_HEIGHT/30,Color.BLUE.value))
    blocks.append(Block(SCREEN_WIDTH/2, 0, SCREEN_WIDTH/40, SCREEN_HEIGHT*7/8 - SCREEN_HEIGHT/30,Color.BLUE.value))

    #jump 1st part
    blocks.append(Block(SCREEN_WIDTH/4 - SCREEN_WIDTH * 3/32, SCREEN_HEIGHT*3/4 + SCREEN_HEIGHT/30, SCREEN_WIDTH/16, SCREEN_HEIGHT/30, Color.BURGUNDY.value, type="jump"))
    blocks.append(Block(PLAYER_WIDTH*2, SCREEN_HEIGHT*3/8 + SCREEN_HEIGHT/20 + SCREEN_HEIGHT/30, SCREEN_WIDTH/16, SCREEN_HEIGHT/30, Color.BURGUNDY.value, type="jump"))

    #lava in air
    length_between_vertical = SCREEN_WIDTH/4 - SCREEN_WIDTH/40
        #1st floor
    blocks.append(Block(SCREEN_WIDTH/4 + SCREEN_WIDTH/40, SCREEN_HEIGHT/4, length_between_vertical/4, SCREEN_HEIGHT/30,Color.RED.value, type="lava"))
    blocks.append(Block(SCREEN_WIDTH/4 + SCREEN_WIDTH/40 + length_between_vertical/2, SCREEN_HEIGHT/4, length_between_vertical/2, SCREEN_HEIGHT/30,Color.RED.value, type="lava"))
        #interfloor
    blocks.append(Block(SCREEN_WIDTH/4 + SCREEN_WIDTH/40 + length_between_vertical/4, SCREEN_HEIGHT*3/8, length_between_vertical/4, SCREEN_HEIGHT/30,Color.BLUE.value))
        #2nd floor
    blocks.append(Block(SCREEN_WIDTH/4 + SCREEN_WIDTH/40, SCREEN_HEIGHT/2, length_between_vertical*3/5, SCREEN_HEIGHT/30,Color.RED.value, type="lava"))
    blocks.append(Block(SCREEN_WIDTH/4 + SCREEN_WIDTH/40 + length_between_vertical*4/5, SCREEN_HEIGHT/2, length_between_vertical/5, SCREEN_HEIGHT/30,Color.RED.value, type="lava"))
        #interfloor
    blocks.append(Block(SCREEN_WIDTH/4 + SCREEN_WIDTH/40 + length_between_vertical*3/5, SCREEN_HEIGHT*5/8, length_between_vertical/5, SCREEN_HEIGHT/30,Color.BLUE.value))
        #3rd floor
    blocks.append(Block(SCREEN_WIDTH/4 + SCREEN_WIDTH/40, SCREEN_HEIGHT*3/4, length_between_vertical*1/6, SCREEN_HEIGHT/30,Color.RED.value, type="lava"))
    blocks.append(Block(SCREEN_WIDTH/4 + SCREEN_WIDTH/40 + length_between_vertical*2/6, SCREEN_HEIGHT*3/4, length_between_vertical*4/6, SCREEN_HEIGHT/30,Color.RED.value, type="lava"))
        #interfloor
    blocks.append(Block(SCREEN_WIDTH/4 + SCREEN_WIDTH/40 + length_between_vertical*1/6, SCREEN_HEIGHT*7/8, length_between_vertical/6, SCREEN_HEIGHT/30,Color.BLUE.value))
    
    blocks.append(Block(SCREEN_WIDTH/4 + SCREEN_WIDTH/40 + length_between_vertical*3/5, SCREEN_HEIGHT*28/30, length_between_vertical/5, SCREEN_HEIGHT/60,Color.BLUE.value))
    
    blocks.append(Block(SCREEN_WIDTH/4 + SCREEN_WIDTH/40 + length_between_vertical, SCREEN_HEIGHT*57/60, length_between_vertical/5, SCREEN_HEIGHT/60,Color.BLUE.value))

    blocks.append(Block(SCREEN_WIDTH*3/4, SCREEN_HEIGHT*57/60, length_between_vertical/5, SCREEN_HEIGHT/60,Color.BLUE.value))

    blocks.append(Block(SCREEN_WIDTH*9/10 - length_between_vertical/10, SCREEN_HEIGHT*47/60, length_between_vertical/10, SCREEN_HEIGHT/60,Color.BURGUNDY.value, type="jump"))

    blocks.append(Block(SCREEN_WIDTH*5/8 - length_between_vertical/10, SCREEN_HEIGHT*5/8, length_between_vertical/10, SCREEN_HEIGHT/60,Color.BURGUNDY.value, type="jump"))

    blocks.append(Block(SCREEN_WIDTH*9/10- length_between_vertical/10, SCREEN_HEIGHT*3/8, length_between_vertical/10, SCREEN_HEIGHT/60,Color.BURGUNDY.value, type="jump"))



    blocks.append(Block(SCREEN_WIDTH - (SCREEN_WIDTH/16 - SCREEN_WIDTH/80) - SCREEN_WIDTH/20, SCREEN_HEIGHT/10, SCREEN_WIDTH/20, SCREEN_HEIGHT/30, Color.YELLOW.value, type="win"))

    return blocks