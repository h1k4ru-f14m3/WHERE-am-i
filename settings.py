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


# The Ground Tiles
map_tiles = pygame.sprite.Group()

# The Sprites to have y sort
object_sprites = pygame.sprite.Group()

# Draw Order
draworder = ["Objects-3", "Wall", "Objects-1", "Objects-2", "Wall-Outline-1", "Wall-Outline-2", "Wall-Outline-3"]

# All Visible Sprites
all_sprites = {
    "Doors-1": pygame.sprite.Group(),
    "Objects-3": pygame.sprite.Group(),
    "Wall": pygame.sprite.Group(),
    "Stairs-Obj": pygame.sprite.Group(),
    "Stairs-Tiles": pygame.sprite.Group(),
    "Objects-1": pygame.sprite.Group(),
    "Objects-2": pygame.sprite.Group(),
    "Wall-Outline-1": pygame.sprite.Group(),
    "Wall-Outline-2": pygame.sprite.Group(),
    "Wall-Outline-3": pygame.sprite.Group(),
    "Doors-2": pygame.sprite.Group()
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
