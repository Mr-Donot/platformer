import pygame
from constants import *
from player import *
from block import *
from map import *
from random import *
import sys


class Homepage():

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Platformer")
        self.result = None


    def create_one_bouton(self, texte, x, y):
        police = pygame.font.Font(None, 36)
        texte_surface = police.render(texte, True, Color.BLACK.value)
        texte_rect = texte_surface.get_rect(center=(x, y))
        return texte_surface, texte_rect
    

    def create_all_buttons(self):
        x_bouton = SCREEN_WIDTH // 2
        y_aventure = SCREEN_HEIGHT // 5
        y_free_play = SCREEN_HEIGHT * 2 // 5
        y_two_players = SCREEN_HEIGHT * 3 // 5
        y_exit = SCREEN_HEIGHT * 4 // 5

        self.aventure_surface, self.aventure_rect = self.create_one_bouton("Aventure", x_bouton, y_aventure)
        self.free_play_surface, self.free_play_rect = self.create_one_bouton("Free Play", x_bouton, y_free_play)
        self.two_players_surface, self.two_players_rect = self.create_one_bouton("2 Players", x_bouton, y_two_players)
        self.exit_surface, self.exit_rect = self.create_one_bouton("Exit", x_bouton, y_exit)


    def run(self):
        self.create_all_buttons()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.aventure_rect.collidepoint(event.pos):
                        pygame.quit()
                        return ["game", FPS, [0, 1, 2, 3]]
                    elif self.free_play_rect.collidepoint(event.pos):
                        pygame.quit()
                        return ["freeplay", None, None]

                    elif self.two_players_rect.collidepoint(event.pos):
                        pygame.quit()
                        return ["2players", FPS, [randint(0, 3)]]
                        
                    elif self.exit_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

            # Affichage des boutons
            self.screen.fill(Color.WHITE.value)

            pygame.draw.rect(self.screen, Color.CYAN.value, self.aventure_rect)
            self.screen.blit(self.aventure_surface, self.aventure_rect)

            pygame.draw.rect(self.screen, Color.LIGHT_GREEN.value, self.free_play_rect)
            self.screen.blit(self.free_play_surface, self.free_play_rect)

            pygame.draw.rect(self.screen, Color.YELLOW.value, self.two_players_rect)
            self.screen.blit(self.two_players_surface, self.two_players_rect)

            pygame.draw.rect(self.screen, Color.DARK_GREY.value, self.exit_rect)
            self.screen.blit(self.exit_surface, self.exit_rect)

            # Mise à jour de l'écran
            pygame.display.flip()