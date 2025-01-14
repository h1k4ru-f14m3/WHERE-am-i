# <ins>WHERE (am i)</ins>

A barebone top down pixel art RPG game.  
  
This project is written in Python using mainly the pygame library.  
  
This project and source code can be used to make a RPG game. 

## Features

This barebone game includes all essential features of one.

### Walking Around
You can go explore around the map, into buildings and just role play by yourself.
### Collision Check
It just wouldn't feel right without hitting objects while you explore, right?
### Player Animation
A static player image is pretty boring in my opinion, don't you think?
### Maps
There is only one map but there are many things to explore! 
### Menus
Every game needs a main menu, settings, and pause screen!
### Background Music
Some music to break the silence!
### Changing Keybinds
Not everyone is the same so why hard code specific keybinds?
### Y Sort (A little wonky but works)
A sense of depth in a 2d game.

## File Structure

The main root directory:
```bash
.
├── config      # The directory for the config file
├── modules     # The modules of the game
├── music       # Background music files here
├── resources   # The graphics of the game 
├── README.md   
└── main.py     # The main file of the game which runs it
```

Modules:
```bash
.
├── ...
├── modules
│   ├── buildings.py        # Loads the building images on the main map
│   ├── camera.py           # Renders everything in the game
│   ├── game.py             # The main game loop
│   ├── map.py              # Loads the main map and tmx files for the building interiors
│   ├── menus.py            # Includes the main menu, settings menu and the pause menu
│   ├── music.py            # Plays the background music
│   ├── player.py           # Includes the logic, image and animation of the player
│   ├── settings.py         # Includes game states and loads the config
│   ├── sprites.py          # Loads sprites into memory
├── ...
```

## Breakdown

## Installation

## Credits

## Note to CS50x staff