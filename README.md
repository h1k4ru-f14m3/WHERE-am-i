# <ins>WHERE (am i)</ins>

A barebone top down pixel art RPG game.  
  
This project is written in Python using mainly the pygame library.  
  
This project and source code can be used to make a RPG game. 

## <ins>Getting Started</ins>

Since this is a game made in python, there are many ways to run this.  

### <ins>Using Code Editors or IDEs</ins>

Whip up the code editor or IDE of your choice and clone the project to the directory you desire. Then, simply run the main.py.  

### <ins>Using the terminal (on Windows)</ins>

Clone the project into a directory of your choice:  
```plain
git clone https://github.com/h1kru-f14m3/WHERE-am-i.git
```
Then, simply run the main.py:  
```plain
python main.py
```

### <ins>Using the terminal (on Linux)</ins>

If you are on Linux, it is a little complicated but I will walk you through it.  
  
Create a virtual environment and activate it:  

```plain
python3 -m venv 

source /bin/activate
```

  
Install the dependencies:  

```plain
pip install pygame-ce
pip install pytmx
```

  
Run main.py:  

```plain
python3 main.py
```

  

## <ins>Features</ins>

Since this is a barebone project. It has all essential features of a game:  

*   Walking around
*   Collision Check
*   Keybinds
*   Player animation
*   Maps
*   Menus
*   Buildings
*   Interiors
*   Y Sort (A little wonky but it works)
*   Background Music

### <ins>Walking around</ins>

This was pretty straight forward to code. In the player.py, I used the get_pressed method from the pygame library which returns a list of keys and their states: pressed(0) and not pressed(1).

This was a pretty easy thing to code. In the player.py, I checked for user input using pygame's get_pressed method. It returns a list of keys and their states. Using that, I checked for specific keys that the user has inputted for their keybinds. After that, depending on the direction the player moved along with the speed that's set in the Player class I've created, I set the player's position in the update method.

### <ins>Collision Check</ins>

In the player.py, I've written a method in the player class to check for collisions by first, iterating through all the sprites in the display. Yes, it sounds inefficient but that was the only way I knew. While iterating the sprites, I check for the player's direction and check if the player is colliding with a sprite using pygame's collide_rect() function. Then, depending on the direction of the player, I set its position relative to the side of the object that it hit.

*Note: the direction I've been talking about is a Vector. The x value of that vector represents the left(-1) and right(1). The y value represents up(-1) and down(1).*

### <ins>Keybinds</ins>

The keybinds feature is present in the menus.py where there are 2 classes: Menu class and Button class. The Menu class is covered in the Menus Section. The keybind feature basically listens for what key you press and then sets it to the function that you are binding the key to. In the button class, there is a method called listen(), which listens for mouse movement and press for buttons and changes the button image based on the mouse movement. When you click on a button that will change your keybind, the code runs a while loop to listen for the key you press then it is saved to the config.json. Since the pygame's get_pressed method I mentioned earlier returns a list of keys, the key you press is an index of that list and then, it is used for player input.
  
