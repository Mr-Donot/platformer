import pygame
from constants import *
import sys, os

class Freeplay():

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Platformer")
        self.font = pygame.font.Font(None, 36)
        self.selected_map = None

    def create_button(self, text, x, y, color):
        text_surface = self.font.render(text, True, Color.BLACK.value)
        text_rect = text_surface.get_rect(center=(x, y))
        return text_surface, text_rect, color

    def create_dropdown(self):
        if os.path.exists("images/map_thumbnail"):
            file_names = [f for f in os.listdir("images/map_thumbnail") if os.path.isfile(os.path.join("images/map_thumbnail", f))]
        
        dropdown_options = []
        for name in file_names:
            dropdown_options.append({"id" : name.replace("map", "").replace(".png", ""),"image": pygame.image.load("images/map_thumbnail/"+name), "title": name.replace("map", "Map ").replace(".png", "")})


        footer = 200
        margin = 10
        dropdown_rect = pygame.Rect(margin, 100, SCREEN_WIDTH - 2 * margin, SCREEN_HEIGHT - margin - footer)  # Adjust the size of the dropdown
        dropdown_color = Color.LIGHT_GREY.value

        return dropdown_options, dropdown_rect, dropdown_color

    def resize_image(self, original_image, target_size):
        original_rect = original_image.get_rect()
        aspect_ratio = original_rect.width / original_rect.height
        new_width = int(target_size * aspect_ratio)
        new_height = int(target_size)
        return pygame.transform.scale(original_image, (new_width, new_height))

    def run(self):
        return_button_surface, return_button_rect, return_button_color = self.create_button("Return", 50, 50, Color.RED.value)
        play_button_surface, play_button_rect, play_button_color = self.create_button("Play", SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50, Color.GREEN.value)
        dropdown_options, dropdown_rect, dropdown_color = self.create_dropdown()

        num_images_per_row = 4
        image_width = 120  # Adjust the size of the images
        image_height = 90  # Adjust the size of the images

        #TODO put some variables in constants.py
        margin_inside_selector = 50
        selector_size = (SCREEN_WIDTH - 2 * 10, SCREEN_HEIGHT - 210)
        col_spacing = (selector_size[0] - (margin_inside_selector*2) - (num_images_per_row * image_width)) // (num_images_per_row - 1)
        
        row_spacing = (selector_size[1] - (margin_inside_selector*2) - ((len(dropdown_options) // num_images_per_row) * image_height)) // (num_images_per_row - 1)
        
        title_height = 20

        for option in dropdown_options:
            option["image"] = self.resize_image(option["image"], min(image_width, image_height))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if return_button_rect.collidepoint(event.pos):
                        pygame.quit()
                        return ["homepage", None, None]
                    elif play_button_rect.collidepoint(event.pos):
                        if self.selected_map is not None :
                            pygame.quit()
                            return ["game", 60, [int(self.selected_map)]] 
                    # Check if any dropdown option is clicked
                    for option in dropdown_options:
                        image_rect = option["image"].get_rect(topleft=(margin_inside_selector + dropdown_rect.x + (dropdown_options.index(option) % num_images_per_row) * (image_width + col_spacing),
                                                                       margin_inside_selector + dropdown_rect.y + (dropdown_options.index(option) // num_images_per_row) * (image_height + row_spacing + title_height)))
                        title_rect = pygame.Rect(image_rect.left, image_rect.bottom, image_width, title_height)
                        if image_rect.collidepoint(event.pos) or title_rect.collidepoint(event.pos):
                            play_button_surface, play_button_rect, play_button_color = self.create_button("Play " + option['title'], SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50, Color.GREEN.value)
                            self.selected_map = option['id']

            self.screen.fill(Color.WHITE.value)

            # Draw return button
            pygame.draw.rect(self.screen, return_button_color, return_button_rect)
            self.screen.blit(return_button_surface, return_button_rect)

            # Draw play button
            pygame.draw.rect(self.screen, play_button_color, play_button_rect)
            self.screen.blit(play_button_surface, play_button_rect)

            # Draw dropdown options
            pygame.draw.rect(self.screen, dropdown_color, dropdown_rect)
            for option in dropdown_options:
                image_rect = option["image"].get_rect(topleft=(margin_inside_selector + dropdown_rect.x + (dropdown_options.index(option) % num_images_per_row) * (image_width + col_spacing),
                                                               margin_inside_selector + dropdown_rect.y + (dropdown_options.index(option) // num_images_per_row) * (image_height + row_spacing + title_height)))
                self.screen.blit(option["image"], image_rect)
                title_font = pygame.font.Font(None, title_height)
                title_surface = title_font.render(option["title"], True, Color.BLACK.value)
                title_rect = title_surface.get_rect(topleft=(image_rect.left, image_rect.bottom))
                self.screen.blit(title_surface, title_rect)

            pygame.display.flip()

# Assuming you have defined Color class and SCREEN_WIDTH/SCREEN_HEIGHT constants elsewhere in your code
