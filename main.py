import pygame
import settings
from game import Game
from menus import Menu
import json

pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
main = Menu(clock)
game = Game(clock)

settings.load_config("config/config.json")

while settings.running:
    if settings.onMainMenu:
        main.main_menu()
    elif settings.onSettings:
        main.settings_menu()
    elif settings.onPause:
        main.pause_menu()
    elif settings.isPlaying:
        game.run()

settings.save_config("config/config.json", settings.config)
pygame.quit()