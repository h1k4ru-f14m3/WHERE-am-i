import pygame
import json

# Sprites Group for Collisions
active_sprites = pygame.sprite.Group()
doors = pygame.sprite.Group()
draw_order = {
    "Stairs-Tiles": 0,
    "Stairs-Obj": 0,
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
    "Doors-2": 7,
    "Top": 8
}


# Game States and Booleans

running = True

onMainMenu = True
onSettings = False
onPause = False
isPlaying = False

onMainMap = True

inBuilding = False
building = "None"
current_floor = 0

stair_end = (0,0)
starting = (0,0)
ending = (0,0)

# Configs

config = {}

def load_config(file_path):
    with open(file_path, "r") as data:
        config.update(json.load(data))

def save_config(file_path):
    data = json.dumps(config)
    with open(file_path, "w") as file:
        file.write(data)