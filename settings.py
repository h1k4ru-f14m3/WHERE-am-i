import pygame

# Sprites Group for Collisions
active_sprites = pygame.sprite.Group()

# The Ground Tiles
map_tiles = pygame.sprite.Group()

# Wall and Wall Outlines
wall_tiles = pygame.sprite.Group()
wall_outline_tiles = pygame.sprite.Group()

# The Sprites to have y sort
object_sprites = pygame.sprite.Group()

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
