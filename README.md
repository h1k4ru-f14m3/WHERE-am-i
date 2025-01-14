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

Resources:
```bash
.
├── ...
├── resources
│   ├── buildings               # Building images/graphics on the main map
│   ├── entities/player         # Player frames
│       ├── back-static.png
│       ├── back-walk-1.png
│       ├── ...
│       ├── back-walk-4.png
│       ├── front-static.png
│       ├── ...
│       ├── left-static.png
│       ├── ...
│       ├── right-static.png
│       ├── ...
│   ├── maps                    # Interiors for the buildings (tmx files and Tilesets)
│   ├── menu
│       ├── fonts               # The font used in the menus
│       ├── pressed             # The pressed version of the buttons
│       ├── static              # The static version or the normal state of the buttons
└── ...
```



## <ins>Breakdown</ins>
This section is about how I wrote the modules for the game; the logic, design, etc.

### ```settings.py```
This module is where I store the game states and load the config into memory. It also includes draw order for the sprites and collision groups. Basically, I wrote all the global variables, the variables I would need to access throughout modules in this file.

#### ```load_config()```
This function uses the json library from python to load ```config.json``` into a dictionary. In ```config.json```, there are user-defined keybinds which the user can change in the settings menu. Most keybinds are in ASCII but for other keys such as UP arrow, DOWN arrow, they are some big value that frankly, I'm not familiar of. I couldn't find out what those values stand for either. I assume those big values are pygame's own mapping for keys.

#### ```save_config()```
This function also uses the json library from python like ```load_config()``` but to save the config in the ```config.json```. 

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
This module is where all the menus are located: main menu, settings menu, and the pause menu. It also includes buttons and their functionality.


#### ```class button()```
This is the class that creates buttons to use in the menus. The arguements of this class are:
- name          *(The name to differenciate the buttons)*
- type          *(The image/resource for the button)*
- pos           *(The position of the button)*
- group         *(The sprite group the button will be in)*
- text="None"   *(The text of the button)*
- listen=True   *(Will the button use the ```listen()``` function)*

*Note: there are 4 more functions in the menus.py that I will not dive deep in because they are easy to understand. They are mainly made for code organization sake.*

#### ```listen()```
This function listens for user mouse movement and input. When the button is hovered, the button image will change to the pressed version which is in the pressed folder. For buttons that will do something, they are in if statements which check their names and mouse press event.

*Note: In each menu's while loop, the buttons are updated each iteration*


#### ```class Menu()```
You can see the Menu class is called before the game loop in the main.py. The reason is in the ```__init__``` function, the variables that are needed in all the menus: screen, clock, and font file are initialized.

*Note: the clock is passed as an arguement. The screen is initialized from getting the display surface with pygame.display.get_surface()*


#### ```main_menu()```
This function prepares the main menu and starts a while loop that displays or renders the main menu. 

It initializes the player image to display at the center of the screen, the play button and the settings button. Then, the while loop starts. It fills the screen with the background color I chose. After that, the player image, the logo text, and the buttons are rendered in the ordered I described. The code after that is just a pygame norm to make the display actually render sprites and images.

*Note: the logo text is initialized in the ```__init__``` function*


#### ```pause_menu()```
This function is frankly a copy-paste of ```main_menu()```. The only difference is that there is a hint text telling: *"Press ESC to go back..."* and instead of the play button, it is a main menu button which returns to the ```main_menu()```


#### ```settings_menu()```
This function is very similar to ```main_menu()```. It initializes the variables, images, texts needed for the settings menu. Then, a while loop is started which renders in the same order as ```main_menu()```. There is also a hint text like ```pause_menu()``` to go back to the main menu.

There is one thing different in the initialization process or the preparing process. In the ```main_menu()``` since there are only 2 buttons, I initialized them separately. However, in the ```settings_menu()```, since there are a total of 5 settings and different buttons, I figured it was inefficient to initialize them separately. Not to mention the labels of the settings which in total will make 10 buttons to initialize. So, I created a dictionary like below for the movement settings. The music on/off button has a different resource which needs to be handled by itself.

```python
labels = {
    'forward': ['move-forward', 'Move Forward', (355,163), (638,163)],
    'left': ['move-left', 'Move Left', (355, 243), (638,243)],
    'backward': ['move-backward', 'Move Backward', (355, 323), (638,323)],
    'right': ['move-right', 'Move Right', (355, 403), (638,403)],
}
```

*The key is the name of the setting. Check the ```config``` structure from above.*

*The values are: the name of the button, the text to be shown, the label position, and the button position.*

After that I initialize those buttons along with their labels in a for-loop. For the music button, I initialize its label and button like I did in ```main_menu()```; I manually initialized them because it seems better and more simple this way. After all this initialization, the while loop starts and does the same as ```main_menu()```.



### ```music.py```
This module is used to play the background music of the game. The functions in this file mainly uses pygame's mixer class which is used to play music. 

There are only 2 functions in this file: ```play_music()``` and ```stop_music()```. Both functions check whether or not the music is already playing. If so, it just returns. If not, they do what they are meant to do; play the background music.

*Note: I do not own the music used in this project.*

### ```sprites.py```
This module is used to initialize the sprites used in the main game. It's really short so I will cut right to the chase. 

This module's class: ```GameSprite()```, sets the sprite's name, image, rect, hitbox, y sort value and z value. The rect is the same as hitbox. I set hitbox the same as rect so there would be less confusion between them. Also, in ```player.py```, the player's collisions are handled with its hitbox which is not the same as its rect. The usage of the Y sort value and Z value is in the ```camera.py```.

### ```map.py```
This module is used to render the interiors of buildings which are tmx files. I named this module ```map.py``` because this can also be used to render tmx files for custom maps which follows the following template and draw order(Last to first):

```bash
11. Hitbox              # The Hitbox layers must not be visible and can have any name.
10. Doors-2
9.  Wall-Outline-3
8.  Wall-Outline-2
7.  Wall-Outline-1
6.  Mini-Objects
5.  Objects-2
4.  Objects-1
3.  Doors-1
2.  Wall
1.  Ground
```

*Note: The tmx file doesn't need to have all the layers. However, all visible layers must have the name as listed above.*

#### ```render_map()```
This function, like the name suggests, renders the map or the tmx file. The arguments of this function are as follows:
- type            *(The file name)*
- group           *(The sprites group that the visible objects will be in)*
- collision_group *(The group that is going to be used to check collisions)*
- floor_num=0     *(the floor of the interior; 0=No second floor)*

Before rendering the map, the function checks all the arguements, especially the floor_num. If the floor_num is higher than 0, a suffix is added to the file name that is going to be used to load the tmx file. Then, the tmx file is loaded using pytmx.

For the layers in the tmx file, 4 for-loops are used to load since there are 4 types of layers: Tile Layers, Object Layers, Invisible Object Layers(Hitboxes), and Markers. Yes, I know it is inefficient but that was the only way I knew to load different layers. In the for-loops, I used the ```GameSprite()``` class in the ```sprites.py``` module to load the objects, tiles, and hitboxes. For the hitboxes, since they don't have a Surface or an image, I had to set the Surface of them by providing additional values for their width and height. For the markers, their positions are stored in a dictionary in the ```settings.py```.

### ```buildings.py```
### ```camera.py```
### ```player.py```
### ```game.py```

## <ins>Installation</ins>

## <ins>Credits</ins>

## <ins>Note to CS50x staff</ins>