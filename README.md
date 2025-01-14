# <ins>WHERE (am i)</ins>

A barebone top down pixel art RPG game.  
  
This project is written in Python using mainly the pygame library.  
  
This project and source code can be used to make a RPG game. 

## <ins>Features</ins>

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

## <ins>File Structure</ins>

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
│   ├── camera.py           # Renders everything in the game (except menus)
│   ├── game.py             # The main game loop
│   ├── map.py              # Loads the main map and tmx files for the building interiors
│   ├── menus.py            # Includes the main menu, settings menu and the pause menu
│   ├── music.py            # Plays the background music
│   ├── player.py           # Includes the logic, image and animation of the player
│   ├── settings.py         # Includes game states and loads the config
│   ├── sprites.py          # Loads sprites into memory
└── ...
```

## <ins>Breakdown</ins>
This section is about how I wrote the modules for the game; the logic, design, etc.
### ```settings.py```
This module is where I store the game states and load the config into memory. It also includes draw order for the sprites and collision groups. Basically, I wrote all the global variables, the variables I would need to access throughout modules in this file.
#### ```load_config()```
This function uses the json library from python to load ```config.json``` into a dictionary. In ```config.json```, there are user-defined keybinds which the user can change in the settings menu. Most keybinds are in ASCII but for other keys such as UP arrow, DOWN arrow, they are some big value that frankly, I'm not familiar of. I couldn't find out what those values stand for either. I assume those big values are pygame's own mapping.
#### ```save_config()```
This function also uses the json library from python but to save the config or the settings of the user in the ```config.json```. 
#### ```config = {}```
It might be confusing on what the config includes according to my words. So, here is what the config dictionary includes and the way it's structured after ```config.json``` is loaded.
```python
config = {
    'forward': 119,     # ASCII value for 'w'
    'left': 97,         # ASCII value for 'a'
    'backward': 115,    # ASCII value for 's'
    'right': 100,       # ASCII value for 'd'
    'sound': 'on'       
}
```
### ```menus.py```
### ```music.py```
### ```sprites.py```
### ```map.py```
### ```buildings.py```
### ```camera.py```
### ```player.py```
### ```game.py```

## <ins>Installation</ins>

## <ins>Credits</ins>

## <ins>Note to CS50x staff</ins>