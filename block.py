


class Block():

    def __init__(self, x, y, width, height, color, type="normal"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.type = type

    def __str__(self):
        return f"{self.type} : \n x,y : [{self.x},{self.y}]\n w,h : [{self.width},{self.height}]"
