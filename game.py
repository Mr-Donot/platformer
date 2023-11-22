import pygame
from constants import *
from player import *
from block import *
from map import *

class Game():

    def __init__(self, fps=60, maps=[0], nb_player=1):
        self.fps = fps
        self.maps = maps
        self.nb_player = nb_player
        

    def init_players(self, keys=["up", "down", "left", "right"], color=Color.GREEN.value, name="player_1"):
        
        self.players.append(Player(self.spawn_block.x + (self.spawn_block.width - PLAYER_WIDTH)/2 , self.spawn_block.y - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT, color=color, keys=keys, name=name))

    def init_block(self, id_map):
        self.blocks = generate_map(id_map)
        self.spawn_block : Block = self.get_spawn_point()
        
    def get_spawn_point(self):
        for block in self.blocks:
            if block.type == "spawn":
                return block
        return None
                

    def run(self):
        pygame.init()
        for m in self.maps:
            self.players = []
            self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
            pygame.display.set_caption("Platformer")
            self.init_block(m)
            self.init_players(keys=["up", "down", "left", "right"], color=Color.RED.value, name="player_1")
            if self.nb_player == 2:
                self.init_players(keys=["z", "s", "q", "d"], color=Color.CYAN.value, name="player_2")

            has_quit = self.run_one_map()
            if has_quit :
                break
        pygame.quit()
        return "homepage" #TODO page de win / game over ici


    def run_one_map(self):
        self.running = True
        clock = pygame.time.Clock()
        mouse_button_held = False
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return True
            
            mouse_buttons = pygame.mouse.get_pressed()

            #if mouse needed
            if mouse_buttons[0]:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if not mouse_button_held:
                    mouse_button_held = True
                else:
                    mouse_button_held = False

            keys = pygame.key.get_pressed()
            for player in self.players:
                self.move_player(player, keys)

            self.update()
            clock.tick(self.fps)
        return False

    def move_player(self, player, keys):
        if keys[KEYS[player.keys[2]]]:
            player.dx -= player.speed_x

        if keys[KEYS[player.keys[3]]]:
            player.dx += player.speed_x

        if keys[KEYS[player.keys[0]]] and player.can_jump:
            player.jumping = True
            player.can_jump = False


        if keys[KEYS[player.keys[1]]] :
            if not player.is_down:
                player.y += SCREEN_HEIGHT/40
                player.height = SCREEN_HEIGHT/40
                player.is_down = True
                player.speed_x /=2
                player.jumping_height *=1.5

        else:
            if player.is_down:
                player.y -= SCREEN_HEIGHT/40
                player.height = SCREEN_HEIGHT/20
                player.speed_x *= 2
                player.jumping_height /=1.5
                player.is_down = False

    def draw_map(self):
        self.screen.fill(Color.BLACK.value)
        block : Block
        for block in self.blocks:
            pygame.draw.rect(self.screen, block.color, (block.x, block.y, block.width, block.height))
        

    def update(self):

        self.draw_map()
        
        for player in self.players:
            player.x += player.dx
            self.jump(player)
            self.add_gravity(player)
            self.add_friction(player)

            player.y += player.dy

            self.check_collisions(player)


            #draw player
            if player.is_buff_jump:
                player.color = Color.WHITE.value
            else:
                if player.name == "player_1" :player.color = Color.RED.value
                if player.name == "player_2" :player.color = Color.CYAN.value

            pygame.draw.rect(self.screen, player.color, (player.x, player.y, player.width, player.height))
            pygame.display.flip()
            
    def jump(self, player: Player):
        if player.jumping and player.nb_jumping_frame < self.fps * player.jumping_time:
            player.dy = - (60 / player.jumping_height) / player.jumping_time
            player.nb_jumping_frame += 1
        else:
            player.jumping = False
            player.nb_jumping_frame = 0


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
                    block.apply_effect(self, player)
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
                player.dy = 0
            elif player.y > SCREEN_HEIGHT - player.height:
                player.y = SCREEN_HEIGHT - player.height
                player.dy = 0
                player.jumping = False
                player.can_jump = True

        if not player_moved:
            player.x += player.dx