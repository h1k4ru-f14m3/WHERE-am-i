import pygame
import settings
from game import Game
from menus import Menu
from music import play_music
import json


# Initialize Pygame and prepare the window
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_icon(pygame.image.load('resources/entities/player/detective-front-static.png').convert_alpha())
pygame.display.set_caption('WHERE (am i)')
clock = pygame.time.Clock()

# Initialize the Main Menu, Game and Configs
main = Menu(clock)
game = Game(clock)

settings.load_config("config/config.json")

# Window Loop
while settings.running:
    # Play The Background Music
    if settings.config['sound'] == "on":
        play_music()

    # Menus and Game
    if settings.onMainMenu:
        main.main_menu()
    elif settings.onSettings:
        main.settings_menu()
    elif settings.onPause:
        main.pause_menu()
    elif settings.isPlaying:
        game.run()

# Save Config and quit
settings.save_config("config/config.json")
pygame.quit()