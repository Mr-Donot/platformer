import pygame
from constants import *
from player import *
from block import *
from map import *

class Game():

    def __init__(self, fps=60, maps=[0]):
        self.fps = fps
        self.maps = maps
        self.start()
        

    def init_player(self):
        self.player = Player(SCREEN_WIDTH/16, SCREEN_HEIGHT - 70, SCREEN_WIDTH/40, SCREEN_HEIGHT/20)

    def init_block(self, id_map):
        self.blocks = generate_map(id_map)
        

    def start(self):
        pygame.init()
        
        
        for m in self.maps:
            self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
            pygame.display.set_caption("Platformer")
            self.init_player()
            self.init_block(m)
            self.run()
        
        pygame.quit()


    def run(self):
        self.running = True
        clock = pygame.time.Clock()
        mouse_button_held = False
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            mouse_buttons = pygame.mouse.get_pressed()

            #if mouse needed
            if mouse_buttons[0]:
                mouse_x, mouse_y = pygame.mouse.get_pos()
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


            if keys[pygame.K_DOWN] :
                if not self.player.is_down:
                    self.player.y += SCREEN_HEIGHT/40
                    self.player.height = SCREEN_HEIGHT/40
                    self.player.is_down = True
                    self.player.speed_x /=2
                    self.player.jumping_height *=1.5

            else:
                if self.player.is_down:
                    self.player.y -= SCREEN_HEIGHT/40
                    self.player.height = SCREEN_HEIGHT/20
                    self.player.speed_x *= 2
                    self.player.jumping_height /=1.5
                    self.player.is_down = False

            self.update()
            clock.tick(self.fps)



    def draw_map(self):
        self.screen.fill(Color.BLACK.value)
        block : Block
        for block in self.blocks:
            pygame.draw.rect(self.screen, block.color, (block.x, block.y, block.width, block.height))
        

    def update(self):

        self.draw_map()
        
        self.player.x += self.player.dx
        self.jump(self.player)
        self.add_gravity(self.player)
        self.add_friction(self.player)

        self.player.y += self.player.dy

        self.check_collisions(self.player)


        #draw player
        if self.player.is_buff_jump:
            self.player.color = Color.WHITE.value
        else:
            self.player.color = Color.RED.value
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
        player_rect = pygame.Rect(player.x, player.y, player.width, player.height)
        player_moved = False

        if player.dx != 0 or player.dy != 0:
            for block in self.blocks:

                block_rect = pygame.Rect(block.x, block.y, block.width, block.height)
                if player_rect.colliderect(block_rect):
                    block.apply_effect(self)
                    if block.type != "jump" and player.is_buff_jump :
                        player.jumping_height *= BUFF_JUMP
                        player.is_buff_jump = False

                    #player fall
                    if player.dy > 0:
                        if block.y > player.y > block.y - player.height  :
                            player.y = block.y - player.height 
                            player.dy = 0

                            player.jumping = False
                            player.can_jump = True
                        else:
                            if player.dx > 0:
                                if block.x > player.x > block.x - player.width  :
                                    player.x = block.x - player.width - 1
                            elif player.dx < 0:
                                if block.x < player.x < block.x + block.width :
                                    player.x = block.x + block.width + 1



                    #player is jumping
                    elif player.dy < 0:
                        
                        if block.y + block.height <= player.y - player.dy:
                            player.y = block.y + block.height
                            player.dy = 0
                        else:
                            if player.dx > 0:
                                if block.x > player.x > block.x - player.width :
                                    player.x = block.x - player.width - 1
                            elif player.dx < 0:
                                if block.x < player.x < block.x + block.width  :
                                    player.x = block.x + block.width + 1
                        


                    player_moved = True

            # Boundary checks to keep the player within the window
            if player.x < 0:
                player.x = 0
            elif player.x > SCREEN_WIDTH - player.width:
                player.x = SCREEN_WIDTH - player.width

            if player.y < 0:
                player.y = 0
            elif player.y > SCREEN_HEIGHT - player.height:
                player.y = SCREEN_HEIGHT - player.height
                player.dy = 0
                player.jumping = False
                player.can_jump = True

        if not player_moved:
            player.x += player.dx