import pygame
from game import Game


screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

game = Game(clock)
game.run()