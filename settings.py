import pygame

# Sprites Group for Collisions
active_sprites = pygame.sprite.Group()
doors = pygame.sprite.Group()
draw_order = {
    "Ground": 0,
    "Objects-3": 1,
    "Player": 2,
    "Wall": 3,
    "Objects-1": 4,
    "Objects-2": 5,
    "Wall-Outline-1": 6,
    "Wall-Outline-2": 6,
    "Wall-Outline-3": 6,
    "Doors-1": 4,
    "Doors-2": 7
}


# Game States and Booleans

onMainMenu = False
onMainMap = True
inBuilding = False
building = "None"
starting = (0,0)
ending = (0,0)