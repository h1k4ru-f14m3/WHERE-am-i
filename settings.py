import pygame

# Sprites Group for Collisions
active_sprites = pygame.sprite.Group()
draw_order = {
    "Ground": 0,
    "Objects-3": 1,
    "Doors-1": 1,
    "Player": 2,
    "Wall": 3,
    "Objects-1": 4,
    "Objects-2": 5,
    "Wall-Outline-1": 6,
    "Wall-Outline-2": 6,
    "Doors-2": 7
}


# Game States and Booleans

onMainMenu = False
onMainMap = False

inTomDiner = False
inMart = False
inPolice1 = False
inPolice2 = False

inHouse1 = False
inHouse2 = False
inHouse3a = False
inHouse3b = False
