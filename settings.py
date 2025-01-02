import pygame

# Sprites LayeredUpdates for Collisions
active_sprites = pygame.sprite.LayeredUpdates()

# The Ground Tiles
map_tiles = pygame.sprite.LayeredUpdates()

# The Sprites to have y sort
object_sprites = pygame.sprite.LayeredUpdates()

# Draw Order
draworder = ["Objects-3", "Wall", "Objects-1", "Objects-2", "Wall-Outline-1", "Wall-Outline-2", "Wall-Outline-3"]

# All Visible Sprites
all_sprites = {
    "Doors-1": pygame.sprite.LayeredUpdates(),
    "Objects-3": pygame.sprite.LayeredUpdates(),
    "Wall": pygame.sprite.LayeredUpdates(),
    "Stairs-Obj": pygame.sprite.LayeredUpdates(),
    "Stairs-Tiles": pygame.sprite.LayeredUpdates(),
    "Objects-1": pygame.sprite.LayeredUpdates(),
    "Objects-2": pygame.sprite.LayeredUpdates(),
    "Wall-Outline-1": pygame.sprite.LayeredUpdates(),
    "Wall-Outline-2": pygame.sprite.LayeredUpdates(),
    "Wall-Outline-3": pygame.sprite.LayeredUpdates(),
    "Doors-2": pygame.sprite.LayeredUpdates()
}

all_sprites_keys = list(all_sprites.keys())

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
