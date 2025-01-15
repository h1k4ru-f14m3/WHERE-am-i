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

## <ins>Installation</ins>
Since this game is your generic python project, you can easily run this on your terminal, as long as you have python installed.

## Dependencies
- Pygame or Pygame-ce:
```bash
pip install pygame
       
pip install pygame-ce
```

- Pytmx:
```bash
pip install pytmx
```

### On Windows
- Open the terminal 
- Go into any directory you like
- Clone the git project:
```bash
git clone https://github.com/h1k4ru-f14m3/WHERE-am-i.git
```
- Go into the project repository:
```bash
cd WHERE-am-i
```
- Simply run the main.py:
```bash
python main.py
```

### On Linux
- Open the terminal
- Go into any directory you like
- Clone the git project:
```bash
git clone https://github.com/h1k4ru-f14m3/WHERE-am-i.git
```
- Go into the project repository:
```bash
cd WHERE-am-i
```
- Make a virtual enviornment for python:
```bash
python3 -m venv <env_name>      # Replace <env_name> with any name you like
```
- Activate the enviornment:
```bash
source <env_name>/bin/activate
```
- Install the dependencies
- Run main.py:
```bash
python3 main.py
```


## <ins>Credits</ins>
I did not collaborate with any developers on this project. However, I would like to note that:

**I DO NOT OWN THE MUSIC USED IN THIS PROJECT**

Credit for the music: [@TrishaRyan](https://www.youtube.com/@TrishaRyan) on Youtube

## <ins>Note to CS50x staff</ins>
I've used some of the suggestions given from [cs50.ai](https://cs50.ai) and also from Stack Overflow on this project. I have not them cited in the code when I wrote it and I can't remember which part of the code I used the suggestions from. That's why I am writing this note.

**Video Demo**: https://www.youtube.com/watch?v=dJOEIKyUPRI

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
│   └── menu
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

This module's class: ```GameSprite()```, sets the sprite's name, image, rect, hitbox, y sort value and z value. The rect is the same as hitbox. I set hitbox the same as rect so there would be less confusion between them. Also, in ```player.py```, the player's collisions are handled with its hitbox which is not the same as its rect. The usage of the Y sort value and Z value is for the draw order and rendering in ```camera.py```.

*Note: The ```y_sort``` value is the y position of the sprite.*

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

For the layers in the tmx file, 4 for-loops are used to load since there are 4 types of layers: Tile Layers, Object Layers, Invisible Object Layers(Hitboxes), and Markers. Yes, I know it is inefficient but that was the only way I knew to load different layers. In the for-loops, I used the ```GameSprite()``` class in the ```sprites.py``` module to load the objects, tiles, and hitboxes. For the hitboxes, since they don't have a Surface or an image, I had to set the Surface of them by providing additional values for their width and height. For the markers, their positions are stored in a dictionary in the ```settings.py``` module.

*Looking back, I don't think I should've named this ```render_map``` since technically, it just just loading the map into memory not rendering it onto the screen*

#### ```getin_building()```
I made this function so that I can easily get the player in the buildings and also for code organization sake. 

This function unloads the map using the ```unload_map()``` function in ```camera.py```. Then, from the player's collision, the sprite type is acquired which helps load the map using ```render_map()```. This function is also used to get upstairs of a building by passing the desired floor num in the arguements. Then, the function checks the current floor the player is in. The position of the player is acquired from the markers that ```render_map()``` acquired. If the player is going up, the player's position is set to the 'start' marker. If not, it is set to 'stair-end'.

### ```buildings.py```
This file includes the functions to initialize and load the buildings you see on the main map into sprite groups. 

#### ```class Buildings()```
This is where the building sprites are initialized, similar to the ```GameSprite()``` class mentioned in ```sprites.py```.

There are some differences between them however. This ```Buildings()``` class initialize the sprite's name, image, rect, hitbox, y sort value and z value like ```GameSprite()``` but the usage of ```GameSprites()``` were for sprites that have their own hitboxes already determined in the tmx files. That's why the rect = hitbox in ```GameSprites()```. However, you may have already realized, the main map isn't a tmx file but rather a png file. The reason was solely because when I was working on the main map, I had little to no knowledge of pygame and its capabilities yet. 

Since everything is just a png file, the hitboxes weren't automatically determined. So, I had to determine them myself using the pygame's ```inflate()``` method which can be used to change the rect of the sprite, to make the hitbox. Then, the hitbox's midbottom position is set to the midbottom of the original rect so that the player will hit the bottom of the building and not hit the top of the building. 

There is also a door position which gets the player into the building when it collides with it. The door position is the midbottom of the sprite's rect. For the sprites that are weird or their doors have an offset, I manually changed the door position. (Take a look at Mart in the game)

#### ```build()```
This method is outside the ```Buildings()``` class so that I can call it to initialize the buildings. This method takes the usual name and group object but the interesting ones are x_pos, y_pos, and counts. It also takes the hitbox size to be set in ```Buildings()```. The main thing it does is initialize all the buildings of a given type so that I don't need to keep repeating ```Buildings()```.

Now, you might be wondering what those 'interesting' arguements are. Well, they are all lists. For simplicity, think of x_pos as the columns in the main map and the y_pos as the rows. The counts are the number of buildings in each row. For example:

```python
x_pos = [5,6,7,6]   # x positions of the buildings
y_pos = [4,3]       # y positions of the buildings
count = [2,2]       # the counts on each y position
```

What this function is going to do is going to loop through the y positions. Then, loop through the x positions, forming a nested loop. The outer loop is for each index of y_pos and the inner is for x_pos. If the index of x_pos loop is greater or equal to the count at the index of y_pos then break the loop for x_pos and then the loop for y_pos restarts. (In the example's first iteration of y_pos(4), when the index(i) for x_pos reaches 2 which is equal to count[0/the index of y_pos], the for-loop for x_pos is broken and the for-loop for y_pos restarts at y_pos[1] or 3.) If not, a building is initialized with the ```Buildings()``` class.

*There is an external index that is keeping track of the x_pos with the resets so the x positions can be assigned correctly.*

#### ```buildall()```
Like the ```build()``` method reduces the amount of copy-paste for ```Buildings()```, this function reduces the copy-paste for ```build()```. 

This function not just initializes one building, it initializes all of them in the main map. For the buildings that have no repetition, I manually initialized them with ```Buildings()``` in this function. For the buildings that have repetition, I used the ```build()```.

*I'm not going to go deeper into ```buildall()``` since it is essentially just some lines of ```Buildings()``` and ```build()```, along with the some x_pos, y_pos and counts.*

### ```camera.py```
This module is all about rendering sprites onto the screen using the ```Camera()``` class within the file.

#### ```class Camera()```
The ```Camera()``` class is a pygame sprite group. The initialization of this class is very straight forward. The class gets the display into it with ```pygame.display.get_surface()``` mentioned in ```menus.py```. Then, it checks if the user is on the main map since it is a png and not a tmx file and may cause some issues. An offset value is also initialized to achieve a player-centered camera in game.

#### ```load_main()```
This is a very small function but I figured I should mention it. This function, like the name suggests, load the main map. The reason there is a function to load the main map is because when the player goes out of buildings, since the main map isn't a tmx file, there needs to be a function to just load the main map along with its buildings/objects.

#### ```unload_map()```
This function is also relatively small and simple but it is very useful. This function unloads any map, png or tmx since everything is a sprite when it is loaded into memory. The reason I wrote this function in the ```Camera()``` class is because the sprites to render are all in here and for the hitboxes, they are stored in ```settings.py``` and they can be easily acessed.

#### ```render()```
This function is the sole function that displays everything in game, except for the menus of course. They are rendered on their own. This function renders or draws the sprites onto the screen for the main gameplay experience, sorted by their ```y_sort``` value and ```z``` value set in ```GameSprites()```. 

There is also an offset that was set in the initialization of ```Camera()```. The offset is a Vector initialized with ```pygame.math```. The offset's x and y values are the player's x and y values subtracted by half of the width and height of the screen. The result is multiplied with -1. Then, during the rendering process, the offset is added to all the sprite's original positions. Basically, the code is not moving the player but rather the whole map. The player is always in the center of the screen. 

The function also turn off updating the offset if the player is close to the border of the main map. The reason is that it can look very weird if it keeps updating the offset.

#### ```get_close_sprite()```
This function might stand out in the ```camera.py```. Why would one need to get the close sprites in here? Well, the reason is this is the first part of making the player's ```z``` value dynamic. 

This function initializes the values for the closest sprite, the second closest and the third closest. Then, loops through all the visible sprites in ```Camera()```. Using the pythagorean theorem to find the distance between the sprite and the player, the function gets the closest sprite, second closest and third closest. After the loop, the function returns the closest, second closest, and third closest sprites.

#### ```update_layer()```
Now, after we have 3 of the closest sprites, we need to update the layer or ```z``` of the player dynamically.

The ```z``` values are stored into a dictionary. Then, the function checks for wall sprites and wall outline sprites then it separtes them into their own lists. The sprites that aren't walls or wall outlines are also put into their own list. Then, using conditionals, I gave the wall outline the least priority and the sprites that aren't wall or wall outlines most priority to influence the player's z. Then, the closest sprite's ```z``` value is set to the player's ```z``` values.

*Looking back to my code, I admit it was very messy.*

### ```player.py```
This module is about everything to do with the player; the image, animation, collisions, etc.

#### ```class Player()```
The initialization of the ```Player()``` class initializes the player image, hitbox, animation frames, the movement speed, the direction vector. It also initializes the initial ```z``` value of the player along with the ```y_sort``` value for draw order. To deal with collisions, the sprite groups for them are also initialized.

#### ```input()```
This function is for checking user input. Using the ```pygame.key.get_pressed()```, which returns a list of keys along with their states; 0 for not pressed, 1 for pressed, the function gets the state of each key on the user's keyboard. Then, it checks the config for which keys to listen to for player movement. If those specific keys were pressed, the player's direction is changed based on the keys.

*The direction value is a Vector from pygame. The x value is for left(-1) and right(1). The y value is for up(-1) and down(1). If there's no input, the direction is 0.*

The main thing of this function is to update the direction of the player since the direction is used to update the player's position by multiplying it with the player speed in ```update()``` function of ```Player()```.

#### ```animation()```
This function, like the name suggests, animates the player. 

In the initialization of the ```Player()``` class individual frames of the player are imported and stored in a dictionary; the key being the name of the direction the player is facing and the values are the frames itself stored in a list. 

This function checks if the player is moving or not based on the direction set in ```input()```. If the player isn't moving, the image of the player is set to the static frame, 0, of the current direction the player is facing. 

If the player is moving, an index for the player animation frames is set and a loop starts. In the loop, 0.15 is added to the animation index and resets if it reaches 5. The reason is in the lists, there are only 5 frames for each direction. The player image is set to the ```int()``` of the animation index for the direction the player is facing.

#### ```collision_check()```
This is the main function to check for collisions. There are 2 more specific functions for collisions but they are separated for code organization sake.

This function loops through each sprite or hitbox in the group to check collisions for. Then, using pygame's ```colliderect()``` and ```collidepoint()``` functions, the function checks if the player is hitting a hitbox. If the hitbox is a normal one, it sets the player's position to the side of the hitbox that it hit. If the hitbox the player hit is supposed to trigger a function, like go into buildings, it triggers that function.

*The way the function differenciate the hitboxes are using conditionals to check if the hitbox of the sprite is of a specific type.*

#### ```update()```
This function mainly updates the player position and image. It also updates the player's ```y_sort``` value since it is the y position of the player which may change upon movement.

This function sets the ```y_sort``` value then checks for user input with ```input()```. Then, it multiplies the speed set in the initialization of ```Player()``` with the direction set in ```input()```. The result of the multiplication is added to the player position. After checking the movement, it checks for collisions. Then, after all that, it runs ```animation()``` for the player animation.


### ```game.py```
This is the file where the main gameplay is located and loaded. Since I have explained everything about the functions in the main gameplay in the sections above, this will be very straight forward.

#### ```class Game()```
This class initializes the variables needed for the gameplay: the screen/window, the clock for controlling the fps, the main map and the player.

#### ```run()```
This function starts the game loop for the gameplay. It also listens for the ```ESC``` key to load the ```pause_menu()```. Then, it renders the sprites using ```Camera()``` class' ```render()``` function. It also runs ```update_layer()``` and ```update()``` for the player, if the user is still playing. The code after that is the norm for updating the whole display/window to render the graphics.
