from homePage import *
from freeplay import *
from game import *



class GameManager():

    def __init__(self, result="homepage"):
        self.result = result
        self.use_result()


    def launch_homepage(self):
        self.page = Homepage()
        self.result = self.page.run()
        self.use_result()


    def launch_freeplay(self):
        self.page = Freeplay()
        self.result = self.page.run()
        self.use_result()
    
    def launch_2players(self, fps, maps):
        self.page = Game(fps, maps)
        self.result = self.page.run()
        self.use_result()

    def launch_game(self, fps, maps):
        self.page = Game(fps, maps)
        self.result = self.page.run()
        self.use_result()


    def use_result(self):
        if self.result is None:
            return
        if self.result[0] == "homepage" or self.result == "homepage":
            self.launch_homepage()
        elif self.result[0] == "freeplay" or self.result == "freeplay":
            self.launch_freeplay()
        elif self.result[0] == "2players" or self.result == "2players":
            self.launch_2players(self.result[1], self.result[2])
        elif self.result[0] == "game":
            self.launch_game(self.result[1], self.result[2])
        