import pygame
import math
from random import randint
from constants import *
from player import *

class Game():

    def __init__(self, fps=60):
        self.fps = fps
        self.start()

    def init_player(self):
        self.player = Player(20, 20, 30, 50)


    def start(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Platformer")
        self.init_player()
        self.run()

    def run(self):
        running = True
        clock = pygame.time.Clock()
        mouse_button_held = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            mouse_buttons = pygame.mouse.get_pressed()

            #add circle
            if mouse_buttons[0]:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print("here", mouse_x, mouse_y)
                if not mouse_button_held:
                    mouse_button_held = True
                else:
                    mouse_button_held = False



            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.player.dx -= self.player.speed_x

            if keys[pygame.K_RIGHT]:
                self.player.dx += self.player.speed_x

            if keys[pygame.K_UP] and self.player.can_jump:
                self.player.jumping = True
                self.player.can_jump = False


            if keys[pygame.K_DOWN]:
                self.player.dy =0
                self.player.jumping = False
                self.player.nb_jumping_frame = 0

            self.update()
            clock.tick(self.fps)

        pygame.quit()

            
    def update(self):

        self.screen.fill(Color.BLACK.value)

        
        self.player.x += self.player.dx
        self.jump(self.player)
        self.add_gravity(self.player)
        self.add_friction(self.player)

        self.player.y += self.player.dy

        self.check_collisions(self.player)

        #draw player
        pygame.draw.rect(self.screen, self.player.color, (self.player.x, self.player.y, self.player.width, self.player.height))
        pygame.display.flip()
            
    def jump(self, player: Player):
        if player.jumping and player.nb_jumping_frame < self.fps * player.jumping_time:
            player.dy = - (60 / player.jumping_height) / player.jumping_time
            player.nb_jumping_frame += 1
        else:
            player.jumping = False
            self.player.nb_jumping_frame = 0


    def add_gravity(self, player):
        if player.y < SCREEN_HEIGHT - player.height : player.dy += GRAVITY

    def add_friction(self, player):
        player.dx *= (1 - FRICTION)
        if -0.05 < player.dx < 0.05 : player.dx = 0

    def check_collisions(self, player):
        if player.x < 0:
            player.x = 0
            player.dx = 0
        elif player.x > SCREEN_WIDTH - player.width:
            player.x = SCREEN_WIDTH - player.width
            player.dx = 0 

        if player.y < 0:
            player.y = 0
            player.dy *= -1
        elif player.y > SCREEN_HEIGHT - player.height:
            player.y = SCREEN_HEIGHT - player.height
            player.dy = 0
            player.jumping = False
            player.can_jump = True
            